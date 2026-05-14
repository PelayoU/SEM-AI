---
category: spec
id: spec-064-developer-maintenance-skill
parent: "[[feature-064-developer-maintenance-skill]]"
artifacts:
  - "[[.claude/skills/developer-maintenance/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 064 — Skill `developer-maintenance` exists and conforms

> Parent: [[feature-064-developer-maintenance-skill]].

## Stories covered

- [[story-064-A-renovate-before-enhance]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #48 (23 work-type taxonomy + 14+ legacy best practices + renovate-before-enhance + 5%/50% error-prone-module rule).

## Gherkin spec

```gherkin
Feature: Skill developer-maintenance
  Scenario: AC-A1 — Skill conforms and cites BP #48
    Given ".claude/skills/developer-maintenance/SKILL.md"
    When I open it
    Then 6 sections present, 23 maintenance work types enumerated, renovate-before-enhance rule cited, 5%/50% error-prone-module empiric stated
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-064-developer-maintenance-skill]].
