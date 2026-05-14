---
category: spec
id: spec-009-role-catalog-design-doc
parent: "[[feature-009-role-catalog-design-doc]]"
artifacts:
  - "[[.claude/sem-role-catalog.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 009 — Role catalog design document

> Parent: [[feature-009-role-catalog-design-doc]].

## Stories covered

- [[story-009-A-role-catalog-source-of-truth]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/sem-role-catalog.md` exists and consistently defines the 5 core + Tier-3 planned + Tier-4 emergence roles + BP↔skill mapping.

## Gherkin spec

```gherkin
Feature: Role catalog as single source of truth

  Scenario: AC-A1 — Catalog consistent with agent files
    Given ".claude/sem-role-catalog.md" enumerates the role catalog
    When I cross-check against ".claude/agents/<role>.md"
    Then every implemented role in the catalog has a matching agent file
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-009-role-catalog-design-doc]].
