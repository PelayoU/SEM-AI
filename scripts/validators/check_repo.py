#!/usr/bin/env python3
"""sem-ai-ci validators — stage runner.

Subcommands:
  skills          Skill frontmatter — framework + node-templates SKILL.md have valid `name:` matching directory
  agents          Agent frontmatter — the six agent.md files have required fields + preload framework + node-templates
  settings        .claude/settings.json — valid JSON; hooks structure (when present)
  engine-harness  engine/ stays harness-agnostic — no code-level references to .claude/ or other harness bindings

Usage:
  python scripts/validators/check_repo.py skills
  python scripts/validators/check_repo.py agents
  python scripts/validators/check_repo.py settings
  python scripts/validators/check_repo.py engine-harness

Exits 0 on pass, 1 on fail with a list of issues, 2 on bad invocation.

Note: ADR coherence is no longer checked here. ADRs live as GitHub Issues
(type:adr) in the project's graph, not as markdown files; their integrity
is enforced by the engine MCP when they are created/updated.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / ".claude" / "skills"
AGENTS_DIR = ROOT / ".claude" / "agents"
SETTINGS_FILE = ROOT / ".claude" / "settings.json"

EXPECTED_SKILLS = ["framework", "node-templates"]
EXPECTED_AGENTS = [
    "product-manager",
    "architect",
    "developer",
    "qa",
    "devops",
    "security-officer",
]


def emit_fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)


def emit_ok(msg: str) -> None:
    print(f"OK: {msg}")


def parse_frontmatter(text: str) -> dict | None:
    """Extract and parse YAML frontmatter from a markdown file."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    block = text[4:end]
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


# ----- Stage 1: Skill frontmatter ----------------------------------------------


def check_skills() -> int:
    errors: list[str] = []
    for name in EXPECTED_SKILLS:
        skill_file = SKILLS_DIR / name / "SKILL.md"
        rel = skill_file.relative_to(ROOT) if skill_file.exists() else f".claude/skills/{name}/SKILL.md"
        if not skill_file.exists():
            errors.append(f"Missing skill file: {rel}")
            continue
        fm = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{rel}: missing or invalid YAML frontmatter")
            continue
        if fm.get("name") != name:
            errors.append(
                f"{rel}: frontmatter 'name' = {fm.get('name')!r}, expected {name!r} (must match directory)"
            )
        if not fm.get("description"):
            errors.append(f"{rel}: missing or empty 'description' field in frontmatter")

    if errors:
        for e in errors:
            emit_fail(e)
        return 1

    emit_ok(f"{len(EXPECTED_SKILLS)} skills validated")
    return 0


# ----- Stage 3: Agent frontmatter ----------------------------------------------


def check_agents() -> int:
    errors: list[str] = []
    for name in EXPECTED_AGENTS:
        agent_file = AGENTS_DIR / f"{name}.md"
        rel = agent_file.relative_to(ROOT) if agent_file.exists() else f".claude/agents/{name}.md"
        if not agent_file.exists():
            errors.append(f"Missing agent file: {rel}")
            continue
        fm = parse_frontmatter(agent_file.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{rel}: missing or invalid YAML frontmatter")
            continue
        if fm.get("name") != name:
            errors.append(f"{rel}: frontmatter 'name' = {fm.get('name')!r}, expected {name!r}")
        if not fm.get("description"):
            errors.append(f"{rel}: missing or empty 'description' field in frontmatter")
        skills = fm.get("skills", [])
        if isinstance(skills, str):
            skills = [skills]
        if not isinstance(skills, list):
            errors.append(f"{rel}: 'skills' must be a list, got {type(skills).__name__}")
            continue
        for required_skill in EXPECTED_SKILLS:
            if required_skill not in skills:
                errors.append(
                    f"{rel}: 'skills:' must include {required_skill!r} (got {skills!r})"
                )

    if errors:
        for e in errors:
            emit_fail(e)
        return 1

    emit_ok(f"{len(EXPECTED_AGENTS)} agents validated")
    return 0


# ----- Stage 4: settings.json --------------------------------------------------


def check_settings() -> int:
    if not SETTINGS_FILE.exists():
        emit_ok(".claude/settings.json: not present (allowed during v0.3.0-pre)")
        return 0
    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        emit_fail(f".claude/settings.json: invalid JSON — {e}")
        return 1
    if not isinstance(data, dict):
        emit_fail(".claude/settings.json: top-level must be an object")
        return 1
    # When hooks are declared (post-v0.3.0), validate structure.
    # For now, presence-only check.
    hooks = data.get("hooks")
    if hooks is not None and not isinstance(hooks, dict):
        emit_fail(".claude/settings.json: 'hooks' must be an object")
        return 1
    emit_ok(".claude/settings.json: valid")
    return 0


# ----- Stage 5: engine/ harness-agnostic -------------------------------------


ENGINE_DIR = ROOT / "engine"

# Patterns that indicate harness-specific leakage in engine/ code.
# We deliberately scan only *code* lines (strip leading whitespace, ignore
# pure-comment lines and docstring continuations) so docstring references to
# `.claude/` for documentation purposes don't false-positive.
_HARNESS_LEAK_RE = re.compile(
    r'^\s*(?:from|import)\s+\S*claude'   # any import that mentions "claude" in the module path
    r'|^[^#]*[\'"`]\.claude/'             # string literals with `.claude/` paths in code (not comments)
)


def check_engine_harness() -> int:
    """Verify engine/ has no code-level references to harness bindings.

    Per ADR #65 (Claude Code is the primary AI harness; engine/ stays
    harness-agnostic), engine/ must not import from .claude/ or reference
    .claude/ paths in code (docstrings + comments documenting the
    relationship are fine).
    """
    if not ENGINE_DIR.exists():
        emit_fail(f"engine/ directory not found: {ENGINE_DIR.relative_to(ROOT)}")
        return 1

    errors: list[str] = []
    for path in sorted(ENGINE_DIR.rglob("*.py")):
        rel = path.relative_to(ROOT)
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        in_docstring = False
        docstring_delim = None
        for lineno, raw in enumerate(lines, 1):
            stripped = raw.strip()
            # Track triple-quoted docstring blocks so we can skip their content.
            if in_docstring:
                if docstring_delim and docstring_delim in raw:
                    in_docstring = False
                    docstring_delim = None
                continue
            for delim in ('"""', "'''"):
                if stripped.startswith(delim):
                    # Single-line docstring like """foo"""?
                    if stripped.count(delim) >= 2:
                        break
                    in_docstring = True
                    docstring_delim = delim
                    break
            if in_docstring:
                continue
            # Skip full-line comments
            if stripped.startswith("#"):
                continue
            if _HARNESS_LEAK_RE.search(raw):
                errors.append(
                    f"{rel}:{lineno}: harness leakage — {stripped[:80]!r}"
                )

    if errors:
        for e in errors:
            emit_fail(e)
        emit_fail(
            "engine/ must stay harness-agnostic per ADR #65. "
            "Move harness-specific code to .claude/ (or future binding dirs)."
        )
        return 1

    emit_ok(f"engine/ harness-clean ({len(list(ENGINE_DIR.rglob('*.py')))} files scanned)")
    return 0


# ----- Dispatcher --------------------------------------------------------------


COMMANDS = {
    "skills": check_skills,
    "agents": check_agents,
    "settings": check_settings,
    "engine-harness": check_engine_harness,
}


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in COMMANDS:
        print(f"Usage: {sys.argv[0]} {{{'|'.join(COMMANDS)}}}", file=sys.stderr)
        return 2
    return COMMANDS[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())
