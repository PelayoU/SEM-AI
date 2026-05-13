---
category: feature
id: feature-<NNN>-<slug>
parent: "[[cap-NN-slug]]"
status: draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# Feature <NNN> — <short title>

> Authored via `po-feature-decomposition`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54 — *"Features/user stories: what is designed and implemented to deliver capabilities. Pieces of deliverable product functionality."* Features and stories sit at the same level; features group stories. INVEST applies to stories. Story Map hierarchy (Patton via GISF `gisf-delivery-backlog-management.pdf` slide 132): **Activity → Task → Sub-task** — features typically map to Tasks; stories map to Sub-tasks.

## What it delivers

> 1–3 sentences. What the feature lets the user do. The functional contract, not the implementation. Pulled from the parent capability.

## Story Map position (Patton via slide 132)

> - **Activity (Epic)** this feature belongs to: <…>
> - **Task** this feature maps to: <this feature>
> - **Release slice** it sits in: <walking skeleton | thickening release N>

## Stories (children)

> Stories carry an `<id>` letter (A, B, C, …) so their acceptance criteria are traceable in the spec sibling (`story-NNN-A` → `AC-A1`, `AC-A2`, …).

- `[[story-NNN-A-slug]]` — As <role>, I want <action>, so that <benefit>.
- `[[story-NNN-B-slug]]` — <…>
- `[[story-NNN-C-slug]]` — <…>

## Spec sibling

> One Gherkin spec per feature, not per story (Cucumber: *"only a single Feature in a `.feature` file"*; `gherkin-reference.pdf` p. 1). The spec aggregates ACs from all child stories. Authored via `po-spec-gherkin`.

- `[[spec-NNN-slug]]`

## 5 Cs cycle reminder (GISF `gisf-life-cycle.pdf` slide 56 + `agile-story-essentials.pdf`)

> The feature card and its stories are tokens for **Conversation → Confirmation → Construction → Consequences**. The detail emerges through conversation; the spec captures Confirmation; Construction follows; Consequences feed the next loop.

## Notes

> Context, decisions taken during the conversation, open questions, known edge cases.

## Source

- Skill: `po-feature-decomposition`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54 (definition) + slide 56 (5 Cs).
- GISF UC3M `gisf-delivery-backlog-management.pdf` slide 132 (Story Map hierarchy: Activity / Task / Sub-task).
- GISF UC3M `agile-story-essentials.pdf` p. 1 (Card / Conversation / Confirmation / Construction / Consequences; Kent Beck origin).
- Spec contract: see `[[spec-NNN-slug]]` and `gherkin-reference.pdf`.
