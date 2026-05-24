#!/usr/bin/env python3
"""SessionStart hook — bootstrap the session doc + project map mínimo.

Per + framework SKILL § Sessions: when a new Claude Code conversation
opens on a `session/*` branch, this hook injects the session doc (Context +
Decisions + Handoff + in-play Issues) as additionalContext so the agent
arrives oriented. On `main` (no active session), it injects a brief note
suggesting `/session-open` if work is starting.

Project map mínimo (vision + goals + capabilities + accepted ADRs) is NOT
loaded here — that is read on demand by the agent via
`mcp__sem_ai_engine__get_project_map` to keep the bootstrap small.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from scripts.hooks._common import ( # noqa: E402
    current_branch,
    emit_context,
    is_session_branch,
    read_input,
)


def main() -> int:
    _payload = read_input()
    branch = current_branch()

    if not is_session_branch(branch):
        emit_context(
            "SessionStart",
            (
                "Not on a session/* branch. "
                "Run `/session-open <slug>` to start a new session, or work "
                "directly on the graph for single-Issue edits."
            ),
        )
        return 0

    session_id = branch.removeprefix("session/")
    doc_path = REPO_ROOT / "sessions" / f"{session_id}.md"

    if not doc_path.exists():
        emit_context(
            "SessionStart",
            (
                f"On session branch '{branch}' but `sessions/{session_id}.md` "
                f"is missing. Either create the session doc or close the "
                f"branch with `/session-close`."
            ),
        )
        return 0

    try:
        doc_text = doc_path.read_text(encoding="utf-8")
    except OSError as e:
        emit_context(
            "SessionStart",
            f"Could not read sessions/{session_id}.md: {e}",
        )
        return 0

    context_lines = [
        f"# Resuming session: {session_id}",
        "",
        "Below is the session doc (Context + Decisions + Handoff). Read",
        "the Handoff to know what the previous role left for you to pick up.",
        "If you're a new role taking over, acknowledge the transition in",
        "your first turn (per framework SKILL § Sessions).",
        "",
        "---",
        doc_text,
    ]
    emit_context("SessionStart", "\n".join(context_lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
