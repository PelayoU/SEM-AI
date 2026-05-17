---
name: product-manager-goals
description: "Create, refine, and validate product goals under an existing vision using the SMART framework and the multilevel-planning horizons (Roadmap, Release, Iteration). Use whenever the human wants to draft a goal, audit an existing goal, decide whether goals still serve the vision, derive goals from a 'why stack', or set planning horizons. Triggers include phrases like 'product goal', 'goal for this quarter', 'release goal', 'objective', 'are these SMART?', 'is this goal aligned with the vision?', 'why are we doing this?'."
---

# product-manager-goals

## Purpose

A product goal expresses a high-level outcome the product should achieve — value for users, value for the business, or both — in a way that is specific, measurable, and time-bounded. This skill lets the Product Manager draft, refine, or audit goals so they descend cleanly from the vision, drive capability discovery downstream, and remain testable instead of decaying into aspirational text.

## When this skill applies

- A vision is set and goals must be derived from it.
- A goal exists but reads as vague, aspirational, or unmeasurable.
- The team feels lost between vision and capabilities and the gap is goal-shaped.
- A planning horizon (roadmap, release, iteration) needs explicit goals attached.
- A capability proposal cannot point to a parent goal — surface this as a missing-goal problem first.

## Formal criteria

A goal passes review only if all of the following hold:

1. **Hierarchical anchoring** — a goal is a high-level outcome to achieve with the product (value to users, value to business, or both). It is one level below the vision and one above capabilities. If it reads as a capability or a feature, it is misclassified.
2. **Parent vision exists and is referenced** — every goal explicitly names its parent vision. Orphan goals are forbidden.
3. **SMART** — the goal is **S**pecific, **M**easurable, **A**chievable, **R**elevant to the vision, and **T**ime-bound. Each letter is checked explicitly, not assumed.
4. **Horizon declared** — the goal sits at one of three planning horizons:
   - **Roadmap goal** — 1 to 2 years, focus on vision / product evolution.
   - **Release goal** — 2 to 9 months, focus on the best value within constraints.
   - **Iteration goal** — 1 to 4 weeks, focus on features to deliver now.
   Without a horizon, "achievable" and "time-bound" cannot be validated.
5. **Stakeholder framing** — the goal is expressible in the form *"In order to [GOAL] as [STAKEHOLDER] I want [capability set]"*. A goal that cannot name the stakeholder is upstream of the wrong audience.
6. **Why-stack defensible** — asking "why?" against the goal lands on a node of the vision, not on another goal. If "why?" keeps producing other goals, the chain is collapsed and the real goal sits higher.

## How you proceed

You scaffold the human's authoring; you do not generate goals from thin air.

1. **Confirm the parent vision is active.** Locate the current vision artifact. If multiple visions exist, ask which one is the parent before proceeding — a goal without an unambiguous parent corrupts the hierarchy.
2. **Ask for the stakeholder before the goal text.** The stakeholder is a constituent of the goal, not metadata. Without it, SMART degenerates.
3. **Run the why-stack.** Take the human's first draft and ask "why?" two or three times. Stop when the answer is the vision (correct depth) or when the answer keeps yielding more goals (the original was too shallow — promote it).
4. **Pick a horizon explicitly** before checking SMART. A two-year roadmap goal and a two-week iteration goal both pass SMART but with different measurability bars.
5. **Run the SMART pass.** For each letter, ask:
   - **S** — Is the population, scope, and outcome bounded?
   - **M** — What numeric or boolean check confirms the goal was hit?
   - **A** — Given current team velocity and constraints, is this hittable within the horizon?
   - **R** — Does this goal advance the vision? If the vision had to retire one goal, would it be this one or another?
   - **T** — What is the deadline implied by the horizon?
6. **Restate the goal in the "In order to … as … I want …" form** and read it back to the human. If they cannot recall the SMART check ten minutes later, simplify.

## Pitfalls to avoid

- **Confusing goals with capabilities.** *"Users can checkout with one click"* is a capability. The goal is the outcome that the one-click checkout serves — e.g., reduce cart abandonment.
- **Skipping the horizon.** A goal without a horizon cannot be measurable; "Time-bound" collapses and SMART becomes SMAR.
- **Goal-stacking instead of why-stacking.** If popping "why?" keeps producing goals, you are not at the real goal yet — keep going until you hit the vision.
- **SMART without numbers.** "Improve user satisfaction" is not measurable; "raise NPS from 32 to 45 within Q3" is. Refuse to mark M as passing on adjectives alone.