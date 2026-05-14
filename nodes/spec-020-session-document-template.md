---
category: spec
id: spec-020-session-document-template
parent: "[[feature-020-session-document-template]]"
artifacts:
  - "[[_obsidian/templates/session.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 020 — Session document template

> Parent: [[feature-020-session-document-template]].

## Stories covered

- [[story-020-A-session-from-template]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `_obsidian/templates/session.md` exists and includes the 5 mandatory body sections (Context, Log, Artifacts touched, Subagent consultations, Closing summary).

## Gherkin spec

```gherkin
Feature: Session document template

  Scenario: AC-A1 — Template carries 5 sections
    Given "_obsidian/templates/session.md" exists
    When I open it
    Then Context, Log, Artifacts touched, Subagent consultations, and Closing summary are all present
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-020-session-document-template]].
