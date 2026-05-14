---
category: spec
id: spec-041-po-user-involvement-skill
parent: "[[feature-041-po-user-involvement-skill]]"
artifacts:
  - "[[.claude/skills/po-user-involvement/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 041 — Skill `po-user-involvement` exists and conforms

> Parent: [[feature-041-po-user-involvement-skill]].

## Stories covered

- [[story-041-A-scale-aware-user-techniques]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #12 (12 forms) + 5–50 % effort-ratio empirics + scale-aware technique selection.

## Gherkin spec

```gherkin
Feature: Skill po-user-involvement
  Scenario: AC-A1 — Skill conforms and cites BP #12
    Given ".claude/skills/po-user-involvement/SKILL.md"
    When I open it
    Then 6 sections present, 12 forms enumerated, effort-ratio band cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-041-po-user-involvement-skill]].
