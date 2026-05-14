---
category: spec
id: spec-005-obsidian-backlinks-pane
parent: "[[feature-005-obsidian-backlinks-pane]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 005 — Obsidian backlinks pane

> Parent: [[feature-005-obsidian-backlinks-pane]].

## Stories covered

- [[story-005-A-backlinks-surface-references]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Backlinks pane is enabled (core plugin) and included in workspace layout; opening any node populates the pane with referring nodes.

## Gherkin spec

```gherkin
Feature: Obsidian backlinks pane

  Scenario: AC-A1 — Backlinks pane populates on node open
    Given backlinks core plugin is enabled in ".obsidian/core-plugins.json"
    And the backlinks pane is in the workspace layout
    When I open a node that has incoming wikilinks
    Then the backlinks pane lists referring nodes
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-005-obsidian-backlinks-pane]].
