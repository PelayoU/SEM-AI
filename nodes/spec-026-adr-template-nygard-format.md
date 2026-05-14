---
category: spec
id: spec-026-adr-template-nygard-format
parent: "[[feature-026-adr-template-nygard-format]]"
artifacts:
  - "[[_obsidian/templates/adr.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 026 — ADR template (Nygard format)

> Parent: [[feature-026-adr-template-nygard-format]].

## Stories covered

- [[story-026-A-adr-template-enforces-structure]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `_obsidian/templates/adr.md` carries: frontmatter (id, parent, status, supersedes/superseded-by) + Status + Context + Decision + Consequences (positive/negative/neutral) + Alternatives considered + Seven fundamental topics touchpoints + Source.

## Gherkin spec

```gherkin
Feature: ADR template enforces audit-grid structure

  Scenario: AC-A1 — Template carries all required sections
    Given "_obsidian/templates/adr.md" exists
    When I open it
    Then frontmatter (status, supersedes), Status, Context, Decision, Consequences (positive/negative/neutral), Alternatives, Seven fundamental topics, Source are all present
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-026-adr-template-nygard-format]]. Jones Ch 7 p. 470 (seven topics).
