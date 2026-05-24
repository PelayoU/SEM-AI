#!/usr/bin/env python3
"""PostToolUse hook for mcp__sem_ai_engine__transition_status.

When a node transitions status, run engine/checks/ semantic CI against it
and surface findings as additionalContext for the agent. Coherent with
ADR-008 update § two layers of CI: the structural validators in the engine
core already hard-rejected illegal transitions; this hook adds the
semantic layer (Security attributes present? AC populated? Value chain
populated when done? etc.).

For v0.3.0 the hook does mechanical findings via `engine/checks/`. Invoking
a role agent (Security Officer, Architect) for deeper review is deferred —
that pattern (claude --agent X "review #N" from inside a hook) requires
more design work and is left for v0.4.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from scripts.hooks._common import emit_context, read_input  # noqa: E402


def main() -> int:
    payload = read_input()

    # Validate this is the right tool
    tool_name = payload.get("tool_name")
    if tool_name != "mcp__sem_ai_engine__transition_status":
        return 0

    # Extract the node id from the tool input
    tool_input = payload.get("tool_input") or {}
    node_id = tool_input.get("node_id")
    if not node_id:
        return 0

    # Run engine/checks/ against the node. Wrap in try/except so a hook
    # failure never blocks the agent.
    try:
        from engine.adapters import GitHubAdapter, load_config
        from engine.checks import run_all_checks
    except ImportError:
        # Engine not on path — silently skip (dev environment without venv)
        return 0

    try:
        adapter = GitHubAdapter(load_config())
        node = adapter.get_issue(node_id)
        findings = run_all_checks(node, adapter)
    except Exception as e:
        emit_context(
            "PostToolUse",
            f"[sem-ai checks hook] could not run checks on {node_id}: {e}",
        )
        return 0

    if not findings:
        return 0  # quiet success

    lines = [
        f"📋 Post-transition checks for {node_id} surfaced {len(findings)} finding(s):",
        "",
    ]
    for f in findings:
        sev_emoji = {"info": "ℹ️", "warning": "⚠️", "error": "❌"}.get(f.severity, "•")
        lines.append(f"  {sev_emoji} [{f.code}] {f.message}")
    lines.append("")
    lines.append(
        "These are warn-level (the engine does not block on them). Address "
        "before proceeding or, when N/A, justify in the body section so a "
        "future reviewer sees the reason."
    )
    emit_context("PostToolUse", "\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
