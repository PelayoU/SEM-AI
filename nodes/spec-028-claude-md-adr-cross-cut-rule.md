---
category: spec
id: spec-028-claude-md-adr-cross-cut-rule
parent: "[[feature-028-claude-md-adr-cross-cut-rule]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 028 — CLAUDE.md ADR cross-cut rule

> Parent: [[feature-028-claude-md-adr-cross-cut-rule]].

## Stories covered

- [[story-028-A-adr-cross-cut-rule-loaded]] — AC-A1

## Acceptance Criteria

- **AC-A1:** CLAUDE.md "The graph" section states ADRs are cross-cutting (`"adrs (architectural decisions can hang off anywhere)"`).

## Gherkin spec

```gherkin
Feature: ADR cross-cut rule in CLAUDE.md

  Scenario: AC-A1 — Cross-cut rule present
    Given CLAUDE.md is loaded
    When I search "The graph" section
    Then "adrs (architectural decisions can hang off anywhere)" appears
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-028-claude-md-adr-cross-cut-rule]].
