---
category: spec
id: spec-037-po-capabilities-skill
parent: "[[feature-037-po-capabilities-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 037 — Skill `po-capabilities` exists and conforms

> Parent: [[feature-037-po-capabilities-skill]].

## Stories covered

- [[story-037-A-derive-implementation-agnostic-capabilities]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/skills/po-capabilities/SKILL.md` exists, conforms to 6-section template, encodes implementation-agnostic test + MVP filter + Cagan 4 risks + slide-54 definition.

## Gherkin spec

```gherkin
Feature: Skill po-capabilities
  Scenario: AC-A1 — Skill conforms
    Given ".claude/skills/po-capabilities/SKILL.md"
    When I open it
    Then 6 sections present and criteria cite GISF slide 54, 69, 64
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-037-po-capabilities-skill]].
