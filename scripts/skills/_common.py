"""Shared helpers for the slash-command skill scripts."""

from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SESSIONS_DIR = REPO_ROOT / "sessions"


def today() -> str:
    """Return today's date as YYYY-MM-DD (UTC)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def slugify(text: str) -> str:
    """Convert text to a session-id slug: lowercase, dashes, no special chars."""
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9-]+", "-", s)
    s = re.sub(r"-+", "-", s)
    s = s.strip("-")
    return s or "session"


def current_branch() -> str | None:
    """Return current git branch, or None."""
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, check=True, timeout=5,
        )
        return result.stdout.strip() or None
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return None


def session_id_from_branch(branch: str) -> str | None:
    """If `branch` is 'session/<id>', return '<id>'; else None."""
    if branch and branch.startswith("session/"):
        return branch[len("session/") :]
    return None


def doc_path_for(session_id: str) -> Path:
    return SESSIONS_DIR / f"{session_id}.md"


def gh_issue_comment(issue_number: str, body: str) -> bool:
    """Post a comment on a GitHub Issue. Returns True on success."""
    try:
        subprocess.run(
            ["gh", "issue", "comment", issue_number, "--body", body],
            capture_output=True, text=True, check=True, timeout=15,
        )
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return False


def normalize_issue_number(issue_ref: str) -> str:
    """Convert '#42' or '42' to '42' (string). Strips surrounding whitespace first."""
    return issue_ref.strip().lstrip("#")
