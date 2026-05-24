#!/usr/bin/env python3
"""PreCompact hook — refresh the Handoff section of the session doc.

Per ADR-004 + framework SKILL § Sessions: before Claude Code compacts the
conversation, this hook appends a timestamp line to the Handoff so the
post-compact state has a marker the next role can rely on. Decisions are
preserved because they live in their own append-only section already.

If we're not on a session branch, this hook is a no-op.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from scripts.hooks._common import (  # noqa: E402
    current_branch,
    emit,
    is_session_branch,
    read_input,
)


_HANDOFF_HEADER_RE = re.compile(
    r"^##\s+Handoff\s*$",
    re.MULTILINE | re.IGNORECASE,
)


def annotate_handoff(doc_text: str, marker: str) -> str:
    """Append `marker` to the Handoff section if present; return updated doc.

    If the Handoff header is missing, return the original doc unchanged
    (the hook should not silently introduce structure).
    """
    m = _HANDOFF_HEADER_RE.search(doc_text)
    if not m:
        return doc_text
    insert_at = m.end()
    return doc_text[:insert_at] + f"\n\n{marker}\n" + doc_text[insert_at:].lstrip("\n")


def main() -> int:
    _payload = read_input()
    branch = current_branch()
    if not is_session_branch(branch):
        return 0

    session_id = branch.removeprefix("session/")
    doc_path = REPO_ROOT / "sessions" / f"{session_id}.md"
    if not doc_path.exists():
        return 0

    try:
        doc_text = doc_path.read_text(encoding="utf-8")
    except OSError:
        return 0

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    marker = (
        f"_[compactation checkpoint at {timestamp} — see Decisions for binding "
        f"history; the transcript before this point is now condensed]_"
    )
    new_text = annotate_handoff(doc_text, marker)
    if new_text != doc_text:
        try:
            doc_path.write_text(new_text, encoding="utf-8")
        except OSError:
            pass

    emit(
        {
            "systemMessage": (
                f"Session doc updated with pre-compact marker: sessions/{session_id}.md"
            )
        }
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
