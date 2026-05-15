---
category: spec
id: spec-073-claude-md-orientation-and-governance
parent: "[[feature-073-claude-md-orientation-and-governance]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Spec 073 — CLAUDE.md orientation + governance

> Authored via `po-spec-gherkin`. One Feature per spec.

## Stories covered

- `[[story-073-A-fresh-session-orientation]]` — AC-A1
- `[[story-073-B-role-jurisdiction-table]]` — AC-B1
- `[[story-073-C-decision-verification-principle]]` — AC-C1

## Acceptance Criteria

- **AC-A1:** `## Orient here before anything else` is the first `##` after the universal-contract paragraph; it states the substrate set + that editing it changes SEM-IA + that `nodes/`/`sessions/` are traceability + that substrate is hard-gated.
- **AC-B1:** A `## Role jurisdiction` table with all 5 roles and columns Role/Owns/Must-NOT-author/Escalation is present and content-consistent with `.claude/role-scope.json`.
- **AC-C1:** `## Operating principles` contains the decision-verification principle (two checks; bare "do it" not a bypass; node-before-artifact hard, names the hook) and the graph-vs-substrate principle.

## Gherkin spec

```gherkin
Feature: CLAUDE.md orientation and governance contract

  In order to make the contract self-sufficient and enforced at read time
  As the SEM-IA universal contract
  I want orientation, jurisdiction and verification stated up front

  Scenario: AC-A1 — orient block first
    Given a reader opens CLAUDE.md
    When they read past the universal-contract paragraph
    Then the next "##" is the Orient block defining substrate vs traceability

  Scenario: AC-B1 — jurisdiction table
    Given CLAUDE.md near the Roles section
    Then a Role-jurisdiction table lists all 5 roles
    And its content matches .claude/role-scope.json

  Scenario: AC-C1 — decision-verification principle
    Given the Operating principles section
    Then it contains the two-check verification principle
    And it states node-before-artifact is hard-enforced and not overridable
```

## Notes

Realized-AC verbatim filled during Phase E (the §5 edits go through the live gate — live proof of AC).

## Source

- Skill: `po-spec-gherkin`. Cucumber `gherkin-reference.pdf` pp. 1–9; GISF `gisf-life-cycle.pdf` slide 54.
