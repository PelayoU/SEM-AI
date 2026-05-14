---
category: spec
id: spec-044-po-change-control-skill
parent: "[[feature-044-po-change-control-skill]]"
artifacts:
  - "[[.claude/skills/po-change-control/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 044 — Skill `po-change-control` exists and conforms

> Parent: [[feature-044-po-change-control-skill]].

## Stories covered

- [[story-044-A-fp-quantified-crs]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #33 (16 practices, joint CCB, 10-FP threshold) + critical-topic Ch 1 p. 19.

## Gherkin spec

```gherkin
Feature: Skill po-change-control
  Scenario: AC-A1 — Skill conforms and cites BP #33
    Given ".claude/skills/po-change-control/SKILL.md"
    When I open it
    Then 6 sections present, 16 practices enumerated, 10-FP re-estimation rule cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-044-po-change-control-skill]].
