"""Role × node-type write authority — data-driven from instance/jurisdiction.yaml.

Mirrors v0.1 mcp/src/jurisdiction.ts. Pure function — no IO, no DB.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .config_loader import Instance

WriteOp = Literal[
    "create_node",
    "update_node",
    "transition_status",
    "supersede",
    "set_related",
    "link_commit",
    "add_label",
    "remove_label",
]


@dataclass(frozen=True)
class WriteDecision:
    allowed: bool
    advisory: bool = False
    reason: str | None = None
    hint: str | None = None
    warning: str | None = None


def owning_skill(instance: Instance, node_type: str) -> str | None:
    """Type → owning skill name (advisory, back-compat with v0.1)."""
    return instance.owning_skill.get(node_type)


def can_role_write(
    instance: Instance,
    role: str,
    node_type: str,
    op: WriteOp,
) -> WriteDecision:
    """Check whether `role` may perform `op` on a node of type `node_type`."""
    perms = instance.role_permissions.get(role)
    if perms is None:
        return WriteDecision(
            allowed=False,
            reason=f"unknown role '{role}'",
            hint=f"valid roles: {sorted(instance.role_set)}",
        )

    if op in ("create_node", "supersede"):
        if node_type in perms.can_create:
            return WriteDecision(allowed=True)
        hint = (
            "Security Officer owns no node type exclusively. Contribute "
            "Security_* sections via dispatch from the owning role "
            "(Architect for ADR topic 7; PM for spec Security AC and "
            "release Security gate)."
            if role == "security-officer"
            else f"Allowed create types for {role}: "
                 f"{', '.join(perms.can_create) or '(none)'}"
        )
        return WriteDecision(
            allowed=False,
            reason=f"role '{role}' cannot {op} node of type '{node_type}'",
            hint=hint,
        )

    if op == "update_node":
        if node_type in perms.can_update:
            return WriteDecision(allowed=True)
        if node_type in perms.advisory_update:
            return WriteDecision(
                allowed=True,
                advisory=True,
                warning=(
                    f"Advisory: role '{role}' updating '{node_type}' — "
                    f"scope your change to the role's contribution surface "
                    f"(for security-officer: Security_* sections only; for "
                    f"devops: operational sections of release only)."
                ),
            )
        return WriteDecision(
            allowed=False,
            reason=f"role '{role}' cannot update_node on type '{node_type}'",
            hint=f"Allowed update types for {role}: "
                 f"{', '.join(perms.can_update) or '(none)'}",
        )

    # transition_status, set_related, link_commit, add_label, remove_label:
    # no role-level enforcement at this layer. Their invariants live in
    # lifecycle.py / graph_walker.py.
    return WriteDecision(allowed=True)
