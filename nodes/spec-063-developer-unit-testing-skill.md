---
category: spec
id: spec-063-developer-unit-testing-skill
parent: "[[feature-063-developer-unit-testing-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 063 — Skill `developer-unit-testing` exists and conforms

> Parent: [[feature-063-developer-unit-testing-skill]].

## Stories covered

- [[story-063-A-test-cases-inspected-too]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #37 developer side (subroutine 50% DRE, module, unit 25 / 52% PSP-TSP) + Ch 9 Table 9-22 + test-case inspection (83% DRE).

## Gherkin spec

```gherkin
Feature: Skill developer-unit-testing
  Scenario: AC-A1 — Skill conforms and cites BP #37
    Given ".claude/skills/developer-unit-testing/SKILL.md"
    When I open it
    Then 6 sections present, subroutine + module + unit testing levels documented, test-case inspection cited as part of stack
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-063-developer-unit-testing-skill]].
