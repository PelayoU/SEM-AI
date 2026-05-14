---
category: spec
id: spec-019-session-close-slash-command
parent: "[[feature-019-session-close-slash-command]]"
artifacts:
  - "[[.claude/commands/session-close.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 019 — `/session-close` slash command

> Parent: [[feature-019-session-close-slash-command]].

## Stories covered

- [[story-019-A-finalise-session-state]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/commands/session-close.md` defines `/session-close`; invocation authors `## Closing summary` (Outcome / Pending / Merge decision) and surfaces the merge decision to the human.

## Gherkin spec

```gherkin
Feature: /session-close slash command

  Scenario: AC-A1 — Closing summary authored at session end
    Given an open session on branch "session/<id>"
    When the active role invokes "/session-close"
    Then "## Closing summary" appears in the session doc
    And Outcome, Pending, and Merge decision are filled
    And the human is prompted to sign the merge decision
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-019-session-close-slash-command]].
