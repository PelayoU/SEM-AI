"""Shared helpers for the hook scripts.

Each hook script:
  - calls `read_input()` to get the JSON payload from stdin
  - calls `emit(...)` to write JSON to stdout when contributing context
"""

from __future__ import annotations

import json
import subprocess
import sys
from typing import Any


def read_input() -> dict[str, Any]:
    """Parse the hook's input from stdin per Claude Code's hook protocol."""
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def emit(payload: dict[str, Any]) -> None:
    """Write a JSON object to stdout. Single-shot; subsequent calls overwrite."""
    sys.stdout.write(json.dumps(payload))
    sys.stdout.flush()


def emit_context(event_name: str, context: str) -> None:
    """Inject `context` as `additionalContext` for the named event."""
    emit(
        {
            "hookSpecificOutput": {
                "hookEventName": event_name,
                "additionalContext": context,
            }
        }
    )


def emit_deny(event_name: str, reason: str) -> None:
    """Block the operation (PreToolUse only) with a reason the agent sees."""
    emit(
        {
            "hookSpecificOutput": {
                "hookEventName": event_name,
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }
    )


def current_branch() -> str | None:
    """Return the current git branch, or None if unavailable."""
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
        return result.stdout.strip() or None
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return None


def is_session_branch(branch: str | None) -> bool:
    """True if `branch` is a session/* branch."""
    return bool(branch and branch.startswith("session/"))
