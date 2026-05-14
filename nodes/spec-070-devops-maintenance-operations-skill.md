---
category: spec
id: spec-070-devops-maintenance-operations-skill
parent: "[[feature-070-devops-maintenance-operations-skill]]"
artifacts:
  - "[[.claude/skills/devops-maintenance-operations/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 070 — Skill `devops-maintenance-operations` exists and conforms

> Parent: [[feature-070-devops-maintenance-operations-skill]].

## Stories covered

- [[story-070-A-flow-visualised-not-tribal]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #48 ops side + Ch 5 Table 5-1 + GISF `gisf-delivery-control-and-monitoring.pdf` (Release Kanban + Burn-Up + Daily stand-up).

## Gherkin spec

```gherkin
Feature: Skill devops-maintenance-operations
  Scenario: AC-A1 — Skill conforms and cites BP #48 + GISF
    Given ".claude/skills/devops-maintenance-operations/SKILL.md"
    When I open it
    Then 6 sections present, ITIL flagged as convention pointer, Release Kanban + Burn-Up + Daily stand-up described
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-070-devops-maintenance-operations-skill]].
