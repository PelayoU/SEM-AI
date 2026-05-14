---
category: spec
id: spec-048-po-milestone-tracking-skill
parent: "[[feature-048-po-milestone-tracking-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 048 — Skill `po-milestone-tracking` exists and conforms

> Parent: [[feature-048-po-milestone-tracking-skill]].

## Stories covered

- [[story-048-A-reject-cosmetic-green-status]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #32 (13 canonical milestones, milestone = formal closure not calendar date, strong-reaction-to-problems mandate).

## Gherkin spec

```gherkin
Feature: Skill po-milestone-tracking
  Scenario: AC-A1 — Skill conforms and cites BP #32
    Given ".claude/skills/po-milestone-tracking/SKILL.md"
    When I open it
    Then 6 sections present, 13 canonical milestones enumerated, cosmetic-green-status anti-pattern named
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-048-po-milestone-tracking-skill]].
