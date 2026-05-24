---
name: node-templates
description: "The canonical body templates for the seven Issue Types the framework recognises — vision, goal, capability, feature, story, spec, adr — plus the per-section pointers to whichever project methodology skill (if any) is supplied to fill each section. Use whenever a node is being created or audited for structural completeness: 'create a capability', 'new vision', 'start a goal', 'scaffold this feature', 'what sections does a spec need', 'node template', 'is this node complete', 'open an ADR'. This skill gives the shape and the flow; the methodology that fills each section comes from the project's skills or the LLM's training, not from this skill. Concepts that ride on native GitHub objects (bugs as labels, releases as Milestones, code inspections as PR reviews) do not have templates here — they live in their native object."
---

# node-templates

## Purpose

A graph node is not a title with a `parent` edge — it is a living document with a defined section structure. This skill is the single place where that structure lives for every Issue Type the framework recognises. Each template states the node's body sections in the order they should be filled, and a `→ method:` pointer per section to whichever methodology skill is currently supplying the depth. The template is the **shape and the flow**; it does not duplicate methodology depth — that comes from the project's methodology skills (if any are installed under `.claude/skills/`) or from the LLM's training, never from this skill.

This dissolves two problems at once: there is no orphan analysis (every analytical artifact is a section of the node it analyzes, so the framework's "no artifact without a node" rule is satisfied structurally), and there is no node-type proliferation — delivery artifacts that span many capabilities live in the **Milestone body** (a native GitHub object outside this skill's scope), not duplicated into capability Issues nor modelled as an extra Issue Type.

## When this skill applies

- A node of one of the seven Issue Types is being created and needs its skeleton.
- An existing node is being audited for structural completeness ("does this capability have its value and risk sections?").
- A reviewer needs to know which methodology skill (if any) owns a given section.
- The boundary question arises: "is this a section of a capability, or a Milestone-level delivery artifact?".

## What this skill does NOT cover

Concepts the framework cares about that **don't** get a template here, because they ride on native GitHub objects:

- **Bug** — a normal Issue with label `bug`. Body is free-form per the project's bug-reporting habit. No section template imposed by the framework.
- **Release planning** — a **GitHub Milestone** with a markdown body. The Milestone body carries Scope / Sizing / Estimate / Risk register / Quality gate / Security gate / Pipeline. The MCP exposes `create_milestone` / `assign_to_milestone` / `publish_release` bridges. The Milestone body sections are operational, not architectural — they don't get a template here.
- **Code inspection** — a **PR review**. The reviewer's threaded line comments are the inspection record; no separate Issue, no template.
- **Spec / ADR inspection** — comments on the inspected Issue itself + label `inspected` when complete. The comment thread is the record; defects raised are opened as separate `bug`-labelled Issues linked from the thread.
- **Quantitative measurements** — CI artifacts, codecov, sonar, dashboards. Numbers don't live in the graph and don't get a template.

If a node-shaped artifact you're asked to scaffold falls into one of these, you don't pick a template — you use the native object directly.

## How to use a template

1. **Pick the template by node type.** Open the Issue with the matching Issue Type (the engine MCP's `create_node(type=…)` does this), set the sub-issue link to the parent, and instantiate the body section skeleton verbatim into the Issue body.
2. **Fill each section via its pointed methodology.** The section order *is* the flow; the `→ method:` pointer *is* the orchestration. Look up the named methodology skill in the Skill listing; if it matches, invoke it. If no methodology skill matches the pointer, fill the section from training and name the method out loud (so the human can accept or substitute).
3. **Sections are method-driven, not freeform.** Do not invent sections; do not skip mandatory ones silently.
4. **A non-applicable optional section is marked, not deleted:** leave the header and write `N/A — <one-line reason>`. This keeps audits one-glance.
5. **Respect granularity.** If the thing you are documenting spans many capabilities (a plan, an estimate, a benchmark, a risk register, a user-involvement plan), it is **not** a capability section — it belongs in the Milestone body. Cross-cutting risks live in the Milestone's Risk register section; capability nodes reference the Milestone, they don't copy the register.
6. **Anchor pending — when the parent hasn't crystallized yet.** When you create a node bottom-up (a feature that emerged from user signals before its capability is named, a capability that emerged from feature patterns before its goal is named), set `parent` to the closest meaningful ancestor that already exists, keep that parent in `status: draft`, and write `anchor pending` in the Map section's `- Parent:` line. The parent link is provisional and will be corrected via `update_node` when the higher level crystallizes. This is the bottom-up half of the hierarchical loop; it is the normal way capabilities emerge from feature patterns and goals from capability patterns, not an exception.

## How node fields map to GitHub Issue mechanisms

Every node lives as a GitHub Issue. Templates below describe the **body** — the sections inside the Issue text. Per-concept "frontmatter" is replaced by native Issue mechanisms set by the engine MCP at write time (not by the agent typing them into the body):

| Concept | Mechanism — set by engine on `create_node` / `update_node` |
|---|---|
| `type` | **Issue Type** (single-select, native) |
| `parent` | **sub-issue** native link (one only — secondary links go to `related`) |
| `related` | **Related** custom field (multi-issue-reference) + native cross-references in the body (`#42`) |
| `status` | **Status** custom field on the Projects v2 board; engine enforces per-type valid set |
| `created` / `updated` | native Issue timestamps |
| `maintained_by_role` | label `role:<role-id>` set from the `acting_role` parameter |
| `labels` | native Issue labels |
| `supersedes` / `superseded-by` | **Supersedes** / **Superseded by** custom fields (available on every type; canonical use is `adr`) |
| `artifacts` | derived from PRs that close the Issue (`Closes #N`) — never typed in by the agent |
| Milestone assignment | native Milestone field — set by `assign_to_milestone`, not typed in the body |

The agent **does not type these into the body**. The engine MCP sets each at write time from the call's arguments. The body is the sections below.

## Templates

### vision  → method: project's vision methodology skill, if any; else from training

Root node — no `parent`. Single vision is the graph root.

```
## Map                  # read-time index, queried from sub-issues + Related — NOT authoritative; the sub-issue link is the only true edge
- Children: this vision's goals
- Related:  cross-axis links, if any
## Why                                            # the deeper reason the product exists
## The future as a context                        # the world the product is being built into; product absent on purpose
## The future product story                       # product inserted into that future
## One-breath narrative                           # repeatable by everyone
## Positioning                                    # target customer, need, category, key benefit, primary differentiation
## Value ambition                                 # the outcomes that define this vision as REALIZED — multi-dimensional success (cross-reference Holistic dimensions); quantifiable when possible, qualitative otherwise. NOT a forecast or commitment — the polar star the work navigates toward. The destination of the value chain. The Maximum Viable Value the team pursues, where 'viable' constrains the ambition to what is technically/economically/operationally reachable.
## Horizon                                        # planning horizon, explicit
## Adopted trends                                 # trends believed to hold over the horizon
## Holistic dimensions                            # each slot is a DESIGN slot AND a RISK-SURFACE slot — silent omission = absorbed risk. Mapping: Monetization↔value risk · UX design↔usability risk · Technology↔viability risk · Acquisition+Offline↔business viability risk. Every slot is considered; N/A only with one-line reason.
- Functionality:        the product's core reason for being
- Technology:           technical posture the vision commits to    → consult: architect
- UX design:            the experience posture (PM in small teams; UX Designer if project ships one)
- Monetization:         how the vision creates and captures economic value
- Acquisition:          how the vision reaches users / customers
- Offline experience:   off-screen experiences essential to deliver the value
```

### goal  → method: project's goal methodology skill, if any; else from training

`parent:` the vision (sub-issue link).

```
## Map                  # read-time index, queried — NOT authoritative; the sub-issue link is the only true edge
- Children: this goal's capabilities
- Related:  constraining adr; the Milestone(s) delivering toward this goal
## Outcome statement                              # the measurable OUTCOME (behavioral / system change observable in the world) this goal asserts. NOT an output (a thing to be built). Mis-stated: "Ship feature X" — that's an output. Well-stated: "X% of users do Y differently". Output / outcome / benefit / value are distinct layers of the value chain.
## Stakeholder                                    # WHO benefits if this goal is realized. Concrete role + context (e.g. "Adopter team's PM + developers", "Solo developer + enterprise PM"). Names the WHO of the template "In order to [outcome], as [STAKEHOLDER], I want { capabilities }". Goals that cannot name a stakeholder are usually solutions in disguise — pop the why-stack until a real beneficiary surfaces.
## Parent vision                                  # explicit reference (sub-issue link)
## Horizon                                        # planning horizon — roadmap / release / iteration scoped. SMART criterion T (Time-bound): continuous / steady-state goals must still name at least one checkpoint (e.g. "by v1.0", "audited quarterly from Q1-2027").
## Acceptance check                               # criteria by which this goal is judged done. SMART criterion M (Measurable) + T (Time-bound): includes a checkpoint condition tied to a release / date / cadence, not just a steady-state property.
## Why this goal                                  # the chain from the vision down to this goal
## Holistic dimensions                            # the outcome this goal pursues in each dimension. Each slot is DESIGN + RISK SURFACE; silent omission = absorbed risk. N/A only with one-line reason.
- Functionality:        functional outcome
- Technology:           technical outcome           → consult: architect
- UX design:            experience outcome
- Monetization:         economic outcome
- Acquisition:          adoption / growth outcome
- Offline experience:   off-screen outcome
```

### capability  → method: project's capability methodology skill, if any; else from training

`parent:` a goal (sub-issue link).

```
## Map                  # read-time index, queried — NOT authoritative; the sub-issue link is the only true edge
- Children: this capability's features
- Related:  constraining adr; the Milestone(s) whose scope includes it; affine spec
## Statement                                      # what the system enables, implementation-agnostic
## Parent goal                                    # explicit reference (sub-issue link)
## Two implementations                            # name two plausible ones — the agnostic test
## Value analysis            → method: project's value-analysis skill, if any
## Risks                     → method: project's risk-analysis skill, if any   # cross-cutting risks go in the Milestone's Risk register, not here
## Go / No-Go                                     # decision and one-line reason
## Holistic dimensions                            # what this capability does in each dimension. Each slot is DESIGN + RISK SURFACE; silent omission = absorbed risk. N/A only with one-line reason.
- Functionality:        what the capability does, functionally
- Technology:           technical components and posture            → consult: architect
- UX design:            experience this capability surfaces or relies on
- Monetization:         contribution to economic value
- Acquisition:          contribution to reaching / retaining users
- Offline experience:   off-screen experience this capability requires or affects
## Feature decomposition     → method: project's feature-decomposition skill, if any   # only for Go capabilities
```

### feature / story  → method: project's feature-decomposition skill, if any; else from training

`parent:` a capability (feature) or a feature (story = sub-task granularity). Same template, smaller scope at story level. The Holistic dimensions and Value chain sections apply to **feature**; at **story** granularity, the dimensions manifest in the Acceptance check and value lives at the parent feature level — sections dropped at story scope.

```
## Map                  # read-time index, queried — NOT authoritative; the sub-issue link is the only true edge
- Children: this feature's stories (none if a leaf story)
- Related:  its spec; constraining adr
## Story                                          # role, need, benefit — phrased per the project's chosen story format
## Uncertainty addressed                          # OPTIONAL — feature only (story drops this). The unknown this cycle resolves (free-form prose). N/A — delivery, not experiment ← legitimate when this feature pays off learning already accumulated. Populated → primary intent is experimental: the cycle's success is judged by whether the uncertainty is resolved (Learning extracted in Value chain), value chain completion is a bonus. The engine MCP applies the native label `experiment` automatically when this slot is populated (and removes it if the slot is cleared to N/A) — visibility from the Issue list / Projects v2 / `gh issue list`. An experiment names which holistic dimension(s) it tests — that mapping IS the risk class it validates (Monetization↔value risk · UX design↔usability risk · Technology↔viability risk · Acquisition+Offline↔business viability risk). Expected final status by sub-type: PROTOTYPE (landing page / mockup / smoke test / concierge — discardable artifact) → `deprecated` always; if the prototype validated the idea, open a new `delivery` feature with `related` link back. SPIKE (technical/design feasibility) → usually `deprecated`, can be `done` if output is light and useful. A/B TEST → `done` (winning variant stays). CONCIERGE (humans doing what software would) → `deprecated` after learning extracted; automation opens as new delivery feature.
## Conditions of satisfaction                     # the back of the card
## Acceptance check                               # criteria by which the output is judged complete (output-layer, not value-layer)
## Position in the larger narrative               # where this fits in the user's flow
## State                                          # where in the lifecycle the conversation/construction sits
## Holistic dimensions                            # FEATURE ONLY (story drops this). How this feature manifests in each dimension. Each slot is DESIGN + RISK SURFACE: Monetization↔value risk · UX design↔usability risk · Technology↔viability risk · Acquisition+Offline↔business viability risk. Silent omission = absorbed risk; mark N/A only with explicit reason.
- Functionality:        what the feature does, functionally
- Technology:           technical components touched                → consult: architect
- UX design:            UX surfaces / flows / copy this feature affects
- Monetization:         economic effect of this feature
- Acquisition:          acquisition / retention effect
- Offline experience:   off-screen effect (support load, logistics, partner impact, …)
## Requirements detail        → method: project's requirements-discovery skill, if any   # when this opens a new feature area
## Spec                       → method: project's spec methodology skill, if any
## Value chain                                    # FEATURE ONLY, post-done. The chain is PROBABILISTIC — most cycles do not complete it fully; honesty matters more than theatre.
- Outputs shipped:        what was actually built (often auto-filled from PRs that closed this Issue)
- Outcomes observed:      behavioral change observed in users / system (or 'none — users did not adopt as expected')
- Benefits measured:      metric movements caused by the outcome (or 'none — outcome did not move the metrics it should have moved'); reference the relevant Holistic dimension(s)
- Value assessment:       honest benefit-to-cost ratio. May be negative. The framework asks for honesty, not celebratory reporting.
- Learning extracted:     what this cycle taught regardless of whether value materialized. THIS IS THE GUARANTEED OUTPUT OF EVERY CYCLE — never N/A; always populate.
- Next cards surfaced:    new Issues this evaluation spawned (deprecate this feature? pivot via supersede? double down? new experiment?)
```

### spec  → method: project's spec methodology skill, if any; else from training

`parent:` a feature (sub-issue link).

```
## Map                  # read-time index, queried — NOT authoritative; the sub-issue link is the only true edge
- Children: none (leaf)
- Related:  constraining adr; affine spec
## Acceptance Criteria                            # AC-A1, AC-A2, … one human sentence each, traceable to story
## Scenarios                                      # concrete examples — Given / When / Then or whatever notation the project's methodology supplies
## Story → AC traceability                        # every scenario maps to a story id
```

### adr  → method: project's architecture-decision methodology skill, if any; else from training

`parent:` the spine node whose scope the decision serves (sub-issue link). `supersedes` / `superseded-by` chains are kept in the namesake custom fields, never in the body.

```
## Map                  # read-time index, queried — NOT authoritative; the sub-issue link is the only true edge
- Parent:   the spine node this decision constrains
- Related:  the affine specs / features / other adrs this decision touches
## Status                                         # proposed | accepted | superseded | deprecated (mirrors the Status field — included in body for offline readers)
## Context                                        # what forces are at play; why this needs a decision
## Decision                                       # the chosen direction, stated as the team's commitment
## Consequences                                   # what becomes easier; what becomes harder; what is now locked in
## Security attributes        → method: project's security-attributes skill, if any   # contributed by Security Officer via consult; silence here is a defect
## Alternatives considered                        # the options weighed and not chosen, with reasoning
```

## Pitfalls to avoid

- **Treating the template as a replacement for the methodology.** The template gives shape and order. *How* to do value analysis well comes from the project's methodology skill (if any) or LLM training, not from this skill.
- **Duplicating Milestone-level artifacts into capability nodes.** The plan, the estimate, the benchmark, the risk register, the user-involvement plan are Milestone-scoped — they live in the **Milestone body**, not in capability Issues. A capability links to the Milestone; it does not own a copy of the register.
- **Inventing sections.** If a node seems to need a section no template defines, that is a signal to revise the template here (one place), not to fork the node structure ad hoc.
- **Deleting non-applicable sections.** Mark `N/A — reason`. A deleted section is indistinguishable from a forgotten one at audit.
- **Filling sections out of order.** The order encodes precedence (value before Go/No-Go before decomposition). Skipping ahead reproduces the failure modes the methodology exists to prevent.
- **Typing the "frontmatter" concepts into the body.** `type` / `parent` / `status` / `related` / Milestone assignment / etc. are not body text — they are native Issue mechanisms set by the engine MCP on write. The body is the sections above, nothing else.
- **Scaffolding a template for a concept that lives natively.** If the work is opening a bug, planning a release, reviewing code, recording an inspection, or logging a measurement — *don't* reach for a template here. Use the native GitHub object directly: label `bug`, Milestone + Release, PR review, comment on the inspected Issue, CI tool.
- **Naming a methodology skill that does not exist in the Skill listing.** A `→ method:` pointer is a *suggestion of where the depth should come from*. If the project does not install a skill matching the pointer, fill from training and name the method out loud — never invent a skill name.
