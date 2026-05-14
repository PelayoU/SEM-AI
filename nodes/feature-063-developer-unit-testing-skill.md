---
category: feature
id: feature-063-developer-unit-testing-skill
parent: "[[cap-06-apply-developer-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 063 — Skill: `developer-unit-testing`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/developer-unit-testing/SKILL.md`. Delivers part of [[cap-06-apply-developer-discipline]].

## What it delivers

Lets the Developer write / run the developer-owned testing layer per Jones BP #37 — subroutine testing (~50 % DRE), module testing, unit testing (25 % plain / 52 % PSP/TSP) — with explicit awareness that this layer is a *complement* to inspection + static analysis, not a substitute. Test cases themselves require inspection (Table 9-22 #8: 83 % DRE on test-case inspection).

## Stories (children)

- [[story-063-A-test-cases-inspected-too]] — As a Developer authoring tests, I want test cases inspected before execution, so test-case defects (which can exceed code defects in some IBM samples) don't propagate.

## Spec sibling

- [[spec-063-developer-unit-testing-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: Capers Jones BP #37 (pp. 128–132); BP #28 practice 9; Ch 9 Table 9-22.
- Substrate evidence: `.claude/skills/developer-unit-testing/SKILL.md`.
