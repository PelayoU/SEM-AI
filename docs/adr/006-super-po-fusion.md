---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-14
updated: 2026-05-22
maintained_by_role: architect
---

# ADR 006 — Product Owner is a super-PO at Tier-1; absorbs Business Analyst and Project Manager functions; split deferred to Tier-4

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — the fusion is operating in the role catalog. `.claude/agents/product-owner.md` carries 15 skills across four buckets (Strategic / Discovery / Tactical / Process); `.claude/sem-role-catalog.md` documents the design rationale; CLAUDE.md § *Roles* table records PO custody as *"Product + business analysis + project management (super-PO fusing PM/PL/BA/PM-project)"*.

## Context

The framework must decide how to decompose the *organizational substrate* — the layer the vision claims has been *"reformulated as a substrate of homologous AI agents"* — into role-agents. Jones's taxonomy assigns distinct empirical specialties for Product Manager, Product Leader, Business Analyst, and Project Manager, with documented separate productivity contributions and assignment scopes (Jones Ch 9 Table 9-23). Three forces are in tension:

1. **The Jones decomposition is human-cognitive.** Jones's recommended separations stem from the cognitive bandwidth limits of human specialists — a BA cannot simultaneously elicit requirements, write user stories, manage a backlog, plan a release, track milestones, and run cost estimates without losing focus or domain depth. Specialisation is the empirical answer when cognition is the bottleneck.
2. **AI agents do not share human cognitive limits.** A role-agent can carry 15 skill files, swap context cleanly between skills, and apply each skill's criteria with full bibliographic anchoring. The justification for human-style separation does not transfer mechanically to AI-mediated work.
3. **Role-bleed is a real risk regardless.** Fusing functions into one agent risks the agent's skills blurring into a single undifferentiated *"product role"* with no discipline boundaries. The benefit of fusion (lower coordination cost, fewer handoffs) is real but only realised if skill cohesion is structurally preserved.

A fourth tension is empirical: at very large scale (>100k FP, multi-team, regulated domains), Jones's separation may reassert itself — workload, organisational politics, and regulatory requirements may force the BA or PM functions out into separate roles.

## Decision

We adopt **super-PO fusion at Tier-1**, with explicit deferred-split semantics:

1. **The Product Owner role at Tier-1 absorbs Product Manager + Product Leader + Business Analyst + Project Manager functions.** Custody covers product strategy (vision, goals, capabilities, features, stories, specs), business analysis (requirements discovery, user involvement, value analysis), and project management (sizing, estimating, planning, tracking, change control, benchmarks). Single agent, 15 skills, four explicit buckets (Strategic / Discovery / Tactical / Process).
2. **Skill cohesion is preserved by bucket organisation.** The 15 skills are partitioned into the four buckets to keep the agent's reasoning legible. Each skill has a precise description so dispatch triggers reach the right skill without bucket blur.
3. **Tier-4 emergence is documented, not preemptively built.** When workload, organisational politics, or regulatory requirements force the BA or PM functions out into separate roles, the framework provides a deferred-split path. `.claude/sem-role-catalog.md` documents the two emergence cases (BA as separate role, PM as separate role) with explicit triggering conditions. Until those conditions appear, the fusion holds.
4. **Default entry is PO.** For new product work, `claude --agent product-owner` is the natural starting point. PO is the integrator; specialists are consulted via subagent dispatch (ADR 005) when needed. This is recorded in CLAUDE.md § *Roles*.

## Consequences

**Positive:**

- **Coordination cost collapses for solo and small-team work.** A single PO covers strategic, tactical, business-analyst, and project-management concerns without the handoff cost that splitting these functions across humans (or across AI agents) would impose. For the vision's claim *"from solo builder to large enterprise"*, the solo-builder end is reachable structurally.
- **Cagan-empowered PO is honoured.** Cagan's modern PO (in *Inspired* + *Empowered*) absorbs PM functions explicitly. The fusion aligns with the most influential out-of-bibliography source on modern product practice — flagged as convention per ADR 003.
- **AI bandwidth is exploited where humans cannot.** The fusion is not a workaround; it is a deliberate use of AI's lack of cognitive bandwidth limits, consistent with the vision's *"AI as infrastructure"* paradigm. The framework would be strictly worse if it copied human-organisational separations that exist only because of human limits.
- **The integrator role is named.** Even in organisations that split BA and PM out, someone has to integrate strategy + business + process. By default that integrator is the super-PO; the framework names this explicitly rather than leaving it implicit.
- **Bibliographic anchors hold per skill.** Each of the 15 PO skills cites its own primary source (Jones BPs, Cagan principles via GISF, GISF slides, Cucumber, Patton, Cohn). The fusion does not weaken citation discipline; the skills remain individually anchored.

**Negative:**

- **Jones's empirical separations are not honoured at face value.** Jones Ch 9 Table 9-23 lists separate productivity contributions for BA, PM, PO, etc. By fusing them into one agent we lose the per-specialty granularity Jones offers and the ability to attribute defect prevention / removal contributions per specialty. The framework's response is *"those numbers are HUMAN-bandwidth numbers"* (per `.claude/sem-role-catalog.md`); this is a defensible argument but it does require defending.
- **Role-bleed risk is real and depends on bucket discipline.** Without strict bucket organisation, the 15 skills could blur into an undifferentiated "product role". The mitigation is the four-bucket partition plus per-skill descriptions; this works if the agent's dispatch logic respects them.
- **Tier-4 emergence is documented but untested.** Splitting BA or PM out at scale is a planned future operation; no project has yet exercised the split. When the split actually happens, the migration of skills from the super-PO catalog to the new specialist role may surface friction not anticipated.
- **The fusion is a paradigm bet, not a derivation.** The claim *"AI agents do not share human cognitive limits"* is itself an act of faith (Cagan principle 9, applied at the framework level). If the bet is wrong — if even AI agents benefit from human-style specialisation — the fusion produces a measurably worse framework than the split. Goal G3 (portability proof) is the first place where this will be tested empirically.
- **Industry compatibility is lower at the role-naming surface.** An organisation that recruits a separate BA, a separate PM, and a separate PO will find SEM-IA's role naming non-obvious. The framework will read *"PO"* and they will read *"three different roles"*. The role catalog documents the mapping; the friction at first contact remains.

**Neutral:**

- **The fusion is a Tier-1 default, not a universal rule.** It is correct for solo, small-team, and most mid-scale work. It is explicitly conditional at large scale. Future projects can split without changing the framework's vision; the role catalog is the substrate for that adaptation.
- **The decision is not Jones-anchored in the *fusion* direction.** Jones's data supports separation; the fusion is justified by Cagan (out of audited bibliography, flagged) and by the AI-as-infrastructure paradigm. The Architect role's role here is to record the trade-off, not to claim Jones validates the fusion.
- **The five other Tier-1/Tier-2 roles (Architect, QA, Developer, DevOps) are *not* fused similarly.** They retain Jones-style separation. The fusion is specific to PO + PM + BA + PL because these functions converge on *direction* and *prioritisation*, where integration value is highest. The technical roles converge on *execution*, where specialisation value remains.

## Alternatives considered

- **Separate PO, BA, PM, PL as four distinct Tier-1 roles from day one.** Rejected for solo / small / mid scale. Jones-aligned in the bibliographic sense but produces three additional handoffs and four sets of agent identity files for a project that may not need them. Forces every new project into the multi-team structure regardless of size.
- **Single "product role" with all 15 skills but no bucket partition.** Rejected. Without buckets the agent's skill catalog blurs; dispatch becomes unreliable; the role's reasoning loses the discipline boundaries that make each skill citable. Bucket organisation is non-negotiable.
- **Super-PO at Tier-1 with no Tier-4 emergence path documented.** Rejected. Closes the door on the legitimate scaling case (large enterprise, regulated domain, multi-team). The framework's *"anyone, any scale"* claim requires the door to remain open.
- **Two-role split: PO (strategy + product) + Project Steward (PM + BA functions).** Rejected. Cuts the integration value in half (strategy and process must talk constantly); creates a handoff between scope-decision and scope-execution at exactly the boundary the super-PO is designed to span.
- **Defer the fusion question entirely; let each project decide.** Rejected. Frameworks that defer foundational role decisions impose the decision cost on every adopter. The fusion is opinionated by design; the override path is the Tier-4 documentation.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Materially affected. The role catalog *is* the framework's organizational decomposition. The fusion changes the top-level shape: 5 core roles (PO, Architect, QA, Developer, DevOps) instead of 8+ (PO, PM, PL, BA, Architect, QA, Developer, DevOps).
- **2. Data structure:** Affected. The agent identity file `.claude/agents/product-owner.md` carries a four-bucket skill catalog; the skill catalog's structure is part of the framework's data architecture. Splitting at Tier-4 would produce new identity files with subset catalogs.
- **3. Interfaces to outside world:** Materially affected. The contributor invokes a role by name; the fusion changes the surface of *which names exist*. A contributor familiar with Jones's separations sees one PO where they expected three to four roles; the mapping must be made explicit (sem-role-catalog.md performs this).
- **4. Decomposition into functional components:** Materially affected. This is the principal topic the decision addresses. The functional decomposition of the organisational substrate is: 5 fused agents covering 7+ Jones-style roles, with Tier-4 split deferred. Every other decomposition decision (skills per role, bucket organisation within PO) depends on this top-level shape.
- **5. Linkage / information transmission among components:** Affected. Fusion reduces inter-role handoffs (no PO-to-BA-to-PM chain when scoping a feature); it also reduces the inter-role linkage surface area. The remaining links (PO↔Architect, PO↔Developer, PO↔QA, PO↔DevOps) are documented per agent file.
- **6. Performance attributes:** Not materially affected. Skill-dispatch latency within the super-PO is comparable to dispatch in any role; the four-bucket structure is for human legibility, not runtime performance. Not applicable.
- **7. Security attributes:** Indirectly affected. A super-PO has broad write authority across the product hierarchy (vision, goals, capabilities, features, stories, specs). This concentrates write authority in one role; mitigation is the human-confirms operating principle (no agent writes without human direction).

## Source

- Skill: `architect-architecture-design` (Jones Ch 7 seven fundamental topics, especially topics 1 and 4); `architect-methodology-selection` for the role-organisation aspect of methodology choice.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 9 Table 9-23 — specialty productivity / defect-prevention contributions (the empirical basis for separation under human cognitive limits).
- Cagan, *Inspired* + *Empowered* — the modern empowered PO concept absorbing PM functions; **not in audited `bibliography/sources/`**, flagged per ADR 003 as convention. Cited indirectly via `.claude/sem-role-catalog.md` § *Design rationale for fusion*.
- CLAUDE.md § *Roles* — encodes the fusion in the role table.
- `.claude/sem-role-catalog.md` — the design rationale and the Tier-4 emergence documentation.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**.
- Related: ADR 005 (subagent dispatch — the mechanism that lets a fused role get specialist input without un-fusing).
