---
category: spec
id: spec-010-claude-md-role-scope-section
parent: "[[feature-010-claude-md-role-scope-section]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 010 — CLAUDE.md `## Roles` section + invocation modes

> Parent: [[feature-010-claude-md-role-scope-section]].

## Stories covered

- [[story-010-A-roles-table-loaded]] — AC-A1
- [[story-010-B-invocation-mode-clarity]] — AC-B1

## Acceptance Criteria

- **AC-A1:** `CLAUDE.md` carries a `## Roles` table loaded at every session start.
- **AC-B1:** The section documents both invocation modes (full role via `claude --agent` vs subagent consultation via `Task`).

## Gherkin spec

```gherkin
Feature: CLAUDE.md roles section + invocation modes

  Scenario: AC-A1 — Roles table loaded at session start
    Given a new session opens
    When CLAUDE.md is loaded by the harness
    Then the "## Roles" table is in the agent's context

  Scenario: AC-B1 — Two invocation modes documented
    Given the "## Roles" section
    When I read the "Invocation modes" subsection
    Then both modes are described with cross-link to ADR 005
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-010-claude-md-role-scope-section]].
