---
category: feature
id: feature-050-architect-architecture-design-skill
parent: "[[cap-04-apply-architect-discipline]]"
artifacts:
  - "[[.claude/skills/architect-architecture-design/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 050 — Skill: `architect-architecture-design`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/architect-architecture-design/SKILL.md`. Delivers part of [[cap-04-apply-architect-discipline]].

## What it delivers

Lets the Architect draft / refine / audit application architecture against Jones's seven fundamental topics (overall structure / data / interfaces / decomposition / linkage / performance / security), the Zachman 6×6 schema, and size-tier importance (Table 7-7: useful at 1 k FP, important at 10 k, critical at 100 k). The skill Architect exercised in Phase 1 to author ADRs.

## Stories (children)

- [[story-050-A-seven-topics-as-audit-grid]] — As an Architect designing or auditing, I want every architectural decision walked against the 7 fundamental topics, so silence on a topic is structural rather than accidental.

## Spec sibling

- [[spec-050-architect-architecture-design-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: Capers Jones BP #14 (pp. 75–77); Ch 7 § Software Architecture (pp. 470–475); Table 7-7; Ch 9 Table 9-23.
- Substrate evidence: `.claude/skills/architect-architecture-design/SKILL.md`.
