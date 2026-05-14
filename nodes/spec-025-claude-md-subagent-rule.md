---
category: spec
id: spec-025-claude-md-subagent-rule
parent: "[[feature-025-claude-md-subagent-rule]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 025 — CLAUDE.md subagent-dispatch rule

> Parent: [[feature-025-claude-md-subagent-rule]].

## Stories covered

- [[story-025-A-rule-loaded-at-session-start]] — AC-A1

## Acceptance Criteria

- **AC-A1:** CLAUDE.md Layer B contains the "Subagent dispatch ≠ authority transfer" rule with concrete framing of when to use full handoff instead.

## Gherkin spec

```gherkin
Feature: Subagent dispatch rule in CLAUDE.md

  Scenario: AC-A1 — Rule present and loaded
    Given CLAUDE.md is loaded at session start
    When I search for "Subagent dispatch"
    Then I find the rule "≠ authority transfer" with explanation
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-025-claude-md-subagent-rule]].
