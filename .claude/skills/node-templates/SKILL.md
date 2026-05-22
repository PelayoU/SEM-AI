---
name: node-templates
description: "The canonical body templates for every graph node type — vision, goal, capability, feature/story, spec, adr, release, defect, measurement, inspection — plus the per-section pointers to whichever project methodology skill (if any) is supplied to fill each section. Use whenever a node is being created or audited for structural completeness: 'create a capability', 'new vision', 'start a goal', 'scaffold this feature', 'what sections does a spec need', 'node template', 'is this node complete', 'release node', 'open an ADR', 'log a defect'. This skill gives the shape and the flow; the methodology that fills each section comes from the project's skills or the LLM's training, not from this skill."
---

# node-templates

## Purpose

A graph node is not a title with a `parent` edge — it is a living document with a defined section structure. This skill is the single place where that structure lives for every node type the framework recognises. Each template states the node's body sections in the order they should be filled, and a `→ method:` pointer per section to whichever methodology skill is currently supplying the depth. The template is the **shape and the flow**; it does not duplicate methodology depth — that comes from the project's methodology skills (if any are installed under `.claude/skills/`) or from the LLM's training, never from this skill.

This dissolves two problems at once: there is no orphan analysis (every analytical artifact is a section of the node it analyzes, so the framework's "no artifact without a node" rule is satisfied structurally), and there is no node-type proliferation (delivery artifacts that span many capabilities live in the release template at the right granularity, not duplicated into every capability).

## When this skill applies

- A node is being created and needs its skeleton.
- An existing node is being audited for structural completeness ("does this capability have its value and risk sections?").
- A reviewer needs to know which methodology skill (if any) owns a given section.
- The boundary question arises: "is this a section of a capability, or a release-level artifact?".

## How to use a template

1. **Pick the template by node type.** Open the Issue with the matching Issue Type (the engine MCP's `create_node(type=…)` does this), set the sub-issue link to the parent, and instantiate the body section skeleton verbatim into the Issue body.
2. **Fill each section via its pointed methodology.** The section order *is* the flow; the `→ method:` pointer *is* the orchestration. Look up the named methodology skill in the Skill listing; if it matches, invoke it. If no methodology skill matches the pointer, fill the section from training and name the method out loud (so the human can accept or substitute).
3. **Sections are method-driven, not freeform.** Do not invent sections; do not skip mandatory ones silently.
4. **A non-applicable optional section is marked, not deleted:** leave the header and write `N/A — <one-line reason>`. This keeps audits one-glance.
5. **Respect granularity.** If the thing you are documenting spans many capabilities (a plan, an estimate, a benchmark, a risk register, a user-involvement plan), it is **not** a capability section — it belongs in the release template. Cross-cutting risks link back to the release node via the `related` custom field.

## How node fields map to GitHub Issue mechanisms

Every node lives as a GitHub Issue (rationale and full mapping in `docs/adr/001-all-nodes-as-github-issues.md`). Templates below describe the **body** — the sections inside the Issue text. The "frontmatter" the v0.1 / v0.2 designs put at the top of a markdown file is replaced, per concept, by native Issue mechanisms set by the engine MCP at write time (not by the agent typing them into the body):

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
## Horizon                                        # planning horizon, explicit
## Adopted trends                                 # trends believed to hold over the horizon
```

### goal  → method: project's goal methodology skill, if any; else from training

`parent:` the vision (sub-issue link).

```
## Map                  # read-time index, queried — NOT authoritative; the sub-issue link is the only true edge
- Children: this goal's capabilities
- Related:  constraining adr; release(s) delivering toward this goal
## Outcome statement                              # the measurable outcome this goal asserts
## Parent vision                                  # explicit reference (sub-issue link)
## Horizon                                        # planning horizon — roadmap / release / iteration scoped
## Acceptance check                               # criteria by which this goal is judged done
## Why this goal                                  # the chain from the vision down to this goal
```

### capability  → method: project's capability methodology skill, if any; else from training

`parent:` a goal (sub-issue link).

```
## Map                  # read-time index, queried — NOT authoritative; the sub-issue link is the only true edge
- Children: this capability's features
- Related:  constraining adr; the release(s) whose scope includes it; affine spec
## Statement                                      # what the system enables, implementation-agnostic
## Parent goal                                    # explicit reference (sub-issue link)
## Two implementations                            # name two plausible ones — the agnostic test
## Value analysis            → method: project's value-analysis skill, if any
## Risks                     → method: project's risk-analysis skill, if any   # cross-cutting risks go in the release risk register, linked via related
## Go / No-Go                                     # decision and one-line reason
## Feature decomposition     → method: project's feature-decomposition skill, if any   # only for Go capabilities
```

### feature / story  → method: project's feature-decomposition skill, if any; else from training

`parent:` a capability (feature) or a feature (story = sub-task granularity). Same template, smaller scope at story level.

```
## Map                  # read-time index, queried — NOT authoritative; the sub-issue link is the only true edge
- Children: this feature's stories (none if a leaf story)
- Related:  its spec; constraining adr
## Story                                          # role, need, benefit — phrased per the project's chosen story format
## Conditions of satisfaction                     # the back of the card
## Acceptance check                               # criteria by which this is judged complete
## Position in the larger narrative               # where this fits in the user's flow
## State                                          # where in the lifecycle the conversation/construction sits
## Requirements detail        → method: project's requirements-discovery skill, if any   # when this opens a new feature area
## Spec                       → method: project's spec methodology skill, if any
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

### release  → method: project's project-planning methodology skill, if any; else from training

`parent:` the `vision` (sub-issue link) — a release slices across goals, so it is not a child of any one. `related:` carries the goals and capabilities pulled into this release's scope (set via the **Related** custom field, not typed in the body). This is where artifacts that span many capabilities live — they are **not** duplicated into capability nodes; cross-cutting risks in those capabilities link back here via `related`.

The Issue tracks the release while it is being built (planning, scope, quality gate, security gate). The publication moment is a **GitHub Release** (native git tag + release notes) linked from the Issue body when the release ships.

```
## Map                  # read-time index, queried — NOT authoritative
- Children: none (off-spine)
- Related:  the goals/capabilities delivered (mirrors the Related custom field); bare links only — rationale stays in Scope
## Version                                        # human label distinguishing this release from prior / next (e.g. "v2.0")
## Target / shipped                               # planned ship date; actual ship date set when status → released
## GitHub Release link                            # set when the release publishes (the native tag + release notes)
## Scope                                          # which capabilities / features this release carries
## Sizing                     → method: project's sizing skill, if any
## Estimate                   → method: project's estimating skill, if any
## Plan                       → method: project's project-planning skill, if any
## Risk register              → method: project's risk-analysis skill, if any   # capabilities link here via related
## Change control             → method: project's change-control skill, if any
## User-involvement plan      → method: project's user-involvement skill, if any
## Milestone tracking         → method: project's milestone-tracking skill, if any
## Benchmarks / baselines     → method: project's benchmarks skill, if any
## Quality gate               → method: project's quality-gate skill, if any   # QA contributes via consult
## Security gate              → method: project's security-gate skill, if any   # Security Officer contributes via consult
```

A finished release keeps its Issue at status `released` with `shipped` set — that is the frozen history (its sizing, plan, milestones sealed in place). v2 is a **new** release Issue; nothing accumulates because the body sections are current-state, and the revision history lives in Issue edit history + the change-control CR log.

### defect  → method: project's defect methodology skill, if any; else from training

`parent:` the node whose work surfaced the defect (sub-issue link) — the `spec` under test, the `inspection` that found it, the `feature` being implemented, etc. Owning role is QA (inspection-found) or Developer (own static-analysis / unit-test) — shared ledger; search before creating to avoid duplicates.

```
## Map                  # read-time index, queried — NOT authoritative
- Parent:   the node whose work surfaced this defect
- Related:  the spec / feature / inspection / measurement this defect interacts with
## Origin                                         # how this was found — inspection | static-analysis | unit-test | integration-test | …
## Severity                                       # impact ranking the project's methodology defines
## Reproduction                                   # exact steps; expected vs actual
## Root cause                                     # filled when known; left as N/A until then
## Fix                                            # the change that resolved it; linked PR via Closes #N
## Verification                                   # how the fix was confirmed (by whom, against what)
```

### measurement  → method: project's measurement methodology skill, if any; else from training

`parent:` the node whose property the measurement describes (sub-issue link). Status is terminal at `recorded` — measurements have no lifecycle. Owning role is QA.

```
## Map                  # read-time index, queried — NOT authoritative
- Parent:   the node this measurement describes
- Related:  the inspection / test run / benchmark this measurement was taken from
## What was measured                              # the metric and its definition
## When                                           # date / build / version measured against
## How                                            # the procedure; the tool; the conditions
## Result                                         # the value; the unit
## Confidence                                     # margin of error / sample size if applicable
```

### inspection  → method: project's inspection methodology skill, if any; else from training

`parent:` the artifact being inspected (sub-issue link). Status is terminal at `recorded`. Owning role is QA. Defects found are separate `defect` nodes linked via `related`.

```
## Map                  # read-time index, queried — NOT authoritative
- Parent:   the artifact inspected (a spec, feature, adr, code module …)
- Related:  the defects this inspection raised
## Participants                                   # who took part; roles
## Checklist                                      # which methodology checklist was applied
## Findings                                       # observations recorded during the inspection
## Defects raised                                 # bare links to the defect Issues (rationale stays on each defect)
## Verdict                                        # the inspection's overall conclusion
```

## Pitfalls to avoid

- **Treating the template as a replacement for the methodology.** The template gives shape and order. *How* to do value analysis well comes from the project's methodology skill (if any) or LLM training, not from this skill.
- **Duplicating release-level artifacts into capability nodes.** The plan, the estimate, the benchmark, the risk register, the user-involvement plan are release scoped. A capability links to a cross-cutting risk via `related`; it does not own a copy of the register.
- **Inventing sections.** If a node seems to need a section no template defines, that is a signal to revise the template here (one place), not to fork the node structure ad hoc.
- **Deleting non-applicable sections.** Mark `N/A — reason`. A deleted section is indistinguishable from a forgotten one at audit.
- **Filling sections out of order.** The order encodes precedence (value before Go/No-Go before decomposition; sizing before estimate before plan). Skipping ahead reproduces the failure modes the methodology exists to prevent.
- **Typing the "frontmatter" concepts into the body.** `type` / `parent` / `status` / `related` / etc. are not body text — they are native Issue mechanisms set by the engine MCP on write. The body is the sections above, nothing else.
- **Naming a methodology skill that does not exist in the Skill listing.** A `→ method:` pointer is a *suggestion of where the depth should come from*. If the project does not install a skill matching the pointer, fill from training and name the method out loud — never invent a skill name.
