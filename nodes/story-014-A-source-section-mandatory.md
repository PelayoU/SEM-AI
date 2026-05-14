---
category: story
id: story-014-A-source-section-mandatory
parent: "[[feature-014-skill-source-section-pattern]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 014-A — `## Source` section is structurally required

> Parent: [[feature-014-skill-source-section-pattern]].

## Cohn statement

As a **skill author**, I want **`## Source` to be one of the 6 required body sections in every SKILL.md**, so that **omitting it fails structural review by inspection rather than passing as "editorial detail"**.

## Conditions of Satisfaction

- `.claude/templates/SKILL.md.template` enumerates `## Source` as required.
- All 37 existing skills carry the section.

## INVEST self-check

✅ I · ✅ N · ✅ V (citation discipline as structural property) · ✅ E · ✅ S · ✅ T (`grep -L "^## Source" .claude/skills/*/SKILL.md` returns empty).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-014-skill-source-section-pattern]].
- [[adr-009-skill-as-canonical-method]].
