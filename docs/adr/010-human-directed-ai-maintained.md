---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-14
updated: 2026-05-22
maintained_by_role: architect
---

# ADR 010 — Human directs, AI maintains: authorship is always the human's, AI proposes and never decides

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — the rule is operating in every conversation across the framework. CLAUDE.md § *Operating principles* declares it as principle #1: *"Human directs; AI maintains. A role proposes; the human confirms before anything is written. Authorship is always the human's."* Every role's agent file echoes the rule (*"Architect proposes; Architect does not decide"* — `.claude/agents/architect.md`, equivalent phrasings across PO, QA, Developer, DevOps).

## Context

The vision claims that the substrate of role-agents *"absorbs the cost specific to working with AI (review burden, hallucination, scope drift, context loss); the human keeps authorship, judgement and the right to sign"*. The decision that operationalises this claim is a choice about *where authority sits*. Three forces are in tension:

1. **AI-as-employee is the dominant industry framing.** Outside SEM-IA, autonomous agents that *"appropriate execution"* are the prevailing direction — agents that decide, write, commit, and sometimes deploy without explicit human confirmation per step. The promise is throughput; the cost is loss of human authorship and a class of failures (hallucination, scope drift, context loss) that fall on the human anyway, after the fact, when reviewing AI output that the agent already committed.
2. **AI-as-tool is the alternative industry framing.** Undifferentiated chat copilots that produce output the human pastes. The human retains authorship by default but loses the discipline benefit — the AI is not bound to a role, a skill, a citation, a method. Output quality varies; coordination across multi-step work is the human's responsibility entirely.
3. **The vision's framing is a third position: AI-as-infrastructure.** Agents are role-scoped, method-anchored, citation-disciplined; they *propose* under the role's discipline; the human *decides* whether to accept the proposal. The discipline cost is borne by the substrate; the authorship is retained by the human. This is neither AI-as-employee (no agent appropriates the decision) nor AI-as-tool (the agent operates inside a disciplined role).

A fourth tension is regulatory and ethical: the EU AI Act, ISO/IEC 42001, and the broader audit ecosystem treat *the human in the loop* as a structural requirement for accountable AI use. A framework that quietly transfers authorship to the AI breaks downstream accountability. A framework that names the rule explicitly and operationalises it survives audit.

## Decision

We adopt the rule **human directs, AI maintains**, with the following structural consequences:

1. **The human is the author of every artifact.** A node committed under SEM-IA carries the human's authorship even if the AI did the keystrokes. The agent is a maintainer, a drafter, a proposer; the signature is the human's.
2. **The agent proposes; the human confirms before anything is written.** No agent commits, merges, writes to `nodes/`, or modifies the substrate without explicit human direction. The pattern is: agent surfaces a proposal in conversation; human reads, accepts / refines / rejects; agent then performs the file operation. The order is non-negotiable.
3. **The agent's failure modes are owned by the substrate, not by the human's review burden.** Hallucination, scope drift, context loss, framing contamination — these are the framework's problems to solve (via citation discipline, role scoping, session continuity, subagent dispatch). The human reviews the *final proposal*, not every AI-generated intermediate; the substrate absorbs the AI-specific cost so the human's review burden remains roughly equivalent to the burden of reviewing a competent human's work.
4. **AI judgement is bounded; human judgement is final.** An agent may form opinions, propose alternatives, flag risks, and surface gaps. Selecting among the proposals, deciding what to publish, deciding what to abandon — these are reserved to the human. The framework names this explicitly as "the human's right to sign".
5. **The rule survives across roles.** Every role-agent applies the same authority pattern; no role is exempt. The Architect proposes ADRs; the human confirms. The PO proposes capabilities; the human confirms. The DevOps proposes a deployment plan; the human confirms. There is no agent in SEM-IA that decides without confirmation.

## Consequences

**Positive:**

- **Authorship and accountability are aligned.** The human who signs the artifact is the human who decided the artifact's content. Downstream audit (TFM tribunal, regulatory review, future maintainer) finds a coherent authorship trail; nothing was decided by a process that cannot be questioned.
- **The AI-specific cost is absorbed by the framework, not by the human.** Citation discipline prevents hallucination; role scoping prevents scope drift; session continuity prevents context loss; subagent dispatch prevents framing contamination. The substrate is engineered to absorb the four costs the vision names; the human's residual review burden is *judgement*, not *forensics*.
- **The framework is robust against AI capability fluctuations.** When the underlying LLM improves, the substrate gains throughput; when the LLM regresses on a class of tasks, the human's confirmation catches the regression. Either way, the artifact's quality is bounded by the human's judgement, not by the AI's variability.
- **The framework is regulator-compatible.** Human-in-the-loop is a structural property, not an aspiration. EU AI Act, ISO/IEC 42001, and similar accountability frameworks find SEM-IA structurally compliant on this axis (other axes such as data provenance, model governance are downstream).
- **The "two-edged sword" of reuse applies analogously.** Just as Jones BP #26/27 warns that high-quality certified reuse delivers +300% ROI and uncertified reuse delivers −300%, the *human-directs* rule prevents the corresponding negative-ROI failure mode for AI work: AI artifacts committed without human confirmation are the AI analogue of uncertified reuse. The rule is the certification gate for agent output.
- **The framework's value proposition becomes legible.** "AI as infrastructure" vs "AI as employee" is a paradigm claim; the *human-directs* rule is the concrete behaviour that distinguishes the two. A reader can recognise SEM-IA's paradigm by observing whether the AI proposed or decided.

**Negative:**

- **Throughput is bounded by human bandwidth.** A fully autonomous agent could produce far more output per unit time than a human-confirmed agent can. SEM-IA explicitly accepts this trade — *authorship* is more valuable than *throughput*. For use cases where throughput is paramount (high-volume content generation, mass document review), SEM-IA is the wrong tool.
- **The rule depends on the agent's compliance.** A misbehaving agent that writes without confirmation breaks the rule. The framework's mitigation is the agent's identity files explicitly stating the discipline; the harness's permission model (Claude Code's tool-use prompts) provides additional defence. Neither is structurally enforced at the file-system level; both are convention-enforced.
- **Confirmation friction is real.** Every meaningful change requires the human to read a proposal and approve it. For long sessions of intensive authoring, the confirmation cadence becomes a load. The mitigation is the role's discipline reducing the *number* of low-quality proposals (anchored by skills + citations), not the friction *per* proposal.
- **The rule does not scale to multi-human teams without governance.** *"The human"* is singular in the framework's current formulation. A team of three humans operating under SEM-IA shares the role of *"the human who confirms"*; without governance (who confirms what, when do they vote), confirmation can become ambiguous. The framework currently assumes solo or designated-human operation; multi-human governance is a future concern.
- **The rule is paradigm-anchored, not Jones-anchored.** Jones speaks of methodology selection (BP #9) and management practices but does not prescribe human-AI authority partition. The decision rests on the vision's paradigm claim (*"AI as infrastructure"*), which itself is flagged as out-of-bibliography per ADR 003. The argument for the rule is internally consistent within SEM-IA's vision; from outside, it is a *claim*, not a *theorem*.

**Neutral:**

- **The rule is meta-recursive.** This very ADR is authored by an Architect agent under the human's direction; the human confirms before the file is written. The bootstrap session that produces SEM-IA's self-model exercises the rule it documents.
- **The rule does not forbid AI-initiated proposals.** An agent may surface a proposal proactively (an Architect agent noticing an architectural decision worth ADR-capture, a QA agent noticing a defect-removal gap). The rule binds *deciding* and *writing*, not *proposing*. Proactive proposal is welcome; unilateral execution is not.
- **The rule applies to the substrate as well as content.** A change to a skill, a template, or an agent identity file requires the same human confirmation. The substrate is no more autonomously editable than the content; the framework does not bootstrap itself without human direction.
- **The framework's ergonomics depend on the human-AI interaction being fluid.** A heavy-friction confirmation flow (e.g., one click per file edit) would make the rule unusable in practice. Claude Code's permission flow is acceptable; future improvements to permission ergonomics are a substrate concern but not an ADR-level change.

## Alternatives considered

- **AI-as-employee: autonomous agents that decide and commit without per-step confirmation.** Rejected. Defeats the authorship property; transfers accountability to a process that cannot be held accountable; produces audit trails that are unverifiable in principle; concedes the AI-specific failure modes (hallucination, scope drift) to the human's after-the-fact review burden.
- **AI-as-tool: undifferentiated chat copilots with no role discipline.** Rejected. Loses the discipline benefit; the human retains authorship by default but bears the full coordination cost; no audit trail of why each authorial decision was made.
- **Hybrid: AI decides on small things, human confirms on big things.** Rejected. The boundary between "small" and "big" is judgemental and shifts; in practice "small" expands until significant decisions get made by agents under the rationalisation of *"it was small"*. A clean rule is operationally more robust than a graduated one.
- **Human decides; AI executes mechanically.** Considered. This is approximately *"AI as compiler"* — the human writes the decision in some intermediate form; the AI translates to artifact. Rejected because it loses the *proposal* surface where the AI's role-discipline adds value; the AI is reduced to a typing assistant.
- **Defer the rule to project-level configuration.** Rejected. The rule is foundational to the paradigm; deferring it would dissolve the *AI as infrastructure* claim into *whatever the local project decides*. Frameworks that defer foundational stances are not infrastructure; they are kits.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Affected. The framework's operating model has a fixed *propose → confirm → execute* loop in every meaningful interaction. This is part of the substrate's top-level behavioural shape.
- **2. Data structure:** Not materially affected. The rule governs *who writes* the data, not the data's structure. ADR 008 governs the data structure; this ADR governs the authority over it.
- **3. Interfaces to outside world:** Materially affected. The interface between the framework and the human is the proposal-confirmation flow. Every meaningful agent action surfaces in conversation as a proposal; the human's response is the gate. This is the principal topic for this ADR.
- **4. Decomposition into functional components:** Affected. The framework's components (agents, skills, slash commands, the human in the loop) compose under the rule that the human's confirmation is the integration point. Components do not bypass the human to coordinate among themselves.
- **5. Linkage / information transmission among components:** Materially affected. Information flows from agents to the human as *proposals*; from the human to agents as *decisions*; from agents to artifacts as *executed writes*. The flow direction is fixed; bypassing the human is forbidden.
- **6. Performance attributes:** Affected. The rule bounds throughput by human bandwidth; the substrate is engineered to make each confirmation high-value (because the proposal is role-anchored and skill-disciplined). This trade-off is intentional.
- **7. Security attributes:** Materially affected. Human-in-the-loop is a security and accountability property. The audit trail is coherent (human decided + AI executed = recorded change). Regulator compliance (EU AI Act, ISO/IEC 42001) finds the framework structurally compliant on this axis.

## Source

- Skill: `architect-architecture-design` (Jones Ch 7 seven fundamental topics, especially topics 3 and 7 — interfaces and security).
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics, used as the audit grid.
- CLAUDE.md § *Operating principles* — principle 1 (*"Human directs; AI maintains"*) is the canonical statement of this decision; every role's agent identity file echoes it.
- [[vision-sem-ia]] Statement — *"The agents absorb the cost specific to working with AI (review burden, hallucination, scope drift, context loss); the human keeps authorship, judgement and the right to sign."*
- EU AI Act, ISO/IEC 42001 — regulatory accountability frameworks that find human-in-the-loop structurally compliant; **not in audited `bibliography/sources/`**; cited as regulatory context per ADR 003 flagging convention.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**.
- "AI as infrastructure" paradigm framing — author's formulation, flagged as out-of-bibliography in [[vision-sem-ia]]'s `## Source`.
- Related: ADR 003 (citation mandate — the discipline that absorbs the hallucination cost), ADR 005 (subagent dispatch — the discipline that absorbs the framing-contamination cost), ADR 006 (super-PO fusion — depends on the rule that fusion does not transfer authority to the agent), ADR 009 (skill discipline — the discipline that anchors agent proposals).
