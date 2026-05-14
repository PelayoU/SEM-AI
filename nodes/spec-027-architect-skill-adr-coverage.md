---
category: spec
id: spec-027-architect-skill-adr-coverage
parent: "[[feature-027-architect-skill-adr-coverage]]"
artifacts:
  - "[[.claude/skills/architect-architecture-design/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 027 — Architect skill provides ADR content criteria

> Parent: [[feature-027-architect-skill-adr-coverage]].

## Stories covered

- [[story-027-A-architect-skill-as-adr-criteria]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/skills/architect-architecture-design/SKILL.md` carries the formal criteria (7 fundamental topics + Zachman + size-tier) used as ADR content reference.

## Gherkin spec

```gherkin
Feature: Architect skill covers ADR content criteria

  Scenario: AC-A1 — Skill enumerates 7 topics + Zachman + size-tier
    Given ".claude/skills/architect-architecture-design/SKILL.md"
    When I read its formal criteria
    Then the 7 fundamental topics, Zachman schema, and size-tier scaling are present
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-027-architect-skill-adr-coverage]].
