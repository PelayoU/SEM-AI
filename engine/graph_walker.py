"""Walk the v0.2 markdown spine + GitHub operational tier.

The strategic spine lives as markdown files under `sem-ai/{vision,goals,
capabilities,features}/` and `docs/adr/`. The operational tier (story / spec /
defect / measurement / inspection) lives as GitHub Issues — surfaced here via
the `gh` CLI when available, otherwise empty (Day 3 wires sync.yml).

Public functions:
    iter_spine_nodes(instance)               → Iterator[Node]
    get_node(instance, node_id)              → Node | None
    children_of(instance, node_id)           → list[Node]
    ancestors_of(instance, node_id)          → list[Node]
    query_nodes(instance, type=, status=, ...) → list[Node]
    search_nodes(instance, query)            → list[Node]
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

import yaml

from .config_loader import Instance


# ----------------------------------------------------------------------------
# Node data model
# ----------------------------------------------------------------------------

@dataclass
class Node:
    """One graph node — either a markdown file on disk or a GitHub Issue."""

    id: str                              # e.g. "vision-001-sem-ai", "cap-03-apply-po-discipline"
    type: str                            # one of instance.node_type_set
    parent: str | None
    status: str
    created: str                         # YYYY-MM-DD
    updated: str
    maintained_by_role: str
    labels: list[str] = field(default_factory=list)
    path: Path | None = None             # disk location (None for GitHub-only nodes)
    issue_number: int | None = None      # GitHub Issue number (None for spine nodes)
    body: str = ""                       # markdown body (without frontmatter)
    # ADR-specific
    supersedes: list[str] = field(default_factory=list)
    superseded_by: list[str] = field(default_factory=list)


# ----------------------------------------------------------------------------
# ID ↔ path conversion
# ----------------------------------------------------------------------------

# Folder name (plural) → singular type prefix.
_FOLDER_TO_TYPE = {
    "vision": "vision",
    "goals": "goal",
    "capabilities": "capability",
    "features": "feature",
}
_TYPE_TO_FOLDER = {v: k for k, v in _FOLDER_TO_TYPE.items()}


def file_to_id(path: Path, instance: Instance) -> str | None:
    """Map a markdown file path to its node id, or None if not a spine node."""
    try:
        rel = path.relative_to(instance.root)
    except ValueError:
        return None
    parts = rel.parts
    if parts[:1] == ("docs",) and parts[1:2] == ("adr",):
        return f"adr-{path.stem}"
    if parts[:1] == ("sem-ai",) and len(parts) >= 3:
        folder = parts[1]
        type_ = _FOLDER_TO_TYPE.get(folder)
        if type_ is None:
            return None
        return f"{type_}-{path.stem}"
    return None


def id_to_path(node_id: str, instance: Instance) -> Path | None:
    """Map a node id to its on-disk path. Returns None for non-spine nodes
    (story / spec / defect / measurement / inspection live in GitHub Issues)."""
    if node_id.startswith("adr-"):
        slug = node_id[len("adr-"):]
        return instance.root / "docs" / "adr" / f"{slug}.md"
    for prefix, folder in [
        ("vision-", "vision"),
        ("goal-", "goals"),
        ("capability-", "capabilities"),
        ("feature-", "features"),
        # Back-compat: v0.1 frontmatter used `cap-NN-…` as the canonical id. We
        # accept both forms when resolving paths so old references resolve.
        ("cap-", "capabilities"),
    ]:
        if node_id.startswith(prefix):
            slug = node_id[len(prefix):]
            return instance.root / "sem-ai" / folder / f"{slug}.md"
    return None


# ----------------------------------------------------------------------------
# Frontmatter + body parsing
# ----------------------------------------------------------------------------

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def parse_node_file(path: Path, instance: Instance) -> Node | None:
    """Parse a markdown file at `path` into a Node. Returns None on hard errors
    (no frontmatter, unknown type, missing required field). Validation is
    *not* run here — that is validators.py's job."""
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    body = m.group(2)
    node_id = file_to_id(path, instance)
    if not node_id:
        return None
    type_ = fm.get("type")
    if type_ not in instance.node_type_set:
        return None
    return Node(
        id=node_id,
        type=type_,
        parent=fm.get("parent"),
        status=fm.get("status", "draft"),
        created=str(fm.get("created", "")),
        updated=str(fm.get("updated", "")),
        maintained_by_role=fm.get("maintained_by_role", instance.node_types[type_].owning_role),
        labels=[str(l) for l in (fm.get("labels") or [])],
        path=path,
        body=body,
        supersedes=_flatten_str(fm.get("supersedes")),
        superseded_by=_flatten_str(fm.get("superseded-by")),
    )


def _flatten_str(value) -> list[str]:
    """Defensive: accept str, list[str], list[list[str]] (legacy migration bug);
    return a flat list[str]."""
    if not value:
        return []
    if isinstance(value, str):
        return [value]
    out: list[str] = []
    for item in value:
        if isinstance(item, list):
            out.extend(str(x) for x in item)
        else:
            out.append(str(item))
    return out


# ----------------------------------------------------------------------------
# Iteration over the spine + ADRs
# ----------------------------------------------------------------------------

def iter_spine_nodes(instance: Instance) -> Iterator[Node]:
    """Yield every spine + ADR node parseable from disk. Order is stable but
    not topological."""
    spine_dir = instance.root / "sem-ai"
    if spine_dir.is_dir():
        for path in sorted(spine_dir.rglob("*.md")):
            node = parse_node_file(path, instance)
            if node:
                yield node
    adr_dir = instance.root / "docs" / "adr"
    if adr_dir.is_dir():
        for path in sorted(adr_dir.glob("*.md")):
            node = parse_node_file(path, instance)
            if node:
                yield node


def get_node(instance: Instance, node_id: str) -> Node | None:
    """Resolve a node by id from the spine or ADRs (operational tier later)."""
    path = id_to_path(node_id, instance)
    if path is None:
        return _get_github_issue_node(instance, node_id)
    return parse_node_file(path, instance)


def children_of(instance: Instance, node_id: str) -> list[Node]:
    """All nodes whose `parent` matches node_id. O(n) over the spine."""
    return [n for n in iter_spine_nodes(instance) if n.parent == node_id]


def ancestors_of(instance: Instance, node_id: str) -> list[Node]:
    """Walk parent chain from node_id up to the vision root. Includes the node
    itself as the first element."""
    seen: set[str] = set()
    chain: list[Node] = []
    current = node_id
    while current and current not in seen:
        seen.add(current)
        node = get_node(instance, current)
        if node is None:
            break
        chain.append(node)
        current = node.parent or ""
    return chain


def query_nodes(
    instance: Instance,
    *,
    type: str | None = None,
    status: str | None = None,
    parent: str | None = None,
    maintained_by_role: str | None = None,
    label: str | None = None,
) -> list[Node]:
    """Filter spine nodes by any combination of frontmatter attributes."""
    out: list[Node] = []
    for n in iter_spine_nodes(instance):
        if type and n.type != type:
            continue
        if status and n.status != status:
            continue
        if parent and n.parent != parent:
            continue
        if maintained_by_role and n.maintained_by_role != maintained_by_role:
            continue
        if label and label not in n.labels:
            continue
        out.append(n)
    return out


def search_nodes(instance: Instance, query: str) -> list[Node]:
    """Substring search across node ids and bodies (case-insensitive)."""
    q = query.lower()
    out: list[Node] = []
    for n in iter_spine_nodes(instance):
        if q in n.id.lower() or q in n.body.lower():
            out.append(n)
    return out


# ----------------------------------------------------------------------------
# GitHub Issues bridge (operational tier — Day 3 wires sync.yml)
# ----------------------------------------------------------------------------

def _get_github_issue_node(instance: Instance, node_id: str) -> Node | None:
    """Look up a node by id in GitHub Issues. Returns None if `gh` is unavailable
    or the id does not match an issue. Best-effort; the engine works without it."""
    # Operational ids look like "story-N" or "spec-N" or "defect-N" where N is the
    # GitHub Issue number. The label `sem-ai:<id>` is set by the engine's create_node.
    if not _gh_available():
        return None
    # Resolve via label search.
    try:
        out = subprocess.run(
            ["gh", "issue", "list", "--label", f"sem-ai:{node_id}", "--json",
             "number,title,labels,body,createdAt,updatedAt,state", "--state", "all"],
            cwd=str(instance.root), capture_output=True, text=True, timeout=10, check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if out.returncode != 0:
        return None
    import json
    issues = json.loads(out.stdout or "[]")
    if not issues:
        return None
    issue = issues[0]
    labels = [l["name"] for l in issue.get("labels", [])]
    # Infer type from id prefix.
    type_ = node_id.split("-", 1)[0]
    if type_ not in instance.node_type_set:
        return None
    return Node(
        id=node_id,
        type=type_,
        parent=None,                                 # parsed from labels in v0.3
        status="active" if issue["state"] == "OPEN" else "done",
        created=issue["createdAt"][:10],
        updated=issue["updatedAt"][:10],
        maintained_by_role=instance.node_types[type_].owning_role,
        labels=labels,
        issue_number=issue["number"],
        body=issue.get("body", ""),
    )


def _gh_available() -> bool:
    try:
        r = subprocess.run(
            ["gh", "--version"], capture_output=True, text=True, timeout=2, check=False
        )
        return r.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False
