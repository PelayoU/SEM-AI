---
category: feature
id: feature-054-architect-performance-analysis-skill
parent: "[[cap-04-apply-architect-discipline]]"
artifacts:
  - "[[.claude/skills/architect-performance-analysis/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 054 — Skill: `architect-performance-analysis`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/architect-performance-analysis/SKILL.md`. Delivers part of [[cap-04-apply-architect-discipline]].

## What it delivers

Lets the Architect plan / execute performance analysis using profilers + instrumentation + the perf↔quality↔security overlap principle (Jones BP #39), with the bug-class taxonomy (heisenbug / bohrbug / mandelbug / schrodenbug) for diagnostic routing. Specialist threshold at 100 k FP.

## Stories (children)

- [[story-054-A-perf-as-architecture-not-tuning]] — As an Architect, I want performance budgeted at design stage (architecture topic 6 per Jones Ch 7), so optimisation isn't a last-mile code patch.

## Spec sibling

- [[spec-054-architect-performance-analysis-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Performance ↔ quality ↔ security overlap: a high-severity bug drops perf to zero; DoS is a perf issue.

## Source

- Anchoring authority: Capers Jones BP #39 (pp. 134–135); Ch 9 Table 9-23 (perf specialist scope); Ch 7 topic 6 cross-link.
- Substrate evidence: `.claude/skills/architect-performance-analysis/SKILL.md`.
