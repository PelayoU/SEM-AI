---
category: spec
id: spec-016-claude-md-citation-mandate
parent: "[[feature-016-claude-md-citation-mandate]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 016 — CLAUDE.md citation mandate + flagging

> Parent: [[feature-016-claude-md-citation-mandate]].

## Stories covered

- [[story-016-A-citation-mandate-loaded]] — AC-A1
- [[story-016-B-out-of-biblio-flagged]] — AC-B1

## Acceptance Criteria

- **AC-A1:** CLAUDE.md operating-principles section names the citation mandate ("every authoritative claim traces to a primary source").
- **AC-B1:** CLAUDE.md names the out-of-bibliography flagging rule ("named, not borrowed silently").

## Gherkin spec

```gherkin
Feature: CLAUDE.md citation mandate

  Scenario: AC-A1 — Citation mandate present
    Given CLAUDE.md is loaded
    When I search the "Operating principles" section
    Then "Citation is mandatory" appears

  Scenario: AC-B1 — Out-of-bibliography flagging rule present
    Given CLAUDE.md is loaded
    When I search for the flagging convention
    Then "Out-of-bibliography is named, not borrowed silently" appears
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-016-claude-md-citation-mandate]].
