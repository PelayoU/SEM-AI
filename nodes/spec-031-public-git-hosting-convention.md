---
category: spec
id: spec-031-public-git-hosting-convention
parent: "[[feature-031-public-git-hosting-convention]]"
status: draft
created: 2026-05-14
updated: 2026-05-14
---

# Spec 031 — Public git hosting

> Parent: [[feature-031-public-git-hosting-convention]] (planned, status `ready-for-implementation`).

## Stories covered

- [[story-031-A-substrate-public-readable]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Repo published to public git host; default branch readable at a public URL without authentication.

## Gherkin spec

```gherkin
Feature: Public git hosting

  Scenario: AC-A1 — Substrate readable at public URL
    Given the repo is pushed to a public git host
    When I fetch the public URL of the default branch without auth
    Then I receive the repo content
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-031-public-git-hosting-convention]].
