---
category: story
id: story-066-A-seven-stage-pipeline
parent: "[[feature-066-devops-deployment-skill]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 066-A — Every change traverses 7 pipeline stages explicitly

> Parent: [[feature-066-devops-deployment-skill]].

As **DevOps designing CI/CD**, I want **every change to traverse the Humble & Farley 7 stages explicitly (Develop → Confirm → Build → Test → Provide → Deploy → Release)**, so that **deployment defects are caught at the right phase rather than reaching production**.

## Conditions of Satisfaction

- Pipeline definition shows all 7 stages.
- Gates pass/fail at each stage; no stage silently skipped.

## INVEST self-check

✅ I · ✅ N · ✅ V · ✅ E · ✅ S · ✅ T (skill prescribes; pipeline run verifies).

## Source

GISF slides 124, 128, 125. Parent: [[feature-066-devops-deployment-skill]].
