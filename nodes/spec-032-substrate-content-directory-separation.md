---
category: spec
id: spec-032-substrate-content-directory-separation
parent: "[[feature-032-substrate-content-directory-separation]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 032 — Substrate / content directory separation

> Parent: [[feature-032-substrate-content-directory-separation]].

## Stories covered

- [[story-032-A-fork-substrate-fresh-content]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Repo layout cleanly separates substrate (`.claude/`, `_obsidian/`, `bibliography/`, `CLAUDE.md`, `LICENSE`) from content (`nodes/`, `sessions/`). Forking the substrate and starting fresh content yields a working SEM-IA-derived project.

## Gherkin spec

```gherkin
Feature: Substrate / content directory partition

  Scenario: AC-A1 — Substrate copyable, content fresh
    Given the SEM-IA repo
    When I copy ".claude/", "_obsidian/", "bibliography/", "CLAUDE.md", "LICENSE" to a new repo
    And I leave "nodes/" and "sessions/" empty in the new repo
    Then the new repo carries the substrate without inheriting SEM-IA's own content
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-032-substrate-content-directory-separation]]. [[adr-004-substrate-content-separation]].
