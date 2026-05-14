---
category: story
id: story-063-A-test-cases-inspected-too
parent: "[[feature-063-developer-unit-testing-skill]]"
artifacts:
  - "[[.claude/skills/developer-unit-testing/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 063-A — Test cases inspected before execution

> Parent: [[feature-063-developer-unit-testing-skill]].

As a **Developer authoring tests**, I want **test cases inspected before execution (Table 9-22 #8: 83 % DRE on test-case inspection)**, so that **test-case defects don't propagate** (IBM samples show some test libraries with higher error density than the code under test).

## Conditions of Satisfaction

- Test-case inspection scheduled as part of test-library hygiene.
- Defects found in test cases logged and fixed before runs.

## INVEST self-check

✅ I · ✅ N · ✅ V · ✅ E · ✅ S · ✅ T (skill prescribes; test-library hygiene enforces).

## Source

GISF slides 124, 128, 125. Parent: [[feature-063-developer-unit-testing-skill]].
