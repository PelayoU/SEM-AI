---
category: feature
id: feature-012-skill-references-traceability
parent: "[[cap-08-citation-discipline]]"
artifacts:
  - "[[bibliography/skill-references.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 012 — Per-skill bibliographic traceability table

> Authored via `po-feature-decomposition`. Delivers part of [[cap-08-citation-discipline]].

## What it delivers

`bibliography/skill-references.md` records the bibliographic sources anchoring each of the 37 skills. Star-marked (★) sources are the literal authority for the skill's criteria; complement sources are convention pointers. Supports external audit (TFM defense, academic peer review) and detects citation drift if a skill is refactored.

## Story Map position

- **Activity (Epic):** Bibliographic infrastructure.
- **Task:** This feature (per-skill traceability).
- **Release slice:** Walking skeleton — required by goal-02 TFM defense.

## Stories (children)

- [[story-012-A-audit-skill-citations]] — As an external auditor, I want to read which sources anchor each skill, so I verify citation discipline without spelunking 37 SKILL.md files.

## Spec sibling

- [[spec-012-skill-references-traceability]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (cross-checked against each skill's own `## Source`) → Construction (one file) → Consequences (academic audit becomes a single-file read).

## Notes

Architectural anchor: [[adr-003-citation-mandate]]. Companion to [[feature-011-bibliography-index]] (INDEX is navigator for skill authors; this file is audit surface for external readers). Goal-02's M-criterion explicitly requires this file complete.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-003-citation-mandate]].
- Substrate evidence: `bibliography/skill-references.md`.
