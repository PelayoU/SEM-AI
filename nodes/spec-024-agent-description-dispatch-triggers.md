---
category: spec
id: spec-024-agent-description-dispatch-triggers
parent: "[[feature-024-agent-description-dispatch-triggers]]"
artifacts:
  - "[[.claude/agents/product-owner.md]]"
  - "[[.claude/agents/architect.md]]"
  - "[[.claude/agents/qa.md]]"
  - "[[.claude/agents/developer.md]]"
  - "[[.claude/agents/devops.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 024 — Agent description dispatch triggers

> Parent: [[feature-024-agent-description-dispatch-triggers]].

## Stories covered

- [[story-024-A-precise-descriptions-route-correctly]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Each `.claude/agents/<role>.md` carries a `description:` field with concrete trigger phrases sufficient for the harness to route work to the correct role on dispatch.

## Gherkin spec

```gherkin
Feature: Agent description as dispatch trigger surface

  Scenario: AC-A1 — Description routes correctly
    Given a calling agent describes work that maps to role <X>
    When dispatch evaluates "description:" fields across agents
    Then ".claude/agents/<X>.md" is the highest match
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-024-agent-description-dispatch-triggers]].
