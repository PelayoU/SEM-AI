"""Data model used by the API and the adapters.

Pure data classes — no behavior, no I/O. Used as the lingua franca between
the API layer (which orchestrates validation + delegates to adapters) and
the adapter layer (which translates to/from concrete backends).

Every adapter returns these types; the API layer returns them to the MCP
server which serializes them as JSON for the agent.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .catalog import NodeType, Status
from .permissions import Role


@dataclass(frozen=True)
class Node:
    """A graph node — the lingua franca between API and adapters.

    Maps 1:1 to a GitHub Issue (with Issue Type = `type`, body = `body`, etc.)
    on the GitHub backend. Future Jira / Linear adapters map it to their
    respective objects.
    """

    id: str
    type: NodeType
    title: str
    body: str
    status: Status
    parent_id: str | None
    related_ids: tuple[str, ...]
    labels: tuple[str, ...]
    created_at: str # ISO 8601 timestamp
    updated_at: str
    maintained_by_role: Role | None
    milestone: str | None


@dataclass(frozen=True)
class Finding:
    """A warn-level finding from `validate_node`.

    Not an exception — findings are surfaced alongside successful writes so
    the agent can act on them before treating the write as final. Sourced
    from the (future) `engine/checks/` library.
    """

    severity: str # "warning" | "info"
    code: str
    message: str


@dataclass(frozen=True)
class SizeEstimate:
    """Result of `estimate_size`. Methodology supplied by project skills."""

    node_id: str
    estimate: str # free-form ("8 story points", "M", "2-3 weeks", etc.)
    confidence: str # free-form ("low", "high", "anchored", etc.)
    rationale: str


@dataclass(frozen=True)
class ProjectMap:
    """The minimum project map injected by SessionStart (per framework SKILL).

    The agent reads this at session bootstrap to hold the strategic spine
    in context: every vision, goal, capability, and accepted ADR. Specs,
    features, and stories are read on demand.
    """

    vision: Node | None
    goals: tuple[Node, ...]
    capabilities: tuple[Node, ...]
    accepted_adrs: tuple[Node, ...]


@dataclass(frozen=True)
class TreeNode:
    """A node in a tree query result, with its sub-issue children inlined."""

    node: Node
    children: tuple["TreeNode", ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Milestone:
    """A GitHub Milestone."""

    number: int
    title: str
    state: str # "open" | "closed"
    due_on: str | None
    body: str
    url: str


@dataclass(frozen=True)
class Release:
    """A GitHub Release."""

    tag: str
    name: str
    body: str
    published_at: str
    url: str


@dataclass(frozen=True)
class InstanceConfig:
    """Project-level configuration the adapter exposes to the agent.

    Sourced from `.sem-ai/config.yaml` + env var overrides. The API tool
    `get_instance_config` returns this so the agent can introspect the
    repo it's operating on.
    """

    repo: str # "owner/name"
    backend: str # "github" for v0.3.0
    project_id: str | None # Projects v2 number or null if not provisioned
    default_milestone: str | None
