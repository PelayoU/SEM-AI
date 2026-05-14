---
category: feature
id: feature-062-developer-static-analysis-skill
parent: "[[cap-06-apply-developer-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 062 — Skill: `developer-static-analysis`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/developer-static-analysis/SKILL.md`. Delivers part of [[cap-06-apply-developer-discipline]].

## What it delivers

Lets the Developer run automated static analysis (~87 % DRE on common coding defects per Table 9-22 #1) as both *removal* and *prevention* (programmers spontaneously avoid the flagged defect classes after seeing them). Supported on ~50 languages (Java, C, C++, C# family) out of ~2,500.

## Stories (children)

- [[story-062-A-run-before-inspection]] — As a Developer preparing code for inspection, I want static analysis run first, so inspectors target deeper logic rather than re-finding structural defects.

## Spec sibling

- [[spec-062-developer-static-analysis-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Combines with inspection + testing for the >95 % DRE stack.

## Source

- Anchoring authority: Capers Jones BP #36 (pp. 124–128); Ch 8 § Automated static analysis as defect prevention (pp. 523–524); Ch 9 Table 9-22 #1.
- Substrate evidence: `.claude/skills/developer-static-analysis/SKILL.md`.
