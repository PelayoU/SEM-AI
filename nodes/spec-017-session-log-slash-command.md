---
category: spec
id: spec-017-session-log-slash-command
parent: "[[feature-017-session-log-slash-command]]"
artifacts:
  - "[[.claude/commands/session-log.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 017 — `/session-log` slash command

> Parent: [[feature-017-session-log-slash-command]].

## Stories covered

- [[story-017-A-append-log-entry]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/commands/session-log.md` defines `/session-log`; invocation appends a structured Log entry (date + role + decisions + artifacts + next-step) to the current session doc.

## Gherkin spec

```gherkin
Feature: /session-log slash command

  Scenario: AC-A1 — Log entry appended to session doc
    Given an open session on branch "session/<id>"
    And the session doc "sessions/<id>.md" exists
    When the active role invokes "/session-log"
    Then a new Log entry appears in the session doc
    And the entry carries date, role tag, decisions, artifacts, next-step
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-017-session-log-slash-command]].
