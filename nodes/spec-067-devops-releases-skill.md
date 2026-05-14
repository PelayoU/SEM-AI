---
category: spec
id: spec-067-devops-releases-skill
parent: "[[feature-067-devops-releases-skill]]"
artifacts:
  - "[[.claude/skills/devops-releases/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 067 — Skill `devops-releases` exists and conforms

> Parent: [[feature-067-devops-releases-skill]].

## Stories covered

- [[story-067-A-no-named-anti-patterns]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #49 (16 anti-patterns + 11 theoretical-but-correct practices) + release cadence options.

## Gherkin spec

```gherkin
Feature: Skill devops-releases
  Scenario: AC-A1 — Skill conforms and cites BP #49
    Given ".claude/skills/devops-releases/SKILL.md"
    When I open it
    Then 6 sections present, 16 anti-patterns enumerated, 11 best practices listed, SLA thresholds (e-mail 48h, phone 5 min) cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-067-devops-releases-skill]].
