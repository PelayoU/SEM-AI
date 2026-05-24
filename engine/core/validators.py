"""Pure validation functions invoked on every write.

Each `validate_*` either returns `None` on success or raises a
`FrameworkRejection` subclass on failure. The MCP server catches these and
translates them into MCP errors with legible reasons.

These functions are **pure** — no I/O, no side effects. They consult only the
catalog and permissions tables. Adapters perform the actual GitHub operations
after validation passes.
"""

from __future__ import annotations

from .catalog import CATALOG, NodeType, Status
from .exceptions import (
    JurisdictionViolation,
    ParentTypeViolation,
    StatusViolation,
    SupersedeViolation,
    TriggeredByViolation,
)
from .permissions import (
    ALWAYS_PERMITTED_OPS,
    JURISDICTION,
    RESTRICTED_OPS,
    Role,
    TriggeredBy,
)


def validate_parent(node_type: NodeType, parent_type: NodeType | None) -> None:
    """Hard-reject if `parent_type` is not a legal parent for `node_type`.

    Args:
        node_type: The type of the node being created or updated.
        parent_type: The type of the proposed parent node, or `None` if no
            parent is being set (only legal for `vision`).

    Raises:
        ParentTypeViolation: If the parent type is incompatible per the
            catalog. Includes both directions of error: a non-root type
            given `parent_type=None`, or a root type (`vision`) given any
            non-None parent.
    """
    contract = CATALOG[node_type]

    if contract.valid_parent_types is None:
        # Root type — no parent allowed.
        if parent_type is not None:
            raise ParentTypeViolation(
                f"{node_type.value} is a root type and cannot have a parent "
                f"(got parent_type={parent_type.value})"
            )
        return

    if parent_type is None:
        raise ParentTypeViolation(
            f"{node_type.value} requires a parent of type "
            f"{{{', '.join(sorted(t.value for t in contract.valid_parent_types))}}}, "
            f"got None"
        )

    if parent_type not in contract.valid_parent_types:
        raise ParentTypeViolation(
            f"{node_type.value}.parent must be one of "
            f"{{{', '.join(sorted(t.value for t in contract.valid_parent_types))}}}, "
            f"got {parent_type.value}"
        )


def validate_status(node_type: NodeType, status: Status) -> None:
    """Hard-reject if `status` is not a legal value for `node_type`.

    Args:
        node_type: The type of the node.
        status: The status being requested (on create, on transition, etc.).

    Raises:
        StatusViolation: If the status is not in the type's `valid_statuses`.
    """
    contract = CATALOG[node_type]
    if status not in contract.valid_statuses:
        raise StatusViolation(
            f"{node_type.value} does not accept status {status.value!r}. "
            f"Legal statuses for {node_type.value}: "
            f"{{{', '.join(sorted(s.value for s in contract.valid_statuses))}}}"
        )


def validate_jurisdiction(node_type: NodeType, acting_role: Role) -> None:
    """Hard-reject if `acting_role` is not authorised to write `node_type`.

    Args:
        node_type: The type of the node being written.
        acting_role: The role the agent claims to be acting as.

    Raises:
        JurisdictionViolation: If `acting_role` is not in `JURISDICTION[node_type]`.
    """
    authorised = JURISDICTION[node_type]
    if acting_role not in authorised:
        raise JurisdictionViolation(
            f"role {acting_role.value!r} is not authorised to author "
            f"{node_type.value}. Authorised role(s): "
            f"{{{', '.join(sorted(r.value for r in authorised))}}}"
        )


def validate_triggered_by(operation: str, triggered_by: TriggeredBy) -> None:
    """Hard-reject if a hook/Action-invoked agent attempts a restricted op.

    Args:
        operation: The name of the API tool being invoked (e.g.
            `"transition_status"`). Must match an entry in either
            `RESTRICTED_OPS` or `ALWAYS_PERMITTED_OPS`.
        triggered_by: How the current write was initiated.

    Raises:
        TriggeredByViolation: If `triggered_by` is HOOK or ACTION and the
            operation is in `RESTRICTED_OPS`.
        ValueError: If `operation` is unknown (defensive — protects against
            typos at the API layer).
    """
    if operation in ALWAYS_PERMITTED_OPS:
        return
    if operation not in RESTRICTED_OPS:
        raise ValueError(
            f"unknown operation {operation!r}; expected one of "
            f"{sorted(RESTRICTED_OPS | ALWAYS_PERMITTED_OPS)}"
        )
    if triggered_by != TriggeredBy.HUMAN:
        raise TriggeredByViolation(
            f"operation {operation!r} is restricted when triggered_by="
            f"{triggered_by.value!r}. Hook- or Action-invoked agents may read "
            f"and comment but cannot mutate existing graph state. To perform "
            f"this operation, run it from an interactive session "
            f"(triggered_by=human)."
        )


def validate_supersede(
    superseding_type: NodeType,
    superseded_type: NodeType,
    superseding_id: str,
    superseded_id: str,
    superseded_current_status: Status,
) -> None:
    """Hard-reject if a supersede operation is malformed.

    Args:
        superseding_type: Type of the new node taking over.
        superseded_type: Type of the node being superseded.
        superseding_id: Identifier of the new node (typically `#N`).
        superseded_id: Identifier of the node being superseded.
        superseded_current_status: Current status of the node being superseded.

    Raises:
        SupersedeViolation: If the operation is self-superseding (same id),
            cross-type (different `NodeType`), or the target is already in
            `deprecated` (an explicitly retired node cannot be superseded;
            either un-deprecate first or open a new node without supersede).
    """
    if superseding_id == superseded_id:
        raise SupersedeViolation(
            f"cannot supersede a node with itself (id={superseding_id!r})"
        )
    if superseding_type != superseded_type:
        raise SupersedeViolation(
            f"supersede requires both nodes to be of the same type. "
            f"superseding {superseding_type.value} {superseding_id!r} cannot "
            f"supersede {superseded_type.value} {superseded_id!r}"
        )
    if superseded_current_status == Status.DEPRECATED:
        raise SupersedeViolation(
            f"node {superseded_id!r} is already deprecated and cannot be "
            f"superseded. An explicitly retired node cannot be replaced; "
            f"open a new node without supersede semantics if a successor is "
            f"intended."
        )
