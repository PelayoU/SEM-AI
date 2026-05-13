---
category: capability
id: cap-<NN>-<slug>
parent: "[[goal-XX-slug]]"
status: draft
mvp: go|no-go
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# Capability <NN> — <short title>

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54 — *"gives stakeholders the ability to achieve some goal or fulfill some task, regardless of implementation. Don't imply a particular implementation."* Capability listing format: GISF `gisf-discovery.pdf` slides 97–99. MVP Go/No-go filter: `gisf-life-cycle.pdf` slide 69. Cagan four-risks discriminator: slide 64.

## Statement (slides 97–99 form)

> In order to **\<parent goal\>** as **\<stakeholder\>** I want **\<this capability — implementation-agnostic ability the stakeholder gains\>**.

## Implementation-agnostic test

> Name two plausible implementations of this capability. If only one comes to mind, the candidate is probably a feature, not a capability.

- Implementation A: <…>
- Implementation B: <…>

## MVP Go / No-go (slide 69 filter)

> Declared in frontmatter as `mvp:`. Use Cagan's four risks (slide 64) as the discriminator:
>
> - **Value risk** — will customers buy / use this?
> - **Usability risk** — can users figure out how to use it?
> - **Viability risk** — can engineers build it with current technology and skills?
> - **Business viability risk** — can sales / marketing / legal / finance cope?

**Decision:** \<go | no-go\> — <one-line rationale>.

## Non-overlap with sibling capabilities

> List sibling capabilities under the same goal. Confirm this capability does not duplicate them. If overlap is significant, merge or split.

- Sibling: `[[cap-NN-…]]` — relation: <independent | adjacent | overlaps>.

## Non-coverage

> What this capability does NOT cover. Explicit boundary.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54 (canonical *capability* definition), slide 69 (Capability filtering → MVP → Go/No-go).
- GISF UC3M `gisf-discovery.pdf` slides 97–99 (capability listing format).
- Cagan four risks captured in `gisf-life-cycle.pdf` slide 64.
