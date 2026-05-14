---
category: feature
id: feature-023-task-tool-integration
parent: "[[cap-10-subagent-consultation]]"
artifacts:
  # No concrete substrate — this node describes an abstract property
  # without a single artefact owner. See CLAUDE.md § Substrate traceability.
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 023 — Task tool integration for subagent dispatch

> Authored via `po-feature-decomposition`. Delivers part of [[cap-10-subagent-consultation]].

## What it calls delivers

Claude Code's `Task` tool with the `subagent_type` parameter enables a calling agent to dispatch a sibling agent (PO → Architect, etc.) inline. The dispatched agent runs in its own context with its own identity, returns a structured response, and the calling agent retains conversation authority. Used in this very session for Phase 1 ADRs (PO → Architect dispatch).

## Story Map position

- **Activity (Epic):** Cross-role consultation substrate.
- **Task:** This feature (Task tool).
- **Release slice:** Walking skeleton.

## Stories (children)

- [[story-023-A-dispatch-by-subagent-type]] — As a calling agent, I want to dispatch a specific role-agent by name via `subagent_type`, so the right specialist is engaged without ambiguity.

## Spec sibling

- [[spec-023-task-tool-integration]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (Phase 1 of this session is the live demo) → Construction (Claude Code substrate; vendor-provided) → Consequences (cross-role expertise reachable in-conversation).

## Notes

Architectural anchor: [[adr-005-subagent-dispatch-not-authority-transfer]]. Task is a tier-2 dependency (Claude Code vendor); the substrate documents the *behaviour expected* of any equivalent dispatch mechanism per the ADR (information transfer, not authority transfer).

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-005-subagent-dispatch-not-authority-transfer]].
- Substrate evidence: Task tool available in Claude Code harness; demonstrated in Phase 1 PO→Architect dispatch.
- Out-of-bibliography: Claude Code (Anthropic vendor) — convention pointer.
