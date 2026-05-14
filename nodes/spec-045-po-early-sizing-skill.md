---
category: spec
id: spec-045-po-early-sizing-skill
parent: "[[feature-045-po-early-sizing-skill]]"
artifacts:
  - "[[.claude/skills/po-early-sizing/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 045 — Skill `po-early-sizing` exists and conforms

> Parent: [[feature-045-po-early-sizing-skill]].

## Stories covered

- [[story-045-A-fp-sizing-before-estimating]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #6 (FP best practice, LOC malpractice, pattern matching, light FP, full IFPUG) + ISBSG (BP #31).

## Gherkin spec

```gherkin
Feature: Skill po-early-sizing
  Scenario: AC-A1 — Skill conforms and cites BP #6
    Given ".claude/skills/po-early-sizing/SKILL.md"
    When I open it
    Then 6 sections present, FP as primary metric documented, LOC explicitly excluded, ISBSG referenced
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-045-po-early-sizing-skill]].
