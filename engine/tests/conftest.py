"""Pytest fixtures + MockAdapter shared by the engine tests.

The MockAdapter implements `BackendAdapter` with in-memory storage. Tests use
it to verify the api layer's orchestration without touching GitHub. The
adapter conformance tests for the real github adapter live separately
(`test_github_adapter.py`, to be added in Bloque B2).
"""

from __future__ import annotations

from dataclasses import replace

import pytest

from engine.adapters.base import BackendAdapter
from engine.core.catalog import NodeType, Status
from engine.core.models import (
    InstanceConfig,
    Milestone,
    Node,
    ProjectMap,
    Release,
    TreeNode,
)
from engine.core.permissions import Role


class MockAdapter(BackendAdapter):
    """In-memory adapter for testing the api layer.

    Stores nodes, milestones, releases in plain dicts. No persistence between
    test cases (a fresh MockAdapter per test). Records every method call for
    assertion-friendly inspection (`adapter.calls`).
    """

    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}
        self.milestones: dict[int, Milestone] = {}
        self.releases: dict[str, Release] = {}
        self.next_issue_number = 1
        self.next_milestone_number = 1
        self.calls: list[tuple[str, dict]] = []

    # --- helpers ---

    def _record(self, name: str, **kwargs) -> None:
        self.calls.append((name, kwargs))

    def _new_id(self) -> str:
        nid = f"#{self.next_issue_number}"
        self.next_issue_number += 1
        return nid

    def _claim_id(self, explicit: str) -> str:
        """Mark an explicit id as used; bump the counter past it."""
        import re

        m = re.match(r"^#(\d+)$", explicit)
        if m:
            n = int(m.group(1))
            if n >= self.next_issue_number:
                self.next_issue_number = n + 1
        return explicit

    def seed_node(
        self,
        *,
        id: str | None = None,
        type: NodeType = NodeType.GOAL,
        title: str = "test",
        body: str = "",
        status: Status | None = None,
        parent_id: str | None = None,
        related_ids: tuple[str, ...] = (),
        labels: tuple[str, ...] = (),
        maintained_by_role: Role | None = None,
        milestone: str | None = None,
    ) -> Node:
        """Pre-populate a node — used by tests to set up scenarios."""
        node_id = self._claim_id(id) if id is not None else self._new_id()
        if status is None:
            from engine.core.catalog import CATALOG

            status = CATALOG[type].initial_status
        node = Node(
            id=node_id,
            type=type,
            title=title,
            body=body,
            status=status,
            parent_id=parent_id,
            related_ids=related_ids,
            labels=labels,
            created_at="2026-05-24T00:00:00Z",
            updated_at="2026-05-24T00:00:00Z",
            maintained_by_role=maintained_by_role,
            milestone=milestone,
        )
        self.nodes[node_id] = node
        return node

    # --- reads ---

    def get_issue(self, issue_id: str) -> Node:
        self._record("get_issue", issue_id=issue_id)
        if issue_id not in self.nodes:
            raise KeyError(f"node not found: {issue_id}")
        return self.nodes[issue_id]

    def list_sub_issues(self, parent_id: str) -> tuple[Node, ...]:
        self._record("list_sub_issues", parent_id=parent_id)
        return tuple(n for n in self.nodes.values() if n.parent_id == parent_id)

    def ancestors(self, issue_id: str) -> tuple[Node, ...]:
        self._record("ancestors", issue_id=issue_id)
        result: list[Node] = []
        current = self.nodes.get(issue_id)
        while current is not None and current.parent_id is not None:
            parent = self.nodes.get(current.parent_id)
            if parent is None:
                break
            result.append(parent)
            current = parent
        return tuple(result)

    def list_related(self, issue_id: str) -> tuple[Node, ...]:
        self._record("list_related", issue_id=issue_id)
        node = self.nodes.get(issue_id)
        if node is None:
            return ()
        return tuple(self.nodes[rid] for rid in node.related_ids if rid in self.nodes)

    def query_issues(
        self,
        *,
        type: NodeType | None = None,
        status: Status | None = None,
        parent: str | None = None,
        label: str | None = None,
        milestone: str | None = None,
    ) -> tuple[Node, ...]:
        self._record(
            "query_issues",
            type=type, status=status, parent=parent, label=label, milestone=milestone,
        )
        result = []
        for n in self.nodes.values():
            if type is not None and n.type != type:
                continue
            if status is not None and n.status != status:
                continue
            if parent is not None and n.parent_id != parent:
                continue
            if label is not None and label not in n.labels:
                continue
            if milestone is not None and n.milestone != milestone:
                continue
            result.append(n)
        return tuple(result)

    def search_issues(self, query: str) -> tuple[Node, ...]:
        self._record("search_issues", query=query)
        q = query.lower()
        return tuple(
            n for n in self.nodes.values()
            if q in n.title.lower() or q in n.body.lower()
        )

    def tree(self, root_id: str | None, max_depth: int) -> TreeNode:
        self._record("tree", root_id=root_id, max_depth=max_depth)
        if root_id is None:
            visions = [n for n in self.nodes.values() if n.type == NodeType.VISION]
            if not visions:
                raise KeyError("no vision in graph")
            root_id = visions[0].id

        def build(node_id: str, depth: int) -> TreeNode:
            node = self.nodes[node_id]
            if depth >= max_depth:
                return TreeNode(node=node, children=())
            children = tuple(
                build(c.id, depth + 1)
                for c in self.list_sub_issues(node_id)
            )
            return TreeNode(node=node, children=children)

        return build(root_id, 0)

    def project_map(self) -> ProjectMap:
        self._record("project_map")
        visions = [n for n in self.nodes.values() if n.type == NodeType.VISION]
        goals = tuple(n for n in self.nodes.values() if n.type == NodeType.GOAL)
        capabilities = tuple(
            n for n in self.nodes.values() if n.type == NodeType.CAPABILITY
        )
        accepted_adrs = tuple(
            n for n in self.nodes.values()
            if n.type == NodeType.ADR and n.status == Status.ACCEPTED
        )
        return ProjectMap(
            vision=visions[0] if visions else None,
            goals=goals,
            capabilities=capabilities,
            accepted_adrs=accepted_adrs,
        )

    # --- writes ---

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
        self._record(
            "create_issue", type=type, title=title, status=status,
            parent_id=parent_id, acting_role=acting_role, labels=labels,
        )
        node = self.seed_node(
            type=type, title=title, body=body, status=status,
            parent_id=parent_id, labels=labels,
            maintained_by_role=acting_role, milestone=milestone,
        )
        return node

    def update_issue(
        self,
        issue_id: str,
        *,
        title: str | None = None,
        body: str | None = None,
        acting_role: Role,
    ) -> Node:
        self._record("update_issue", issue_id=issue_id, title=title, body=body)
        existing = self.nodes[issue_id]
        updated = replace(
            existing,
            title=title if title is not None else existing.title,
            body=body if body is not None else existing.body,
            maintained_by_role=acting_role,
            updated_at="2026-05-24T00:00:01Z",
        )
        self.nodes[issue_id] = updated
        return updated

    def set_status(
        self, issue_id: str, status: Status, *, acting_role: Role
    ) -> Node:
        self._record("set_status", issue_id=issue_id, status=status)
        existing = self.nodes[issue_id]
        updated = replace(existing, status=status, maintained_by_role=acting_role)
        self.nodes[issue_id] = updated
        return updated

    def link_commit(
        self, issue_id: str, commit_sha: str, *, acting_role: Role
    ) -> None:
        self._record("link_commit", issue_id=issue_id, commit_sha=commit_sha)

    def set_related(
        self, issue_id: str, related_ids: tuple[str, ...], *, acting_role: Role
    ) -> None:
        self._record("set_related", issue_id=issue_id, related_ids=related_ids)
        existing = self.nodes[issue_id]
        self.nodes[issue_id] = replace(existing, related_ids=related_ids)

    def add_label(self, issue_id: str, label: str, *, acting_role: Role) -> None:
        self._record("add_label", issue_id=issue_id, label=label)
        existing = self.nodes[issue_id]
        if label not in existing.labels:
            self.nodes[issue_id] = replace(
                existing, labels=existing.labels + (label,)
            )

    def remove_label(self, issue_id: str, label: str, *, acting_role: Role) -> None:
        self._record("remove_label", issue_id=issue_id, label=label)
        existing = self.nodes[issue_id]
        if label in existing.labels:
            self.nodes[issue_id] = replace(
                existing,
                labels=tuple(lab for lab in existing.labels if lab != label),
            )

    def supersede(
        self, superseding_id: str, superseded_id: str, *, acting_role: Role
    ) -> None:
        self._record(
            "supersede",
            superseding_id=superseding_id, superseded_id=superseded_id,
        )
        sd = self.nodes[superseded_id]
        self.nodes[superseded_id] = replace(sd, status=Status.SUPERSEDED)

    # --- bridges ---

    def create_milestone(
        self, title: str, due_date: str | None, body: str, *, acting_role: Role,
    ) -> Milestone:
        self._record(
            "create_milestone", title=title, due_date=due_date, body=body,
        )
        num = self.next_milestone_number
        self.next_milestone_number += 1
        m = Milestone(
            number=num, title=title, state="open",
            due_on=due_date, body=body,
            url=f"https://example.com/milestone/{num}",
        )
        self.milestones[num] = m
        return m

    def assign_to_milestone(
        self, issue_id: str, milestone_number: int, *, acting_role: Role,
    ) -> None:
        self._record(
            "assign_to_milestone",
            issue_id=issue_id, milestone_number=milestone_number,
        )
        existing = self.nodes[issue_id]
        m = self.milestones[milestone_number]
        self.nodes[issue_id] = replace(existing, milestone=m.title)

    def publish_release(
        self, milestone_number: int, tag: str, notes: str, *, acting_role: Role,
    ) -> Release:
        self._record(
            "publish_release",
            milestone_number=milestone_number, tag=tag, notes=notes,
        )
        m = self.milestones[milestone_number]
        self.milestones[milestone_number] = replace(m, state="closed")
        rel = Release(
            tag=tag, name=tag, body=notes,
            published_at="2026-05-24T00:00:00Z",
            url=f"https://example.com/release/{tag}",
        )
        self.releases[tag] = rel
        return rel

    def instance_config(self) -> InstanceConfig:
        self._record("instance_config")
        return InstanceConfig(
            repo="example/test-repo", backend="github",
            project_id="42", default_milestone=None,
        )


@pytest.fixture
def adapter() -> MockAdapter:
    """A fresh MockAdapter per test."""
    return MockAdapter()


@pytest.fixture
def vision(adapter: MockAdapter) -> Node:
    """A pre-seeded vision node — the root of the graph for tests that need ancestry."""
    return adapter.seed_node(
        id="#1", type=NodeType.VISION, title="Vision",
        status=Status.ACTIVE, maintained_by_role=Role.PM,
    )
