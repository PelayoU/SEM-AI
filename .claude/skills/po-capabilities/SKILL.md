---
name: po-capabilities
description: "Derive, refine, and validate product capabilities under a goal, keeping them implementation-agnostic and filterable into an MVP. Use whenever the human wants to brainstorm capabilities, audit an existing capability list, decide what gets into the MVP vs later versions, or check whether a 'capability' is actually a feature in disguise. Triggers include phrases like 'product capability', 'what should the product do', 'capability list', 'MVP scope', 'Go/No-go on this capability', 'is this a capability or a feature?'."
---

# po-capabilities

## Purpose

A product capability is what the product enables a stakeholder to do, expressed without committing to a particular implementation. This skill lets the Product Owner derive capabilities from a goal, separate capabilities from features (the most common confusion in practice), and pass them through the capability-filtering gate that produces the MVP. Without this discipline, teams jump from goal to feature and lock implementation choices before they should.

## When this skill applies

- A goal is established and the team needs the capability set beneath it.
- An existing capability reads as a feature ("button that does X") rather than a capability.
- The MVP scope is being negotiated and capabilities need a Go / No-go filter.
- A feature proposal cannot point to a parent capability — surface this as a missing-capability problem first.
- A capability appears to duplicate or compete with another — the catalog needs deduplication.

## Formal criteria

A capability passes review only if all of the following hold:

1. **Canonical definition** *(GISF `gisf-life-cycle.pdf` slide 54)* — *"Capability: gives stakeholders the ability to achieve some goal or fulfill some task, regardless of implementation. Don't imply a particular implementation."* If the text names a UI element, a screen, an API endpoint, or a specific technology, it is a feature, not a capability.
2. **Parent goal exists and is referenced** — every capability explicitly names its parent goal. Orphan capabilities are forbidden.
3. **Stakeholder framing** *(GISF `gisf-discovery.pdf` slides 98–99)* — capabilities are listed using *"In order to [GOAL] as [STAKEHOLDER] I want { capability, capability, … }"*. The capability must name an ability the stakeholder gains, not a step the system takes.
4. **Implementation-agnostic** — two valid implementations of the same capability must be conceivable. Example: *"coinless hypermarket trolley"* (slide 98) is a capability; *"NFC-unlocked trolley"* is one possible implementation of it.
5. **Filterable** *(GISF `gisf-life-cycle.pdf` slide 69)* — the capability can be assigned a Go or No-go for the MVP. Capabilities that resist Go/No-go are usually multiple capabilities glued together; split them.
6. **Non-overlapping with siblings** — two capabilities under the same goal should be doable independently. Heavy overlap suggests either a duplicate or a missing parent capability.
7. **Decomposable into features** — a capability that cannot be expressed as one or more features is either too abstract (closer to a goal) or trivially small (closer to a feature).

## How you proceed

1. **Confirm the parent goal is active and SMART.** A capability beneath a fuzzy goal inherits the fuzziness; if the goal is weak, go back to `po-goals` before continuing.
2. **Ask for the stakeholder explicitly.** Different stakeholders under the same goal often produce different capability sets. *"As Rapid Young Customer"* and *"As Family Buyer"* may need different capabilities under the same easy-buying goal.
3. **Brainstorm in the slide-95 form, plural.** Generate the capability set as a comma-separated list in *"In order to [GOAL] as [STAKEHOLDER] I want { … }"*. Stay above implementation. If a candidate names a UI, technology, or step, reformulate as the ability it grants.
4. **Run the implementation-agnostic test.** For each capability, name two plausible implementations. If only one comes to mind, the candidate is probably a feature.
5. **Pass each through the Go / No-go filter for the MVP** *(slide 69)*. Use the Cagan four-risks lens captured on slide 64 (value, usability, viability, business viability) as the discriminator: capabilities that resolve a high-value risk go into the MVP; capabilities that postpone risk to V1/V2 are deferred.
6. **Deduplicate.** If two capabilities under the same goal could ship together without changing anything user-facing, merge them. If they conflict, surface the conflict to the human before continuing.
7. **Record the Go/No-go decision in the capability node**, with a one-line reason. Future feature decomposition only operates on Go capabilities.

## Pitfalls to avoid

- **Treating UI elements as capabilities.** *"Login button"* is not a capability; *"customer can authenticate"* is. The button is one feature implementing the capability.
- **Restating the goal as the capability.** If the capability text is paraphrased goal text, it is at the wrong level — push down or surface that the goal already covers it.
- **Pre-committing implementation in the capability name.** *"OAuth login"* names a protocol; *"customer can authenticate using their existing identity provider"* names the ability. The former locks design; the latter leaves design open.
- **Skipping the MVP filter.** A capability without a Go/No-go decision will silently end up in scope through feature work. Decide before decomposing.
- **Inheriting frameworks not in audited bibliography.** Earlier drafts cited Torres's Opportunity Solution Tree, Rumelt, and Christensen JTBD as criteria for capability derivation — none of these is present in the audited `bibliography/sources/`. Do not cite them as authority here. If the human wants those frameworks, surface the gap before importing.

## Source

- **Canonical definition of *capability*** — GISF UC3M `gisf-life-cycle.pdf` slide 54.
- **Capability filtering → MVP → Go/No-go** — `gisf-life-cycle.pdf` slide 69.
- **Capability listing format ("In order to / as / I want { … }")** — `gisf-discovery.pdf` slides 97–99.
- **Hierarchy Vision → Goals → Capabilities → Features → Stories → AC → Examples** — `gisf-life-cycle.pdf` slide 53 (pyramid); restated in `gisf-delivery-backlog-management.pdf` slide 121.
- **Cagan four risks (used as Go/No-go discriminator)** — Marty Cagan, *Inspired*. Captured in `gisf-life-cycle.pdf` slide 64.
- Full traceability: `bibliography/skill-references.md` § `po-capabilities`.
