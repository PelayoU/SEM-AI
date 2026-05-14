---
category: feature
id: feature-057-qa-inspections-program-skill
parent: "[[cap-05-apply-qa-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 057 — Skill: `qa-inspections-program`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/qa-inspections-program/SKILL.md`. Delivers part of [[cap-05-apply-qa-discipline]].

## What it delivers

Lets QA plan / schedule / moderate formal Fagan-origin inspections (IBM, 35+ years) of 8 artifact classes (architecture, requirements, design, DB design, code, test plan, test case, user doc) — average 65 % DRE per artifact, peaks 85–88 % (Tom Gilb), highest single removal method known. 5 preconditions per session (moderator / recorder / prep time / defect log / no appraisal use).

## Stories (children)

- [[story-057-A-inspect-requirements-not-test-them]] — As QA running the inspection program, I want requirements defects caught at requirements inspection, not deferred to testing (which cannot find them per Y2K-style cases).

## Spec sibling

- [[spec-057-qa-inspections-program-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Pairs with static analysis (87 % DRE on coding defects) for the combined defect-removal stack.

## Source

- Anchoring authority: Capers Jones BP #36 (pp. 124–128); Ch 9 Table 9-22; Table 9-23 inspection moderator scope.
- Substrate evidence: `.claude/skills/qa-inspections-program/SKILL.md`.
