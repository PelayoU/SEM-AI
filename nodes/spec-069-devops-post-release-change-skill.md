---
category: spec
id: spec-069-devops-post-release-change-skill
parent: "[[feature-069-devops-post-release-change-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 069 — Skill `devops-post-release-change` exists and conforms

> Parent: [[feature-069-devops-post-release-change-skill]].

## Stories covered

- [[story-069-A-post-release-same-rigor]] — AC-A1

## Acceptance Criteria

- **AC-A1:** Skill file exists, conforms to template, anchors on Jones BP #47 (10-tool renovation inventory + spec-staleness empirics + same-rigor-as-pre-release rule).

## Gherkin spec

```gherkin
Feature: Skill devops-post-release-change
  Scenario: AC-A1 — Skill conforms and cites BP #47
    Given ".claude/skills/devops-post-release-change/SKILL.md"
    When I open it
    Then 6 sections present, 10-tool inventory enumerated, ~5 year spec-staleness empiric cited, same-rigor-as-pre-release rule stated
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-069-devops-post-release-change-skill]].
