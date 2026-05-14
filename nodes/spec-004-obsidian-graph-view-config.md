---
category: spec
id: spec-004-obsidian-graph-view-config
parent: "[[feature-004-obsidian-graph-view-config]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 004 — Obsidian graph-view configuration

> Parent: [[feature-004-obsidian-graph-view-config]].

## Stories covered

- [[story-004-A-graph-view-renders-backbone]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.obsidian/graph.json` carries the SEM-IA-tuned graph-view config; opening graph view in Obsidian renders the backbone hierarchy with distinguishable category clusters.

## Gherkin spec

```gherkin
Feature: Obsidian graph-view configuration

  Scenario: AC-A1 — Graph view renders backbone legibly
    Given the vault is open in Obsidian
    And ".obsidian/graph.json" carries the SEM-IA config
    When I open graph view
    Then I see distinguishable clusters for vision, goal, capability, feature, story, spec, adr
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-004-obsidian-graph-view-config]].
