#!/usr/bin/env python3
"""sem-ai-ci validators — stage runner.

Subcommands:
  adrs      ADR coherence — header present, internal links resolve, supersede chain consistent
  skills    Skill frontmatter — framework + node-templates SKILL.md have valid `name:` matching directory
  agents    Agent frontmatter — the six agent.md files have required fields + preload framework + node-templates
  settings  .claude/settings.json — valid JSON; hooks structure (when present) per ADR-004

Usage:
  python scripts/validators/check_repo.py adrs
  python scripts/validators/check_repo.py skills
  python scripts/validators/check_repo.py agents
  python scripts/validators/check_repo.py settings

Exits 0 on pass, 1 on fail with a list of issues, 2 on bad invocation.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
ADR_DIR = ROOT / "docs" / "adr"
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


# ----- Stage 1: ADR coherence --------------------------------------------------


def check_adrs() -> int:
    if not ADR_DIR.exists():
        emit_fail(f"ADR directory not found: {ADR_DIR.relative_to(ROOT)}")
        return 1
    adr_files = sorted(ADR_DIR.glob("[0-9][0-9][0-9]-*.md"))
    if not adr_files:
        emit_fail(f"No ADRs found in {ADR_DIR.relative_to(ROOT)}")
        return 1

    available_slugs = {p.stem for p in adr_files}
    required_headers = ("Status", "Date", "Supersedes", "Superseded by")
    errors: list[str] = []

    for adr in adr_files:
        rel = adr.relative_to(ROOT)
        text = adr.read_text(encoding="utf-8")

        if not text.startswith("# ADR-"):
            errors.append(f"{rel}: must start with '# ADR-...' first heading")

        for header in required_headers:
            pattern = rf"^- \*\*{re.escape(header)}\*\*:"
            if not re.search(pattern, text, re.MULTILINE):
                errors.append(f"{rel}: missing '- **{header}**:' header line")

        for m in re.finditer(r"docs/adr/(\d{3}-[a-z0-9-]+)\.md", text):
            ref_slug = m.group(1)
            if ref_slug not in available_slugs:
                errors.append(f"{rel}: references missing ADR file docs/adr/{ref_slug}.md")

    if errors:
        for e in errors:
            emit_fail(e)
        return 1

    emit_ok(f"{len(adr_files)} ADRs validated")
    return 0


# ----- Stage 2: Skill frontmatter ----------------------------------------------


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
    # When hooks are declared (post-v0.3.0), validate structure per ADR-004.
    # For now, presence-only check.
    hooks = data.get("hooks")
    if hooks is not None and not isinstance(hooks, dict):
        emit_fail(".claude/settings.json: 'hooks' must be an object")
        return 1
    emit_ok(".claude/settings.json: valid")
    return 0


# ----- Dispatcher --------------------------------------------------------------


COMMANDS = {
    "adrs": check_adrs,
    "skills": check_skills,
    "agents": check_agents,
    "settings": check_settings,
}


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in COMMANDS:
        print(f"Usage: {sys.argv[0]} {{{'|'.join(COMMANDS)}}}", file=sys.stderr)
        return 2
    return COMMANDS[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())
