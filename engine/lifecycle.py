"""Status state machine — data-driven from instance/lifecycle.yaml.

Mirrors the v0.1 mcp/src/lifecycle.ts contract exactly, but reads transitions
from the loaded Instance instead of a hard-coded dict.
"""

from __future__ import annotations

from .config_loader import Instance


def legal_next(instance: Instance, from_status: str) -> list[str]:
    """Legal next statuses via transition_status (excludes `superseded`,
    which is supersede-only)."""
    nexts = instance.transitions.get(from_status, ())
    return [s for s in nexts if s != "superseded"]


def can_transition(instance: Instance, from_status: str, to_status: str) -> bool:
    """True iff `transition_status(from, to)` is legal.

    `superseded` is never reachable via transition_status — only via supersede.
    """
    if to_status == "superseded":
        return False
    return to_status in legal_next(instance, from_status)
