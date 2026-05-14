---
category: adr
id: adr-009-skill-as-canonical-method
parent: "[[vision-sem-ia]]"
artifacts:
  - "[[.claude/templates/SKILL.md.template]]"
status: accepted
created: 2026-05-14
updated: 2026-05-14
supersedes:
superseded-by:
---

# ADR 009 — A skill is the canonical method for one operation, anchored verbatim in primary sources, and is the unit of agent decomposition

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — the skill structure is operating across all five implemented roles. CLAUDE.md § *Skills convention* declares the rule (`.claude/skills/<role>-<name>/SKILL.md`, ≤500 lines, fixed sections, citation mandate, read-before-write); `.claude/templates/SKILL.md.template` encodes the pattern for new skills; 37 skills exist anchored to Jones / Cagan (via GISF) / GISF UC3M / Cucumber / Patton / Cohn (via GISF) per [[cap-08-citation-discipline]].

## Context

Once role-scoped agents are decided (ADR 006 fusion + the broader role catalog), a further decomposition question arises: *how does a role-agent know what it knows, and how does it apply that knowledge consistently?* Three forces are in tension:

1. **A role is too coarse a unit for reliable behaviour.** A "PO agent" with 15 functions blurs into an undifferentiated reasoner if all 15 functions are mixed in one prompt or one identity file. The agent needs a *decomposition* of its knowledge into discrete operations it can apply individually.
2. **Each operation must be reliably applied the same way every time.** Calling on the PO to "do a vision exercise" should produce a Cagan-Ten-Principles-anchored output every time, not whatever the agent's general knowledge of "vision" produces in a given moment. The reliability property is the difference between an *infrastructure* and a *general-purpose assistant*.
3. **The agent must be auditable per operation.** When the PO authors a vision, an auditor must be able to trace the operation back to its method, the method back to its formal criteria, and the criteria back to their primary source. Without per-operation auditability, the citation discipline (ADR 003) has no anchor point in the agent's reasoning.

A fourth tension: the agent's identity file must remain small enough to be loaded into every conversation. Identity files balloon to thousands of lines if they encode every operation in detail. A separation between *identity* (small, always-loaded) and *method* (larger, loaded on demand) becomes structural.

## Decision

We adopt **skill = canonical method for one operation** with the following structural rules:

1. **One skill = one operation.** Each `.claude/skills/<role>-<name>/SKILL.md` covers exactly one named operation (drafting a vision, decomposing a feature, inspecting code, sizing a project, etc.). Multi-operation skills are split; cross-operation methods are decomposed.
2. **Skills are role-scoped.** Each skill belongs to exactly one role; the filename prefix (`<role>-<name>`) makes the ownership unambiguous. A skill is dispatched only by its owning role; another role consults it via subagent dispatch (ADR 005), it does not borrow the skill silently.
3. **Skill structure is fixed.** Every SKILL.md carries six sections in order: `## Purpose`, `## When this skill applies`, `## Formal criteria`, `## How you proceed`, `## Pitfalls to avoid`, `## Source` (CLAUDE.md § *Skills convention*). Frontmatter has two required fields: `name`, `description` (Anthropic skill-creator convention).
4. **Citation per criterion.** Every threshold, anti-pattern, decision rule, or formal criterion in `## Formal criteria` cites a primary source inline (ADR 003). Skills without per-criterion citations are non-compliant with the framework.
5. **Read-before-write.** Authoring a new skill requires reading the binding primary source firsthand (or a `pdftotext` extract) before writing the skill. CLAUDE.md § *Skills convention* names this discipline. The constructor verifies the citation by reading; downstream readers can verify by following the citation.
6. **≤500-line cap.** Skills are bounded in length to remain loadable and readable. Larger units of knowledge decompose into multiple skills.
7. **Out-of-bibliography frameworks may appear in `## Source` but flagged as convention** (ADR 003 corollary). A skill may invoke Cagan-via-the-books, Nygard ADRs, ITIL, SOLID, Clean Code, etc., but each such reference carries the *"not in audited `bibliography/sources/`"* disclaimer.

## Consequences

**Positive:**

- **Per-operation reliability.** When the PO is asked to draft a vision, dispatch goes to `po-vision`; the agent reads its `## Formal criteria` and `## How you proceed`; the output is structured by the skill's discipline. The reliability gap between "general-purpose product reasoning" and "Cagan-Ten-Principles-anchored vision draft" closes.
- **Per-operation auditability.** Every skill's `## Source` section traces its criteria to primary sources; `bibliography/skill-references.md` maintains the per-skill traceability index. An auditor selects a skill and reproduces its criteria from the source — the same audit operation as for any node.
- **Agent identity files stay small.** A role's `<role>.md` carries the role's identity, scope, hand-offs, and skill catalog table; the skills themselves live in separate files. Identity files load with every conversation; skills load on dispatch. The token budget is bounded.
- **The framework grows by composition.** Adding a new role's capability is adding a new skill, not modifying existing ones. The skill is a unit of versioning and review; the role catalog is a unit of orchestration.
- **The discipline composes with all other ADRs.** Skills obey ADR 003 (citation mandate), ADR 008 (markdown + frontmatter), ADR 002 (skills don't have `parent:` because they live in substrate, not in the content graph — but the meta-template enforces the same structural discipline). The skill format is the canonical *substrate operational unit*.
- **Substrate portability is per-skill.** A skill that proves useful in SEM-IA's bootstrap can be lifted into a downstream project (per [[cap-13-portability]]) intact; the skill's anchors (Jones BP #, GISF slide #) are the same; the role catalog adopts the skill on the new project. Skill reuse is a planned outcome of the framework's evolution.

**Negative:**

- **Skill proliferation is a real risk.** With 37 skills already authored and the framework expecting more, the catalog can balloon. Discoverability degrades; dispatch routing becomes harder; the role's identity file table must keep pace. The mitigation is the role's bucket structure (e.g., PO's four buckets) — this works for now, may not scale to 100+ skills without further organisation.
- **The skill format is opinionated.** Six sections in a fixed order, ≤500 lines, citation per criterion. Authors familiar with other knowledge-base formats (long-form notes, FAQs, runbooks) must conform. The friction is real for first-time authors.
- **Read-before-write is a discipline, not an enforced check.** Nothing structurally prevents an agent (or a careless author) from writing a skill without reading the source — the citation would still appear, but it would be unverified. The mitigation is review-time audit and the moral commitment of the framework's authorship.
- **Cross-cutting knowledge is awkward.** A method that genuinely spans multiple roles (e.g., a measurement that PO + QA + DevOps all use) must either live in one role's catalog and be consulted by the others (per ADR 005) or be replicated. Replication breaks DRY; consultation works but adds dispatch cost. The current framework has not had to confront a strict cross-role skill; the case is not yet pressing.
- **The 500-line cap is a working heuristic, not a hard rule.** Some methods genuinely warrant more space (the architect-architecture-design skill brushes the cap with seven topics, Zachman, size-tier rules, and 40+ notations). The cap is enforced socially; a skill that exceeds it warrants splitting, but the split point is judgemental.

**Neutral:**

- **The skill structure follows Anthropic's skill-creator pattern** (community convention) and the framework's own meta-template. Anthropic's pattern is not in audited `bibliography/sources/`; flagged as convention per ADR 003.
- **The skill is not the agent.** Skills are knowledge units the agent applies; the agent is the role-scoped reasoner. A skill exists in the substrate; an agent invocation is a session moment. The distinction is structural and load-bearing.
- **A skill does not replace primary sources.** The skill is a *method*, citing the source for each criterion. The source remains the authority; the skill is the operationalisation. Removing the source would break the skill; updating the skill in response to a new edition of the source is the normal evolution path.

## Alternatives considered

- **No skill decomposition; encode all role knowledge in the agent identity file.** Rejected. Identity files balloon; reliability per operation degrades; per-operation auditability is lost. The framework would resemble a general-purpose role-prompt rather than a methodology.
- **Skills as informal long-form notes, no fixed structure.** Rejected. Loses per-criterion auditability; loses the citation discipline anchor; loses the loadable-on-demand property if the file structure is unpredictable.
- **Skills as compiled code (Python plugins, agent toolchains).** Rejected. Couples the framework to a specific runtime; defeats LLM-readability; loses the *"substrate inspection = reading text"* property.
- **One skill per role (the role itself is the skill).** Rejected. Same failure mode as no decomposition; per-operation discipline is lost.
- **Skills as a knowledge graph with typed edges.** Rejected for the same reasons graph-DB nodes were rejected in ADR 008 — breaks human-readability, breaks git-native semantics, breaks LLM-friendliness.
- **Cross-role shared skills directory.** Considered. Loses the *one skill, one role* property; introduces ambiguity about which role dispatches a shared skill. Rejected; cross-role information transfer goes through subagent dispatch (ADR 005), not through skill sharing.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Materially affected. The substrate has a dedicated `.claude/skills/` directory; per-role subdirectories; one skill per file. This is part of the framework's top-level structural shape.
- **2. Data structure:** Affected. The skill format (frontmatter + fixed sections + citation pattern) is a constrained schema for substrate knowledge artifacts. The schema is enforced by the meta-template.
- **3. Interfaces to outside world:** Affected. A skill is the interface between the framework's primary-source bibliography (Jones, Cagan via GISF, GISF, Cucumber, Patton, Cohn) and the operating agent. The skill *translates* the source into actionable criteria the agent applies; the citation is the bidirectional reference between the two surfaces.
- **4. Decomposition into functional components:** Materially affected. This is the principal topic the decision addresses. The functional decomposition of every role-agent is its skill catalog. The agent is one unit of dispatch; each skill is one unit of method. The decomposition is bounded (≤500 lines per skill, ~5–15 skills per role).
- **5. Linkage / information transmission among components:** Affected. A skill links upward to its primary source (via citation) and downward to the nodes the agent produces (via the methods the skill encodes). The agent reads the skill on dispatch; the source is read at authoring time. The linkage is one-directional in operation (skill → output), bidirectional in audit (output → skill → source).
- **6. Performance attributes:** Affected. The ≤500-line cap is in part a token-budget concern: skills are loaded into the agent's context on dispatch; larger skills consume more context. At the framework's scale this is comfortable; at 100+ skills per role the catalog-loading approach may need refinement.
- **7. Security attributes:** Indirectly affected. Every authoritative claim an agent makes is traceable to a skill, which is traceable to a primary source. A claim that cannot be traced is suspect by construction. This is the audit-trail property in its agent-behaviour form, parallel to the citation property in its data-content form.

## Source

- Skill: `architect-architecture-design` (Jones Ch 7 seven fundamental topics, especially topic 4 — decomposition).
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics, used as the audit grid; BP #26 *Reusability* (pp. 99–101) as a conceptual neighbour (skills are reusable methods at the substrate level).
- CLAUDE.md § *Skills convention* — the structural rules and the read-before-write discipline.
- `.claude/templates/SKILL.md.template` — the meta-template that encodes the format for new skills.
- `bibliography/skill-references.md` — the per-skill traceability index.
- Anthropic skill-creator pattern (community convention) — **not in audited `bibliography/sources/`**; flagged as convention per ADR 003.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**.
- Related: ADR 002 (the substrate's graph rules), ADR 003 (citation mandate that skills must obey), ADR 005 (subagent dispatch as the cross-skill consultation mechanism), ADR 006 (role catalog that skills decompose), ADR 008 (markdown + frontmatter as the skill's data format).
