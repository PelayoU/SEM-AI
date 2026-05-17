---
name: product-manager-capabilities
description: "Derive, refine, and validate product capabilities under a goal, keeping them implementation-agnostic and filterable into an MVP. Use whenever the human wants to brainstorm capabilities, audit an existing capability list, decide what gets into the MVP vs later versions, or check whether a 'capability' is actually a feature in disguise. Triggers include phrases like 'product capability', 'what should the product do', 'capability list', 'MVP scope', 'Go/No-go on this capability', 'is this a capability or a feature?'."
---

# product-manager-capabilities

## Purpose

A product capability is what the product enables a stakeholder to do, expressed without committing to a particular implementation. This skill lets the Product Manager derive capabilities from a goal, separate capabilities from features (the most common confusion in practice), and pass them through the capability-filtering gate that produces the MVP. Without this discipline, teams jump from goal to feature and lock implementation choices before they should.

## When this skill applies

- A goal is established and the team needs the capability set beneath it.
- An existing capability reads as a feature ("button that does X") rather than a capability.
- The MVP scope is being negotiated and capabilities need a Go / No-go filter.
- A feature proposal cannot point to a parent capability — surface this as a missing-capability problem first.
- A capability appears to duplicate or compete with another — the catalog needs deduplication.

## Formal criteria

A capability passes review only if all of the following hold:

1. **Canonical definition** — a capability gives a stakeholder the ability to achieve a goal or fulfil a task, *regardless of implementation*, and must not imply one. If the text names a UI element, a screen, an API endpoint, or a specific technology, it is a feature, not a capability.
2. **Parent goal exists and is referenced** — every capability explicitly names its parent goal. Orphan capabilities are forbidden.
3. **Stakeholder framing** — capabilities are listed as *"In order to [GOAL] as [STAKEHOLDER] I want { capability, capability, … }"*. The capability names an ability the stakeholder gains, not a step the system takes.
4. **Implementation-agnostic** — two valid implementations of the same capability must be conceivable. *"Coinless hypermarket trolley"* is a capability; *"NFC-unlocked trolley"* is one possible implementation of it.
5. **Filterable into the MVP** — the capability can be assigned a Go or No-go via the four-risks discriminator (see *How you proceed*). Capabilities that resist Go/No-go are usually several capabilities glued together; split them.
6. **Non-overlapping with siblings** — two capabilities under the same goal should be independently doable. Heavy overlap means a duplicate, or a missing parent capability.
7. **Decomposable into features** — a capability that cannot be expressed as one or more features is too abstract (closer to a goal) or trivially small (closer to a feature).

## How you proceed

1. **Confirm the parent goal is active and SMART.** A capability beneath a fuzzy goal inherits the fuzziness; if the goal is weak, go back to `product-manager-goals` first.
2. **Ask for the stakeholder explicitly.** Different stakeholders under the same goal often produce different capability sets.
3. **Brainstorm in the stakeholder form, plural.** Generate the set as *"In order to [GOAL] as [STAKEHOLDER] I want { … }"*. Stay above implementation; if a candidate names a UI, technology, or step, reformulate it as the ability it grants.
4. **Run the implementation-agnostic test.** For each capability, name two plausible implementations. If only one comes to mind, it is probably a feature.
5. **Pass each through the MVP Go/No-go filter, discriminating with Cagan's four product risks:** *value* — will customers buy or choose it? *usability* — can they figure out how to use it? *feasibility* — can we build it with the time, skills and technology we have? *business viability* — does it work for the business (legal, financial, brand, sales, ethics)? A capability that retires a high *value* (or other high) risk goes into the MVP; one that only postpones risk to V1/V2 is deferred.
6. **Deduplicate.** If two capabilities under the same goal could ship together with nothing user-facing changing, merge them. If they conflict, surface the conflict to the human before continuing.
7. **Record the Go/No-go decision in the capability node**, with a one-line reason. Feature decomposition only operates on Go capabilities.

## Pitfalls to avoid

- **Treating UI elements as capabilities.** *"Login button"* is not a capability; *"customer can authenticate"* is. The button is one feature implementing the capability.
- **Restating the goal as the capability.** If the capability text is paraphrased goal text, it is at the wrong level — push down, or surface that the goal already covers it.
- **Pre-committing implementation in the capability name.** *"OAuth login"* names a protocol; *"customer can authenticate using their existing identity provider"* names the ability. The former locks design; the latter leaves it open.
- **Skipping the MVP filter.** A capability without a Go/No-go decision silently ends up in scope through feature work. Decide before decomposing.