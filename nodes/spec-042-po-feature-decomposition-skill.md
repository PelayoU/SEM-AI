---
category: spec
id: spec-042-po-feature-decomposition-skill
parent: "[[feature-042-po-feature-decomposition-skill]]"
artifacts:
  - "[[.claude/skills/po-feature-decomposition/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 042 — Skill `po-feature-decomposition` exists and conforms

> Parent: [[feature-042-po-feature-decomposition-skill]].

## Stories covered

- [[story-042-A-decompose-with-invest]] — AC-A1
- [[story-042-B-story-map-narrative-flow]] — AC-B1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, encodes INVEST + Cohn format + 5 Cs cycle.
- **AC-B1:** Skill encodes Patton User Story Map (Activity → Task → Sub-task) with release-slice rule.

## Gherkin spec

```gherkin
Feature: Skill po-feature-decomposition
  Scenario: AC-A1 — INVEST + Cohn + 5 Cs documented
    Given ".claude/skills/po-feature-decomposition/SKILL.md"
    When I open it
    Then INVEST letters enumerated, Cohn template present, 5 Cs cycle described

  Scenario: AC-B1 — Patton USM documented
    Given the same skill
    When I read the story-map section
    Then Activity → Task → Sub-task hierarchy and release-slice rule are present
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-042-po-feature-decomposition-skill]].
