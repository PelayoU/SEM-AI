---
category: feature
id: feature-015-skill-meta-template
parent: "[[cap-08-citation-discipline]]"
artifacts:
  - "[[.claude/templates/SKILL.md.template]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 015 — Skill meta-template (`SKILL.md.template`)

> Authored via `po-feature-decomposition`. Delivers part of [[cap-08-citation-discipline]]; also serves [[cap-13-portability]] as the extension mechanism for new skills.

## What it delivers

`.claude/templates/SKILL.md.template` encodes the canonical structure for every skill: frontmatter (`name`, pushy `description`), six fixed body sections (`## Purpose` · `## When this skill applies` · `## Formal criteria` · `## How you proceed` · `## Pitfalls to avoid` · `## Source`), citation-per-criterion mandate, ≤500-line cap, read-before-write rule. New skills (Security, Designer roles' skills when implemented; future skill additions) are scaffolded from this template, ensuring uniformity.

## Story Map position

- **Activity (Epic):** Skill substrate extensibility.
- **Task:** This feature (skill meta-template).
- **Release slice:** Thickening release — every skill added after the initial 37 uses this scaffold.

## Stories (children)

- [[story-015-A-new-skill-from-template]] — As a framework maintainer, I want to scaffold a new skill from the meta-template, so structural conformance and citation discipline are inherited rather than copied.

## Spec sibling

- [[spec-015-skill-meta-template]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (cross-checked against 37 existing skills' structure) → Construction (template extracted from observed pattern) → Consequences (skill additions are conformant by design).

## Notes

Architectural anchors: [[adr-009-skill-as-canonical-method]] (the rule); [[adr-003-citation-mandate]] (template enforces `## Source`). Cross-cap serving: [[cap-13-portability]] needs this template for substrate-extensibility on forked projects.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-009-skill-as-canonical-method]], [[adr-003-citation-mandate]].
- Substrate evidence: `.claude/templates/SKILL.md.template`.
- Convention pointer: Anthropic skill-creator pattern (out-of-bibliography).
