---
category: feature
id: feature-058-qa-testing-strategy-skill
parent: "[[cap-05-apply-qa-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 058 — Skill: `qa-testing-strategy`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/qa-testing-strategy/SKILL.md`. Delivers part of [[cap-05-apply-qa-discipline]].

## What it delivers

Lets QA design the testing portfolio from Jones BP #37's 20+ test forms organized as developer / specialist-SQA / customer testing — choosing the 3–12 forms typically applied — with explicit awareness that cumulative testing-alone DRE seldom tops 80 %, so the >95 % safe minimum requires combining testing with inspections + static analysis.

## Stories (children)

- [[story-058-A-testing-is-not-the-stack]] — As QA defending the test strategy, I want explicit framing that testing alone <80 % and the full DRE stack is mandatory, so a "testing only" plan is rejected as malpractice for mission-critical work.

## Spec sibling

- [[spec-058-qa-testing-strategy-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: Capers Jones BP #37 (pp. 128–132); Ch 9 Table 9-22 (test-form DRE values); Table 9-23 (Tester scope).
- Substrate evidence: `.claude/skills/qa-testing-strategy/SKILL.md`.
