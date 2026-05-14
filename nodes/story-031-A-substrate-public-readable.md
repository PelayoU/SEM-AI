---
category: story
id: story-031-A-substrate-public-readable
parent: "[[feature-031-public-git-hosting-convention]]"
artifacts:
  # No concrete substrate — this node describes an abstract property
  # without a single artefact owner. See CLAUDE.md § Substrate traceability.
status: ready-for-implementation
created: 2026-05-14
updated: 2026-05-14
---

# Story 031-A — Substrate readable at a public URL

> Parent: [[feature-031-public-git-hosting-convention]].

## Cohn statement

As an **external reader anywhere with internet access**, I want **the substrate readable at a public URL without authentication**, so that **SEM-IA is reachable as infrastructure rather than as private property**.

## Conditions of Satisfaction

- Repository pushed to public host (GitHub or equivalent).
- Default branch readable without auth.

## INVEST self-check

✅ I · ✅ N · ✅ V (operationalises Cagan principle 10) · ✅ E · ✅ S · ✅ T (curl public URL; observe substrate visible).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-031-public-git-hosting-convention]].
- Cagan principle 10 via GISF `gisf-discovery.pdf` slide 89.
