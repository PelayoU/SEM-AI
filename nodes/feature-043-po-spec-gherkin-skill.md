---
category: feature
id: feature-043-po-spec-gherkin-skill
parent: "[[cap-03-apply-po-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 043 — Skill: `po-spec-gherkin`

> Authored via `po-feature-decomposition`. Wrapper around `.claude/skills/po-spec-gherkin/SKILL.md`. Delivers part of [[cap-03-apply-po-discipline]].

## What it delivers

Lets the PO produce / refine the formal Gherkin spec for a feature using Cucumber's primary keywords (Feature, Scenario, Given/When/Then/And/But, Background, Scenario Outline + Examples) with story-to-AC traceability convention (`story-NNN-A` → `AC-A1`, `AC-A2`, …).

## Stories (children)

- [[story-043-A-author-gherkin-per-feature]] — As a PO with INVEST-passing stories, I want a Gherkin spec sibling that aggregates ACs, so QA can validate via inspection + testing without spec ambiguity.

## Spec sibling

- [[spec-043-po-spec-gherkin-skill]]

## Notes

Full criteria + workflow in the wrapped SKILL.md per [[adr-009-skill-as-canonical-method]]. Cucumber convention: 1 Feature per spec file.

## Source

- Anchoring authority: Cucumber `gherkin-reference.pdf` pp. 1–9; specification-by-example structure GISF `gisf-delivery-backlog-management.pdf` slide 126; examples → AC `gisf-life-cycle.pdf` slide 54.
- Substrate evidence: `.claude/skills/po-spec-gherkin/SKILL.md`.
