---
category: spec
id: spec-029-license-file
parent: "[[feature-029-license-file]]"
artifacts:
  - "[[LICENSE]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 029 — LICENSE at repo root

> Parent: [[feature-029-license-file]].

## Stories covered

- [[story-029-A-license-at-repo-root]] — AC-A1

## Acceptance Criteria

- **AC-A1:** A file named `LICENSE` exists at repo root. (Substantive license text pending PO decision per Architect Phase-1 concern; this AC tests only the file's presence.)

## Gherkin spec

```gherkin
Feature: LICENSE file at repo root

  Scenario: AC-A1 — LICENSE file present
    Given the repo working tree
    When I run "test -f LICENSE"
    Then exit status is 0
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-029-license-file]].
