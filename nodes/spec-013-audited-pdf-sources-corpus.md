---
category: spec
id: spec-013-audited-pdf-sources-corpus
parent: "[[feature-013-audited-pdf-sources-corpus]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 013 — Audited PDF sources corpus

> Parent: [[feature-013-audited-pdf-sources-corpus]].

## Stories covered

- [[story-013-A-corpus-versioned-with-substrate]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `bibliography/sources/` contains 12 audited PDF files (Jones BP + 8 GISF + Cucumber + Patton + agile-story-essentials).

## Gherkin spec

```gherkin
Feature: Audited PDF sources corpus

  Scenario: AC-A1 — Corpus complete
    Given "bibliography/sources/"
    When I list the PDF files
    Then 12 audited primary-source PDFs are present
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-013-audited-pdf-sources-corpus]].
