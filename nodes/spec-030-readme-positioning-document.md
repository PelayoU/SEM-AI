---
category: spec
id: spec-030-readme-positioning-document
parent: "[[feature-030-readme-positioning-document]]"
artifacts:
  # No concrete substrate — this node describes an abstract property
  # without a single artefact owner. See CLAUDE.md § Substrate traceability.
status: draft
created: 2026-05-14
updated: 2026-05-14
---

# Spec 030 — README opens with positioning + navigation guide

> Parent: [[feature-030-readme-positioning-document]] (planned, status `ready-for-implementation`).

## Stories covered

- [[story-030-A-readme-opens-with-positioning]] — AC-A1
- [[story-030-B-readme-navigation-guide]] — AC-B1

## Acceptance Criteria

- **AC-A1:** README first paragraph echoes the one-breath statement from [[vision-sem-ia]] step 4 (*"SEM-IA is AI-as-infrastructure: one homologous agent per classical SE role, vault-mediated, human-directed, making software engineering rigor available at any scale."*).
- **AC-B1:** README includes a "How to navigate" section pointing to `nodes/`, `bibliography/`, `_obsidian/templates/`, the fork-instantiation pattern, and Obsidian setup.

## Gherkin spec

```gherkin
Feature: README opens with positioning + navigation

  Scenario: AC-A1 — First paragraph carries one-breath positioning
    Given a "README.md" file exists at repo root
    When I read the first paragraph
    Then it echoes the AI-as-infrastructure one-breath statement

  Scenario: AC-B1 — Navigation guide present
    Given the README
    When I locate the "How to navigate" section
    Then it references nodes/, bibliography/, _obsidian/templates/, fork-instantiation, and Obsidian setup
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-030-readme-positioning-document]]. Cagan principle 10 via GISF slide 89.
