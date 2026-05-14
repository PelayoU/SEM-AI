---
category: spec
id: spec-<NNN>-<slug>
parent: "[[feature-NNN-slug]]"
artifacts:
  # Optional. List of substrate paths this spec verifies (the Gherkin `Given` clauses typically reference the same path).
  # Omit when the spec covers an abstract property without a single artefact owner.
  # See CLAUDE.md § Substrate traceability for the rule.
  # - "[[.claude/skills/<role>-<name>/SKILL.md]]"
status: draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# Spec <NNN> — <feature title>

> Authored via `po-spec-gherkin`. **One Feature per spec file** (Cucumber convention: *"You can only have a single Feature in a `.feature` file."* — `gherkin-reference.pdf` p. 1). The Gherkin block aggregates Scenarios for the acceptance criteria of every child story under the parent feature; AC numbering carries the story letter for traceability (`story-NNN-A` → `AC-A1`, `AC-A2`, …).

## Stories covered

> Each child story contributes one or more numbered AC. Without an AC, the story has no contract.

- `[[story-NNN-A-slug]]` — AC-A1, AC-A2, AC-A3
- `[[story-NNN-B-slug]]` — AC-B1, AC-B2
- `[[story-NNN-C-slug]]` — AC-C1

## Acceptance Criteria (human form, GISF `gisf-life-cycle.pdf` slide 54: *"Examples form the basis for the Acceptance criteria of a feature"*)

> One short human sentence per AC. The Gherkin Scenarios below realise each AC.

- **AC-A1:** <one sentence>
- **AC-A2:** <one sentence>
- **AC-B1:** <one sentence>
- …

## Gherkin spec (Cucumber, `gherkin-reference.pdf` pp. 1–9)

```gherkin
Feature: <feature title>

  In order to <benefit>
  As a <role>
  I want <capability>

  # Optional: Background runs before every Scenario.
  # Use only when every Scenario actually needs it.
  Background:
    Given <shared precondition>

  # Scenarios for story-NNN-A: <short story-A title>
  Scenario: AC-A1 — <short AC title>
    Given <context>
    When <action>
    Then <observable outcome>
    And <additional observable assertion>

  Scenario: AC-A2 — <short AC title>
    Given …
    When …
    Then …

  # Scenarios for story-NNN-B: <short story-B title>
  Scenario: AC-B1 — <short AC title>
    Given …
    When …
    Then …
```

### Gherkin reminders (Cucumber reference)

- 3–5 steps per Scenario; longer scenarios test too many things and become fragile.
- `Then` names what is observable (state, output, side effect). Implementation language in `Then` is the most common defect.
- `Scenario Outline` + `Examples` for table-driven cases instead of duplicating Scenarios.
- Secondary keywords: `"""` Doc Strings · `|` Data Tables · `@` Tags · `#` Comments.
- Worked illustrative example: GISF UC3M `gisf-delivery-backlog-management.pdf` slide 126 (*"Transferring money between accounts"*).

## Notes

> Decisions taken while writing the spec, edge cases discussed, ACs intentionally deferred with rationale.

## Source

- Skill: `po-spec-gherkin`.
- Cucumber Gherkin reference: `gherkin-reference.pdf` pp. 1–9 (Feature, Rule, Example/Scenario, Given/When/Then/And/But, Background, Scenario Outline + Examples, Doc Strings, Data Tables, Tags, Comments, localised languages, one Feature per file).
- *Examples → AC*: GISF UC3M `gisf-life-cycle.pdf` slide 54.
- Worked Gherkin example: GISF UC3M `gisf-delivery-backlog-management.pdf` slide 126.
- "Agree on what test confirms done before you build": GISF UC3M `agile-story-essentials.pdf` p. 1.
- Specification by Example as a class of practice: Gojko Adzic, *Specification by Example* (Manning, 2011) — book not in audited `bibliography/sources/`; concept captured via GISF + Cucumber reference above.
