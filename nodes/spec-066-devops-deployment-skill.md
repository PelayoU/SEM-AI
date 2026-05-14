---
category: spec
id: spec-066-devops-deployment-skill
parent: "[[feature-066-devops-deployment-skill]]"
artifacts:
  - "[[.claude/skills/devops-deployment/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 066 — Skill `devops-deployment` exists and conforms

> Parent: [[feature-066-devops-deployment-skill]].

## Stories covered

- [[story-066-A-seven-stage-pipeline]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #43 + GISF `gisf-pipeline-devops.pdf` (Humble & Farley 7-stage pipeline + 5-axis strategy framework + ERP-class baseline).

## Gherkin spec

```gherkin
Feature: Skill devops-deployment
  Scenario: AC-A1 — Skill conforms and cites pipeline model
    Given ".claude/skills/devops-deployment/SKILL.md"
    When I open it
    Then 6 sections present, 7-stage Humble & Farley pipeline described, 5-axis strategy framework documented, ERP baseline cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-066-devops-deployment-skill]].
