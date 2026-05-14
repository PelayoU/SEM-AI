---
category: spec
id: spec-065-devops-configuration-control-skill
parent: "[[feature-065-devops-configuration-control-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 065 — Skill `devops-configuration-control` exists and conforms

> Parent: [[feature-065-devops-configuration-control-skill]].

## Stories covered

- [[story-065-A-all-deliverables-under-cm]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #34 + ISO 10007-2003 + IEEE 828-1998 (all deliverables under CM, unique IDs, cross-deliverable mapping, locked masters, mechanical-not-judgemental rule).

## Gherkin spec

```gherkin
Feature: Skill devops-configuration-control
  Scenario: AC-A1 — Skill conforms and cites BP #34 + standards
    Given ".claude/skills/devops-configuration-control/SKILL.md"
    When I open it
    Then 6 sections present, all deliverable classes covered, ISO 10007 + IEEE 828 cited as convention, mechanical-vs-judgement scope boundary stated
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-065-devops-configuration-control-skill]].
