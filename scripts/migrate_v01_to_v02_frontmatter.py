#!/usr/bin/env python3
"""Day 1.8 — Migrate v0.1 graph/ frontmatter to v0.2 7-field shape.

v0.1 schema (variable across types):
  category, id, parent (Obsidian wiki-link), status, created, updated,
  artifacts, mvp, horizon, supersedes, superseded-by

v0.2 schema (uniform):
  type, parent, status, created, updated, maintained_by_role, labels[]
  (+ supersedes / superseded-by retained ONLY for ADRs — structural)

Transformations:
  - category   → type
  - parent: "[[X]]"  → parent: X  (strip Obsidian wiki-link)
  - parent: vision-sem-ia  → parent: vision-001-sem-ai  (re-parent to v0.2 vision)
  - inject maintained_by_role per type→role map
  - move mvp / horizon  → labels (mvp:go, horizon:release)
  - drop id, slug, owning_skill, artifacts (id derivable from path)
  - ADR supersedes/superseded-by: strip [[...]] from comma-list, drop if empty
  - updated: bump to today (2026-05-22)

Idempotent — running twice yields the same result.
"""

import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml


def normalize_date(value):
    """Any date/datetime/string → YYYY-MM-DD string."""
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str):
        # Strip ISO time component if present.
        return value.split("T")[0].split(" ")[0]
    return str(value)

# v0.2 instance role map (vision/goal/cap/feature → product-manager; adr → architect)
TYPE_TO_ROLE = {
    "vision": "product-manager",
    "goal": "product-manager",
    "capability": "product-manager",
    "feature": "product-manager",
    "adr": "architect",
}

# old slug → new slug (only for re-parenting the inherited self-bootstrap goals
# from the May-14 vision to the v0.2 vision)
PARENT_REMAP = {
    "vision-sem-ia": "vision-001-sem-ai",
}

WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
TODAY = date.today().isoformat()


def strip_wiki_links(value):
    """[[X]] → X; commaseparated [[A]], [[B]] → A, B."""
    if not isinstance(value, str):
        return value
    return WIKI_LINK_RE.sub(r"\1", value).strip()


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    fm_yaml = text[4:end]
    body = text[end + 5 :]
    return yaml.safe_load(fm_yaml) or {}, body


def serialize_frontmatter(fm):
    """Emit YAML in fixed key order, list-form for labels, omit empty fields."""
    order = [
        "type",
        "parent",
        "status",
        "created",
        "updated",
        "maintained_by_role",
        "labels",
        # ADR-only structural extras (kept for chain integrity)
        "supersedes",
        "superseded-by",
    ]
    lines = ["---"]
    for key in order:
        if key not in fm:
            continue
        val = fm[key]
        if val in (None, "", []):
            continue
        if key == "labels":
            lines.append("labels:")
            for label in val:
                lines.append(f"  - {label}")
        elif isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---\n")
    return "\n".join(lines)


def derive_type_and_id(path):
    """sem-ai/goals/01-X.md → ('goal', 'goal-01-X'); docs/adr/001-X.md → ('adr', 'adr-001-X')."""
    parts = path.parts
    if "docs" in parts and "adr" in parts:
        return "adr", f"adr-{path.stem}"
    folder = path.parent.name
    folder_to_type = {
        "vision": "vision",
        "goals": "goal",
        "capabilities": "capability",
        "features": "feature",
    }
    type_ = folder_to_type.get(folder)
    if type_ is None:
        raise ValueError(f"unknown folder for {path}: {folder}")
    return type_, f"{type_}-{path.stem}"


def migrate(path: Path) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if fm is None:
        return False, "no frontmatter"

    type_, _ = derive_type_and_id(path)
    new = {}

    # type: from folder, override any existing category/type
    new["type"] = type_

    # parent: strip wiki-link + remap legacy vision id
    if "parent" in fm and fm["parent"]:
        parent = strip_wiki_links(fm["parent"])
        # if multiple comma-separated, keep only the first (parent is single)
        parent = parent.split(",")[0].strip()
        new["parent"] = PARENT_REMAP.get(parent, parent)
    # vision has no parent (legitimate); other types must have one
    elif type_ != "vision":
        return False, f"missing parent for {type_}"

    # status: preserve, fallback to draft
    new["status"] = fm.get("status", "draft")

    # created: preserve, fallback to today; always normalized to YYYY-MM-DD
    new["created"] = normalize_date(fm.get("created", TODAY))

    # updated: bump to today (this migration touched the file)
    new["updated"] = TODAY

    # maintained_by_role: derived from type
    new["maintained_by_role"] = TYPE_TO_ROLE[type_]

    # labels: collect from mvp, horizon, plus any pre-existing labels
    labels = []
    if fm.get("mvp"):
        labels.append(f"mvp:{fm['mvp']}")
    if fm.get("horizon"):
        labels.append(f"horizon:{fm['horizon']}")
    if fm.get("labels"):
        labels.extend(fm["labels"])
    if labels:
        new["labels"] = labels

    # ADR-only: supersedes / superseded-by — preserve as cleaned lists
    if type_ == "adr":
        for key in ("supersedes", "superseded-by"):
            raw = fm.get(key)
            if not raw:
                continue
            cleaned = strip_wiki_links(str(raw))
            items = [s.strip() for s in cleaned.split(",") if s.strip()]
            if items:
                new[key] = items

    out = serialize_frontmatter(new) + body
    if out == text:
        return False, "no change"
    path.write_text(out, encoding="utf-8")
    return True, "migrated"


def main():
    root = Path(__file__).parent.parent
    targets = []
    for sub in ("sem-ai/vision", "sem-ai/goals", "sem-ai/capabilities", "sem-ai/features"):
        targets.extend(sorted((root / sub).glob("*.md")))
    targets.extend(sorted((root / "docs/adr").glob("*.md")))

    counts = {"migrated": 0, "no change": 0, "skip": 0}
    for path in targets:
        ok, msg = migrate(path)
        bucket = "migrated" if ok else ("no change" if msg == "no change" else "skip")
        counts[bucket] += 1
        rel = path.relative_to(root)
        print(f"{'OK' if ok else '--'} {rel}: {msg}")

    print(f"\nTotal: {sum(counts.values())} files · "
          f"migrated={counts['migrated']} · "
          f"no-change={counts['no change']} · "
          f"skipped={counts['skip']}")
    return 0 if counts["skip"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
