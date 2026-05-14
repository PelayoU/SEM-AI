---
category: story
id: story-065-A-all-deliverables-under-cm
parent: "[[feature-065-devops-configuration-control-skill]]"
artifacts:
  - "[[.claude/skills/devops-configuration-control/SKILL.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 065-A — Every deliverable under configuration control, not just code

> Parent: [[feature-065-devops-configuration-control-skill]].

As **DevOps setting up CM**, I want **every deliverable class under control (requirements, specs, code, tests, user docs)**, so that **cross-deliverable consistency survives changes** rather than drifting silently.

## Conditions of Satisfaction

- Unique IDs across all deliverable classes.
- Cross-deliverable mapping maintained when a CR affects more than one.

## INVEST self-check

✅ I · ✅ N · ✅ V · ✅ E · ✅ S · ✅ T (skill prescribes; CM tooling enforces).

## Source

GISF slides 124, 128, 125. Parent: [[feature-065-devops-configuration-control-skill]].
