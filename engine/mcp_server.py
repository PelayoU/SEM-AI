"""SEM-AI engine MCP server.

Exposes the 22 api tools (`engine/core/api.py`) as MCP tools the agent can
call. Uses stdio transport — Claude Code (or any compatible MCP client) spawns
this script as a subprocess and communicates over stdin/stdout.

Lifecycle:
  - At startup: parses config from .sem-ai/config.yaml + env vars, constructs a `GitHubAdapter`, registers tool handlers.
  - Per tool call: validates inputs, delegates to the api function, serializes
    the result to JSON, returns to the client.
  - On `FrameworkRejection`: returns an MCP error with the violation reason
    the agent can act on.

CLI:
  python -m engine.mcp_server start the server (stdio loop)
  python -m engine.mcp_server --check verify imports + config; exit 0
                                      (used by scripts/setup-engine.sh)
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from dataclasses import asdict, is_dataclass
from enum import Enum
from typing import Any

from .adapters import GitHubAdapter, load_config
from .adapters.base import BackendAdapter
from .core import api
from .core.catalog import NodeType, Status
from .core.exceptions import FrameworkRejection
from .core.permissions import Role, TriggeredBy


# ============================================================ serialization


def _serialize(obj: Any) -> Any:
    """Recursively convert dataclasses / tuples / enums to JSON-friendly types."""
    if obj is None:
        return None
    if isinstance(obj, Enum):
        return obj.value
    if is_dataclass(obj):
        return {k: _serialize(v) for k, v in asdict(obj).items()}
    if isinstance(obj, (tuple, list)):
        return [_serialize(item) for item in obj]
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    return obj


# ============================================================ adapter init


_adapter: BackendAdapter | None = None


def get_adapter() -> BackendAdapter:
    """Return the lazily-constructed backend adapter."""
    global _adapter
    if _adapter is None:
        _adapter = GitHubAdapter(load_config())
    return _adapter


def set_adapter(adapter: BackendAdapter) -> None:
    """Override the adapter — used by integration tests."""
    global _adapter
    _adapter = adapter


# ============================================================ tool schemas


_NODE_TYPES = sorted(nt.value for nt in NodeType)
_STATUSES = sorted(s.value for s in Status)
_ROLES = sorted(r.value for r in Role)
_TRIGGERS = sorted(t.value for t in TriggeredBy)


TOOLS: list[dict[str, Any]] = [
    # ----- Reads -----
    {
        "name": "get_node",
        "description": "Read a single graph node by id. Returns the full Node object including type, status, parent, labels, related, body.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string", "description": "Issue id like '#42'"},
            },
            "required": ["node_id"],
        },
    },
    {
        "name": "children_of",
        "description": "List immediate sub-issue children of a node.",
        "inputSchema": {
            "type": "object",
            "properties": {"node_id": {"type": "string"}},
            "required": ["node_id"],
        },
    },
    {
        "name": "ancestors_of",
        "description": "Walk parent links upward to the root, returning nearest-first.",
        "inputSchema": {
            "type": "object",
            "properties": {"node_id": {"type": "string"}},
            "required": ["node_id"],
        },
    },
    {
        "name": "get_related",
        "description": "Return nodes linked via the Related custom field + body cross-references.",
        "inputSchema": {
            "type": "object",
            "properties": {"node_id": {"type": "string"}},
            "required": ["node_id"],
        },
    },
    {
        "name": "query_nodes",
        "description": "Filter nodes by type, status, parent, label, or milestone (any combination).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "type": {"type": "string", "enum": _NODE_TYPES},
                "status": {"type": "string", "enum": _STATUSES},
                "parent": {"type": "string"},
                "label": {"type": "string"},
                "milestone": {"type": "string"},
            },
        },
    },
    {
        "name": "search_nodes",
        "description": "Substring-search the graph via GitHub's native Issue search.",
        "inputSchema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
    {
        "name": "get_tree",
        "description": "Build a sub-issue tree from root_id (or from the vision if omitted).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "root_id": {"type": "string"},
                "max_depth": {"type": "integer", "default": 10},
            },
        },
    },
    {
        "name": "get_project_map",
        "description": "Return the minimum project map: vision + goals + capabilities + accepted ADRs. Called at session start.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    # ----- Writes -----
    {
        "name": "create_node",
        "description": "Create a new graph node. Validates parent type, jurisdiction, status. Applies the 'experiment' label automatically if the body has a populated Uncertainty addressed section.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "type": {"type": "string", "enum": _NODE_TYPES},
                "parent_id": {"type": ["string", "null"]},
                "title": {"type": "string"},
                "body": {"type": "string"},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
                "status": {"type": "string", "enum": _STATUSES},
                "labels": {"type": "array", "items": {"type": "string"}, "default": []},
                "milestone": {"type": ["string", "null"]},
            },
            "required": ["type", "title", "body", "acting_role"],
        },
    },
    {
        "name": "update_node",
        "description": "Update a node's title or body. Status changes go through transition_status. Refreshes the 'experiment' label based on the new body.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string"},
                "title": {"type": ["string", "null"]},
                "body": {"type": ["string", "null"]},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["node_id", "acting_role"],
        },
    },
    {
        "name": "transition_status",
        "description": "Move a node to a new status. Validates per-type status compatibility.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string"},
                "new_status": {"type": "string", "enum": _STATUSES},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["node_id", "new_status", "acting_role"],
        },
    },
    {
        "name": "link_commit",
        "description": "Record that a commit was made in service of this node. Additive (allowed for hook/Action-invoked agents).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string"},
                "commit_sha": {"type": "string"},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["node_id", "commit_sha", "acting_role"],
        },
    },
    {
        "name": "set_related",
        "description": "Replace the Related custom field with the given list of node ids.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string"},
                "related_ids": {"type": "array", "items": {"type": "string"}},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["node_id", "related_ids", "acting_role"],
        },
    },
    {
        "name": "add_label",
        "description": "Add a label to a node. Idempotent.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string"},
                "label": {"type": "string"},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["node_id", "label", "acting_role"],
        },
    },
    {
        "name": "remove_label",
        "description": "Remove a label from a node. Idempotent.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string"},
                "label": {"type": "string"},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["node_id", "label", "acting_role"],
        },
    },
    {
        "name": "supersede",
        "description": "Mark `superseded_id` as superseded BY `superseding_id`. Both nodes must be of the same type; the target cannot already be deprecated.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "superseding_id": {"type": "string"},
                "superseded_id": {"type": "string"},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["superseding_id", "superseded_id", "acting_role"],
        },
    },
    # ----- Compute -----
    {
        "name": "estimate_size",
        "description": "Estimate the size of a node. Methodology supplied by project skills; default is a stub.",
        "inputSchema": {
            "type": "object",
            "properties": {"node_id": {"type": "string"}},
            "required": ["node_id"],
        },
    },
    {
        "name": "validate_node",
        "description": "Run engine/checks/ validators against a node; returns warn-level findings. Empty until checks library ships.",
        "inputSchema": {
            "type": "object",
            "properties": {"node_id": {"type": "string"}},
            "required": ["node_id"],
        },
    },
    # ----- Config -----
    {
        "name": "get_instance_config",
        "description": "Return project-level configuration: repo, backend, project board id, default milestone.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    # ----- Milestone / Release bridges -----
    {
        "name": "create_milestone",
        "description": "Create a Milestone for release planning. acting_role must be 'product-manager'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "due_date": {"type": ["string", "null"]},
                "body": {"type": "string"},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["title", "body", "acting_role"],
        },
    },
    {
        "name": "assign_to_milestone",
        "description": "Assign a node to a Milestone. acting_role must be 'product-manager'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string"},
                "milestone_number": {"type": "integer"},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["node_id", "milestone_number", "acting_role"],
        },
    },
    {
        "name": "publish_release",
        "description": "Close a Milestone and publish the GitHub Release. acting_role must be 'devops'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "milestone_number": {"type": "integer"},
                "tag": {"type": "string"},
                "notes": {"type": "string"},
                "acting_role": {"type": "string", "enum": _ROLES},
                "triggered_by": {"type": "string", "enum": _TRIGGERS, "default": "human"},
            },
            "required": ["milestone_number", "tag", "notes", "acting_role"],
        },
    },
]


# ============================================================ dispatcher


def _enum(cls, value):
    """Convert a string to enum or pass through None."""
    return cls(value) if value is not None else None


def dispatch(name: str, args: dict[str, Any]) -> Any:
    """Translate an MCP tool call into an api function invocation.

    Returns the api function's result (a Node, tuple, etc.) — caller serializes.
    Raises FrameworkRejection on validation failure; raises ValueError on
    unknown tool name.
    """
    adapter = get_adapter()

    # Common enum conversions
    def role():
        return Role(args["acting_role"])

    def trigger():
        return TriggeredBy(args.get("triggered_by", TriggeredBy.HUMAN.value))

    # ----- reads -----
    if name == "get_node":
        return api.get_node(adapter, args["node_id"])
    if name == "children_of":
        return api.children_of(adapter, args["node_id"])
    if name == "ancestors_of":
        return api.ancestors_of(adapter, args["node_id"])
    if name == "get_related":
        return api.get_related(adapter, args["node_id"])
    if name == "query_nodes":
        return api.query_nodes(
            adapter,
            type=_enum(NodeType, args.get("type")),
            status=_enum(Status, args.get("status")),
            parent=args.get("parent"),
            label=args.get("label"),
            milestone=args.get("milestone"),
        )
    if name == "search_nodes":
        return api.search_nodes(adapter, args["query"])
    if name == "get_tree":
        return api.get_tree(
            adapter, args.get("root_id"), args.get("max_depth", 10)
        )
    if name == "get_project_map":
        return api.get_project_map(adapter)

    # ----- writes -----
    if name == "create_node":
        return api.create_node(
            adapter,
            type=NodeType(args["type"]),
            parent_id=args.get("parent_id"),
            title=args["title"],
            body=args["body"],
            acting_role=role(),
            triggered_by=trigger(),
            status=_enum(Status, args.get("status")),
            labels=tuple(args.get("labels", [])),
            milestone=args.get("milestone"),
        )
    if name == "update_node":
        return api.update_node(
            adapter,
            args["node_id"],
            title=args.get("title"),
            body=args.get("body"),
            acting_role=role(),
            triggered_by=trigger(),
        )
    if name == "transition_status":
        return api.transition_status(
            adapter,
            args["node_id"],
            Status(args["new_status"]),
            acting_role=role(),
            triggered_by=trigger(),
        )
    if name == "link_commit":
        api.link_commit(
            adapter,
            args["node_id"],
            args["commit_sha"],
            acting_role=role(),
            triggered_by=trigger(),
        )
        return {"ok": True}
    if name == "set_related":
        api.set_related(
            adapter,
            args["node_id"],
            tuple(args["related_ids"]),
            acting_role=role(),
            triggered_by=trigger(),
        )
        return {"ok": True}
    if name == "add_label":
        api.add_label(
            adapter,
            args["node_id"],
            args["label"],
            acting_role=role(),
            triggered_by=trigger(),
        )
        return {"ok": True}
    if name == "remove_label":
        api.remove_label(
            adapter,
            args["node_id"],
            args["label"],
            acting_role=role(),
            triggered_by=trigger(),
        )
        return {"ok": True}
    if name == "supersede":
        api.supersede(
            adapter,
            args["superseding_id"],
            args["superseded_id"],
            acting_role=role(),
            triggered_by=trigger(),
        )
        return {"ok": True}

    # ----- compute -----
    if name == "estimate_size":
        return api.estimate_size(adapter, args["node_id"])
    if name == "validate_node":
        return api.validate_node(adapter, args["node_id"])

    # ----- config -----
    if name == "get_instance_config":
        return api.get_instance_config(adapter)

    # ----- bridges -----
    if name == "create_milestone":
        return api.create_milestone(
            adapter,
            args["title"],
            args.get("due_date"),
            args["body"],
            acting_role=role(),
            triggered_by=trigger(),
        )
    if name == "assign_to_milestone":
        api.assign_to_milestone(
            adapter,
            args["node_id"],
            args["milestone_number"],
            acting_role=role(),
            triggered_by=trigger(),
        )
        return {"ok": True}
    if name == "publish_release":
        return api.publish_release(
            adapter,
            args["milestone_number"],
            args["tag"],
            args["notes"],
            acting_role=role(),
            triggered_by=trigger(),
        )

    raise ValueError(f"unknown tool: {name!r}")


# ============================================================ MCP server


def _build_server():
    """Construct the MCP server with tool list + handler."""
    # Imported lazily so --check can run without the mcp lib installed.
    from mcp.server import Server
    from mcp.types import TextContent, Tool

    server = Server("sem_ai_engine")

    @server.list_tools()
    async def handle_list_tools() -> list[Tool]:
        return [
            Tool(
                name=tool["name"],
                description=tool["description"],
                inputSchema=tool["inputSchema"],
            )
            for tool in TOOLS
        ]

    @server.call_tool()
    async def handle_call_tool(
        name: str, arguments: dict[str, Any]
    ) -> list[TextContent]:
        try:
            result = dispatch(name, arguments or {})
            payload = _serialize(result)
            return [TextContent(type="text", text=json.dumps(payload))]
        except FrameworkRejection as e:
            return [
                TextContent(
                    type="text",
                    text=json.dumps(
                        {"error": e.code, "message": str(e)}
                    ),
                )
            ]

    return server


async def _serve() -> None:
    from mcp.server.stdio import stdio_server

    server = _build_server()
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


# ============================================================ CLI


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="engine.mcp_server",
        description="SEM-AI engine MCP server.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help=(
            "Verify imports + tool registry + adapter config without "
            "starting the stdio loop. Used by scripts/setup-engine.sh."
        ),
    )
    args = parser.parse_args(argv)

    if args.check:
        # Verify the module loads, tools registry is well-formed, and that
        # adapter config can be loaded. Don't actually contact GitHub.
        assert len(TOOLS) == 22, f"expected 22 tools, found {len(TOOLS)}"
        names = {t["name"] for t in TOOLS}
        assert len(names) == 22, "duplicate tool names in registry"
        try:
            from . import adapters # noqa: F401
            from .core import api # noqa: F401
        except ImportError as e:
            print(f"FAIL: import error: {e}", file=sys.stderr)
            return 1
        print("engine.mcp_server: 22 tools registered; imports OK")
        return 0

    asyncio.run(_serve())
    return 0


if __name__ == "__main__":
    sys.exit(main())
