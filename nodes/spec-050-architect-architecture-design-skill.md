---
category: spec
id: spec-050-architect-architecture-design-skill
parent: "[[feature-050-architect-architecture-design-skill]]"
artifacts:
  - "[[.claude/skills/architect-architecture-design/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 050 — Skill `architect-architecture-design` exists and conforms

> Parent: [[feature-050-architect-architecture-design-skill]].

## Stories covered

- [[story-050-A-seven-topics-as-audit-grid]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #14 + Ch 7 (seven fundamental topics + Zachman 6×6 + size-tier Table 7-7) + Ch 9 Table 9-23.

## Gherkin spec

```gherkin
Feature: Skill architect-architecture-design
  Scenario: AC-A1 — Skill conforms and cites Ch 7
    Given ".claude/skills/architect-architecture-design/SKILL.md"
    When I open it
    Then 6 sections present, 7 fundamental topics enumerated, Zachman schema referenced, Table 7-7 size-tier rule cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-050-architect-architecture-design-skill]].
