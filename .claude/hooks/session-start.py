#!/usr/bin/env python3
"""SessionStart hook for SEM-AI v0.2.

Injects two things into every agent's context at session start:

  1. The at-minimum **project map** — every active `vision`, `goal`,
     `capability`, `adr`. The "one rule" of the framework says agents must
     hold this before acting; the hook makes it mechanical.

  2. The matching **session doc**, if the working tree is on a `session/*`
     branch. Same behaviour as the v0.1 bash hook (load-session.sh) it
     replaces.

Never fails session start: any problem → silent no-op (exit 0).

Reads stdin per Claude Code's hook protocol; writes JSON to stdout with a
`hookSpecificOutput.additionalContext` field.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def _project_root() -> Path:
    """Resolve project root from $CLAUDE_PROJECT_DIR or fall back to cwd."""
    return Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())).resolve()


def _git_branch(root: Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(root), "branch", "--show-current"],
            stderr=subprocess.DEVNULL,
            timeout=5,
        ).decode()
        return out.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return ""


def _project_map(root: Path) -> str:
    """Render the at-minimum project map as a compact markdown table.
    Falls back to empty string on any error (engine not installed yet, etc.)."""
    sys.path.insert(0, str(root))
    try:
        from engine.config_loader import load_instance
        from engine.graph_walker import iter_spine_nodes
    except Exception:
        return ""
    try:
        inst = load_instance(root)
    except Exception:
        return ""
    rows: list[tuple[str, str, str, str, str]] = []
    for n in iter_spine_nodes(inst):
        if n.type in ("vision", "goal", "capability", "adr"):
            rows.append(
                (n.type, n.id, n.parent or "—", n.status, n.maintained_by_role)
            )
    if not rows:
        return ""
    lines = [
        "# SEM-AI project map (auto-injected by SessionStart hook)",
        "",
        "> The at-minimum context every role holds — every active "
        "`vision`, `goal`, `capability`, and `adr`. Reach the rest of the "
        "spine via `mcp__sem_ai_engine__get_node` / `children_of` / "
        "`ancestors_of` / `query_nodes`.",
        "",
        "| Type | Id | Parent | Status | Role |",
        "|---|---|---|---|---|",
    ]
    for t, id_, parent, status, role in sorted(rows):
        lines.append(f"| {t} | `{id_}` | `{parent}` | {status} | {role} |")
    return "\n".join(lines)


def _session_doc(root: Path, branch: str) -> str:
    if not branch.startswith("session/"):
        return ""
    session_id = branch[len("session/"):]
    doc = root / "sessions" / f"{session_id}.md"
    if not doc.exists():
        return ""
    try:
        body = doc.read_text(encoding="utf-8")
    except OSError:
        return ""
    return (
        f"# Session doc for branch `{branch}` (auto-loaded)\n\n"
        f"> Attributed, third-person record of prior work on this session. "
        f"You did NOT perform these entries — read as inherited context, "
        f"not your own memory; do not adopt a prior role's voice. Continue "
        f"as the role your agent defines; the doc's Handoff section states "
        f"what you pick up.\n\n"
        f"{body}"
    )


def main() -> int:
    root = _project_root()

    pieces: list[str] = []
    pmap = _project_map(root)
    if pmap:
        pieces.append(pmap)
    branch = _git_branch(root)
    sdoc = _session_doc(root, branch)
    if sdoc:
        pieces.append(sdoc)

    if not pieces:
        return 0

    payload = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "\n\n---\n\n".join(pieces),
        }
    }
    sys.stdout.write(json.dumps(payload))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
