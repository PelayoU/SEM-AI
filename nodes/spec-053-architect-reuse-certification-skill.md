---
category: spec
id: spec-053-architect-reuse-certification-skill
parent: "[[feature-053-architect-reuse-certification-skill]]"
artifacts:
  - "[[.claude/skills/architect-reuse-certification/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 053 — Skill `architect-reuse-certification` exists and conforms

> Parent: [[feature-053-architect-reuse-certification-skill]].

## Stories covered

- [[story-053-A-no-uncertified-admission]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #27 (zero-defect target + 11 supporting practices + security back-door warning).

## Gherkin spec

```gherkin
Feature: Skill architect-reuse-certification
  Scenario: AC-A1 — Skill conforms and cites BP #27
    Given ".claude/skills/architect-reuse-certification/SKILL.md"
    When I open it
    Then 6 sections present, 11 supporting practices enumerated, security back-door warning cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-053-architect-reuse-certification-skill]].
