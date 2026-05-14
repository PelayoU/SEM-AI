---
category: spec
id: spec-054-architect-performance-analysis-skill
parent: "[[feature-054-architect-performance-analysis-skill]]"
artifacts:
  - "[[.claude/skills/architect-performance-analysis/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 054 — Skill `architect-performance-analysis` exists and conforms

> Parent: [[feature-054-architect-performance-analysis-skill]].

## Stories covered

- [[story-054-A-perf-as-architecture-not-tuning]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #39 (profilers + instrumentation + perf↔quality↔security overlap + heisenbug/bohrbug/mandelbug/schrodenbug taxonomy + 100k FP specialist threshold).

## Gherkin spec

```gherkin
Feature: Skill architect-performance-analysis
  Scenario: AC-A1 — Skill conforms and cites BP #39
    Given ".claude/skills/architect-performance-analysis/SKILL.md"
    When I open it
    Then 6 sections present, bug taxonomy enumerated, perf↔quality↔security overlap principle stated, 100k FP specialist threshold cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-054-architect-performance-analysis-skill]].
