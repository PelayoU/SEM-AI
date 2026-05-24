#!/usr/bin/env python3
"""One-shot cleanup: strip ADR-N and docs/adr/ citations from code/comments.

The ADRs migrated to GitHub Issues (#2-#10 in the SEM-AI repo); inline
'per ADR-N' citations are stale references to a now-deleted filesystem
store. The framework's behaviour is the answer to those decisions; the
inline citation adds nothing.

This script removes:
  - parenthetical citations: '(per ADR-N[ update][ § ...])', '(ADR-N...)',
    '(see ADR-N...)', '(per ADR-N + ADR-M)'
  - line-leading citation prose: 'Per ADR-N + ADR-M:', 'Per ADR-N update'
  - standalone 'ADR-N' tokens
  - docs/adr/NNN-slug.md references (link or path)

Run once, idempotent.

IMPORTANT: do NOT collapse multi-space runs — that destroys Python
indentation. Only collapse spaces that follow non-whitespace on the
same line.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

TARGET_DIRS = ["engine", "scripts", "examples", ".github"]
TARGET_EXTS = {".py", ".md", ".yml", ".yaml", ".sh", ".txt"}

# Order matters: longer/more-specific patterns first.
PATTERNS: list[tuple[str, str]] = [
    (r"`docs/adr/\d+-[a-z0-9-]+\.md`", "the framework's design"),
    (r"docs/adr/\d+-[a-z0-9-]+\.md", "the framework's design"),
    (r"\s*\(per ADR-\d+(?:\s*\+\s*ADR-\d+)*(?:\s+update)?(?:\s+§[^)]+)?\)", ""),
    (r"\s*\(see ADR-\d+(?:\s*\+\s*ADR-\d+)*(?:\s+update)?(?:\s+§[^)]+)?\)", ""),
    (r"\s*\(ADR-\d+(?:\s*\+\s*ADR-\d+)*(?:\s+update)?(?:\s+§[^)]+)?\)", ""),
    (
        r"Per ADR-\d+(?:\s*\+\s*ADR-\d+)*(?:\s+update)?(?:\s+§[^:.\n]+)?:\s*",
        "",
    ),
    (
        r"Source:\s*ADR-\d+(?:\s*\+\s*ADR-\d+)*(?:\s+update)?(?:\s+§[^.\n]+)?\.?",
        "",
    ),
    (
        r"[ \t]+per ADR-\d+(?:\s*\+\s*ADR-\d+)*(?:\s+update)?(?:\s+§[^.,;\n]+)?",
        "",
    ),
    (
        r"[ \t]+see ADR-\d+(?:\s*\+\s*ADR-\d+)*(?:\s+update)?(?:\s+§[^.,;\n]+)?",
        "",
    ),
    (r"ADR-\d+(?:\s*\+\s*ADR-\d+)*(?:\s+update)?(?:\s+§\s*[^.,;\n)]+)?", ""),
]


_DOUBLE_SPACE_NON_INDENT = re.compile(r"(\S) +")


def transform(text: str) -> str:
    for pattern, replacement in PATTERNS:
        text = re.sub(pattern, replacement, text)
    # Collapse runs of spaces that follow visible text on the same line
    # (does NOT touch leading whitespace, so Python/YAML indent survives).
    text = _DOUBLE_SPACE_NON_INDENT.sub(lambda m: m.group(1) + " ", text)
    # Trim trailing spaces before newlines.
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text


def main() -> int:
    changed = 0
    for top in TARGET_DIRS:
        base = REPO_ROOT / top
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix not in TARGET_EXTS:
                continue
            try:
                original = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            updated = transform(original)
            if updated != original:
                path.write_text(updated, encoding="utf-8")
                print(f" edited {path.relative_to(REPO_ROOT)}")
                changed += 1
    print(f"\nDone — {changed} files modified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
