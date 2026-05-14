---
category: spec
id: spec-046-po-cost-estimating-skill
parent: "[[feature-046-po-cost-estimating-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 046 — Skill `po-cost-estimating` exists and conforms

> Parent: [[feature-046-po-cost-estimating-skill]].

## Stories covered

- [[story-046-A-automated-tools-above-10kfp]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #16 (automated mandatory above 10k FP; COCOMO/SEER/SLIM/etc.) + critical-topic Ch 1 p. 19.

## Gherkin spec

```gherkin
Feature: Skill po-cost-estimating
  Scenario: AC-A1 — Skill conforms and cites BP #16
    Given ".claude/skills/po-cost-estimating/SKILL.md"
    When I open it
    Then 6 sections present, automated-mandatory-above-10kFP rule cited, COCOMO/SEER/SLIM named
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-046-po-cost-estimating-skill]].
