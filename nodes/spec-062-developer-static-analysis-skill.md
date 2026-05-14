---
category: spec
id: spec-062-developer-static-analysis-skill
parent: "[[feature-062-developer-static-analysis-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 062 — Skill `developer-static-analysis` exists and conforms

> Parent: [[feature-062-developer-static-analysis-skill]].

## Stories covered

- [[story-062-A-run-before-inspection]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #36 + Ch 8 § Automated static analysis (~87% DRE; ~50 supported languages; tuning vs suppression rule; pre-inspection sequence).

## Gherkin spec

```gherkin
Feature: Skill developer-static-analysis
  Scenario: AC-A1 — Skill conforms and cites BP #36 + Ch 8
    Given ".claude/skills/developer-static-analysis/SKILL.md"
    When I open it
    Then 6 sections present, ~87% DRE figure cited, supported-languages range stated, pre-inspection-sequence rule named
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-062-developer-static-analysis-skill]].
