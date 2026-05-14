---
category: spec
id: spec-060-developer-coding-practices-skill
parent: "[[feature-060-developer-coding-practices-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 060 — Skill `developer-coding-practices` exists and conforms

> Parent: [[feature-060-developer-coding-practices-skill]].

## Stories covered

- [[story-060-A-thirteen-practices-walked]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #28 (13 coding best practices) + Ch 8 § Forms of Programming Defect Prevention.

## Gherkin spec

```gherkin
Feature: Skill developer-coding-practices
  Scenario: AC-A1 — Skill conforms and cites BP #28
    Given ".claude/skills/developer-coding-practices/SKILL.md"
    When I open it
    Then 6 sections present, 13 practices enumerated, complexity ceilings (<10 / >20) cited, custom-coded-most-expensive observation referenced
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-060-developer-coding-practices-skill]].
