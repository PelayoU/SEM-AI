---
category: spec
id: spec-051-architect-methodology-selection-skill
parent: "[[feature-051-architect-methodology-selection-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 051 — Skill `architect-methodology-selection` exists and conforms

> Parent: [[feature-051-architect-methodology-selection-skill]].

## Stories covered

- [[story-051-A-benchmark-anchored-selection]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #9 (5-axis suitability: size / type / nature / attribute / activity) + benchmark-as-input mandate.

## Gherkin spec

```gherkin
Feature: Skill architect-methodology-selection
  Scenario: AC-A1 — Skill conforms and cites BP #9
    Given ".claude/skills/architect-methodology-selection/SKILL.md"
    When I open it
    Then 6 sections present, 5-axis matrix described, ~18 methodology candidates listed, fashion-driven failure mode named
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-051-architect-methodology-selection-skill]].
