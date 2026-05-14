---
category: spec
id: spec-043-po-spec-gherkin-skill
parent: "[[feature-043-po-spec-gherkin-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 043 — Skill `po-spec-gherkin` exists and conforms

> Parent: [[feature-043-po-spec-gherkin-skill]].

## Stories covered

- [[story-043-A-author-gherkin-per-feature]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, encodes Cucumber Gherkin reference + one-Feature-per-file rule + story-to-AC traceability + 3–5-steps-per-Scenario rule.

## Gherkin spec

```gherkin
Feature: Skill po-spec-gherkin
  Scenario: AC-A1 — Skill conforms and cites Cucumber
    Given ".claude/skills/po-spec-gherkin/SKILL.md"
    When I open it
    Then 6 sections present, Gherkin keywords documented, one-Feature-per-file rule cited, AC-letter traceability convention described
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-043-po-spec-gherkin-skill]].
