---
category: spec
id: spec-061-developer-reuse-application-skill
parent: "[[feature-061-developer-reuse-application-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 061 — Skill `developer-reuse-application` exists and conforms

> Parent: [[feature-061-developer-reuse-application-skill]].

## Stories covered

- [[story-061-A-check-library-before-custom]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BPs #26 + #27 + #28 + Ch 8 § Code reuse as defect prevention (consumer side of reuse; reuse-before-custom rule; uncertified-is-hazardous warning).

## Gherkin spec

```gherkin
Feature: Skill developer-reuse-application
  Scenario: AC-A1 — Skill conforms and cites the reuse stack
    Given ".claude/skills/developer-reuse-application/SKILL.md"
    When I open it
    Then 6 sections present, reuse-before-custom rule cited, certification gate referenced, familiarity-gap debug cost named
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-061-developer-reuse-application-skill]].
