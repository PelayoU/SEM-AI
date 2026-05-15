---
category: spec
id: spec-074-agent-decision-verification
parent: "[[feature-074-agent-decision-verification]]"
artifacts:
  - "[[.claude/agents/product-owner.md]]"
  - "[[.claude/agents/architect.md]]"
  - "[[.claude/agents/qa.md]]"
  - "[[.claude/agents/developer.md]]"
  - "[[.claude/agents/devops.md]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Spec 074 — Per-agent decision-verification

> Authored via `po-spec-gherkin`. One Feature per spec.

## Stories covered

- `[[story-074-A-workflow-decision-verification]]` — AC-A1
- `[[story-074-B-workflow-scope-refusal]]` — AC-B1, AC-B2

## Acceptance Criteria

- **AC-A1:** Each of the 5 `.claude/agents/*.md` `## Workflow` contains the decision-verification step (jurisdiction + node-before-artifact), identical in substance.
- **AC-B1:** The step refuses out-of-jurisdiction action on an explicit "do it" and routes feedback→subagent-consultation, work→`/role`.
- **AC-B2:** The step states a consulted subagent is non-authoring (active-role marker = human's declared role).

## Gherkin spec

```gherkin
Feature: Per-agent decision-verification and scope refusal

  In order to make role discipline behavioural, not only audited
  As any role-agent
  I want a Workflow step that verifies before acting and refuses out of scope

  Scenario: AC-A1 — step present in all agents
    Given the 5 agent files
    Then each ## Workflow contains the decision-verification step

  Scenario: AC-B1 — out-of-jurisdiction refused and routed
    Given the active role is product-owner
    When the human says "do it" for an architecture decision
    Then the agent refuses, offers subagent consultation for feedback
    And states cross-role work needs a /role switch

  Scenario: AC-B2 — consultation is non-authoring
    Given a subagent is consulted while .claude/.active-role is product-owner
    When the consulted role would write an ADR path
    Then the gate blocks it (marker reflects the human's role)
```

## Notes

Realized-AC verbatim filled during Phase E (test 5/10 + agent-file inspection).

## Source

- Skill: `po-spec-gherkin`. Cucumber `gherkin-reference.pdf` pp. 1–9; GISF `gisf-life-cycle.pdf` slide 54.
