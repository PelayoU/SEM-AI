---
category: spec
id: spec-033-license-permits-forks
parent: "[[feature-033-license-permits-forks]]"
artifacts:
  - "[[LICENSE]]"
status: draft
created: 2026-05-14
updated: 2026-05-14
---

# Spec 033 — LICENSE legally permits forks

> Parent: [[feature-033-license-permits-forks]] (planned; license choice pending).

## Stories covered

- [[story-033-A-license-permits-fork]] — AC-A1

## Acceptance Criteria

- **AC-A1:** LICENSE terms explicitly permit copying the substrate, modification, and derivative works (OSI-approved or equivalent permissive license).

## Gherkin spec

```gherkin
Feature: LICENSE permits forks legally

  Scenario: AC-A1 — License terms permit derivative works
    Given the LICENSE file with substantive license text
    When I read the granted rights
    Then the rights include: copying, modification, derivative works, use in commercial / academic contexts
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-033-license-permits-forks]]. Future ADR pending PO license choice.
