---
category: spec
id: spec-006-show-hidden-files-plugin
parent: "[[feature-006-show-hidden-files-plugin]]"
artifacts:
  - "[[.obsidian/plugins/show-hidden-files/manifest.json]]"
  - "[[.obsidian/community-plugins.json]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 006 — Show-hidden-files plugin

> Parent: [[feature-006-show-hidden-files-plugin]].

## Stories covered

- [[story-006-A-dot-files-visible]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Show-hidden-files community plugin is installed and enabled; dot-prefixed files (`.claude/`) are visible in Obsidian's file tree.

## Gherkin spec

```gherkin
Feature: Show-hidden-files plugin exposes .claude/

  Scenario: AC-A1 — Dot-prefixed files visible
    Given the show-hidden-files plugin installed under ".obsidian/plugins/"
    And it is enabled in ".obsidian/community-plugins.json"
    When I view the Obsidian file tree
    Then ".claude/" and other dot-prefixed paths are visible
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-006-show-hidden-files-plugin]].
