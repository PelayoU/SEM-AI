---
name: product-manager-feature-decomposition
description: "Decompose a capability into features and a feature into stories using INVEST criteria, Patton's User Story Mapping (Activity → Task → Sub-task), and the 5 Cs cycle (Card, Conversation, Confirmation, Construction, Consequences). Use whenever the human wants to break down a capability, slice work into a release, split an oversized story, organize a backlog around narrative flow, or check whether the current stories satisfy INVEST. Triggers include phrases like 'break this down', 'split this story', 'epic vs story', 'thin slice', 'release slice', 'story map', 'INVEST check', 'this story is too big', 'walking skeleton'."
---

# product-manager-feature-decomposition

## Purpose

A capability is what the product enables; a feature is what gets designed and built; a story is the unit a team can pull, discuss, and demonstrate. This skill lets the Product Manager cross those three levels deliberately — using Patton's User Story Mapping for narrative coherence, Cohn's INVEST for individual story quality, and the 5 Cs cycle to remember that the story card is a token for the conversation, not the spec itself. Without this discipline, backlogs become long lists of disconnected tickets and the team loses the user narrative.

## When this skill applies

- A capability is established and the team needs the features beneath it.
- An existing feature is too large for a single iteration.
- A backlog lacks narrative flow — stories appear in arbitrary order.
- A story fails one or more INVEST criteria and needs splitting or merging.
- Release planning needs a "thin slice" — the smallest end-to-end set of tasks that lets target users reach their goal.

## Formal criteria

A decomposition pass is acceptable only if all of the following hold:

1. **Hierarchical anchoring** *(GISF `gisf-life-cycle.pdf` slide 54 and `gisf-delivery-backlog-management.pdf` slide 121)* — features and user stories are at the same level (*"Features/user stories: what is designed and implemented to deliver capabilities. Pieces of deliverable product functionality."*). The parent is always a capability.
2. **Story format** *(GISF `gisf-delivery-backlog-management.pdf` slides 124–125)* — *As a [role], I want [capability], so that [benefit]*. The back of the card carries the *Conditions of Satisfaction*. A story without the *so that* clause fails Valuable in INVEST.
3. **INVEST satisfied** *(GISF `gisf-delivery-backlog-management.pdf` slide 128)* — each story is **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall (sized appropriately), **T**estable. The check is explicit, letter by letter.
4. **Narrative flow on the backbone** *(Patton, *User Story Mapping*, p. 1)* — when a feature decomposes into multiple stories, they sit on a story map's *backbone* (left-to-right is the order you would tell the story about the user). Stories with no narrative position are at risk of being orphans.
5. **Story Map hierarchy** *(GISF slide 132, after Patton)* — Activity (Epic) → Task (Theme) → Sub-task (User Story). Use this to test whether a so-called "story" is actually an epic. Activities and tasks are the *backbone*; sub-tasks are the *ribs*.
6. **5 Cs honored** *(GISF `gisf-life-cycle.pdf` slide 56 + `agile-story-essentials.pdf` p. 1)* — the workflow is **C**ard (write the story), **C**onversation (discuss with team), **C**onfirmation (agree on acceptance test before building), **C**onstruction (build), **C**onsequences (learn from working software). Skipping Confirmation produces stories that pass build and fail review.
7. **Release slices are thin and viable** *(Patton, p. 1)* — the smallest number of tasks that lets the target user reach their goal composes a viable release. Slices are horizontal across the backbone, not vertical chunks of one activity.

## How you proceed

1. **Confirm the parent capability is Go for MVP.** Decomposing a No-go capability is wasted effort. If the Go/No-go is missing, go back to `product-manager-capabilities`.
2. **Frame the story** *(Patton p. 2, step 1)* — name the product/feature, who uses it, why this work matters. Without the frame, decomposition drifts.
3. **Map the big picture as a story map.** Lay out the user's activities left-to-right in narrative order (Activity → Task). The backbone is the user's day or workflow at goal level — not the system's modules.
4. **Hang sub-tasks (stories) under each task.** Variations, alternatives, edge cases descend from the backbone. The map quickly shows where the work is concentrated and where it is sparse.
5. **Write each story in the GISF slide-124 format**: *As a [role], I want [capability], so that [benefit]*. Add Conditions of Satisfaction on the back of the card.
6. **Run the INVEST check on each story** *(slide 128)*:
   - **I** — independent enough that the team can pull it without blocking on a sibling.
   - **N** — the details are still negotiable; the card is a token, not the contract.
   - **V** — there is a clear *so that*; the benefit names a user or business outcome.
   - **E** — the team can estimate it. If not, split or do a knowledge-acquisition spike first (PBI type per GISF slide 137).
   - **S** — small enough to fit in one iteration. If it cannot, split.
   - **T** — testable. There is at least one observable outcome that can confirm done. Defer the Gherkin form to `product-manager-spec-gherkin`.
7. **Cut release slices horizontally across the backbone** *(Patton p. 1, "Release Slice")*. A release slice picks the minimum sub-tasks per activity that lets the target user complete the goal end-to-end. This is the walking skeleton; further releases thicken it.
8. **Honor the 5 Cs cycle**. After Card and Conversation, write Confirmation as the acceptance test before Construction begins. Do not let stories go to Construction without Confirmation, even if everyone "knows what we mean".

## Pitfalls to avoid

- **Decomposing vertically into one activity.** A vertical slice — all functionality under "Account Management", nothing under "Checkout" — does not let any real user complete a real workflow. Slice horizontally.
- **Pre-INVEST stories that are actually epics.** "User can manage their account" is an activity, not a story. Use the Activity → Task → Sub-task hierarchy to surface this.
- **Card-as-spec.** Writing every detail on the card defeats the conversation. The card is the token; the spec is the Confirmation (handled by `product-manager-spec-gherkin`).
- **Skipping the *so that* clause.** Stories without an explicit benefit fail Valuable. They survive as "the team wants it" rather than as user value.
- **Story map without narrative order.** A map with arbitrary left-to-right ordering loses its core property — the user's story is not legible. Order is the value.
- **Mixing PBI types into the story format** *(GISF slide 137)*. Defects, technical improvements, knowledge acquisitions are valid PBIs but are not user stories — they do not need INVEST or Conditions of Satisfaction. Tag them by type.

## Source

- **Story format (*As a / I want / so that*)** — Mike Cohn, *User Stories Applied* (Addison-Wesley, 2004). Format captured in GISF UC3M `gisf-delivery-backlog-management.pdf` slide 124.
- **INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)** — Bill Wake (originally 2003). Captured verbatim in `gisf-delivery-backlog-management.pdf` slide 128.
- **5 Cs cycle (Card / Conversation / Confirmation / Construction / Consequences)** — `gisf-life-cycle.pdf` slide 56 (cites Antonio Machado) and `agile-story-essentials.pdf` p. 1 (Patton / Comakers 2013, attributing the conversation-token concept to Kent Beck, late 1990s).
- **User Story Mapping (Activity / Task / Sub-task; narrative flow; release slices)** — Jeff Patton, *User Story Mapping* (O'Reilly, 2014). Concept summary in `user-story-mapping.pdf` pp. 1–2. Hierarchy restated in `gisf-delivery-backlog-management.pdf` slide 132.
- **Product Backlog Item types (Feature, Change, Defect, Technical improvement, Knowledge acquisition)** — `gisf-delivery-backlog-management.pdf` slide 137.
- Full traceability: `bibliography/skill-references.md` § `product-manager-feature-decomposition`.
