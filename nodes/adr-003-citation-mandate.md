---
category: adr
id: adr-003-citation-mandate
parent: "[[cap-08-citation-discipline]]"
artifacts:
  - "[[CLAUDE.md]]"
  - "[[bibliography/INDEX.md]]"
  - "[[bibliography/skill-references.md]]"
  - "[[.claude/templates/SKILL.md.template]]"
status: accepted
created: 2026-05-14
updated: 2026-05-14
supersedes:
superseded-by:
---

# ADR 003 — Every authoritative claim cites a primary source; out-of-bibliography frameworks are flagged as convention

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — the rule is operating across every skill, every agent, every node template, and every node authored to date. CLAUDE.md § *Operating principles* declares *"Citation is mandatory"* as principle #2; every skill's `## Source` section anchors its criteria to Jones BP # / Ch # / page, GISF slide #, Cucumber page, Patton page, or Cohn via GISF. The flagging discipline for out-of-bibliography references is visible across the vision, goals, capabilities and skills (every "Not in audited bibliography" disclaimer in the substrate is an instance of this rule in force).

## Context

The framework's external defensibility — TFM defense, public-artifact reception (goal G2), and any future portability claim (goal G3) — rests on the *content* of the authoritative claims agents make being verifiable. Three forces are in tension:

1. **Authoritative claims must be defensible.** A skill that says "cyclomatic complexity above 20 is dangerous" carries weight only if it can be traced to a source the reader can verify. Without traceability the claim collapses to opinion, and the framework reduces to *"another set of opinions"* (per [[cap-08-citation-discipline]] value-risk). The TFM defense rests on this property.
2. **Useful frameworks exist outside the audited bibliography.** Cagan's own books, Sinek's *Start with Why*, Doran's SMART, Nygard's ADRs, ITIL, CMMI, ISO/IEEE standards, Patton (where not via the audited handouts), Lean Startup, Eric Ries, Michael Feathers on legacy code — all are useful, frequently the right reference, and not in `bibliography/sources/`. Forbidding their use would impoverish the framework. Letting them in silently as authority would dissolve the very defensibility we're protecting.
3. **The cost of citation must be low enough to be habitual.** Citation discipline that requires a footnote engine, a citation manager, or a separate review tool collapses under its own weight. The discipline must be writable inline by an agent in the middle of authoring, readable inline by any reader, and machine-greppable for audit.

The Capability [[cap-08-citation-discipline]] declares the property; this ADR records the structural decision and the flagging convention that resolves the second tension.

## Decision

We adopt **two complementary rules**:

1. **Citation mandate.** Every authoritative claim — a formal criterion, a threshold, an anti-pattern, a decision rule, a verbatim definition — cites a primary source inline, using a short reference pattern: `(Jones BP #14, p. 76)` · `(Jones Ch 7, p. 470)` · `(GISF gisf-discovery.pdf slide 89)` · `(Cucumber gherkin-reference.pdf p. 1)`. A statement without such a citation is not a statement from this framework — it is conversational opinion, hypothesis, or conjecture, and must be marked as such if it appears in an authoritative section.

2. **Out-of-bibliography flagging.** When a useful framework that is not in audited `bibliography/sources/` is invoked (Cagan books directly, Sinek, Doran's SMART, Nygard's ADRs, ITIL, CMMI, ISO/IEEE, Lean Startup, etc.), the reference is **explicitly flagged as convention rather than authority**. The flag takes the form of a short disclaimer in the affected skill's or node's `## Source` section — e.g., *"Nygard ADR format — industry convention, not in audited `bibliography/sources/`"*. The flag is mandatory; the use is permitted.

Together these rules establish a two-tier source structure:

- **Tier 1 (authority):** sources in `bibliography/sources/` — currently Capers Jones *Software Engineering Best Practices*, eight GISF UC3M PDFs, the Cucumber Gherkin reference, the Patton story-mapping handout, the agile-story-essentials handout. Anchored citations of these may stand as authoritative claims.
- **Tier 2 (convention):** anything else — useful, often the right reference, but explicitly framed as convention. May guide design; must not be cited as authority.

The Architect role's reuse-certification skill (`architect-reuse-certification`) is the structural analogue of this rule applied to reusable artifacts: tier-1 sources are like certified reuse, tier-2 sources are like uncertified reuse. Both demand a gate.

## Consequences

**Positive:**

- **External defensibility is built into the substrate.** Every authoritative claim is grep-traceable to its source; auditors can verify the framework by sampling. The TFM defense rests on a property that is structurally checkable, not on the author's testimony.
- **The framework remains open to useful out-of-bibliography ideas.** Cagan principles, ADR convention, SMART, etc. are admitted via the flagging mechanism instead of being silently smuggled in. Honesty preserved, usefulness preserved.
- **Citation friction is low.** Inline parenthetical references are habitual; no separate citation manager; no footnote machinery; grep is the audit tool.
- **The discipline transfers to new skills and new projects.** A skill authored years from now under this framework inherits the citation rule from `.claude/templates/SKILL.md.template`. A project lifting the substrate (per [[cap-13-portability]]) inherits the rule unchanged.
- **The flagging convention disciplines the author's reasoning.** Having to write *"flagged as convention"* makes the author conscious that they are leaving the audited bibliography and inviting future challenge. Several legitimate uses of out-of-bibliography material have been more carefully placed because of this friction.

**Negative:**

- **Bibliographic gaps are felt frequently.** Cagan's *Inspired* is genuinely the source for the Ten Principles; we cite via GISF slide 89 (a handout that quotes Cagan). The chain is honest but indirect, and a hostile reader could push: *"why not the book itself?"*. Adding the book to `bibliography/sources/` would close this gap; until then, the indirection is a cost.
- **The flagging discipline can become decorative.** "Not in audited bibliography" can be appended habitually to references that don't strictly need the flag (a public-domain definition, a mathematical identity, a long-established programming-language concept). Calibration of *when* the flag is required is non-trivial; the skill `architect-architecture-design` carries the working heuristic but not a formal rule.
- **Quoting from `bibliography/sources/` requires read access to the source.** Audit-quality citation demands the auditor has the source available. The PDFs are committed to the repo, but a downstream consumer of a public copy may lack access to copyrighted material; the citations remain verifiable in principle but require obtaining the books.
- **Tier-1 / Tier-2 is a hard boundary.** A widely-adopted but unsourced framework — e.g., ADRs themselves — sits in tier-2 even when it's the *de facto* industry standard. Calling it convention rather than authority is technically correct but can read as pedantic to industry practitioners.

**Neutral:**

- **The rule is meta-recursive.** This ADR itself must obey the rule. Every authoritative claim in this ADR's body is anchored (Jones Ch 7 p. 470, CLAUDE.md § *Operating principles*, [[cap-08-citation-discipline]]), and the Nygard ADR convention is flagged as out-of-bibliography in the header and in this `## Source` section. The bootstrap is self-applying.
- **The rule does not address the audit method.** *How* citations are verified at audit time (sampling, exhaustive verification, automated linting, etc.) is QA-scope — explicitly out of scope for this ADR. The rule guarantees the *property*; the audit method is downstream.
- **The bibliography is intentionally finite and expandable.** `bibliography/sources/` is not a closed set. Adding a source is a substrate change; once added, the source moves from tier-2 to tier-1 and existing citations to it can be promoted. The framework anticipates growth of the audited bibliography over time.

## Alternatives considered

- **No citation requirement; trust the author.** Rejected. Defeats the entire defensibility property the framework claims; reduces SEM-IA to opinion-ware; makes the TFM defense unwinnable.
- **Citation required but no flagging convention for out-of-bibliography work.** Rejected. Either bans useful frameworks (Cagan books directly, Nygard ADRs, etc.) or smuggles them in as silent authority. The framework would lose either honesty or usefulness.
- **Footnote-style or BibTeX-style citation database in a separate file.** Rejected. Inline parenthetical references are lower-friction; the audit benefit of an external bibliographic database does not justify the maintenance overhead at this scale. The current `bibliography/skill-references.md` provides the per-skill traceability index that an external DB would otherwise provide.
- **Anchored citations only — forbid any out-of-bibliography reference.** Rejected. Forbids ADRs themselves (Nygard is not in the bibliography), Cagan principles cited via the books rather than the handouts, SMART, Lean Startup, etc. The framework would lose access to ~30% of its conceptual scaffolding.
- **Automated citation linter as a hard gate.** Deferred. Useful — catches uncited authoritative claims at commit time — but the current discipline is enforced socially through skill templates and review. A linter is a *strengthening* of this ADR, not an alternative; it remains a candidate improvement.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Materially affected. The substrate has a dedicated `bibliography/` directory at repo root, holding the audited sources, the navigable index, and the per-skill traceability record. This is a top-level structural component of the framework.
- **2. Data structure:** Materially affected. Citation references follow a constrained inline pattern (`(Source short-ref, p. N)` / `(GISF <pdf> slide N)`); skill `## Source` sections carry a defined structure; out-of-bibliography flags follow a recognisable pattern. The citation format is part of the framework's data architecture.
- **3. Interfaces to outside world:** Materially affected. The interface to the external auditor (TFM tribunal, future reader, peer reviewer) is the citation property itself. The auditor reads any authoritative claim, follows the inline reference, opens `bibliography/sources/<pdf>`, and verifies. The interface is the citation pattern + the bibliography directory.
- **4. Decomposition into functional components:** Affected. The audited bibliography (tier-1) and the body of out-of-bibliography conventions (tier-2) are two functional components of the framework's source layer. The flagging discipline is the third — the demarcation mechanism between them.
- **5. Linkage / information transmission among components:** Materially affected. The citation linkage is the channel that transmits *epistemic warrant* from primary sources to skills to agents to nodes. Without it the chain has no warrant; every authoritative claim would be a free-floating assertion.
- **6. Performance attributes:** Not materially affected. Citation parsing is grep-cheap; the audit operation is O(claims). At the framework's scale this is uninteresting. Not applicable.
- **7. Security attributes:** Indirectly affected. Citations are the framework's analogue of "code provenance" — a reviewer can trace every authoritative claim to its origin. This is parallel to supply-chain security in software: knowing where a claim came from is the first line of defense against unsourced or fabricated authority (an LLM-specific risk).

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics, used here as the audit grid; the Architect skill's "Citation is mandatory" gotcha derives from this.
- CLAUDE.md § *Operating principles* (principle 2: *"Citation is mandatory"*) and § *Skills convention* (*"Citation mandate"* paragraph) — the substrate that operationalises this decision.
- `bibliography/sources/` — the tier-1 source directory; `bibliography/INDEX.md` — the navigable map; `bibliography/skill-references.md` — the per-skill traceability record.
- `.claude/templates/SKILL.md.template` — template-level encoding of the citation discipline.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**; adopted as convention. The fact that this very ADR uses an out-of-bibliography format is itself an instance of the flagging rule in force.
- Capability anchor: [[cap-08-citation-discipline]] (the property this decision materialises).
