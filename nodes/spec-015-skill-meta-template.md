---
category: spec
id: spec-015-skill-meta-template
parent: "[[feature-015-skill-meta-template]]"
artifacts:
  - "[[.claude/templates/SKILL.md.template]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 015 — Skill meta-template

> Parent: [[feature-015-skill-meta-template]].

## Stories covered

- [[story-015-A-new-skill-from-template]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/templates/SKILL.md.template` exists with the 6 fixed body sections (Purpose / When this skill applies / Formal criteria / How you proceed / Pitfalls to avoid / Source) and the citation-per-criterion pattern.

## Gherkin spec

```gherkin
Feature: Skill meta-template

  Scenario: AC-A1 — Meta-template carries 6 fixed sections
    Given ".claude/templates/SKILL.md.template" exists
    When I instantiate a new skill from it
    Then Purpose / When this skill applies / Formal criteria / How you proceed / Pitfalls to avoid / Source are all present
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-015-skill-meta-template]].
