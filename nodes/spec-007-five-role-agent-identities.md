---
category: spec
id: spec-007-five-role-agent-identities
parent: "[[feature-007-five-role-agent-identities]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 007 — Five role-agent identities

> Parent: [[feature-007-five-role-agent-identities]].

## Stories covered

- [[story-007-A-invoke-role-agent]] — AC-A1
- [[story-007-B-subagent-dispatch-by-description]] — AC-B1

## Acceptance Criteria

- **AC-A1:** Five `.claude/agents/<role>.md` files exist (product-owner, architect, qa, developer, devops); `claude --agent <role>` loads the agent's identity.
- **AC-B1:** `Task` dispatch with `subagent_type: <role>` routes to the matching agent via its `description:` field.

## Gherkin spec

```gherkin
Feature: Five implemented role-agent identities

  Scenario: AC-A1 — Invoke a role-agent by name
    Given five agent files under ".claude/agents/"
    When I invoke "claude --agent <role>"
    Then the agent's identity is loaded alongside CLAUDE.md

  Scenario: AC-B1 — Subagent dispatch routes by description match
    Given a calling agent uses Task with "subagent_type: <role>"
    When dispatch resolves
    Then the matching ".claude/agents/<role>.md" runs in a fresh context
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-007-five-role-agent-identities]].
