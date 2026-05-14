---
category: spec
id: spec-040-po-requirements-discovery-skill
parent: "[[feature-040-po-requirements-discovery-skill]]"
artifacts:
  - "[[.claude/skills/po-requirements-discovery/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 040 — Skill `po-requirements-discovery` exists and conforms

> Parent: [[feature-040-po-requirements-discovery-skill]].

## Stories covered

- [[story-040-A-baseline-jad-not-interviews]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/skills/po-requirements-discovery/SKILL.md` exists, conforms to template, anchors on Jones BP #11 (14 practices: JAD, QFD, prototypes, legacy mining, requirements inspections) + 2%/month churn empirics.

## Gherkin spec

```gherkin
Feature: Skill po-requirements-discovery
  Scenario: AC-A1 — Skill conforms and cites BP #11
    Given ".claude/skills/po-requirements-discovery/SKILL.md"
    When I open it
    Then 6 sections present, 14 practices enumerated, churn empirics cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-040-po-requirements-discovery-skill]].
