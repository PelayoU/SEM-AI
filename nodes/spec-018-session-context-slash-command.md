---
category: spec
id: spec-018-session-context-slash-command
parent: "[[feature-018-session-context-slash-command]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 018 — `/session-context` slash command

> Parent: [[feature-018-session-context-slash-command]].

## Stories covered

- [[story-018-A-rehydrate-session-state]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/commands/session-context.md` defines `/session-context`; invocation re-reads the current session doc into the active conversation.

## Gherkin spec

```gherkin
Feature: /session-context slash command

  Scenario: AC-A1 — Session doc re-read into context
    Given an open session on branch "session/<id>"
    When the active role invokes "/session-context"
    Then the session doc content appears in the next turn's context
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-018-session-context-slash-command]].
