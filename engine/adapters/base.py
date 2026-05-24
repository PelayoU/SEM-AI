"""Abstract backend adapter — the contract every concrete adapter implements.

The api layer (`engine/core/api.py`) talks ONLY to this interface; it never
touches GitHub / Jira / Linear directly. This is what makes backends
swappable per ADR-004 update + ADR-009.

The interface is internal to the engine — adopters do not implement adapters
themselves. New adapters are framework contributions per ADR-008
extensibility boundary.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from ..core.catalog import NodeType, Status
from ..core.models import (
    InstanceConfig,
    Milestone,
    Node,
    ProjectMap,
    Release,
    TreeNode,
)
from ..core.permissions import Role


class BackendAdapter(ABC):
    """Contract for a graph backend.

    Concrete subclasses (`GitHubAdapter`, future `JiraAdapter`, etc.) translate
    these methods into backend-specific calls. The methods are deliberately
    granular — each maps to a focused backend operation; the api layer
    orchestrates compound operations (e.g. `create_node` calls `create_issue`
    + `link_sub_issue` + `set_status` atomically).
    """

    # ----- Reads -----

    @abstractmethod
    def get_issue(self, issue_id: str) -> Node:
        """Read a single Issue by id and return it as a Node."""

    @abstractmethod
    def list_sub_issues(self, parent_id: str) -> tuple[Node, ...]:
        """List the immediate children (sub-issue links) of the given parent."""

    @abstractmethod
    def ancestors(self, issue_id: str) -> tuple[Node, ...]:
        """Walk parent links upward to the root, returning nearest-first."""

    @abstractmethod
    def list_related(self, issue_id: str) -> tuple[Node, ...]:
        """Return issues linked via the Related custom field + cross-refs."""

    @abstractmethod
    def query_issues(
        self,
        *,
        type: NodeType | None = None,
        status: Status | None = None,
        parent: str | None = None,
        label: str | None = None,
        milestone: str | None = None,
    ) -> tuple[Node, ...]:
        """Filter Issues by any combination of the criteria."""

    @abstractmethod
    def search_issues(self, query: str) -> tuple[Node, ...]:
        """Substring-search Issues via the backend's native search."""

    @abstractmethod
    def tree(self, root_id: str | None, max_depth: int) -> TreeNode:
        """Build a sub-issue tree from root_id (or the vision if None)."""

    @abstractmethod
    def project_map(self) -> ProjectMap:
        """Return the minimum project map: vision + goals + capabilities + accepted ADRs."""

    # ----- Writes -----

    @abstractmethod
    def create_issue(
        self,
        *,
        type: NodeType,
        title: str,
        body: str,
        status: Status,
        parent_id: str | None,
        acting_role: Role,
        labels: tuple[str, ...] = (),
        milestone: str | None = None,
    ) -> Node:
        """Create a new Issue with type + parent link + initial status + label."""

    @abstractmethod
    def update_issue(
        self,
        issue_id: str,
        *,
        title: str | None = None,
        body: str | None = None,
        acting_role: Role,
    ) -> Node:
        """Update title or body of an existing Issue."""

    @abstractmethod
    def set_status(self, issue_id: str, status: Status, *, acting_role: Role) -> Node:
        """Set the Projects v2 Status custom field for the Issue."""

    @abstractmethod
    def link_commit(self, issue_id: str, commit_sha: str, *, acting_role: Role) -> None:
        """Record that a commit was made in service of this issue."""

    @abstractmethod
    def set_related(
        self, issue_id: str, related_ids: tuple[str, ...], *, acting_role: Role
    ) -> None:
        """Replace the Issue's Related custom field with the given list."""

    @abstractmethod
    def add_label(self, issue_id: str, label: str, *, acting_role: Role) -> None:
        """Add a label to the Issue (idempotent)."""

    @abstractmethod
    def remove_label(self, issue_id: str, label: str, *, acting_role: Role) -> None:
        """Remove a label from the Issue (idempotent)."""

    @abstractmethod
    def supersede(
        self,
        superseding_id: str,
        superseded_id: str,
        *,
        acting_role: Role,
    ) -> None:
        """Link superseded_id as superseded BY superseding_id; close the chain."""

    # ----- Milestone / Release bridges (ADR-001 § Milestone and Release operations) -----

    @abstractmethod
    def create_milestone(
        self,
        title: str,
        due_date: str | None,
        body: str,
        *,
        acting_role: Role,
    ) -> Milestone:
        """Create a Milestone on the backend."""

    @abstractmethod
    def assign_to_milestone(
        self, issue_id: str, milestone_number: int, *, acting_role: Role
    ) -> None:
        """Assign an Issue to a Milestone."""

    @abstractmethod
    def publish_release(
        self,
        milestone_number: int,
        tag: str,
        notes: str,
        *,
        acting_role: Role,
    ) -> Release:
        """Close the Milestone and publish a GitHub Release with given tag + notes."""

    # ----- Config -----

    @abstractmethod
    def instance_config(self) -> InstanceConfig:
        """Return the project-level configuration the agent introspects."""
