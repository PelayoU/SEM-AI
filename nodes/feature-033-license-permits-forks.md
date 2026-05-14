---
category: feature
id: feature-033-license-permits-forks
parent: "[[cap-13-portability]]"
artifacts:
  - "[[LICENSE]]"
status: ready-for-implementation
created: 2026-05-14
updated: 2026-05-14
---

# Feature 033 — `LICENSE` permits forks (legal precondition for portability)

> Authored via `po-feature-decomposition`. Delivers part of [[cap-13-portability]].

## What it delivers (pending license choice)

The `LICENSE` at repo root must permit forks, derivative works, and use in commercial / academic projects. Without a permissive license, [[cap-13-portability]] is structurally legal-blocked even if the directory separation is clean. Currently `LICENSE` is a placeholder; the operationalising license choice is pending PO decision. Status: `ready-for-implementation`.

## Story Map position

- **Activity (Epic):** Portability substrate.
- **Task:** This feature (license terms permit forking).
- **Release slice:** Walking skeleton for goal-03.

## Stories (children)

- [[story-033-A-license-permits-fork]] — As a new-project author or external fork author, I want the LICENSE to explicitly permit copying the substrate to a new project, so portability is legally clean.

## Spec sibling

- [[spec-033-license-permits-forks]]

## 5 Cs cycle reminder

Card → Conversation (license choice — Apache 2.0, MIT, CC-BY-SA for the substrate? PO decides; Architect flagged the gap) → Confirmation (license terms include "may be used in derivative works") → Construction (pending) → Consequences (portability legally enabled).

## Notes

Companion to [[feature-029-license-file]] (the file exists; this is about the *terms*). Architect's Phase 1 concern 5 directly addresses this: when PO picks a license, capture the choice as an ADR.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: pending — license choice is a future ADR per Architect's Phase 1 concern.
- Substrate evidence: `LICENSE` (placeholder).
- Convention pointer: SPDX license identifiers, OSI-approved licenses.
