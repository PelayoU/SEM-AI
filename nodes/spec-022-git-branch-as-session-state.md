---
category: spec
id: spec-022-git-branch-as-session-state
parent: "[[feature-022-git-branch-as-session-state]]"
artifacts:
  # No concrete substrate — this node describes an abstract property
  # without a single artefact owner. See CLAUDE.md § Substrate traceability.
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 022 — Git branch as session-state carrier

> Parent: [[feature-022-git-branch-as-session-state]].

## Stories covered

- [[story-022-A-session-as-branch]] — AC-A1
- [[story-022-B-branch-list-as-open-sessions]] — AC-B1

## Acceptance Criteria

- **AC-A1:** Every session lives on a git branch named `session/<id>` matching its session doc id at `sessions/<id>.md`.
- **AC-B1:** Listing open sessions = `git branch --list 'session/*'`.

## Gherkin spec

```gherkin
Feature: Git branch as session state

  Scenario: AC-A1 — Session has matching branch
    Given a session id "<id>"
    When I run "git branch --show-current"
    Then I see "session/<id>"
    And "sessions/<id>.md" exists on the branch

  Scenario: AC-B1 — Open sessions enumerated by branch listing
    Given any number of open sessions
    When I run "git branch --list 'session/*'"
    Then the result lists exactly the open sessions
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-022-git-branch-as-session-state]].
