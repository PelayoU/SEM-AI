---
category: spec
id: spec-057-qa-inspections-program-skill
parent: "[[feature-057-qa-inspections-program-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 057 — Skill `qa-inspections-program` exists and conforms

> Parent: [[feature-057-qa-inspections-program-skill]].

## Stories covered

- [[story-057-A-inspect-requirements-not-test-them]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #36 (Fagan origin, 5 preconditions, 8 artifact classes, 65–85% DRE) + Ch 9 Table 9-22.

## Gherkin spec

```gherkin
Feature: Skill qa-inspections-program
  Scenario: AC-A1 — Skill conforms and cites BP #36
    Given ".claude/skills/qa-inspections-program/SKILL.md"
    When I open it
    Then 6 sections present, 5 Fagan preconditions enumerated, 8 inspectable artifacts listed, defect-origin → optimal-removal table referenced
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-057-qa-inspections-program-skill]].
