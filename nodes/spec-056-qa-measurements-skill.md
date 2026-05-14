---
category: spec
id: spec-056-qa-measurements-skill
parent: "[[feature-056-qa-measurements-skill]]"
artifacts:
  - "[[.claude/skills/qa-measurements/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 056 — Skill `qa-measurements` exists and conforms

> Parent: [[feature-056-qa-measurements-skill]].

## Stories covered

- [[story-056-A-no-loc-no-cost-per-defect]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #30 (9 measures + 2 forbidden metrics LOC + cost-per-defect + DRE definition with fixed post-release window).

## Gherkin spec

```gherkin
Feature: Skill qa-measurements
  Scenario: AC-A1 — Skill conforms and cites BP #30
    Given ".claude/skills/qa-measurements/SKILL.md"
    When I open it
    Then 6 sections present, 9 measures enumerated, LOC + cost-per-defect explicitly forbidden, DRE formula defined
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-056-qa-measurements-skill]].
