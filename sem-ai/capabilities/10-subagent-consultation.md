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

# Capability 10 — Cross-role consultation as information transfer (not authority transfer)

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **let a role get input from another role's expertise without dissolving its own scope authority** (parent goal [[goal-01-self-bootstrap-validation]] — the bootstrap surfaced exactly when consultation is and is not needed — also serves [[goal-03-portability-proof]]),
as **anyone running a software engineering effort under SEM-IA, in any role**,
I want **the ability to invoke another role-agent for specialist input synchronously while retaining final authority over the artifact being authored — and to have the consultation logged so the trail survives the conversation**.

## Implementation-agnostic test

- **Implementation A** (current): `Task` tool with `subagent_type` parameter dispatches a sibling agent; the calling agent retains the conversation and writes the artifact; consultation logged in the session doc under `## Subagent consultations`.
- **Implementation B** (alternative): the human relays a question to a parallel conversation with the other role-agent and brings the answer back; less automated, same logical capability.

A third plausible: structured API call to a domain-expert microservice that returns advice without claiming any write authority. The capability is *cross-role information transfer with explicit scope-preservation*, not the dispatch mechanism.

## MVP Go / No-go

- **Value risk:** Without this capability, cross-role information transfer either forces full handoff (heavy) or silent contamination (dangerous — as observed earlier in this bootstrap when reading other roles' skills bled their framing into PO reasoning). Pillar 2 of the Layer B operating triangle depends on it.
- **Usability risk:** Moderate — the calling role must know *when* to invoke and *when not to*; the deferred *consultation matrix* improvement candidate proposes codifying this.
- **Viability risk:** Proven — `Task` tool supports this pattern; agent `description` fields drive dispatch.
- **Business viability risk:** N/A.

**Decision: Go** — essential for clean cross-role work without scope blur.

## Non-overlap with sibling capabilities

- Sibling: [[cap-02-role-scoped-agents]] — adjacent. Role scoping is the *property* (boundaries exist); this capability is one *mechanism* to cross boundaries safely.
- Sibling: [[cap-09-session-continuity]] — adjacent. Sessions are *the thread*; consultations are *events logged within the thread*.

## Non-coverage

- **Not about authority transfer.** Full role handoff (the other role taking the wheel) is a different mechanism — closing the conversation and opening a new one with a different agent on the same branch. The capability is explicitly *consultation*, not *handoff*.
- **Not about consultation triggers.** *When* to invoke is a workflow question. The framework currently relies on agent judgment + the human's veto; the deferred *consultation matrix* improvement candidate proposes codifying this.
- **Not about agent-to-agent communication without a human.** The pattern is always *invoked by a role for that role's benefit*, with the human in the loop.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- CLAUDE.md Layer B § *Subagent dispatch ≠ authority transfer*.
- Features delivering this capability: `Task` tool integration, agent `description` fields that drive dispatch triggers, CLAUDE.md operating principle on scope authority preservation.
