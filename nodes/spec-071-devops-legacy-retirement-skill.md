---
category: spec
id: spec-071-devops-legacy-retirement-skill
parent: "[[feature-071-devops-legacy-retirement-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 071 — Skill `devops-legacy-retirement` exists and conforms

> Parent: [[feature-071-devops-legacy-retirement-skill]].

## Stories covered

- [[story-071-A-mine-rules-before-replacement]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #50 (8 retirement practices: mine business rules, survey users, search alternatives, stabilize, SOA fit, certified reuse, language conversion, static analysis) + long-lifespan empirics (20–30+ years).

## Gherkin spec

```gherkin
Feature: Skill devops-legacy-retirement
  Scenario: AC-A1 — Skill conforms and cites BP #50
    Given ".claude/skills/devops-legacy-retirement/SKILL.md"
    When I open it
    Then 6 sections present, 8 retirement practices enumerated, dead-language problem named, just-turn-it-off anti-pattern explicitly refused
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-071-devops-legacy-retirement-skill]].
