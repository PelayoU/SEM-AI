"""SEM-AI engine MCP server — typed tools over the v0.2 markdown spine + GitHub.

Exposes ~19 tools grouped as:

  read    (8): get_project_map · get_node · children_of · ancestors_of ·
                query_nodes · search_nodes · get_related · get_tree
  write   (8): create_node · update_node · transition_status · link_commit ·
                set_related · add_label · remove_label · supersede
  compute (2): estimate_size · validate_node
  config  (1): get_instance_config

Every write enforces:
  - parent-type rules           → hard reject (ToolError)
  - role jurisdiction           → hard reject (ToolError)
  - lifecycle legality          → hard reject (ToolError)
  - section / required-field / forbidden-pattern / security cross-section
                                → warn-level findings returned in the response

Run with:
    python -m engine.mcp_server
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import asdict
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from mcp.server.fastmcp import FastMCP

from .config_loader import Instance, load_instance
from .estimator import estimate_size as _estimate_size
from .graph_walker import (
    Node,
    children_of as _children_of,
    file_to_id,
    get_node as _get_node,
    id_to_path,
    iter_spine_nodes,
    parse_node_file,
    query_nodes as _query_nodes,
    search_nodes as _search_nodes,
    ancestors_of as _ancestors_of,
)
from .jurisdiction import can_role_write, owning_skill
from .lifecycle import can_transition, legal_next
from .tree_renderer import render_tree
from .validators import (
    ValidationError,
    WriteAttempt,
    validate_node as _validate_node,
    validate_attempt,
)


# ----------------------------------------------------------------------------
# Server bootstrap
# ----------------------------------------------------------------------------

ROOT = Path(os.environ.get("SEM_AI_ROOT", os.getcwd())).resolve()
INSTANCE: Instance = load_instance(ROOT)
TODAY = date.today().isoformat()

mcp = FastMCP("sem_ai_engine")


def _node_to_dict(n: Node) -> dict[str, Any]:
    """Serialise a Node for transport (Path is not JSON-serialisable)."""
    out = asdict(n)
    out["path"] = str(n.path.relative_to(INSTANCE.root)) if n.path else None
    return out


def _serialize_estimate(e: Any) -> dict[str, Any]:
    return {
        "value": e.value,
        "unit": e.unit,
        "method": e.method,
        "source_release": e.source_release,
        "breakdown": e.breakdown,
        "display": f"≈{e.value:g} {e.unit}" if e.method == "auto" else f"{e.value:g} {e.unit}",
    }


# ----------------------------------------------------------------------------
# READ tools
# ----------------------------------------------------------------------------

@mcp.tool()
def get_project_map() -> dict[str, Any]:
    """The at-minimum project map every agent must hold at session start:
    every vision, goal, capability, and ADR. Cheap; called by SessionStart hook."""
    nodes = []
    for n in iter_spine_nodes(INSTANCE):
        if n.type in ("vision", "goal", "capability", "adr"):
            nodes.append({
                "id": n.id,
                "type": n.type,
                "parent": n.parent,
                "status": n.status,
                "maintained_by_role": n.maintained_by_role,
                "labels": n.labels,
            })
    return {"count": len(nodes), "nodes": nodes}


@mcp.tool()
def get_node(node_id: str) -> dict[str, Any]:
    """Get the full body + frontmatter of one node by id."""
    n = _get_node(INSTANCE, node_id)
    if n is None:
        return {"error": f"node '{node_id}' not found"}
    return _node_to_dict(n)


@mcp.tool()
def children_of(node_id: str) -> dict[str, Any]:
    """List nodes whose `parent` is `node_id`."""
    nodes = _children_of(INSTANCE, node_id)
    return {"count": len(nodes), "nodes": [_node_to_dict(n) for n in nodes]}


@mcp.tool()
def ancestors_of(node_id: str) -> dict[str, Any]:
    """Walk parent chain from `node_id` to the root vision. Includes the node itself."""
    chain = _ancestors_of(INSTANCE, node_id)
    return {"count": len(chain), "nodes": [_node_to_dict(n) for n in chain]}


@mcp.tool()
def query_nodes(
    type: str | None = None,
    status: str | None = None,
    parent: str | None = None,
    maintained_by_role: str | None = None,
    label: str | None = None,
) -> dict[str, Any]:
    """Filter spine nodes by any combination of frontmatter attributes."""
    nodes = _query_nodes(
        INSTANCE,
        type=type,
        status=status,
        parent=parent,
        maintained_by_role=maintained_by_role,
        label=label,
    )
    return {"count": len(nodes), "nodes": [_node_to_dict(n) for n in nodes]}


@mcp.tool()
def search_nodes(query: str) -> dict[str, Any]:
    """Substring search across node ids and body text (case-insensitive)."""
    nodes = _search_nodes(INSTANCE, query)
    return {"count": len(nodes), "nodes": [_node_to_dict(n) for n in nodes]}


@mcp.tool()
def get_related(node_id: str) -> dict[str, Any]:
    """List related-axis edges: ADRs that supersede/are-superseded-by this
    node, and labels containing related: prefix. Pure read."""
    n = _get_node(INSTANCE, node_id)
    if n is None:
        return {"error": f"node '{node_id}' not found"}
    related: dict[str, list[str]] = {"supersedes": n.supersedes, "superseded_by": n.superseded_by}
    related["labels_related"] = [l for l in n.labels if l.startswith("related:")]
    return related


@mcp.tool()
def get_tree() -> dict[str, str]:
    """Render the project tree (TREE.md content) without writing to disk."""
    return {"tree_md": render_tree(INSTANCE)}


# ----------------------------------------------------------------------------
# WRITE tools — every write requires acting_role
# ----------------------------------------------------------------------------

def _enforce_jurisdiction(role: str, node_type: str, op: str) -> None:
    d = can_role_write(INSTANCE, role, node_type, op)
    if not d.allowed:
        raise ValueError(f"[jurisdiction-violation] {d.reason}. Hint: {d.hint}")


def _slug_to_filename(slug: str) -> str:
    # Sanitise slug to filesystem-safe.
    safe = re.sub(r"[^a-z0-9-]", "-", slug.lower()).strip("-")
    return safe


def _frontmatter_yaml(fields: dict[str, Any]) -> str:
    """Emit YAML frontmatter in v0.2 7-field shape."""
    order = ["type", "parent", "status", "created", "updated", "maintained_by_role", "labels",
             "supersedes", "superseded-by"]
    lines = ["---"]
    for key in order:
        if key not in fields:
            continue
        val = fields[key]
        if val in (None, "", []):
            continue
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---\n")
    return "\n".join(lines)


@mcp.tool()
def create_node(
    type: str,
    slug: str,
    parent: str | None,
    body: str,
    acting_role: str,
    labels: list[str] | None = None,
) -> dict[str, Any]:
    """Create a new spine / ADR node deterministically.

    - Hard-rejects on jurisdiction or parent-type violation.
    - Warns on missing sections, missing required fields, forbidden patterns,
      security cross-section findings.
    - Writes the markdown file under `instance.paths.spine_dir/<folder>/` or
      `docs/adr/`. The id is derived: `<type>-<slug>` (or `adr-<slug>`).
    """
    _enforce_jurisdiction(acting_role, type, "create_node")
    attempt = WriteAttempt(type=type, parent=parent, body=body, acting_role=acting_role, op="create_node")
    try:
        _, warnings = validate_attempt(INSTANCE, attempt)
    except ValidationError as e:
        raise ValueError(f"[parent-type-violation] {e}")

    fname = _slug_to_filename(slug)
    new_id = f"adr-{fname}" if type == "adr" else f"{type}-{fname}"
    path = id_to_path(new_id, INSTANCE)
    if path is None:
        raise ValueError(f"cannot determine storage path for type='{type}', slug='{slug}'")
    if path.exists():
        raise ValueError(f"node already exists at {path.relative_to(INSTANCE.root)}")

    fields = {
        "type": type,
        "parent": parent,
        "status": "draft",
        "created": TODAY,
        "updated": TODAY,
        "maintained_by_role": acting_role,
    }
    if labels:
        fields["labels"] = labels

    content = _frontmatter_yaml(fields) + body.lstrip("\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return {
        "id": new_id,
        "path": str(path.relative_to(INSTANCE.root)),
        "warnings": warnings,
    }


@mcp.tool()
def update_node(node_id: str, body: str, acting_role: str) -> dict[str, Any]:
    """Replace the body of an existing node, preserve frontmatter (only bump
    `updated:` to today and `maintained_by_role:` to `acting_role`)."""
    n = _get_node(INSTANCE, node_id)
    if n is None:
        raise ValueError(f"node '{node_id}' not found")
    _enforce_jurisdiction(acting_role, n.type, "update_node")

    attempt = WriteAttempt(type=n.type, parent=n.parent, body=body, acting_role=acting_role, op="update_node")
    _, warnings = validate_attempt(INSTANCE, attempt)

    # Re-emit frontmatter with bumped updated + acting_role.
    fields = {
        "type": n.type,
        "parent": n.parent,
        "status": n.status,
        "created": n.created,
        "updated": TODAY,
        "maintained_by_role": acting_role,
    }
    if n.labels:
        fields["labels"] = n.labels
    if n.supersedes:
        fields["supersedes"] = n.supersedes
    if n.superseded_by:
        fields["superseded-by"] = n.superseded_by

    content = _frontmatter_yaml(fields) + body.lstrip("\n")
    if n.path is None:
        raise ValueError(f"node '{node_id}' is not file-backed (operational tier — use GitHub MCP)")
    n.path.write_text(content, encoding="utf-8")
    return {"id": node_id, "warnings": warnings}


@mcp.tool()
def transition_status(node_id: str, to_status: str, acting_role: str) -> dict[str, Any]:
    """Move a node's status through the lifecycle. Hard-reject on illegal transition."""
    n = _get_node(INSTANCE, node_id)
    if n is None:
        raise ValueError(f"node '{node_id}' not found")
    if not can_transition(INSTANCE, n.status, to_status):
        legal = legal_next(INSTANCE, n.status)
        raise ValueError(
            f"[lifecycle-violation] cannot transition {n.type} '{node_id}' "
            f"from '{n.status}' to '{to_status}'. Legal next: {legal}"
        )
    # Update only the status field in frontmatter; preserve body.
    fields = {
        "type": n.type,
        "parent": n.parent,
        "status": to_status,
        "created": n.created,
        "updated": TODAY,
        "maintained_by_role": acting_role,
    }
    if n.labels:
        fields["labels"] = n.labels
    if n.supersedes:
        fields["supersedes"] = n.supersedes
    if n.superseded_by:
        fields["superseded-by"] = n.superseded_by
    content = _frontmatter_yaml(fields) + n.body.lstrip("\n")
    if n.path is None:
        raise ValueError(f"node '{node_id}' is not file-backed")
    n.path.write_text(content, encoding="utf-8")
    return {"id": node_id, "from": n.status, "to": to_status}


@mcp.tool()
def link_commit(spec_id: str, commit_sha: str, acting_role: str) -> dict[str, Any]:
    """Attach a code commit SHA to the spec/story it satisfies. Currently
    appends to the spec's `## Code commits` section (creates if missing).
    Used by Developer to bridge code to intent."""
    n = _get_node(INSTANCE, spec_id)
    if n is None:
        raise ValueError(f"node '{spec_id}' not found")
    if n.type not in ("spec", "story", "feature"):
        raise ValueError(
            f"link_commit target must be spec/story/feature; '{spec_id}' is {n.type}"
        )
    body = n.body
    if "## Code commits" not in body:
        body = body.rstrip() + "\n\n## Code commits\n"
    body += f"\n- `{commit_sha}` (linked by {acting_role}, {TODAY})\n"
    return update_node(node_id=spec_id, body=body, acting_role=acting_role)


@mcp.tool()
def set_related(node_id: str, related_ids: list[str], acting_role: str) -> dict[str, Any]:
    """Set the cross-axis `related:` labels on a node (replacing existing
    related: entries)."""
    n = _get_node(INSTANCE, node_id)
    if n is None:
        raise ValueError(f"node '{node_id}' not found")
    new_labels = [l for l in n.labels if not l.startswith("related:")]
    new_labels.extend(f"related:{r}" for r in related_ids)
    return _update_labels(n, new_labels, acting_role)


@mcp.tool()
def add_label(node_id: str, label: str, acting_role: str) -> dict[str, Any]:
    """Add a label to a node (lowercase, ≤32 chars). Idempotent."""
    n = _get_node(INSTANCE, node_id)
    if n is None:
        raise ValueError(f"node '{node_id}' not found")
    label = label.lower()
    if len(label) > 32:
        raise ValueError(f"label length must be ≤32 chars; got {len(label)}")
    if label in n.labels:
        return {"id": node_id, "label": label, "noop": True}
    return _update_labels(n, n.labels + [label], acting_role)


@mcp.tool()
def remove_label(node_id: str, label: str, acting_role: str) -> dict[str, Any]:
    """Remove a label from a node. Idempotent."""
    n = _get_node(INSTANCE, node_id)
    if n is None:
        raise ValueError(f"node '{node_id}' not found")
    label = label.lower()
    if label not in n.labels:
        return {"id": node_id, "label": label, "noop": True}
    return _update_labels(n, [l for l in n.labels if l != label], acting_role)


def _update_labels(n: Node, new_labels: list[str], acting_role: str) -> dict[str, Any]:
    fields = {
        "type": n.type,
        "parent": n.parent,
        "status": n.status,
        "created": n.created,
        "updated": TODAY,
        "maintained_by_role": acting_role,
    }
    if new_labels:
        fields["labels"] = new_labels
    if n.supersedes:
        fields["supersedes"] = n.supersedes
    if n.superseded_by:
        fields["superseded-by"] = n.superseded_by
    content = _frontmatter_yaml(fields) + n.body.lstrip("\n")
    if n.path is None:
        raise ValueError(f"node '{n.id}' is not file-backed")
    n.path.write_text(content, encoding="utf-8")
    return {"id": n.id, "labels": new_labels}


@mcp.tool()
def supersede(
    old_id: str, new_slug: str, body: str, acting_role: str
) -> dict[str, Any]:
    """Create a new ADR (or supersede-chain node) that supersedes `old_id`.

    The new node carries `supersedes: [old_id]`; the old node is updated to
    `superseded_by: [new_id]` and its status moves to `superseded`.
    """
    old = _get_node(INSTANCE, old_id)
    if old is None:
        raise ValueError(f"node '{old_id}' not found")
    _enforce_jurisdiction(acting_role, old.type, "supersede")

    # Create the new node.
    fname = _slug_to_filename(new_slug)
    new_id = f"adr-{fname}" if old.type == "adr" else f"{old.type}-{fname}"
    new_path = id_to_path(new_id, INSTANCE)
    if new_path is None or new_path.exists():
        raise ValueError(f"cannot create new node at {new_path}")

    attempt = WriteAttempt(type=old.type, parent=old.parent, body=body, acting_role=acting_role, op="supersede")
    try:
        _, warnings = validate_attempt(INSTANCE, attempt)
    except ValidationError as e:
        raise ValueError(f"[parent-type-violation] {e}")

    new_fields = {
        "type": old.type,
        "parent": old.parent,
        "status": "draft",
        "created": TODAY,
        "updated": TODAY,
        "maintained_by_role": acting_role,
        "supersedes": [old_id],
    }
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path.write_text(_frontmatter_yaml(new_fields) + body.lstrip("\n"), encoding="utf-8")

    # Update old node: superseded_by + status=superseded.
    old_fields = {
        "type": old.type,
        "parent": old.parent,
        "status": "superseded",
        "created": old.created,
        "updated": TODAY,
        "maintained_by_role": old.maintained_by_role,
    }
    if old.labels:
        old_fields["labels"] = old.labels
    if old.supersedes:
        old_fields["supersedes"] = old.supersedes
    old_fields["superseded-by"] = (old.superseded_by or []) + [new_id]
    old.path.write_text(_frontmatter_yaml(old_fields) + old.body.lstrip("\n"), encoding="utf-8")
    return {"new_id": new_id, "old_id": old_id, "warnings": warnings}


# ----------------------------------------------------------------------------
# COMPUTE tools
# ----------------------------------------------------------------------------

@mcp.tool()
def estimate_size(release_id: str | None = None) -> dict[str, Any]:
    """Function-point estimate for the project, or for a specific release.
    Manual override in `release.## Sizing` takes precedence over the auto-estimate."""
    return _serialize_estimate(_estimate_size(INSTANCE, release_id))


@mcp.tool()
def validate_node(node_id: str) -> dict[str, Any]:
    """Re-validate an existing node — return list of warnings."""
    n = _get_node(INSTANCE, node_id)
    if n is None:
        return {"error": f"node '{node_id}' not found"}
    warnings = _validate_node(INSTANCE, n)
    return {"id": node_id, "type": n.type, "warnings": warnings, "warning_count": len(warnings)}


# ----------------------------------------------------------------------------
# CONFIG tool
# ----------------------------------------------------------------------------

@mcp.tool()
def get_instance_config() -> dict[str, Any]:
    """Return the loaded methodology instance config (read-only snapshot).
    Useful for agents to know which thresholds, forbidden patterns, and role
    permissions are in force without re-reading the YAML files."""
    return {
        "name": "sem-ai",
        "roles": list(INSTANCE.role_set),
        "node_types": list(INSTANCE.node_type_set),
        "thresholds": INSTANCE.thresholds,
        "sizing_unit": INSTANCE.sizing_unit,
        "sizing_coefficients": INSTANCE.sizing_coefficients,
        "owning_skill": INSTANCE.owning_skill,
    }


# ----------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------

def main() -> None:
    """Run the MCP server on stdio."""
    mcp.run()


if __name__ == "__main__":
    main()
