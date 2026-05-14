---
category: spec
id: spec-001-parent-pointer-convention
parent: "[[feature-001-parent-pointer-convention]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 001 — Parent-pointer convention

> Authored via `po-spec-gherkin`. One Feature per spec (Cucumber rule). Parent: [[feature-001-parent-pointer-convention]].

## Stories covered

- [[story-001-A-parent-pointer-authoring]] — AC-A1, AC-A2

## Acceptance Criteria

- **AC-A1:** Every non-root node carries a `parent:` field in YAML frontmatter.
- **AC-A2:** The `parent:` value is a `[[wikilink]]` that resolves to an existing file under `nodes/`.

## Gherkin spec

```gherkin
Feature: Parent-pointer convention in node frontmatter

  Scenario: AC-A1 — Non-root node carries parent field
    Given a node file under "nodes/" that is not "vision-sem-ia.md"
    When I read its YAML frontmatter
    Then a "parent:" field exists

  Scenario: AC-A2 — Parent wikilink resolves to an existing node
    Given a node with a "parent: [[X]]" field
    When I look for the file "nodes/X.md"
    Then the file exists
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9; GISF `gisf-life-cycle.pdf` slide 54 (examples → AC); `gisf-delivery-backlog-management.pdf` slide 126 (SbE structure). Parent: [[feature-001-parent-pointer-convention]].
