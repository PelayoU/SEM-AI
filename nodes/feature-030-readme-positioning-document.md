---
category: feature
id: feature-030-readme-positioning-document
parent: "[[cap-12-public-publication]]"
artifacts:
  # No concrete substrate — this node describes an abstract property
  # without a single artefact owner. See CLAUDE.md § Substrate traceability.
status: ready-for-implementation
created: 2026-05-14
updated: 2026-05-14
---

# Feature 030 — `README.md` opening with AI-as-infrastructure positioning

> Authored via `po-feature-decomposition`. Delivers part of [[cap-12-public-publication]].

## What it delivers (planned)

A `README.md` at repo root that opens with the AI-as-infrastructure positioning (the one-breath statement from [[vision-sem-ia]] step 4) and lays out: what SEM-IA is, how to navigate the substrate, how to read the graph, how to fork. **Currently does not exist.** Required for goal-02 (TFM + public artifact). Status: `ready-for-implementation`.

## Story Map position

- **Activity (Epic):** Publication substrate.
- **Task:** This feature (README as positioning surface).
- **Release slice:** Walking skeleton for goal-02 publication step.

## Stories (children)

- [[story-030-A-readme-opens-with-positioning]] — As an external reader landing on the GitHub page, I want the README to open with what SEM-IA is in one breath, so I know whether to keep reading.
- [[story-030-B-readme-navigation-guide]] — As an external reader past the positioning, I want a navigation guide to the substrate (how to read the graph, where the bibliography lives, how forks work), so I can explore without trial and error.

## Spec sibling

- [[spec-030-readme-positioning-document]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (spec encodes the one-breath statement + navigation guide as required content) → Construction (pending, status: ready-for-implementation) → Consequences (public-artifact surface complete; goal-02 unblocked).

## Notes

Architectural anchor: [[adr-007-obsidian-as-editor-surface]] (the README should also note Obsidian as recommended editor + the fork-and-instantiate pattern). Pending PO authoring; tracked as goal-02 deliverable.

## Source

- Skill: `po-feature-decomposition`.
- Cagan principle 10 (*"evangelize continuously"*) via GISF `gisf-discovery.pdf` slide 89.
- ADRs: [[adr-007-obsidian-as-editor-surface]].
- Substrate evidence: TBD — file not yet created. Slot reserved.
