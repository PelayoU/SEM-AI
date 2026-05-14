---
category: spec
id: spec-058-qa-testing-strategy-skill
parent: "[[feature-058-qa-testing-strategy-skill]]"
artifacts:
  - "[[.claude/skills/qa-testing-strategy/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 058 — Skill `qa-testing-strategy` exists and conforms

> Parent: [[feature-058-qa-testing-strategy-skill]].

## Stories covered

- [[story-058-A-testing-is-not-the-stack]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #37 (20+ test forms grouped developer/specialist/customer, 3–12 typically applied, testing-alone <80% cumulative, ≥95% requires combination).

## Gherkin spec

```gherkin
Feature: Skill qa-testing-strategy
  Scenario: AC-A1 — Skill conforms and cites BP #37
    Given ".claude/skills/qa-testing-strategy/SKILL.md"
    When I open it
    Then 6 sections present, 20+ test forms inventory documented, testing-alone-<80% empirics cited, combined-stack >95% requirement stated
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-058-qa-testing-strategy-skill]].
