---
category: spec
id: spec-047-po-project-planning-skill
parent: "[[feature-047-po-project-planning-skill]]"
artifacts:
  - "[[.claude/skills/po-project-planning/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 047 — Skill `po-project-planning` exists and conforms

> Parent: [[feature-047-po-project-planning-skill]].

## Stories covered

- [[story-047-A-allot-time-for-the-five-skipped]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #15 (11 planning elements + 5 common failures) + GISF multilevel horizons (slide 150).

## Gherkin spec

```gherkin
Feature: Skill po-project-planning
  Scenario: AC-A1 — Skill conforms and cites BP #15
    Given ".claude/skills/po-project-planning/SKILL.md"
    When I open it
    Then 6 sections present, 11 planning elements + 5 common failures documented, Roadmap/Release/Iteration horizons cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-047-po-project-planning-skill]].
