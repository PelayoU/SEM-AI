---
type: capability
parent: goal-01-self-bootstrap-validation
status: draft
created: 2026-05-14
updated: 2026-05-22
maintained_by_role: product-manager
labels:
  - mvp:go
---

# Capability 09 — Work-thread continuity via sessions

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **make threads of work survive interruption, role-switch, and contributor change without context loss** (parent goal [[goal-01-self-bootstrap-validation]] — the current bootstrap is exercising this capability now — also serves [[goal-03-portability-proof]]),
as **anyone running a software engineering effort under SEM-IA, whether solo or multi-contributor**,
I want **the ability to open, suspend, resume, and close a unit of work as a first-class artifact that carries the full context (what was decided, what was touched, who contributed) — so the cost of *"let me catch you up"* approaches zero**.

## Implementation-agnostic test

- **Implementation A** (current): session = git branch (`session/<id>`) + session document (`sessions/<id>.md`) with Context / Log / Artifacts touched / Subagent consultations / Closing summary sections; bootstrap is conversational at session start; three slash commands (`session-log`, `session-context`, `session-close`) cover the ceremony moments.
- **Implementation B** (alternative): session = database row with structured state JSON, opened/resumed by ID; transcript stored in object storage; agent reads session metadata at start.

A third plausible: session = a long-running LLM context window with externalised checkpoints persisted at each turn. The capability is *work-thread state preservation across discontinuity*, not the storage mechanism.

## MVP Go / No-go

- **Value risk:** Without this capability, every conversation starts cold and cross-role handoff degrades to *"read everything to catch up"*. Pillar 3 of the operating triangle in Layer B depends on it.
- **Usability risk:** Moderate — the human must understand the open-session bootstrap and the close ritual; the session bootstrap procedure (CLAUDE.md Layer B) is conversational and self-documenting.
- **Viability risk:** Proven — this very session is exercising the capability.
- **Business viability risk:** N/A.

**Decision: Go** — operationally critical for any multi-step project.

## Non-overlap with sibling capabilities

- Sibling: [[cap-10-subagent-consultation]] — adjacent. Sessions are *the persistent thread*; subagent consultation is *one event within a thread*.
- Sibling: [[cap-01-vision-to-code-audit]] — independent. Sessions track *how work happened over time*; audit-by-navigation follows *what was produced*.

## Non-coverage

- **Not about session UX.** Slash commands, status line, tool surface are implementation.
- **Not about session size limits.** Token budget, context window management are implementation properties.
- **Not about session-as-meeting.** Sessions are work-threads, not synchronous human meetings.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- CLAUDE.md Layer B § *Sessions = git branch*: *"Branch state is session state."*
- Features delivering this capability: 3 slash commands (`.claude/commands/session-log.md`, `session-context.md`, `session-close.md`); `_obsidian/templates/session.md`; CLAUDE.md Layer B section; git as the branch substrate.
- Cross-link to the operating triangle, pillar 3 *"Sessions as shared context"*.
