---
category: spec
id: spec-023-task-tool-integration
parent: "[[feature-023-task-tool-integration]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 023 — Task tool integration

> Parent: [[feature-023-task-tool-integration]].

## Stories covered

- [[story-023-A-dispatch-by-subagent-type]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Claude Code's `Task` tool with `subagent_type: <role>` dispatches the matching `.claude/agents/<role>.md` and returns a structured response.

## Gherkin spec

```gherkin
Feature: Task tool integration for subagent dispatch

  Scenario: AC-A1 — Dispatch routes by subagent_type
    Given the harness exposes the Task tool
    When a calling agent invokes Task with "subagent_type: <role>"
    Then ".claude/agents/<role>.md" runs in a fresh context
    And the calling agent receives a structured response when complete
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-023-task-tool-integration]].
