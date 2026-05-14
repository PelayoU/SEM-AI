---
category: spec
id: spec-012-skill-references-traceability
parent: "[[feature-012-skill-references-traceability]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 012 — Per-skill bibliographic traceability

> Parent: [[feature-012-skill-references-traceability]].

## Stories covered

- [[story-012-A-audit-skill-citations]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `bibliography/skill-references.md` lists the bibliographic anchors of all 37 skills with star-marked primary sources distinguished from complements.

## Gherkin spec

```gherkin
Feature: Per-skill bibliographic traceability

  Scenario: AC-A1 — Audit-surface complete for 37 skills
    Given "bibliography/skill-references.md"
    When I count sections (one per skill)
    Then all 37 skills are covered
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-012-skill-references-traceability]].
