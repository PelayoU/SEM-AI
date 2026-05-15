---
category: spec
id: spec-076-per-turn-role-reinforcement
parent: "[[feature-076-per-turn-role-reinforcement]]"
artifacts:
  - "[[.claude/hooks/role-reinforce.sh]]"
  - "[[.claude/settings.json]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Spec 076 — Per-turn role reinforcement

> Authored via `po-spec-gherkin`. One Feature per spec.

## Stories covered

- `[[story-076-A-active-role-injected-each-turn]]` — AC-A1
- `[[story-076-B-no-role-injects-run-role-prompt]]` — AC-B1

## Acceptance Criteria

- **AC-A1:** On a prompt with `.claude/.active-role` set, the `UserPromptSubmit` hook injects context containing the active role + its jurisdiction + the decision-verification checklist; ~4–6 lines; never blocks.
- **AC-B1:** With the marker absent, the injection is the "no active role — run `/role`" message; never blocks.

## Gherkin spec

```gherkin
Feature: Per-turn role reinforcement

  In order to make the guardrail non-forgettable at the moment of a "do it"
  As the SEM-IA framework
  I want active role + checklist re-injected every turn

  Scenario: AC-A1 — role injected
    Given .claude/.active-role is "architect"
    When the human submits any prompt
    Then injected context names role, jurisdiction and the verification checklist
    And the prompt is not blocked

  Scenario: AC-B1 — no role message
    Given .claude/.active-role is absent
    When the human submits any prompt
    Then injected context says to run /role and that substrate is hard-blocked
    And the prompt is not blocked
```

## Notes

**Realized (Phase E, 2026-05-15):** AC-A1 ✅ with `.active-role` set, injection contains role + jurisdiction + the verification checklist; never blocks. AC-B1 ✅ with no marker, injection is the run-`/role` message; never blocks.

## Source

- Skill: `po-spec-gherkin`. Cucumber `gherkin-reference.pdf` pp. 1–9; GISF `gisf-life-cycle.pdf` slide 54.
