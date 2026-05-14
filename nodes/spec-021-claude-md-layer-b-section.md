---
category: spec
id: spec-021-claude-md-layer-b-section
parent: "[[feature-021-claude-md-layer-b-section]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 021 — CLAUDE.md Layer B section

> Parent: [[feature-021-claude-md-layer-b-section]].

## Stories covered

- [[story-021-A-bootstrap-procedure-loaded]] — AC-A1

## Acceptance Criteria

- **AC-A1:** CLAUDE.md `## Layer B — operating the framework` section documents: sessions = git branch, session bootstrap procedure, writing to the session doc, slash commands, subagent dispatch, direct work on main.

## Gherkin spec

```gherkin
Feature: CLAUDE.md Layer B operating section

  Scenario: AC-A1 — Layer B documented in universal contract
    Given CLAUDE.md is loaded
    When I navigate to "Layer B — operating the framework"
    Then the section documents sessions-as-branch, bootstrap procedure, slash commands, and subagent dispatch rules
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-021-claude-md-layer-b-section]].
