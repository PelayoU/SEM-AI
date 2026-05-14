---
category: spec
id: spec-008-agent-meta-template
parent: "[[feature-008-agent-meta-template]]"
artifacts:
  - "[[.claude/templates/agent.md.template]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 008 — Agent meta-template

> Parent: [[feature-008-agent-meta-template]].

## Stories covered

- [[story-008-A-new-role-from-template]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/templates/agent.md.template` exists and carries the required structure (frontmatter + Identity / When to invoke / Skills / Workflow / Interaction / Gotchas / Source).

## Gherkin spec

```gherkin
Feature: Agent meta-template for new role-agents

  Scenario: AC-A1 — Meta-template carries required structure
    Given the file ".claude/templates/agent.md.template" exists
    When I instantiate a new role-agent from it
    Then frontmatter, Identity, When-to-invoke, Skills, Workflow, Interaction, Gotchas, and Source sections are present
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-008-agent-meta-template]].
