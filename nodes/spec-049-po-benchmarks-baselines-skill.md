---
category: spec
id: spec-049-po-benchmarks-baselines-skill
parent: "[[feature-049-po-benchmarks-baselines-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 049 — Skill `po-benchmarks-baselines` exists and conforms

> Parent: [[feature-049-po-benchmarks-baselines-skill]].

## Stories covered

- [[story-049-A-acquire-isbsg-for-class]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #31 (25-topic full + 10-topic partial; ISBSG ~5k projects; benchmark vs baseline distinction).

## Gherkin spec

```gherkin
Feature: Skill po-benchmarks-baselines
  Scenario: AC-A1 — Skill conforms and cites BP #31
    Given ".claude/skills/po-benchmarks-baselines/SKILL.md"
    When I open it
    Then 6 sections present, 25-topic + 10-topic inventories enumerated, ISBSG named, benchmark/baseline distinction explicit
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-049-po-benchmarks-baselines-skill]].
