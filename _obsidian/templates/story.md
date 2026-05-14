---
category: story
id: story-<NNN>-<X>-<slug>
parent: "[[feature-NNN-slug]]"
artifacts:
  # Optional. List of substrate paths this story exercises (typically inherited from parent feature when concrete).
  # Omit when the story is about an abstract property without a single artefact owner.
  # See CLAUDE.md § Substrate traceability for the rule.
  # - "[[.claude/skills/<role>-<name>/SKILL.md]]"
status: draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# Story <NNN>-<X> — <short title>

> Authored via `po-feature-decomposition`. The letter **\<X\>** (A, B, C, …) traces this story's acceptance criteria in the spec sibling: `story-<NNN>-A` → `AC-A1`, `AC-A2`, …
>
> *"A story is a token for a conversation."* — Kent Beck via Comakers (`agile-story-essentials.pdf` p. 1). The card text is the start; detail emerges through the 5 Cs cycle.

## Cohn statement (GISF `gisf-delivery-backlog-management.pdf` slide 124)

As **\<role\>**,
I want **\<action / capability\>**,
so that **\<benefit\>**.

- **Role:** an actor — a user persona, a stakeholder type, or a system role.
- **Action:** the concrete capability the actor gains.
- **Benefit:** the outcome that links to the parent feature and capability.

## Conditions of Satisfaction (back of card, GISF slide 125)

> Brief, human-readable conditions the team agrees describe *done* for this story. These conditions feed the AC block in the spec sibling, where each becomes one or more numbered `AC-<X>N` Scenarios in Gherkin.

- <condition 1>
- <condition 2>
- <condition 3>

## INVEST self-check (GISF `gisf-delivery-backlog-management.pdf` slide 128)

Mark ✅ / ⚠️ / ❌ with one-line reason:

- **I — Independent:** can be pulled without blocking on a sibling story.
- **N — Negotiable:** card is a token, not the contract; details still open.
- **V — Valuable:** the *so that* clause names a user or business outcome.
- **E — Estimable:** team can size it with reasonable confidence.
- **S — Small:** fits in a single iteration.
- **T — Testable:** at least one observable outcome can confirm done.

## Source

- Skill: `po-feature-decomposition`.
- Cohn story format: GISF UC3M `gisf-delivery-backlog-management.pdf` slide 124. Origin: Mike Cohn, *User Stories Applied* (Addison-Wesley, 2004) — book not in audited `bibliography/sources/`; cited via GISF.
- INVEST: GISF `gisf-delivery-backlog-management.pdf` slide 128. Origin: Bill Wake (2003).
- Conditions of Satisfaction (back of card): GISF slide 125.
- "Token for a conversation" attribution: GISF UC3M `agile-story-essentials.pdf` p. 1 (Kent Beck, late 1990s).
