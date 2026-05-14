---
category: spec
id: spec-035-po-vision-skill
parent: "[[feature-035-po-vision-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 035 — Skill `po-vision` exists and conforms

> Parent: [[feature-035-po-vision-skill]].

## Stories covered

- [[story-035-A-author-vision-against-cagan-ten]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/skills/po-vision/SKILL.md` exists; carries the 6 fixed body sections + Cagan 10 principles verbatim + 5-step method + 2–10-year horizon + positioning template; every criterion cites primary source.

## Gherkin spec

```gherkin
Feature: Skill po-vision

  Scenario: AC-A1 — Skill file conforms and cites
    Given ".claude/skills/po-vision/SKILL.md"
    When I open the file
    Then Purpose / When applies / Formal criteria / How you proceed / Pitfalls / Source are present
    And Cagan 10 principles are listed verbatim
    And every criterion carries a primary-source citation
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-035-po-vision-skill]].
