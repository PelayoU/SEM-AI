---
category: feature
id: feature-061-developer-reuse-application-skill
parent: "[[cap-06-apply-developer-discipline]]"
artifacts:
  - "[[.claude/skills/developer-reuse-application/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 061 — Skill: `developer-reuse-application`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/developer-reuse-application/SKILL.md`. Delivers part of [[cap-06-apply-developer-discipline]].

## What it delivers

Lets the Developer consume already-certified reusable artifacts from the project's reuse library (Architect-curated) — applying the reuse-before-custom rule per Jones BP #28 + #26 + #27, respecting the certification gate, and refusing uncertified candidates that look attractive but are hazardous (negative-ROI risk).

## Stories (children)

- [[story-061-A-check-library-before-custom]] — As a Developer about to implement a feature, I want the reuse library checked first, so custom-coding is the fallback rather than the default.

## Spec sibling

- [[spec-061-developer-reuse-application-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Consumer side of reuse; Architect's `architect-reusability-strategy` + `architect-reuse-certification` set up the library.

## Source

- Anchoring authority: Capers Jones BP #26 (pp. 99–101); BP #27 (pp. 101–103); BP #28 (pp. 107–109); Ch 8 § Code reuse as defect prevention (p. 522).
- Substrate evidence: `.claude/skills/developer-reuse-application/SKILL.md`.
