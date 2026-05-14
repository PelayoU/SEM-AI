---
category: spec
id: spec-002-wikilinks-narrative-cross-reference
parent: "[[feature-002-wikilinks-narrative-cross-reference]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 002 — Wikilinks for narrative cross-reference

> Parent: [[feature-002-wikilinks-narrative-cross-reference]].

## Stories covered

- [[story-002-A-wikilinks-in-body]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Wikilinks `[[id]]` in node body resolve to existing nodes (or are explicitly deferred placeholders), and Obsidian's backlinks pane populates for every referenced node.

## Gherkin spec

```gherkin
Feature: Wikilinks for narrative cross-reference

  Scenario: AC-A1 — Wikilink resolves and backlinks populate
    Given a node "A.md" referencing "[[B]]" in its body
    And a node "B.md" exists
    When I open "B.md" in Obsidian
    Then the backlinks pane lists "A.md" as a referring file
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9; GISF slide 54. Parent: [[feature-002-wikilinks-narrative-cross-reference]].
