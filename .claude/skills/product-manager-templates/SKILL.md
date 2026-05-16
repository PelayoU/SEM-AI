---
name: product-manager-templates
description: "The canonical body templates for every Product Manager graph node — vision, goal, capability, feature/story, spec, and the release/project node — plus the section-by-section pointers to the method skill that fills each section. Use whenever a Product Manager node is being created or audited for structural completeness: 'create a capability', 'new vision', 'start a goal', 'scaffold this feature', 'what sections does a spec need', 'node template', 'is this node complete', 'release node'. This skill gives the shape and the flow; the pointed-to method skills give the depth."
---

# product-manager-templates

## Purpose

A graph node is not a title with a `parent` edge — it is a living document with a defined section structure. This skill is the single place where that structure lives for every Product Manager node type. Each template states the node's frontmatter, its body sections in the order they should be filled, and a `→ método:` pointer per section to the method skill that knows how to fill it well. The template is the **shape and the flow**; it does not duplicate method depth — Cagan's four risks, INVEST, Gherkin, Jones's inventories all stay in their own skills and are reached through the pointers.

This dissolves two problems at once: there is no orphan analysis (every analytical artifact is a section of the node it analyzes, so the framework's "no artifact without a node" rule is satisfied structurally), and there is no node-type proliferation (delivery artifacts that span many capabilities live in the release/project template at the right granularity, not duplicated into every capability).

## When this skill applies

- A Product Manager node is being created and needs its skeleton.
- An existing node is being audited for structural completeness ("does this capability have its value and risk sections?").
- A reviewer needs to know which method skill owns a given section.
- The boundary question arises: "is this a section of a capability, or a release-level artifact?".

## How to use a template

1. **Pick the template by node type.** Instantiate the frontmatter + section skeleton verbatim into the node file (`graph/<type>-<id>-<slug>.md`).
2. **Fill each section via its pointed method skill.** The section order *is* the flow; the `→ método:` pointer *is* the orchestration. You do not need a separate orchestrator — follow the sections top to bottom, invoking the named skill for each.
3. **Sections are method-driven, not freeform.** Do not invent sections; do not skip mandatory ones silently.
4. **A non-applicable optional section is marked, not deleted:** leave the header and write `N/A — <one-line reason>`. This keeps audits one-glance and matches the convention used across every method skill.
5. **Respect granularity.** If the thing you are documenting spans many capabilities (a plan, an estimate, a benchmark, the risk register, the user-involvement plan), it is **not** a capability section — it belongs in the release/project template. Cross-cutting risks link back with `related`.

## Frontmatter (all node types)

Per the `framework` contract. `children` is the body section index, never a frontmatter field.

```
---
type: <vision|goal|capability|feature|story|spec|release>
status: draft        # draft → active → done → superseded (or deprecated)
parent: <type-id-slug>   # omitted only for the single root vision
related: []          # non-derivable cross-axis links only
artifacts: []        # optional: external evidence files hung off this node
---
```

## Templates

### vision  → método: `product-manager-vision`

Root node — no `parent`. Single vision is the graph root.

```
## Why (start with why)
## The future as a socio-technical system        # product absent on purpose
## The future product story                      # product inserted into that future
## One-breath narrative                           # repeatable by everyone
## Positioning statement
  > For [target customer] who [need], the [product] is a [category]
  > that [key benefit]. Unlike [competitive alternative], our product
  > [primary differentiation].
## Horizon                                        # 2–10 years, explicit
## Adopted trends                                 # trends believed to hold over the horizon
```

### goal  → método: `product-manager-goals`

`parent:` the vision.

```
## Outcome statement
  > In order to [GOAL] as [STAKEHOLDER] I want [capability set]
## Parent vision                                  # explicit reference
## Horizon                                        # roadmap 1–2y | release 2–9mo | iteration 1–4w
## SMART check                                    # S / M / A / R / T, letter by letter, M carries a number
## Why-stack                                      # "why?" lands on the vision, not another goal
```

### capability  → método: `product-manager-capabilities`

`parent:` a goal.

```
## Statement                                      # "In order to [GOAL] as [STAKEHOLDER] I want { … }", implementation-agnostic
## Parent goal                                    # explicit reference
## Two implementations                            # the agnostic test: name two plausible ones
## Value analysis            → método: product-manager-value-analysis
## Risks (Cagan four-risks tag)  → método: product-manager-risk-analysis   # cross-cutting risks go in the release risk register, linked via related
## Go / No-Go                                     # four-risks discriminator, one-line reason
## Feature decomposition     → método: product-manager-feature-decomposition   # only for Go capabilities
```

### feature / story  → método: `product-manager-feature-decomposition`

`parent:` a capability (feature) or a feature (story = sub-task granularity). Same template, smaller scope at story level.

```
## Story
  > As a [role], I want [capability], so that [benefit]
## Conditions of satisfaction                     # back of the card
## INVEST check                                   # I/N/V/E/S/T, letter by letter
## Story-map position                             # Activity → Task → Sub-task; narrative order
## 5 Cs status                                    # Card / Conversation / Confirmation / Construction / Consequences
## Requirements detail        → método: product-manager-requirements-discovery   # when this opens a new feature area
## Spec                       → método: product-manager-spec-gherkin
```

### spec  → método: `product-manager-spec-gherkin`

`parent:` a feature.

```
## Acceptance Criteria                            # AC-A1, AC-A2, … one human sentence each, traceable to story letter
## Gherkin
  ```gherkin
  Feature: <human capability>
    <free-form description: why, business rules>
    Background:            # only if EVERY scenario shares it
    Scenario: …    # AC-A1
      Given … When … Then …
    Scenario Outline: …    # table-driven cases
  ```
## Story → AC traceability                        # every scenario maps to a story id
```

### release / project  → orchestrated by the delivery skills

`parent:` a roadmap-horizon goal. This is where artifacts that span many capabilities live — they are **not** duplicated into capability nodes.

```
## Scope                                          # which capabilities/features this release carries
## Sizing                     → método: product-manager-early-sizing            # FP band + growth band + tier
## Estimate                   → método: product-manager-cost-estimating         # cost/schedule/quality, benchmark-defended
## Plan                       → método: product-manager-project-planning        # WBS, critical path, Roadmap/Release/Iteration horizons
## Risk register              → método: product-manager-risk-analysis           # Jones 14 + Cagan 4 + size escalation; capabilities link here via related
## Change control             → método: product-manager-change-control          # CCB, CR log, FP>10 re-estimation trigger
## User-involvement plan      → método: product-manager-user-involvement         # 12 forms, 10–50% effort ratio
## Milestone tracking         → método: product-manager-milestone-tracking      # 13 canonical milestones, reviewed-deliverable closure
## Benchmarks / baselines     → método: product-manager-benchmarks-baselines     # ISBSG comparison / SPI baseline
```

## Pitfalls to avoid

- **Treating the template as a replacement for the method skills.** The template gives shape and order. *How* to do value analysis well is still `product-manager-value-analysis`. Inlining method depth here would bloat the template and create a second source of truth.
- **Duplicating release-level artifacts into capability nodes.** The plan, the estimate, the benchmark, the risk register, the user-involvement plan are release/project scoped. A capability links to a cross-cutting risk via `related`; it does not own a copy of the register.
- **Inventing sections.** If a node seems to need a section no template defines, that is a signal to revise the template here (one place), not to fork the node structure ad hoc.
- **Deleting non-applicable sections.** Mark `N/A — reason`. A deleted section is indistinguishable from a forgotten one at audit.
- **Filling sections out of order.** The order encodes precedence (value before Go/No-Go before decomposition; sizing before estimate before plan). Skipping ahead reproduces the failure modes the method skills exist to prevent.
- **Putting method depth in the wrong layer.** New empirical content (a new Jones practice, a new Cagan principle) belongs in the relevant method skill, never in the template.
