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

# Capability 02 — Role-scoped AI agents with explicit custody

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **engage AI specialists per classical SE role without role-bleed** (parent goal [[goal-01-self-bootstrap-validation]] — the 5-role-authorship M-criterion materialises this — also serves [[goal-03-portability-proof]]),
as **anyone running a software engineering effort under SEM-IA**,
I want **the ability to invoke an AI agent for a specific role (PO, Architect, QA, Developer, DevOps; Security and Designer planned), each with its own bounded scope, custody, bibliography, and skill catalog — and not have any agent appropriate another role's territory**.

## Implementation-agnostic test

- **Implementation A** (current): `.claude/agents/<role>.md` identity files loaded by the harness via `--agent <role>` flag or `Task` subagent dispatch; meta-template `.claude/templates/agent.md.template` for new roles.
- **Implementation B** (alternative): separate LLM-instance-per-role with role-specific system prompts and tool restrictions; orchestration router.

A third plausible: prompt-engineering layer over a single LLM that switches persona+ruleset by session context. The capability is *role scoping as a property of the AI layer*, not the dispatch mechanism.

## MVP Go / No-go

- **Value risk:** Without this capability, *"AI as infrastructure"* collapses to *"AI as undifferentiated assistant"* and the central paradigm of the vision fails.
- **Usability risk:** Moderate — humans must know which role they engage at any moment.
- **Viability risk:** Proven — 5 implemented (PO, Architect, QA, Developer, DevOps); 2 planned (Security, Designer).
- **Business viability risk:** N/A.

**Decision: Go** — foundational to the paradigm.

## Non-overlap with sibling capabilities

- Sibling: [[cap-01-vision-to-code-audit]] — independent. Roles author artifacts; this capability is about role boundary; cap-01 is about traversal.
- Sibling: [[cap-10-subagent-consultation]] — adjacent. Role scoping is the *property*; subagent consultation is one *mechanism* to cross boundaries safely.
- Sibling: [[cap-03-apply-po-discipline]] through [[cap-07-apply-devops-discipline]] — adjacent. Role-scope (this cap) is the *property of bounded territory*; the apply-X-discipline capabilities are *what each role enables*.

## Non-coverage

- **Not about agent runtime / harness.** Claude Code vs Cursor vs custom is implementation.
- **Not about role count.** 5+2 today; the capability is *that roles are scoped*, not *which exist*.
- **Not about role authority.** Who signs a release is governance.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- Cross-link to vision: [[vision-sem-ia]] Statement *"reformulated as a substrate of homologous AI agents"*.
- Features delivering this capability: 5 agent files, `.claude/templates/agent.md.template`, `.claude/sem-role-catalog.md`, CLAUDE.md role section, `.claude/settings.json`.
