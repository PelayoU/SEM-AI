---
category: spec
id: spec-036-po-goals-skill
parent: "[[feature-036-po-goals-skill]]"
artifacts:
  - "[[.claude/skills/po-goals/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 036 — Skill `po-goals` exists and conforms

> Parent: [[feature-036-po-goals-skill]].

## Stories covered

- [[story-036-A-derive-smart-goals-under-vision]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/skills/po-goals/SKILL.md` exists, conforms to 6-section template, encodes SMART criteria + multilevel horizons + why-stack + slide-95 stakeholder form, citation per criterion.

## Gherkin spec

```gherkin
Feature: Skill po-goals
  Scenario: AC-A1 — Skill conforms
    Given ".claude/skills/po-goals/SKILL.md"
    When I open it
    Then 6 fixed sections present, SMART + horizons + why-stack documented, citations per criterion
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-036-po-goals-skill]].
