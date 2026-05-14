---
category: feature
id: feature-060-developer-coding-practices-skill
parent: "[[cap-06-apply-developer-discipline]]"
artifacts:
  - "[[.claude/skills/developer-coding-practices/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 060 — Skill: `developer-coding-practices`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/developer-coding-practices/SKILL.md`. Delivers part of [[cap-06-apply-developer-discipline]].

## What it delivers

Lets the Developer apply Jones BP #28's 13 programming best practices when writing new code: language selection (from >700), structured programming, certified reuse, security planning, complexity ceilings (<10 safe / >20 dangerous), clear comments, static analysis, TDD or concurrent test design, formal code inspections, re-inspection after change, legacy renovation, error-prone-module removal.

## Stories (children)

- [[story-060-A-thirteen-practices-walked]] — As a Developer about to write new code, I want each of the 13 practices applied or explicitly marked not applicable, so silence on a practice is structural rather than oversight.

## Spec sibling

- [[spec-060-developer-coding-practices-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: Capers Jones BP #28 (pp. 107–109); Ch 8 § Forms of Programming Defect Prevention (pp. 519–525); Ch 9 Table 9-22.
- Substrate evidence: `.claude/skills/developer-coding-practices/SKILL.md`.
