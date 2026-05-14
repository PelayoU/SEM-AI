---
category: story
id: story-043-A-author-gherkin-per-feature
parent: "[[feature-043-po-spec-gherkin-skill]]"
artifacts:
  - "[[.claude/skills/po-spec-gherkin/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 043-A — Author Gherkin spec sibling per feature

> Parent: [[feature-043-po-spec-gherkin-skill]].

As a **PO with INVEST-passing stories under a feature**, I want **a Gherkin spec sibling aggregating ACs from all child stories with story-to-AC traceability**, so that **QA can validate via inspection + testing without spec ambiguity**.

## Conditions of Satisfaction

- One Feature per spec file (Cucumber rule).
- AC numbered with story letter (`AC-A1`, `AC-A2`, …).
- 3–5 steps per Scenario typically.

## INVEST self-check

✅ I · ✅ N · ✅ V · ✅ E · ✅ S · ✅ T (Phase 5 of this session is the live exercise).

## Source

GISF slides 124, 128, 125. Parent: [[feature-043-po-spec-gherkin-skill]]. Cucumber `gherkin-reference.pdf`.
