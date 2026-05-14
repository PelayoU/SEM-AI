---
category: spec
id: spec-068-devops-customer-support-skill
parent: "[[feature-068-devops-customer-support-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 068 — Skill `devops-customer-support` exists and conforms

> Parent: [[feature-068-devops-customer-support-skill]].

## Stories covered

- [[story-068-A-quality-as-support-lever]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #45 (1/10kFP + 1/150 customers staffing; 220-defect ≈ 1 FTE multiplier; L0/L1/L2/L3 tiering).

## Gherkin spec

```gherkin
Feature: Skill devops-customer-support
  Scenario: AC-A1 — Skill conforms and cites BP #45
    Given ".claude/skills/devops-customer-support/SKILL.md"
    When I open it
    Then 6 sections present, both staffing ratios cited, 220-defect multiplier present, L0/L1/L2/L3 tiering described
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-068-devops-customer-support-skill]].
