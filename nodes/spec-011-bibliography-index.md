---
category: spec
id: spec-011-bibliography-index
parent: "[[feature-011-bibliography-index]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 011 — Bibliography INDEX

> Parent: [[feature-011-bibliography-index]].

## Stories covered

- [[story-011-A-locate-citation-via-index]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `bibliography/INDEX.md` lists per-PDF slide/page anchors for every concept cited by skills.

## Gherkin spec

```gherkin
Feature: Bibliography INDEX navigator

  Scenario: AC-A1 — Concept locatable via INDEX
    Given the file "bibliography/INDEX.md" exists
    When I search the INDEX for a concept cited by a skill
    Then I find the exact PDF + slide/page reference
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-011-bibliography-index]].
