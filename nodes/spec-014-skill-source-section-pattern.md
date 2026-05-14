---
category: spec
id: spec-014-skill-source-section-pattern
parent: "[[feature-014-skill-source-section-pattern]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 014 — Mandatory `## Source` in every skill

> Parent: [[feature-014-skill-source-section-pattern]].

## Stories covered

- [[story-014-A-source-section-mandatory]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Every SKILL.md file under `.claude/skills/` carries a `## Source` section.

## Gherkin spec

```gherkin
Feature: Mandatory Source section per skill

  Scenario: AC-A1 — Every SKILL.md has Source section
    Given all SKILL.md files under ".claude/skills/"
    When I run "grep -L '^## Source' .claude/skills/*/SKILL.md"
    Then the result is empty (no skill lacks the section)
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-014-skill-source-section-pattern]].
