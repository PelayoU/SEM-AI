"""Integration tests for `engine.mcp_server`.

Tests focus on:
  - _serialize handles all return types correctly
  - dispatch() routes each MCP tool call to the right api function with
    the right argument conversions (enums, tuples, etc.)
  - The --check CLI mode validates the tool registry

The tests use MockAdapter (from conftest.py) injected via set_adapter().
The actual MCP stdio transport is not tested here — it would require
spawning a subprocess and writing JSON-RPC by hand. That is deferred.
"""

from __future__ import annotations

import pytest

from engine import mcp_server
from engine.core.catalog import NodeType, Status
from engine.core.exceptions import (
    FrameworkRejection,
    JurisdictionViolation,
    ParentTypeViolation,
)
from engine.core.models import Node
from engine.core.permissions import Role

from .conftest import MockAdapter


# ----- fixtures -------------------------------------------------------------


@pytest.fixture(autouse=True)
def reset_adapter():
    """Reset the module-level adapter between tests."""
    mcp_server._adapter = None
    yield
    mcp_server._adapter = None


@pytest.fixture
def mock_adapter():
    """Mock adapter wired into the mcp_server module."""
    adapter = MockAdapter()
    mcp_server.set_adapter(adapter)
    return adapter


# ----- _serialize -----------------------------------------------------------


class TestSerialize:
    def test_none(self):
        assert mcp_server._serialize(None) is None

    def test_primitives(self):
        assert mcp_server._serialize("abc") == "abc"
        assert mcp_server._serialize(42) == 42
        assert mcp_server._serialize(True) is True

    def test_enum(self):
        assert mcp_server._serialize(NodeType.GOAL) == "goal"
        assert mcp_server._serialize(Status.ACTIVE) == "active"
        assert mcp_server._serialize(Role.PM) == "product-manager"

    def test_dataclass(self):
        node = Node(
            id="#1",
            type=NodeType.VISION,
            title="V",
            body="",
            status=Status.ACTIVE,
            parent_id=None,
            related_ids=(),
            labels=(),
            created_at="2026-05-24T00:00:00Z",
            updated_at="2026-05-24T00:00:00Z",
            maintained_by_role=Role.PM,
            milestone=None,
        )
        result = mcp_server._serialize(node)
        assert result["id"] == "#1"
        assert result["type"] == "vision"
        assert result["status"] == "active"
        assert result["maintained_by_role"] == "product-manager"
        assert result["parent_id"] is None

    def test_tuple_of_dataclasses(self):
        node1 = Node(
            id="#1", type=NodeType.GOAL, title="g", body="",
            status=Status.DRAFT, parent_id=None, related_ids=(),
            labels=(), created_at="", updated_at="",
            maintained_by_role=Role.PM, milestone=None,
        )
        result = mcp_server._serialize((node1,))
        assert isinstance(result, list)
        assert result[0]["type"] == "goal"


# ----- TOOLS registry -------------------------------------------------------


class TestToolsRegistry:
    def test_has_22_tools(self):
        assert len(mcp_server.TOOLS) == 22

    def test_tool_names_unique(self):
        names = [t["name"] for t in mcp_server.TOOLS]
        assert len(set(names)) == len(names)

    def test_every_tool_has_required_fields(self):
        for tool in mcp_server.TOOLS:
            assert "name" in tool
            assert "description" in tool
            assert "inputSchema" in tool
            assert tool["inputSchema"]["type"] == "object"

    def test_specific_tools_present(self):
        names = {t["name"] for t in mcp_server.TOOLS}
        # Reads (8)
        for n in [
            "get_node", "children_of", "ancestors_of", "get_related",
            "query_nodes", "search_nodes", "get_tree", "get_project_map",
        ]:
            assert n in names
        # Writes (8)
        for n in [
            "create_node", "update_node", "transition_status", "link_commit",
            "set_related", "add_label", "remove_label", "supersede",
        ]:
            assert n in names
        # Compute (2)
        assert "estimate_size" in names
        assert "validate_node" in names
        # Config (1)
        assert "get_instance_config" in names
        # Bridges (3)
        for n in ["create_milestone", "assign_to_milestone", "publish_release"]:
            assert n in names


# ----- dispatcher: reads ----------------------------------------------------


class TestDispatchReads:
    def test_get_node(self, mock_adapter: MockAdapter):
        node = mock_adapter.seed_node(
            id="#1", type=NodeType.VISION, status=Status.ACTIVE
        )
        result = mcp_server.dispatch("get_node", {"node_id": "#1"})
        assert result.id == "#1"
        assert result.type == NodeType.VISION

    def test_children_of(self, mock_adapter: MockAdapter):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        mock_adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        result = mcp_server.dispatch("children_of", {"node_id": "#1"})
        assert len(result) == 1

    def test_query_nodes_filters_by_type(self, mock_adapter: MockAdapter):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        mock_adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        mock_adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        result = mcp_server.dispatch("query_nodes", {"type": "goal"})
        assert len(result) == 2

    def test_query_nodes_no_filters(self, mock_adapter: MockAdapter):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        mock_adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        result = mcp_server.dispatch("query_nodes", {})
        assert len(result) == 2

    def test_get_project_map(self, mock_adapter: MockAdapter):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        mock_adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        result = mcp_server.dispatch("get_project_map", {})
        assert result.vision.id == "#1"
        assert len(result.goals) == 1


# ----- dispatcher: writes ---------------------------------------------------


class TestDispatchWrites:
    def test_create_node(self, mock_adapter: MockAdapter):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        result = mcp_server.dispatch(
            "create_node",
            {
                "type": "goal",
                "parent_id": "#1",
                "title": "Increase retention",
                "body": "",
                "acting_role": "product-manager",
            },
        )
        assert result.type == NodeType.GOAL
        assert result.parent_id == "#1"

    def test_create_node_with_wrong_parent_type_raises(
        self, mock_adapter: MockAdapter
    ):
        mock_adapter.seed_node(
            id="#1", type=NodeType.FEATURE, status=Status.BACKLOG
        )
        with pytest.raises(ParentTypeViolation):
            mcp_server.dispatch(
                "create_node",
                {
                    "type": "goal",
                    "parent_id": "#1",
                    "title": "g",
                    "body": "",
                    "acting_role": "product-manager",
                },
            )

    def test_create_node_by_unauthorised_role_raises(
        self, mock_adapter: MockAdapter
    ):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        with pytest.raises(JurisdictionViolation):
            mcp_server.dispatch(
                "create_node",
                {
                    "type": "goal",
                    "parent_id": "#1",
                    "title": "g",
                    "body": "",
                    "acting_role": "developer",
                },
            )

    def test_transition_status(self, mock_adapter: MockAdapter):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        node = mock_adapter.seed_node(
            type=NodeType.GOAL, parent_id="#1", status=Status.DRAFT
        )
        result = mcp_server.dispatch(
            "transition_status",
            {
                "node_id": node.id,
                "new_status": "active",
                "acting_role": "product-manager",
            },
        )
        assert result.status == Status.ACTIVE

    def test_link_commit_returns_ok(self, mock_adapter: MockAdapter):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        node = mock_adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        result = mcp_server.dispatch(
            "link_commit",
            {
                "node_id": node.id,
                "commit_sha": "abc123",
                "acting_role": "developer",
            },
        )
        assert result == {"ok": True}

    def test_set_related_converts_list_to_tuple(
        self, mock_adapter: MockAdapter
    ):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        node = mock_adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        result = mcp_server.dispatch(
            "set_related",
            {
                "node_id": node.id,
                "related_ids": ["#99", "#88"],
                "acting_role": "product-manager",
            },
        )
        assert result == {"ok": True}
        assert mock_adapter.nodes[node.id].related_ids == ("#99", "#88")


# ----- dispatcher: triggered_by --------------------------------------------


class TestDispatchTriggeredBy:
    def test_default_is_human(self, mock_adapter: MockAdapter):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        node = mock_adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        # No triggered_by passed → default 'human' → transition allowed
        mcp_server.dispatch(
            "transition_status",
            {
                "node_id": node.id,
                "new_status": "active",
                "acting_role": "product-manager",
            },
        )

    def test_hook_blocks_restricted_op(self, mock_adapter: MockAdapter):
        mock_adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        node = mock_adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        with pytest.raises(FrameworkRejection):
            mcp_server.dispatch(
                "transition_status",
                {
                    "node_id": node.id,
                    "new_status": "active",
                    "acting_role": "product-manager",
                    "triggered_by": "hook",
                },
            )


# ----- dispatcher: bridges --------------------------------------------------


class TestDispatchBridges:
    def test_create_milestone_by_pm(self, mock_adapter: MockAdapter):
        result = mcp_server.dispatch(
            "create_milestone",
            {
                "title": "v1.0",
                "due_date": "2026-12-01",
                "body": "Release plan",
                "acting_role": "product-manager",
            },
        )
        assert result.number == 1

    def test_publish_release_by_devops(self, mock_adapter: MockAdapter):
        # PM creates first
        m = mcp_server.dispatch(
            "create_milestone",
            {
                "title": "v1.0",
                "body": "",
                "acting_role": "product-manager",
            },
        )
        result = mcp_server.dispatch(
            "publish_release",
            {
                "milestone_number": m.number,
                "tag": "v1.0",
                "notes": "First release",
                "acting_role": "devops",
            },
        )
        assert result.tag == "v1.0"


# ----- dispatcher: errors ---------------------------------------------------


class TestDispatchErrors:
    def test_unknown_tool_raises_value_error(self, mock_adapter: MockAdapter):
        with pytest.raises(ValueError, match="unknown tool"):
            mcp_server.dispatch("nonexistent_tool", {})


# ----- CLI --check ----------------------------------------------------------


class TestCheckMode:
    def test_check_returns_zero_with_valid_registry(self, capsys, monkeypatch):
        # --check verifies the tool registry, not the adapter. Use a dummy
        # SEM_AI_REPO so load_config doesn't choke if it were invoked
        # (currently --check doesn't call load_config).
        monkeypatch.setenv("SEM_AI_REPO", "test/repo")
        rc = mcp_server.main(["--check"])
        out = capsys.readouterr().out
        assert rc == 0
        assert "22 tools registered" in out
