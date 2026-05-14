---
category: spec
id: spec-055-qa-sqa-program-skill
parent: "[[feature-055-qa-sqa-program-skill]]"
artifacts:
  - "[[.claude/skills/qa-sqa-program/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 055 — Skill `qa-sqa-program` exists and conforms

> Parent: [[feature-055-qa-sqa-program-skill]].

## Stories covered

- [[story-055-A-independence-structurally]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #35 + Ch 5 § SQA Organizations (independence imperative p. 282, 4 organizational patterns, 1–3% staff ratio, mandatory >2,500 FP, release-stop authority).

## Gherkin spec

```gherkin
Feature: Skill qa-sqa-program
  Scenario: AC-A1 — Skill conforms and cites BP #35 + Ch 5
    Given ".claude/skills/qa-sqa-program/SKILL.md"
    When I open it
    Then 6 sections present, independence imperative quoted from Ch 5 p. 282, 4 organizational patterns named, mandatory >2,500 FP threshold cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-055-qa-sqa-program-skill]].
