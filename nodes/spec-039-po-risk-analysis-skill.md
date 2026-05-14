---
category: spec
id: spec-039-po-risk-analysis-skill
parent: "[[feature-039-po-risk-analysis-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 039 — Skill `po-risk-analysis` exists and conforms

> Parent: [[feature-039-po-risk-analysis-skill]].

## Stories covered

- [[story-039-A-sweep-fourteen-categories]] — AC-A1

## Acceptance Criteria

- **AC-A1:** `.claude/skills/po-risk-analysis/SKILL.md` exists, conforms to template, anchors on Jones BP #17 (14 categories + size escalation 1k/10k/100k FP) + Cagan 4 risks.

## Gherkin spec

```gherkin
Feature: Skill po-risk-analysis
  Scenario: AC-A1 — Skill conforms and cites BP #17
    Given ".claude/skills/po-risk-analysis/SKILL.md"
    When I open it
    Then 6 sections present, 14 risk categories enumerated, size-tier escalation rules cited
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-039-po-risk-analysis-skill]].
