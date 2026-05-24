"""The catalog of seven Issue Types and their per-type contracts.

Each entry in `CATALOG` codifies, for one `NodeType`, the framework's invariant
rules: which parent types are valid, which statuses are legal, where the
lifecycle starts, and which terminal states it can end at. The validators
(`engine/core/validators.py`) consult this table on every write.

Source of truth: (catalog of 7 types + status validation per type)
plus (anchor-pending pattern uses `draft` as initial for most types).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class NodeType(str, Enum):
    """The seven Issue Types the framework recognises."""

    VISION = "vision"
    GOAL = "goal"
    CAPABILITY = "capability"
    FEATURE = "feature"
    STORY = "story"
    SPEC = "spec"
    ADR = "adr"


class Status(str, Enum):
    """The union of all per-type statuses.

    Projects v2 exposes one "Status" select field at board level whose option
    list is this union. Each type's legal subset is enforced by the validators,
    not by the GitHub field itself.
    """

    # spine top-level (vision)
    ACTIVE = "active"

    # spine middle (goal, capability)
    DRAFT = "draft"
    DONE = "done"

    # universal terminal
    DEPRECATED = "deprecated"

    # feature / story
    BACKLOG = "backlog"
    IN_PROGRESS = "in-progress"
    REVIEW = "review"

    # spec
    READY_FOR_IMPLEMENTATION = "ready-for-implementation"
    IN_IMPLEMENTATION = "in-implementation"

    # adr
    PROPOSED = "proposed"
    ACCEPTED = "accepted"
    SUPERSEDED = "superseded"


@dataclass(frozen=True)
class TypeContract:
    """Per-type rules: parent constraints, valid statuses, lifecycle endpoints.

    Attributes:
        valid_parent_types: Set of `NodeType` that may be the parent of a node
            of this type. `None` means the type has no parent (root only —
            only `VISION` qualifies).
        valid_statuses: All statuses this type may ever hold.
        initial_status: The default status assigned on creation if the caller
            does not specify one.
        terminal_statuses: Statuses that mark the end of the lifecycle; a node
            in a terminal status is closed (`done`, `deprecated`, `superseded`).
    """

    valid_parent_types: frozenset[NodeType] | None
    valid_statuses: frozenset[Status]
    initial_status: Status
    terminal_statuses: frozenset[Status]


#: The catalog — single source of truth for the 7 Issue Types.
#: Codified from .
CATALOG: dict[NodeType, TypeContract] = {
    NodeType.VISION: TypeContract(
        valid_parent_types=None, # root — only one vision per project
        valid_statuses=frozenset({Status.ACTIVE, Status.DEPRECATED}),
        initial_status=Status.ACTIVE,
        terminal_statuses=frozenset({Status.DEPRECATED}),
    ),
    NodeType.GOAL: TypeContract(
        valid_parent_types=frozenset({NodeType.VISION}),
        valid_statuses=frozenset(
            {Status.DRAFT, Status.ACTIVE, Status.DONE, Status.DEPRECATED}
        ),
        initial_status=Status.DRAFT,
        terminal_statuses=frozenset({Status.DONE, Status.DEPRECATED}),
    ),
    NodeType.CAPABILITY: TypeContract(
        valid_parent_types=frozenset({NodeType.GOAL}),
        valid_statuses=frozenset(
            {Status.DRAFT, Status.ACTIVE, Status.DONE, Status.DEPRECATED}
        ),
        initial_status=Status.DRAFT,
        terminal_statuses=frozenset({Status.DONE, Status.DEPRECATED}),
    ),
    NodeType.FEATURE: TypeContract(
        valid_parent_types=frozenset({NodeType.CAPABILITY}),
        valid_statuses=frozenset(
            {
                Status.BACKLOG,
                Status.IN_PROGRESS,
                Status.REVIEW,
                Status.DONE,
                Status.DEPRECATED,
            }
        ),
        initial_status=Status.BACKLOG,
        terminal_statuses=frozenset({Status.DONE, Status.DEPRECATED}),
    ),
    NodeType.STORY: TypeContract(
        valid_parent_types=frozenset({NodeType.FEATURE}),
        valid_statuses=frozenset(
            {
                Status.BACKLOG,
                Status.IN_PROGRESS,
                Status.REVIEW,
                Status.DONE,
                Status.DEPRECATED,
            }
        ),
        initial_status=Status.BACKLOG,
        terminal_statuses=frozenset({Status.DONE, Status.DEPRECATED}),
    ),
    NodeType.SPEC: TypeContract(
        valid_parent_types=frozenset({NodeType.FEATURE}),
        valid_statuses=frozenset(
            {
                Status.DRAFT,
                Status.READY_FOR_IMPLEMENTATION,
                Status.IN_IMPLEMENTATION,
                Status.DONE,
                Status.DEPRECATED,
            }
        ),
        initial_status=Status.DRAFT,
        terminal_statuses=frozenset({Status.DONE, Status.DEPRECATED}),
    ),
    NodeType.ADR: TypeContract(
        # ADRs constrain ANY spine node: their parent is the spine node whose
        # scope the decision serves. The validator accepts any of the 6 spine
        # types as parent for ADR.
        valid_parent_types=frozenset(
            {
                NodeType.VISION,
                NodeType.GOAL,
                NodeType.CAPABILITY,
                NodeType.FEATURE,
                NodeType.STORY,
                NodeType.SPEC,
            }
        ),
        valid_statuses=frozenset(
            {
                Status.PROPOSED,
                Status.ACCEPTED,
                Status.SUPERSEDED,
                Status.DEPRECATED,
            }
        ),
        initial_status=Status.PROPOSED,
        terminal_statuses=frozenset({Status.SUPERSEDED, Status.DEPRECATED}),
    ),
}


def get_contract(node_type: NodeType) -> TypeContract:
    """Return the `TypeContract` for `node_type`.

    Raises:
        KeyError: if `node_type` is not in the catalog (should never happen
            given the closed `NodeType` enum, but defensive).
    """
    return CATALOG[node_type]
