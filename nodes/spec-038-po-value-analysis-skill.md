---
category: spec
id: spec-038-po-value-analysis-skill
parent: "[[feature-038-po-value-analysis-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 038 — Skill `po-value-analysis` exists and conforms

> Parent: [[feature-038-po-value-analysis-skill]].

## Stories covered

- [[story-038-A-prioritise-by-value-not-loudest-voice]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/skills/po-value-analysis/SKILL.md` exists, conforms to template, anchors on Jones BP #18 (10 tangible + 9 intangible) + Cagan 4 risks.

## Gherkin spec

```gherkin
Feature: Skill po-value-analysis
  Scenario: AC-A1 — Skill conforms and cites BP #18
    Given ".claude/skills/po-value-analysis/SKILL.md"
    When I open it
    Then 6 sections present, BP #18 tangible/intangible items enumerated, Cagan 4 risks present
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-038-po-value-analysis-skill]].
