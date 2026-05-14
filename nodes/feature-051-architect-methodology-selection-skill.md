---
category: feature
id: feature-051-architect-methodology-selection-skill
parent: "[[cap-04-apply-architect-discipline]]"
artifacts:
  - "[[.claude/skills/architect-methodology-selection/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 051 — Skill: `architect-methodology-selection`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/architect-methodology-selection/SKILL.md`. Delivers part of [[cap-04-apply-architect-discipline]].

## What it delivers

Lets the Architect select a development methodology (or hybrid) via Jones BP #9's 5-axis suitability matrix (size / type / nature / attribute / activity) anchored in benchmark data, against ~18 candidate methodologies and ~10 partial methods. Refuses fashion-driven choice.

## Stories (children)

- [[story-051-A-benchmark-anchored-selection]] — As an Architect choosing a methodology, I want ISBSG-class benchmark data on similar applications, so selection is empirical rather than fashionable.

## Spec sibling

- [[spec-051-architect-methodology-selection-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]].

## Source

- Anchoring authority: Capers Jones BP #9 (pp. 59–61); ISBSG cross-reference BP #31; legacy-replacement (80 %) BP #11.
- Substrate evidence: `.claude/skills/architect-methodology-selection/SKILL.md`.
