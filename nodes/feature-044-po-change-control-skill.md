---
category: feature
id: feature-044-po-change-control-skill
parent: "[[cap-03-apply-po-discipline]]"
artifacts:
  - "[[.claude/skills/po-change-control/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 044 — Skill: `po-change-control`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-change-control/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO manage scope changes before release using Jones BP #33's 16-practice inventory: joint client/development Change Control Board, function-point-quantified CRs, re-estimation trigger above 10 FP, multirelease assignment, cross-artifact ripple discipline.

## Stories (children)

- [[story-044-A-fp-quantified-crs]] — As a PO receiving a "small change", I want every CR FP-quantified, so the 10-FP re-estimation gate is objective.

## Spec sibling

- [[spec-044-po-change-control-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Coordinates with [[feature-065-devops-configuration-control-skill]] (CM tracks the changes; CCB judges them).

## Source

- Anchoring authority: Capers Jones BP #33 (pp. 117–119); critical-topic Ch 1 p. 19.
- Substrate evidence: `.claude/skills/po-change-control/SKILL.md`.
