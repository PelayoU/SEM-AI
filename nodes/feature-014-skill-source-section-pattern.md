---
category: feature
id: feature-014-skill-source-section-pattern
parent: "[[cap-08-citation-discipline]]"
artifacts:
  - "[[.claude/templates/SKILL.md.template]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 014 — Mandatory `## Source` section in every skill

> Authored via `po-feature-decomposition`. Delivers part of [[cap-08-citation-discipline]].

## What it delivers

Every SKILL.md file ends with a mandatory `## Source` section that enumerates the bibliographic anchors of the skill's criteria. The section convention: star-marked (★) primary sources cite Jones BP # + page, GISF slide + PDF, Cucumber page, Patton page; out-of-bibliography conventions are listed separately with explicit disclaimer. Citation appears inline in `## Formal criteria` too, but the `## Source` section is the audit-surface roll-up.

## Story Map position

- **Activity (Epic):** Bibliographic infrastructure.
- **Task:** This feature (per-skill source roll-up).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-014-A-source-section-mandatory]] — As a skill author, I want the source section to be a required structural element, so omitting it fails review by inspection.

## Spec sibling

- [[spec-014-skill-source-section-pattern]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (template enforces it; review fails without it) → Construction (37/37 skills have it) → Consequences (citation audit becomes a structural property, not an editorial habit).

## Notes

Architectural anchor: [[adr-003-citation-mandate]] + [[adr-009-skill-as-canonical-method]] (`## Source` is one of the 6 fixed sections of every skill). Companion to [[feature-015-skill-meta-template]] (template enforces the section).

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-003-citation-mandate]], [[adr-009-skill-as-canonical-method]].
- Substrate evidence: 37 SKILL.md files each carry `## Source` (verifiable: `grep -l "^## Source" .claude/skills/*/SKILL.md | wc -l` → 37).
