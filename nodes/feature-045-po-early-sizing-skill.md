---
category: feature
id: feature-045-po-early-sizing-skill
parent: "[[cap-03-apply-po-discipline]]"
artifacts:
  - "[[.claude/skills/po-early-sizing/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 045 — Skill: `po-early-sizing`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-early-sizing/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO size a software application early using function-point methods (full IFPUG / COSMIC, light FP approximation, pattern-matching against ISBSG-class historical data) so estimation, planning, and risk analysis proceed on quantitative ground. Refuses LOC as primary size metric.

## Stories (children)

- [[story-045-A-fp-sizing-before-estimating]] — As a PO before cost-estimating, I want an FP size with band (low / central / high), so the estimate is anchored rather than guessed.

## Spec sibling

- [[spec-045-po-early-sizing-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Absorbed PM scope per [[adr-006-super-po-fusion]].

## Source

- Anchoring authority: Capers Jones BP #6 (pp. 51–53); BP #31 (ISBSG, pp. 113–114); BP #11 growth-rate empirics (p. 71).
- Substrate evidence: `.claude/skills/po-early-sizing/SKILL.md`.
