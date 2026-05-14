---
category: feature
id: feature-053-architect-reuse-certification-skill
parent: "[[cap-04-apply-architect-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 053 — Skill: `architect-reuse-certification`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/architect-reuse-certification/SKILL.md`. Delivers part of [[cap-04-apply-architect-discipline]].

## What it delivers

Lets the Architect operate the certification gate that decides whether a candidate reusable artifact is safe to admit into the project's reuse library, per Jones BP #27's preconditions: substantially bug-free + free of viruses/back-doors + 11 supporting practices (taxonomy, standard interfaces, test cases + scripts, defect repo, source ID, change records, variation records, distribution records, charging method, warranties).

## Stories (children)

- [[story-053-A-no-uncertified-admission]] — As an Architect curating the reuse library, I want admission gated on certification evidence, so the library doesn't accumulate hazardous artifacts.

## Spec sibling

- [[spec-053-architect-reuse-certification-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Two-edged sword: certified reuse +300 % ROI; uncertified can be –300 %.

## Source

- Anchoring authority: Capers Jones BP #27 (pp. 101–103); cross-link BP #26.
- Substrate evidence: `.claude/skills/architect-reuse-certification/SKILL.md`.
