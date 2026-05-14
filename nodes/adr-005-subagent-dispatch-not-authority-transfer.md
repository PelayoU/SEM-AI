---
category: adr
id: adr-005-subagent-dispatch-not-authority-transfer
parent: "[[cap-10-subagent-consultation]]"
artifacts:
  - "[[CLAUDE.md]]"
  - "[[.claude/agents/product-owner.md]]"
  - "[[.claude/agents/architect.md]]"
  - "[[.claude/agents/qa.md]]"
  - "[[.claude/agents/developer.md]]"
  - "[[.claude/agents/devops.md]]"
status: accepted
created: 2026-05-14
updated: 2026-05-14
supersedes:
superseded-by:
---

# ADR 005 — Subagent dispatch is information transfer, not authority transfer; the calling role retains scope

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — operating across every subagent dispatch in the framework. CLAUDE.md Layer B § *Subagent dispatch ≠ authority transfer* declares the rule; the session document's `## Subagent consultations` section logs the trail; pillar 2 of the operating triangle (*scope discipline*) depends on this property.

## Context

Three forces converge on the question of *how a role gets input from another role's expertise*:

1. **Role scope is a hard boundary.** [[cap-02-role-scoped-agents]] declares that each agent has bounded scope, custody, bibliography, and skill catalog. The vision's *"AI as infrastructure"* paradigm collapses to undifferentiated assistance if roles bleed into each other. Pillar 2 of the Layer B triangle (*scope discipline*) is grounded in this.
2. **Real work crosses role boundaries constantly.** A PO authoring a capability needs to know whether the capability is *technically feasible* (Architect scope) and whether the *quality program supports it* (QA scope). An Architect designing the data layer needs to know what *value the data serves* (PO scope). Without a mechanism to cross boundaries safely, the framework forces every cross-role consultation into one of two anti-patterns: full role handoff (heavy) or silent reading of the other role's skills (dangerous — observed in this bootstrap when reading sibling skills bled their framing into the calling role's reasoning).
3. **The audit trail must survive the consultation.** When the PO authors a feature with input from the Architect, the audit reader downstream must be able to see that the consultation happened, what was asked, what was returned, and which role authored the final artifact. Without this, the boundary is technically preserved but operationally invisible.

The Capability [[cap-10-subagent-consultation]] declares the property; this ADR records the decision that makes the boundary preservation explicit.

## Decision

We adopt the rule **subagent dispatch is information transfer, not authority transfer**, with the following corollaries:

1. **The calling role retains scope authority.** When role A invokes role B via the `Task` tool, B returns *consultation* — analysis, recommendations, criteria, references. A reads B's response as data and authors the final artifact in A's scope, in A's skill vocabulary, citing B as a consulted source where relevant. B does not write to `nodes/` on A's behalf; B does not commit; B does not author the node.
2. **The consultation is logged.** Every subagent dispatch produces an entry in the session document's `## Subagent consultations` section: who consulted whom, on what question, with what outcome. The Log entry that captures the calling role's *use* of the consultation is authored under the calling role's tag.
3. **Full ownership transfer is a separate, deliberate mechanism.** If full authority transfer is genuinely what's needed (rare), the operating pattern is: close the conversation with role A, open a new conversation with role B on the same session branch. The session document records the handoff via the participants array and via a closing Log entry from A pointing to B's pickup. This is *cross-conversation handoff*, not subagent dispatch; the two mechanisms are deliberately distinct.

The decision rests on a structural distinction between two patterns that look similar at the level of "agent A talks to agent B" but produce fundamentally different audit and ownership properties.

## Consequences

**Positive:**

- **Role scope is preserved under cross-role work.** A PO authoring a capability with Architect input still authors as PO; the capability cites PO sources and uses PO skill vocabulary; the Architect's contribution is recorded as consultation and credited as such. The framework's *"one role, one scope"* property holds even in the most common multi-role moment.
- **The audit trail is operationally complete.** `## Subagent consultations` produces a per-session log of every cross-role interaction. A downstream auditor can reconstruct *who consulted whom and why* without reading the full conversation.
- **Silent contamination is structurally discouraged.** The alternative (one role silently reading another role's skills to "borrow" criteria) was observed in this very bootstrap and produced framing drift. Forcing the consultation through a logged, named dispatch makes the cross-role move visible and challengeable.
- **The mechanism is reversible.** A consultation that produced a bad recommendation is recorded as such; the calling role can decline the recommendation and document the decline. Authority remained with the caller throughout.
- **The framework's `Task` tool semantics align with the decision.** `Task` returns the subagent's response to the calling conversation; the calling agent decides what to do with it. The harness already implements the desired pattern; this ADR records the *semantic* commitment, not a new mechanism.

**Negative:**

- **The rule depends on calling-role discipline.** A calling role that takes the subagent's response and pastes it verbatim into a node is technically authoring the artifact but materially appropriating the subagent's voice. The framework currently relies on the calling role's judgement and on the human's veto (CLAUDE.md operating principle: *"Human directs; AI maintains"*). The discipline is socially enforced, not structurally enforced.
- **The boundary between consultation and handoff requires judgement.** *"This is a consultation"* vs *"this is genuinely a handoff"* is a judgement call. The framework provides the two mechanisms and asks the contributor to choose; it does not codify when one is appropriate vs the other. A future *consultation matrix* improvement candidate (mentioned in [[cap-10-subagent-consultation]] non-coverage) would address this gap.
- **Subagent dispatch carries token cost.** Each invocation spins up a new agent context, loads the agent's role file, and reads the relevant skill. For frequent small consultations the cost adds up; the alternative (silent reading) would be cheaper but breaks the property. The framework accepts the cost in favour of the property.
- **The mechanism has no machine-checkable enforcement.** No linter rejects a node authored under role A that quotes role B verbatim without a consultation log. The discipline is convention-enforced at the agent-behaviour level and review-enforced at the human level.

**Neutral:**

- **Subagent dispatch is harness-specific in mechanism, decision-stable in principle.** The current implementation uses Claude Code's `Task` tool with `subagent_type:`. A different harness would implement the dispatch differently; the *principle* (information not authority, logged) transfers.
- **The rule is not Jones-anchored.** Jones speaks of role coordination and skill overlap (Ch 9 Table 9-23 productivity contributions of specialists) but does not prescribe a consultation-vs-handoff distinction for AI-mediated work. The decision is grounded in the framework's *"AI as infrastructure"* paradigm and the observed contamination risk, not in audited bibliography.
- **The rule scales with the operating triangle.** Pillar 2 (scope discipline) of the Layer B triangle replaces a *"working agreement"* mechanism; this ADR makes that replacement structural. The same discipline applies regardless of how many roles exist in the framework (5 today, 7 with Security + Designer planned, more in future).

## Alternatives considered

- **Subagent dispatch transfers authority to the dispatched role.** Rejected. Defeats the role-scope property; the dispatched role would write its own framing into the calling role's artifact, producing role-bleed by design. The vision's *"AI as infrastructure"* paradigm depends on roles staying scoped.
- **No subagent dispatch; every cross-role need triggers a session handoff.** Rejected. Too heavy. A PO seeking a five-minute feasibility check from the Architect should not have to close the conversation and reopen it under the Architect; the ceremony cost would discourage cross-role consultation, leading to either silent contamination or under-consulted work.
- **Subagent dispatch is the only cross-role mechanism; no handoff exists.** Rejected. Some work genuinely requires full role ownership transfer (a feature moves from PO scope to Developer scope when the spec is ready; the Developer authors implementation under their own framing, not via PO consultation). Forcing this through subagent dispatch only would lose the ownership-shift semantics.
- **Allow subagents to write nodes directly.** Rejected. Breaks the audit trail (who authored what becomes unclear), breaks the "calling role retains scope" property, and creates non-deterministic ownership when several roles consult on the same artifact. The constraint that the calling role authors is load-bearing.
- **Make consultation invisible (no log).** Rejected. Defeats the audit-trail property; cross-role work would happen but be untraceable; the framework's claim of full traceability would have a known hole.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Affected. The structural property *roles have bounded scope; cross-role work is logged but does not transfer authority* shapes how every multi-role thread proceeds. It is one of the substrate's defining behavioural rules.
- **2. Data structure:** Affected. The `## Subagent consultations` section in session documents is the data home for the consultation trail. The format (who, when, on what, with what outcome) is a constrained schema.
- **3. Interfaces to outside world:** Materially affected. The interface between role-agents is the consultation pattern itself. The calling role sees the consulted role's response as data, not as a co-author; the audit reader sees the consultation as a named event, not as silent influence.
- **4. Decomposition into functional components:** Materially affected. Roles are the framework's *organizational* decomposition; this ADR governs the linkage between those components. Without it the decomposition has no inter-component contract.
- **5. Linkage / information transmission among components:** Materially affected. This is the principal topic the decision addresses. Information flows from consulted to calling role (typed as consultation, logged); authority does not flow at all (each role retains its own); ownership flows only via explicit handoff (a distinct mechanism). The decision is essentially the *information-vs-authority* type discipline of cross-role linkage.
- **6. Performance attributes:** Indirectly affected. Subagent dispatch costs more tokens than silent reading; the framework accepts this cost in exchange for the scope property. At the framework's scale this is not a budget concern; for a large-portfolio adoption it would warrant measurement.
- **7. Security attributes:** Indirectly affected. The audit trail produced by `## Subagent consultations` is the analogue of a system call log — every cross-role boundary crossing is recorded. This is a *visibility* property; it does not prevent malicious behaviour, but it makes such behaviour reviewable.

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics, used here as the audit grid.
- CLAUDE.md Layer B § *Subagent dispatch ≠ authority transfer*, § *The triangle* (pillar 2: scope discipline), § *Writing to the session doc* (the `## Subagent consultations` section).
- `.claude/agents/<role>.md` — each agent's `description` field drives dispatch triggers; each agent's `## Interaction with other roles` table declares the legitimate hand-offs.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**.
- Capability anchor: [[cap-10-subagent-consultation]] (the property this decision materialises).
