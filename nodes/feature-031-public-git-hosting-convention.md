---
category: feature
id: feature-031-public-git-hosting-convention
parent: "[[cap-12-public-publication]]"
status: ready-for-implementation
created: 2026-05-14
updated: 2026-05-14
---

# Feature 031 — Public git hosting convention (GitHub / equivalent)

> Authored via `po-feature-decomposition`. Delivers part of [[cap-12-public-publication]].

## What it delivers (planned)

The substrate is published on a public git host (GitHub or equivalent) with the default branch readable without authentication. This is the operational surface of [[cap-12-public-publication]] — without it, the LICENSE and README are private artifacts. **Currently the repo is local.** Publication is a goal-02 deliverable; status: `ready-for-implementation`.

## Story Map position

- **Activity (Epic):** Publication substrate.
- **Task:** This feature (public hosting).
- **Release slice:** Walking skeleton for goal-02 publication step.

## Stories (children)

- [[story-031-A-substrate-public-readable]] — As an external reader anywhere with internet, I want the substrate readable at a public URL without auth, so SEM-IA is reachable as infrastructure rather than as private property.

## Spec sibling

- [[spec-031-public-git-hosting-convention]]

## 5 Cs cycle reminder

Card → Conversation (host choice: GitHub / GitLab / Codeberg) → Confirmation (substrate visible at public URL; LICENSE renders; README renders) → Construction (pending push to public host) → Consequences (goal-02 deliverable satisfied).

## Notes

Out-of-bibliography: specific host vendor (GitHub etc.) is convention pointer, not Jones-anchored authority. Publication channel is implementation per [[cap-12-public-publication]]'s implementation-agnostic test.

## Source

- Skill: `po-feature-decomposition`.
- Cagan principle 10 (*"evangelize continuously"*) via GISF `gisf-discovery.pdf` slide 89.
- Substrate evidence: TBD — repository not yet published. Slot reserved as part of goal-02 deliverable.
