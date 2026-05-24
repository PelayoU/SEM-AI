"""Role-jurisdiction matrix and triggered_by permission table.

Two enforcement mechanisms live here:

1. **JURISDICTION** — which `Role` is authorised to author each `NodeType`.
   The validator (`validate_jurisdiction`) rejects writes whose `acting_role`
   is not in the type's authorised set. Source: framework SKILL § role-
   jurisdiction map, derived from the six `.claude/agents/<role>.md` files.

2. **RESTRICTED_OPS** — operations that an agent invoked by hook or Action
   (i.e. `triggered_by != HUMAN`) is not allowed to perform. Auto-invoked
   agents read and comment freely, may open new bug/security-finding Issues,
   but cannot transition status or edit existing nodes. Source: ADR-004 update
   § restricted permissions for hook/Action-invoked agents.

The two mechanisms are independent: a write must pass both checks to proceed.
"""

from __future__ import annotations

from enum import Enum

from .catalog import NodeType


class Role(str, Enum):
    """The six canonical roles (framework SKILL § Working as roles)."""

    PM = "product-manager"
    ARCHITECT = "architect"
    DEVELOPER = "developer"
    QA = "qa"
    DEVOPS = "devops"
    SECURITY_OFFICER = "security-officer"


class TriggeredBy(str, Enum):
    """Who initiated the write (ADR-004 update).

    The MCP server defaults to HUMAN when the agent's prompt came from the
    interactive session. Hooks set HOOK; Actions set ACTION. These two trigger
    restricted permissions per `RESTRICTED_OPS`.
    """

    HUMAN = "human"
    HOOK = "hook"
    ACTION = "action"


#: Who can author / write each Issue Type.
#: Codified from framework SKILL § Working as roles + each agent.md.
JURISDICTION: dict[NodeType, frozenset[Role]] = {
    NodeType.VISION: frozenset({Role.PM}),
    NodeType.GOAL: frozenset({Role.PM}),
    NodeType.CAPABILITY: frozenset({Role.PM}),
    NodeType.FEATURE: frozenset({Role.PM}),
    NodeType.STORY: frozenset({Role.PM}),
    NodeType.SPEC: frozenset({Role.PM}),
    NodeType.ADR: frozenset({Role.ARCHITECT}),
}


#: Operations blocked when `triggered_by != TriggeredBy.HUMAN`.
#: Hooks and Actions may invoke agents reactively but those agents are
#: restricted to read + comment + open new Issues. They cannot mutate
#: existing graph state.
#: Source: ADR-004 update § restricted permissions for hook/Action-invoked
#: agents.
RESTRICTED_OPS: frozenset[str] = frozenset(
    {
        "update_node",
        "transition_status",
        "set_related",
        "supersede",
        "add_label",
        "remove_label",
        "assign_to_milestone",
        "publish_release",
    }
)


#: Operations always permitted regardless of `triggered_by`.
#: These are read-only or additive operations that cannot corrupt graph state.
ALWAYS_PERMITTED_OPS: frozenset[str] = frozenset(
    {
        "get_node",
        "children_of",
        "ancestors_of",
        "get_related",
        "query_nodes",
        "search_nodes",
        "get_tree",
        "get_project_map",
        "estimate_size",
        "validate_node",
        "get_instance_config",
        "create_node",  # restricted in another way: only for new Issues; not editing existing
        "link_commit",  # additive: linking a commit doesn't mutate the node's state
    }
)
