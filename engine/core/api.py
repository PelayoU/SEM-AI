"""The 22 API tools the engine MCP exposes to the agent.

Each function:
1. Validates inputs via the validators (`engine/core/validators.py`).
2. Delegates the I/O to a `BackendAdapter` (the github / jira / linear etc.
   implementation passed in).
3. Maintains coherence between body and labels (per ADR-006 update: the
   `experiment` label tracks the `Uncertainty addressed` slot).

The functions are pure with respect to the adapter — they don't know how the
adapter talks to GitHub, only what the adapter promises (`engine/adapters/
base.py`). The MCP server (`engine/mcp_server.py`) wraps these in MCP tool
schemas and routes calls from the agent.
"""

from __future__ import annotations

import re

from ..adapters.base import BackendAdapter
from .catalog import CATALOG, NodeType, Status
from .models import (
    Finding,
    InstanceConfig,
    Milestone,
    Node,
    ProjectMap,
    Release,
    SizeEstimate,
    TreeNode,
)
from .permissions import Role, TriggeredBy
from .validators import (
    validate_jurisdiction,
    validate_parent,
    validate_status,
    validate_supersede,
    validate_triggered_by,
)


# -------------------------------------------------------------------- helpers


_UNCERTAINTY_SECTION_RE = re.compile(
    # Match the section header (allowing trailing comment text on same line),
    # then capture everything up to the next "## " header or end of body.
    r"^##\s+Uncertainty\s+addressed[^\n]*\n(.*?)(?=\n##\s|\Z)",
    re.MULTILINE | re.DOTALL | re.IGNORECASE,
)
_EXPERIMENT_LABEL = "experiment"


def _is_experimental_body(body: str | None) -> bool:
    """Detect whether the Uncertainty addressed section is populated.

    Returns False if the body is empty, the section is absent, or the
    section's content starts with `N/A` (case-insensitive). Returns True
    otherwise.

    Implements the slot-label coherence rule of ADR-006 update.
    """
    if not body:
        return False
    match = _UNCERTAINTY_SECTION_RE.search(body)
    if not match:
        return False
    content = match.group(1).strip()
    if not content:
        return False
    if content.upper().startswith("N/A"):
        return False
    return True


def _ensure_experiment_label_coherence(
    adapter: BackendAdapter,
    node: Node,
    new_body: str | None,
    acting_role: Role,
) -> Node:
    """Add or remove the `experiment` label based on Uncertainty addressed.

    Called from `create_node` and `update_node` after the backend write
    completes. The label tracks the slot mechanically — agent never curates
    it. Returns the node reflecting the label change (re-fetched after
    add/remove); if no change was needed, returns the input node unchanged.
    """
    if node.type is not NodeType.FEATURE:
        return node  # the slot exists only on feature; story drops it
    should_be_experimental = _is_experimental_body(new_body)
    currently_has = _EXPERIMENT_LABEL in node.labels
    if should_be_experimental and not currently_has:
        adapter.add_label(node.id, _EXPERIMENT_LABEL, acting_role=acting_role)
        return adapter.get_issue(node.id)
    if not should_be_experimental and currently_has:
        adapter.remove_label(node.id, _EXPERIMENT_LABEL, acting_role=acting_role)
        return adapter.get_issue(node.id)
    return node


# ============================================================== READS (8)


def get_node(adapter: BackendAdapter, node_id: str) -> Node:
    """Read a single node by id."""
    return adapter.get_issue(node_id)


def children_of(adapter: BackendAdapter, node_id: str) -> tuple[Node, ...]:
    """Return the immediate sub-issue children of `node_id`."""
    return adapter.list_sub_issues(node_id)


def ancestors_of(adapter: BackendAdapter, node_id: str) -> tuple[Node, ...]:
    """Walk parent links upward to the root, nearest-first."""
    return adapter.ancestors(node_id)


def get_related(adapter: BackendAdapter, node_id: str) -> tuple[Node, ...]:
    """Return nodes linked via the Related custom field + cross-refs."""
    return adapter.list_related(node_id)


def query_nodes(
    adapter: BackendAdapter,
    *,
    type: NodeType | None = None,
    status: Status | None = None,
    parent: str | None = None,
    label: str | None = None,
    milestone: str | None = None,
) -> tuple[Node, ...]:
    """Filter nodes by any combination of the criteria."""
    return adapter.query_issues(
        type=type, status=status, parent=parent, label=label, milestone=milestone
    )


def search_nodes(adapter: BackendAdapter, query: str) -> tuple[Node, ...]:
    """Substring-search the graph via the backend's native search."""
    return adapter.search_issues(query)


def get_tree(
    adapter: BackendAdapter, root_id: str | None = None, max_depth: int = 10
) -> TreeNode:
    """Build a sub-issue tree from `root_id` or from the vision if None."""
    return adapter.tree(root_id, max_depth)


def get_project_map(adapter: BackendAdapter) -> ProjectMap:
    """Return the minimum project map: vision + goals + capabilities + accepted ADRs."""
    return adapter.project_map()


# ============================================================== WRITES (8)


def create_node(
    adapter: BackendAdapter,
    *,
    type: NodeType,
    parent_id: str | None,
    title: str,
    body: str,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
    status: Status | None = None,
    labels: tuple[str, ...] = (),
    milestone: str | None = None,
) -> Node:
    """Create a new graph node.

    Orchestrates validation + create + parent link + initial status + label
    coherence. Atomic from the agent's perspective: either the node is
    created complete or the operation raises.
    """
    validate_triggered_by("create_node", triggered_by)
    validate_jurisdiction(type, acting_role)

    parent_type = adapter.get_issue(parent_id).type if parent_id else None
    validate_parent(type, parent_type)

    if status is None:
        status = CATALOG[type].initial_status
    validate_status(type, status)

    node = adapter.create_issue(
        type=type,
        title=title,
        body=body,
        status=status,
        parent_id=parent_id,
        acting_role=acting_role,
        labels=labels,
        milestone=milestone,
    )

    return _ensure_experiment_label_coherence(adapter, node, body, acting_role)


def update_node(
    adapter: BackendAdapter,
    node_id: str,
    *,
    title: str | None = None,
    body: str | None = None,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> Node:
    """Update a node's title or body. Status changes go through transition_status."""
    validate_triggered_by("update_node", triggered_by)
    existing = adapter.get_issue(node_id)
    validate_jurisdiction(existing.type, acting_role)

    updated = adapter.update_issue(
        node_id, title=title, body=body, acting_role=acting_role
    )

    if body is not None:
        updated = _ensure_experiment_label_coherence(
            adapter, updated, body, acting_role
        )

    return updated


def transition_status(
    adapter: BackendAdapter,
    node_id: str,
    new_status: Status,
    *,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> Node:
    """Move a node to a new status, validating type-status compatibility."""
    validate_triggered_by("transition_status", triggered_by)
    existing = adapter.get_issue(node_id)
    validate_jurisdiction(existing.type, acting_role)
    validate_status(existing.type, new_status)
    return adapter.set_status(node_id, new_status, acting_role=acting_role)


def link_commit(
    adapter: BackendAdapter,
    node_id: str,
    commit_sha: str,
    *,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> None:
    """Record that a commit was made in service of this node.

    Additive operation — does not mutate node state, so it is permitted for
    hook/Action-invoked agents (per RESTRICTED_OPS / ALWAYS_PERMITTED_OPS).
    """
    validate_triggered_by("link_commit", triggered_by)
    adapter.link_commit(node_id, commit_sha, acting_role=acting_role)


def set_related(
    adapter: BackendAdapter,
    node_id: str,
    related_ids: tuple[str, ...],
    *,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> None:
    """Replace the node's Related custom field with the given list."""
    validate_triggered_by("set_related", triggered_by)
    existing = adapter.get_issue(node_id)
    validate_jurisdiction(existing.type, acting_role)
    adapter.set_related(node_id, related_ids, acting_role=acting_role)


def add_label(
    adapter: BackendAdapter,
    node_id: str,
    label: str,
    *,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> None:
    """Add a label to the node. Idempotent."""
    validate_triggered_by("add_label", triggered_by)
    adapter.add_label(node_id, label, acting_role=acting_role)


def remove_label(
    adapter: BackendAdapter,
    node_id: str,
    label: str,
    *,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> None:
    """Remove a label from the node. Idempotent."""
    validate_triggered_by("remove_label", triggered_by)
    adapter.remove_label(node_id, label, acting_role=acting_role)


def supersede(
    adapter: BackendAdapter,
    superseding_id: str,
    superseded_id: str,
    *,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> None:
    """Mark `superseded_id` as superseded BY `superseding_id`.

    Validates the operation per `validate_supersede` (same type, no self-loop,
    target not already deprecated), then delegates to the adapter.
    """
    validate_triggered_by("supersede", triggered_by)
    superseding = adapter.get_issue(superseding_id)
    superseded = adapter.get_issue(superseded_id)
    validate_jurisdiction(superseding.type, acting_role)
    validate_supersede(
        superseding_type=superseding.type,
        superseded_type=superseded.type,
        superseding_id=superseding_id,
        superseded_id=superseded_id,
        superseded_current_status=superseded.status,
    )
    adapter.supersede(superseding_id, superseded_id, acting_role=acting_role)


# ============================================================== COMPUTE (2)


def estimate_size(adapter: BackendAdapter, node_id: str) -> SizeEstimate:
    """Estimate the size of a node — methodology supplied by project skills.

    The engine returns a stub estimate by default; project methodology skills
    (e.g. `product-manager-early-sizing`) override the estimation logic.
    The agent calls a sizing skill before this tool when a serious estimate
    is needed.
    """
    node = adapter.get_issue(node_id)
    return SizeEstimate(
        node_id=node.id,
        estimate="unknown",
        confidence="none",
        rationale="default — no project methodology skill applied",
    )


def validate_node(adapter: BackendAdapter, node_id: str) -> tuple[Finding, ...]:
    """Run the engine's checks against a node, returning warn-level findings.

    The actual findings come from `engine/checks/` library (security_review,
    architect_coherence, etc.) — pending implementation per ADR-008 update §
    semantic CI. Until those land, returns an empty tuple.
    """
    _ = adapter.get_issue(node_id)  # raises if missing
    # TODO(engine/checks): wire to the semantic CI library when it ships
    return ()


# ============================================================== CONFIG (1)


def get_instance_config(adapter: BackendAdapter) -> InstanceConfig:
    """Return the project-level configuration."""
    return adapter.instance_config()


# ============================================================== BRIDGES (3)


def create_milestone(
    adapter: BackendAdapter,
    title: str,
    due_date: str | None,
    body: str,
    *,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> Milestone:
    """Create a Milestone — release planning, per ADR-001 § Milestone operations.

    Only `acting_role=pm` is authorised (per ADR-001 table). The validator
    here is a special case — milestone is not in the Issue Type catalog, so
    the jurisdiction check is inlined.
    """
    validate_triggered_by("create_milestone", triggered_by)
    if acting_role != Role.PM:
        from .exceptions import JurisdictionViolation

        raise JurisdictionViolation(
            f"role {acting_role.value!r} is not authorised to create Milestones. "
            f"Authorised role: 'product-manager' (ADR-001 § Milestone operations)"
        )
    return adapter.create_milestone(title, due_date, body, acting_role=acting_role)


def assign_to_milestone(
    adapter: BackendAdapter,
    node_id: str,
    milestone_number: int,
    *,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> None:
    """Assign a node to a Milestone. Only PM is authorised."""
    validate_triggered_by("assign_to_milestone", triggered_by)
    if acting_role != Role.PM:
        from .exceptions import JurisdictionViolation

        raise JurisdictionViolation(
            f"role {acting_role.value!r} is not authorised to assign to Milestones. "
            f"Authorised role: 'product-manager'"
        )
    adapter.assign_to_milestone(node_id, milestone_number, acting_role=acting_role)


def publish_release(
    adapter: BackendAdapter,
    milestone_number: int,
    tag: str,
    notes: str,
    *,
    acting_role: Role,
    triggered_by: TriggeredBy = TriggeredBy.HUMAN,
) -> Release:
    """Close a Milestone and publish the corresponding GitHub Release.

    Only `acting_role=devops` is authorised (per ADR-001 table). DevOps owns
    the publication moment of a release.
    """
    validate_triggered_by("publish_release", triggered_by)
    if acting_role != Role.DEVOPS:
        from .exceptions import JurisdictionViolation

        raise JurisdictionViolation(
            f"role {acting_role.value!r} is not authorised to publish Releases. "
            f"Authorised role: 'devops' (ADR-001 § Milestone operations)"
        )
    return adapter.publish_release(milestone_number, tag, notes, acting_role=acting_role)
