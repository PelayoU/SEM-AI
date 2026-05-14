---
category: adr
id: adr-<NNN>-<slug>
parent:
artifacts:
  # Optional. List of substrate paths this decision materially affects (e.g., agent identity, skill catalog, template, command).
  # Omit for paradigm-level decisions that affect the framework as a whole without a single artefact owner.
  # See CLAUDE.md § Substrate traceability for the rule.
  # - "[[CLAUDE.md]]"
  # - "[[.claude/agents/<role>.md]]"
status: proposed
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
supersedes:
superseded-by:
---

# ADR <NNN> — <decision title>

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

> Also reflected in frontmatter:
>
> - **proposed** — drafted, not yet agreed.
> - **accepted** — agreed by stakeholders.
> - **superseded** — replaced by a later ADR (fill `superseded-by:` in frontmatter).
> - **deprecated** — no longer applies (no replacement).

## Context

> The situation that motivates the decision. Value-neutral, descriptive. Capture the forces in tension (technical, organisational, regulatory, local) without taking sides yet.

## Decision

> What we decided to do. Active voice, present tense, complete sentences. *"We adopt X.", "We migrate to Y."* Mandatory section.

## Consequences

> The context that results after applying the decision. Honest in all three directions.

**Positive:**

**Negative:**

**Neutral:**

## Alternatives considered

> Other options evaluated and why each was rejected. Without this, the ADR loses audit value.

- **Alternative 1:** description + reason for rejection.
- **Alternative 2:**

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

> Identify which of the seven architectural topics this ADR materially affects. Surface the trade-offs the decision makes against each.

- **1. Overall structure:** <…>
- **2. Data structure:** <…>
- **3. Interfaces to outside world:** <…>
- **4. Decomposition into functional components:** <…>
- **5. Linkage / information transmission among components:** <…>
- **6. Performance attributes:** <…>
- **7. Security attributes:** <…>

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics + Table 7-7 size-importance scaling.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**; adopted as convention.
