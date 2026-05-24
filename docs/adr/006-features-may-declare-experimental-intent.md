# ADR-006 — Features may declare experimental intent

- **Status**: accepted
- **Date**: 2026-05-23
- **Supersedes**: —
- **Superseded by**: —

## Context

ADR-005 established that the value chain (Output → Outcome → Benefit → Value) is **probabilistic** and that **learning is the guaranteed output of every cycle**. It also stated that the framework **enables** value rather than providing it. With those decisions in place, an implicit corollary remains unstated:

**A feature can be built with the primary intent of resolving an uncertainty, not of delivering value.**

ADR-005 acknowledged that learning is always valuable; this ADR goes one step further and says some features exist *primarily for the learning*. That changes how the team measures success: an experiment is successful when the uncertainty is resolved (regardless of the value chain), while a delivery is successful when the value chain completes (regardless of incidental learning).

The framework risks pretending all features are delivery — that every cycle is expected to produce value. Without naming experimental intent explicitly:

- Experiments are forced to live as "deliveries that didn't quite work" — celebrated as misses instead of as successful resolutions of uncertainty.
- Teams that should build small experiments to de-risk a path build bigger deliveries instead, because the framework's structure only recognises delivery.
- The Value chain section (ADR-005) is read as "did we deliver value?" when for an experiment the relevant question is "did we resolve the uncertainty?".

This ADR closes that gap.

## Decision

A feature may carry one of two intents, declared at creation time:

| Intent | Purpose | Success criterion |
|---|---|---|
| **Delivery** | Produce value directly. The feature pays off learning already accumulated. | Value chain completes (per ADR-005) — outputs lead to outcomes, outcomes to benefits, benefits to value. |
| **Experiment** | Resolve an uncertainty about the path toward the vision. The feature exists to produce learning. | The named uncertainty is resolved (yes/no/partially), with reasoning. Value chain completion is a bonus, not the standard. |

Both intents are legitimate. The framework accepts both as first-class. The difference shows up only in:

- The `Uncertainty addressed` slot in the feature template (populated for experiments; `N/A` for pure deliveries).
- How the Value chain section (ADR-005, post-done) is read: experiments are judged primarily on Learning extracted; deliveries primarily on Value assessment.

**A feature may also be mixed** — primarily delivery but with a declared uncertainty it also resolves; or primarily experiment that happens to ship something with incidental value. The intent declaration is the *primary* intent, not the only one. The framework treats this as a continuum, not a binary.

### The vision is the polar star; features are the steps

This ADR completes the model started in ADR-002 (hierarchical loop) and ADR-005 (value chain):

- **The vision** encodes the team's ambition — identity (Positioning) + destination of value (Value ambition, the new slot per this set of commits). The vision is the polar star: where the work navigates toward, multi-dimensional, quantifiable when possible.
- **The features** are the steps toward that polar star. Some are experiments — they de-risk the path by resolving an uncertainty. Others are deliveries — they accumulate value once the path is sufficiently de-risked.
- **A healthy product cycle interleaves both**. Pure experiments without eventual deliveries never consolidate value; pure deliveries without experiments mean the team is building blind on assumptions that should have been tested.
- **Which dominates at any moment is a management call**, not a framework rule. The framework provides the slots; the team picks the intent per feature based on what they don't yet know vs what they've already validated.

This is the canonical resolution of a tension that the framework otherwise left implicit: how to reconcile "the path is enredado and probabilistic" (ADR-005) with "we ship features to deliver value" (the natural reading of the feature template). The reconciliation: some features deliver; some experiments don't pretend to.

## What the framework does NOT impose

The framework does not import:

- The name "MVP" or "Minimum Viable Prototype" (Eric Ries / Lean Startup vocabulary). The framework uses "feature with experimental intent" — same idea, no methodology import.
- The name "MVV" or "Maximum Viable Value". The framework uses "Value ambition" — same idea expressed structurally.
- Specific experiment forms (landing page, concierge, wizard of oz, A/B test, …). Those are methodology — the project's methodology skills supply them.
- Specific frameworks (Agile, Lean, XP, Scrum, Kanban). The intent of a feature is orthogonal to which methodology the project ships.
- A required field "uncertainty type" or "experiment classification". The slot is free-form prose; how to classify experiments is methodology choice.
- A separate Issue Type "experiment". An experiment is a feature with an Uncertainty addressed slot populated. No new Type, no inflated catalog.

## Why no new Issue Type

Considered: adding `experiment` as a distinct Issue Type alongside `feature`. Rejected because:

- It would inflate the catalog (per ADR-001 audit principle: keep types minimal).
- The structure of an experiment is identical to a feature (parent, body sections, lifecycle, jurisdictions). Only the declared intent and the reading of success differ.
- A mixed-intent feature (primarily delivery with a side experiment) would be awkward to model as either Type. Free-form prose in a slot accommodates the continuum.
- Existing tooling (Projects v2 filters, queries, status flows) keeps working uniformly across all features without special-casing experiments.

## Why no new status

Considered: adding `experiment-in-progress` as a status, or making `done` mean different things by intent. Rejected because:

- Status semantics should be uniform — `done` means "the feature was built and shipped", regardless of intent. The intent affects how the Value chain section is *read*, not what `done` means.
- Lifecycle flows would fragment by intent if intent altered status semantics. Keep status flows uniform.

## Consequences

- `node-templates/SKILL.md` feature template gains an **optional** `## Uncertainty addressed` slot at the top of the section list (or near the Story). Populated for experiments; `N/A — delivery, not experiment` for pure deliveries.
- `node-templates/SKILL.md` vision template gains a `## Value ambition` slot (the polar-star destination this ADR's narrative depends on, also referenced by ADR-005 § *value chain*).
- `framework/SKILL.md` § The graph gains a paragraph naming vision-as-polar-star + features-as-steps (delivery or experiment).
- The Value chain section in the feature template (ADR-005) is **read differently by intent**: for experiments, Learning extracted is the primary signal; for deliveries, Value assessment is the primary signal. Both slots are populated regardless; only the emphasis changes.
- `/session-close` (pending implementation) prompts the active role to confirm the intent of any feature touched and ensures the Uncertainty addressed slot is populated for experiments before the session closes.
- Coherence checks (ADR-002 mentioned) can include: if the parent capability is in `draft` and the feature is in-progress, the feature is likely an experiment (resolving uncertainty about the capability itself). Surfacing this can prompt the team to declare the intent explicitly.

## Alternatives considered

- **Treat all features as delivery; let experiments hide as "small features".** Rejected. This is the status quo before this ADR and it produces the failure modes named in Context — experiments mislabelled as missed deliveries, teams over-investing in delivery shape when experiment shape was right.
- **New Issue Type `experiment`.** Rejected per ADR-001 audit principle.
- **A status `experimental` in parallel with `draft`/`active`/`done`.** Rejected: intent is orthogonal to lifecycle. A feature can be in-progress while either delivery or experiment intent.
- **A custom field `intent` (enum: delivery / experiment / mixed).** Considered. Rejected in favor of the free-form `Uncertainty addressed` slot — having text describing the uncertainty is more useful than a label, and a populated slot implies experimental intent without needing a separate field.
- **A separate ADR for `Value ambition` in vision.** Rejected. The slot exists *because* features can be experiments aimed at the polar star, and the polar star is the vision's value ambition. One coherent narrative, one ADR.

## Status

Accepted. Features may declare experimental intent via the Uncertainty addressed slot; the vision declares its destination via the Value ambition slot; the framework reads both intents (delivery / experiment) as legitimate first-class shapes of work.

---

## Update — label `experiment` as the visible counterpart to the slot (2026-05-24)

After the original decision was operationalized, a gap surfaced: the `Uncertainty addressed` slot lives **inside** the Issue body and is only visible when the Issue is opened. From the Issue list, from the Projects v2 board, from a `gh issue list` invocation, there is no signal that a given feature is an experiment vs a delivery. For a team that interleaves discovery and delivery (the dual-track operational mode), that opacity creates friction — agents and humans alike read the list of features without knowing which are validating unknowns and which are paying off learning already accumulated.

This update closes the gap **without contradicting the original decision** — none of the original rejections (no new Issue Type, no new status, no enum custom field) is reversed.

### Decision (update)

The framework recognises **a native GitHub label `experiment`** as the visible counterpart to the `Uncertainty addressed` slot. The engine MCP applies it automatically when the slot is populated on `create_node(type=feature, …)` or `update_node`; it removes it when the slot is cleared to N/A. The label is **mechanical**, not free-form: the team does not curate it directly; the engine maintains coherence between slot and label.

Reading guide:

| Signal | What it tells you |
|---|---|
| Feature has no `experiment` label | Delivery feature (pays off learning already accumulated; success = value chain completion per ADR-005) |
| Feature has `experiment` label | Experimental feature (Uncertainty addressed is populated; success = the uncertainty is resolved, value chain completion is bonus) |

The slot and the label encode the same truth from two angles: the slot says **what** uncertainty (free-form, useful for the agent that will work on it); the label says **that** it is an experiment (visible, queryable, filterable).

### Why a label (and not Issue Type or status or enum)

The label is the **single mechanism** that achieves visibility without contradicting any of the original rejections:

- It is **not a new Issue Type** — feature stays feature; ADR-001 audit principle holds.
- It is **not a new status** — the lifecycle remains uniform across delivery and experiment.
- It is **not an enum custom field** — the free-form prose in the slot remains the primary description; the label is a derived signal.
- It is **native to GitHub** — Projects v2 supports it as a filter/group natively; `gh issue list -l experiment` works out of the box; the team's existing tools keep functioning without special-casing.
- It is **maintained by the engine, not the team** — coherence between slot and label is mechanical, not a discipline burden.

This matches the pattern of how the framework handles `bug` (per ADR-001): a native label rather than an Issue Type. Same decision shape, same justification.

### Expected destination by experiment sub-type

The `Uncertainty addressed` slot accommodates any kind of experiment. Different sub-types have different natural destinations; the framework documents these as convention, does not enforce them:

| Experiment sub-type | What it ships | Natural final status |
|---|---|---|
| **Prototype** (landing page, mockup, smoke test, concierge) | Discardable artifact whose only purpose was to produce the learning | `deprecated` — sea que validated or invalidated. If validated, open a new feature with `delivery` intent and a `related` link back to this experiment for the production version. |
| **Spike** (technical or design exploration to validate feasibility) | A decision + possibly throwaway code | Usually `deprecated`; can be `done` if the spike's output is light and useful enough to keep. |
| **A/B test** | A chosen variant + data on the comparison | `done` — the winning variant stays in production; the experiment Issue closes with learning recorded. |
| **Concierge** (humans manually doing what software would eventually do) | Operational data on what is worth automating | `deprecated` after the learning is extracted; the automation (if validated) opens as a new delivery feature. |

The label `experiment` covers all four uniformly; the sub-type is captured in the slot's prose (free-form). If a project finds itself wanting a sub-label like `prototype` to filter only the discardable sub-type, it can add that locally — the framework's default set is the single `experiment` label.

### Consequences (update)

- The engine MCP gains responsibility for label-slot coherence: on every write of a `feature` Issue, if `Uncertainty addressed` is populated → ensure label `experiment` is present; if cleared to N/A → ensure label `experiment` is absent.
- The framework SKILL § The graph (the polar-star / features-as-steps paragraph) mentions the label briefly as the visibility complement.
- The `node-templates` slot comment for `Uncertainty addressed` references the auto-applied label and documents the destination conventions by sub-type.
- The label `experiment` is provisioned by `scripts/setup-github-project.sh` alongside the `bug` label (when that script is implemented).
- Projects v2 saved views can include "All experiments in progress" as a default view, surfacing the discovery work distinct from the delivery work — supporting the dual-track operational mode without imposing it as a framework requirement.

### What this update does NOT change

- The Uncertainty addressed slot stays exactly as decided in the original ADR — free-form prose, optional, N/A for pure deliveries.
- The intent of a feature (delivery / experiment) remains a continuum; the label is the *primary* signal, not the only one. Mixed-intent features (primarily delivery with a side experiment) populate the slot lightly with the side uncertainty; the label flips on; the team reads the situation as "primarily delivery with experimental sub-component", which the framework does not need to model with more granularity.
- The Value chain section in the feature template (ADR-005) is read by intent as before; the label just makes the intent visible from the outside before the Value chain section is even reached.
