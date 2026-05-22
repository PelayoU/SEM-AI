---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-22
updated: 2026-05-22
maintained_by_role: architect
supersedes:
  - adr-005-subagent-dispatch-not-authority-transfer
---

# ADR 018 — Symmetric role primacy (no orchestrator)

## Context & forces

A mid-v0.1 commit (`d4bc229` "Orchestrator pattern") introduced a PM-as-orchestrator model that contradicted the vision's homologous-roles claim. In that model PM was always primary; other roles were author-dispatched subagents that returned to PM. Architect / Developer / QA / DevOps / Security Officer became second-class — never "the active role", always "subagents returning".

The vision says: each SEM dimension (scope / architecture / code / quality / operations / security) has an AI agent **homologous** to a human practitioner. Homologous means: same primacy in its dimension. Not "always serving PM".

Forces:

- The orchestrator model collapses long architectural sessions onto PM's context.
- It biases agent.md against deep specialised work (the spec implies you defer to PM).
- It conflates two distinct cross-role mechanics: *information consultation* (one role helps another for 1-3 turns) and *sustained work* (4+ turns in a dimension means the human should switch surface).

## Decision

**Symmetric primacy.** Each role is primary in its dimension; PM is default-opener when the dimension is unclear; cross-role coordination via:

- **consult** — dispatch the role as a subagent for *information only*; you stay primary, never take its authorship.
- **hand off** (a.k.a. **surface-switch**) — sustained work (4+ turns) belongs to another role; the human surface-switches via `claude --agent <other>`; you stop; you do not silently do the other role's work.

Each `.claude/agents/<role>.md` declares the explicit *Interaction with other roles* table — directional triggers naming when to consult vs hand off, peer-to-peer rather than always-via-PM.

## Overall structure

6 role-homologous agents. No "primary orchestrator" role exists. The active role is whichever the human picked with `claude --agent <role>`.

## Data structure

The `maintained_by_role` frontmatter field surfaces which role wrote each node (`vision`/`goal`/`capability`/`feature`/`story`/`spec`/`release` → product-manager; `adr` → architect; `measurement` → qa; `inspection` → qa; `defect` → qa or developer; security sections → security-officer). A category error (e.g., a `goal` `maintained_by 'developer'`) is mechanically visible.

## Interfaces to the outside world

`claude --agent <role>` selects the active role. Dispatch happens through the Task tool inside Claude Code; the dispatched role reads its own `.claude/agents/<role>.md` + the `framework` skill.

## Decomposition into functional components

6 agent.md files, each absorbing its role's generic discipline (Day 1.9). Each agent.md ends with the *Interaction with other roles* table — the operative layer.

## Linkage / information transmission

Consult returns data only; the active role integrates and writes. Hand-off transfers authorship; the prior role stops.

## Performance attributes

Consultation is 1-3 turns by definition; longer than that the cost of context-passing exceeds the cost of surface-switching, and the human should switch role.

## Security attributes

Dispatched to Security Officer.

- Security Officer holds **release-stop authority on security grounds** in parallel to QA's quality-grounds veto (modern hybrid governance).
- Independence is structural: Security Officer reports outside the development chain — analogous to QA's independence pattern.
- Security Officer owns *no node type exclusively* — contributes sections (Security AC in spec; Security gate in release; Security attributes Topic 7 in ADR) into nodes owned by other roles. This is intentional: section-contribution preserves audit trail (the section's `maintained_by_role` could be recorded; the parent node's authorship stays with its owning role).

## Style: chosen + rejected

- **Chosen**: symmetric primacy with directional Interaction tables per role.
- **Rejected**: PM-as-orchestrator (the d4bc229 model). Collapses contexts, biases against specialised sessions.
- **Rejected**: free-form role mixing (no consult / hand-off discipline). Becomes "any agent does anything", category errors invisible.
- **Rejected**: pure peer-to-peer with no default-opener. Friction at session start when the user's request straddles dimensions; PM-as-default-opener resolves the cold-start.

## Consequences

- An Architect-led session is a first-class workflow, not a degradation of a PM session.
- Cross-role consult is bounded (1-3 turns); sustained cross-role work surface-switches → less context contamination.
- The agent.md set is the operative source of truth; the jurisdiction matrix in `instance/jurisdiction.yaml` is the derived map.
- Loss: cold-start friction for users who don't know which role to pick. Mitigation: PM is the documented default-opener (per CLAUDE.md), and the SessionStart hook injects the project map across every role identically.

## Design inspection

Negative test on the verification gate (Day 3.8): PM tries to author a measurement; the engine's jurisdiction matrix hard-rejects. Proves the symmetric primacy is mechanically enforced, not just aspirational.
