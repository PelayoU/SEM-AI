"""Hard-reject exceptions raised by the validators.

the engine MCP **hard-rejects** parent-type,
jurisdiction, lifecycle, and triggered_by violations. These are mechanical,
not discretionary — the agent receives a structured error and adjusts.

Soft / warning-level issues (missing template sections, forbidden patterns,
security cross-section gaps) are handled by `engine/checks/` library and are
not exceptions — they are findings posted as warnings alongside successful
writes.
"""

from __future__ import annotations


class FrameworkRejection(Exception):
    """Base class for all engine hard-rejections.

    Any operation that violates the framework's structural contracts raises a
    subclass of this. The MCP server translates these into MCP errors with
    legible messages the agent can act on.
    """

    def __init__(self, message: str, *, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code or self.__class__.__name__


class ParentTypeViolation(FrameworkRejection):
    """Raised when the parent's `NodeType` is not valid for the child type.

    Example: trying to create a `goal` whose `parent` is a `feature`. A
    goal's parent must be a `vision`.
    """


class StatusViolation(FrameworkRejection):
    """Raised when the requested status is not legal for this `NodeType`.

    Example: trying to set status `proposed` on a `vision` — that status only
    applies to `adr`. Each NodeType has a closed set of legal statuses.
    """


class JurisdictionViolation(FrameworkRejection):
    """Raised when the `acting_role` is not authorised to author this type.

    Example: a `developer` trying to create a `goal`. Per the role-jurisdiction
    map: only `product-manager` writes spine nodes (vision/goal/capability/
    feature/story/spec); only `architect` writes `adr`.
    """


class TriggeredByViolation(FrameworkRejection):
    """Raised when a hook- or Action-invoked agent attempts a restricted op.

    `triggered_by` of HOOK or ACTION restricts the agent
    to read + comment + open new Issues. Operations that mutate existing
    graph state (update_node, transition_status, set_related, supersede,
    add_label, remove_label, assign_to_milestone, publish_release) are
    blocked.
    """


class SupersedeViolation(FrameworkRejection):
    """Raised when a supersede operation is malformed.

    Examples:
        - Trying to supersede a node with itself (self-loop).
        - The superseding and superseded nodes are not of the same `NodeType`.
        - The superseded node is already in a terminal status that disallows
          supersede.
    """
