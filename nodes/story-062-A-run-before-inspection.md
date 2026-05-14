---
category: story
id: story-062-A-run-before-inspection
parent: "[[feature-062-developer-static-analysis-skill]]"
artifacts:
  - "[[.claude/skills/developer-static-analysis/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 062-A — Run static analysis before code inspection

> Parent: [[feature-062-developer-static-analysis-skill]].

As a **Developer preparing code for inspection**, I want **static analysis run (and findings triaged) before the inspection session**, so that **inspectors target deeper logic rather than re-finding structural defects the tool already catches**.

## Conditions of Satisfaction

- Static analysis runs as part of pre-inspection package.
- Findings: each is fix / suppress-with-reason / open-issue.
- False positives tuned, not silenced wholesale.

## INVEST self-check

✅ I · ✅ N · ✅ V · ✅ E · ✅ S · ✅ T (skill prescribes; inspection workflow enforces).

## Source

GISF slides 124, 128, 125. Parent: [[feature-062-developer-static-analysis-skill]].
