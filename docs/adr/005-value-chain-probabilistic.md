# ADR-005 — The value chain: Output → Outcome → Benefit → Value, and probabilistic

- **Status**: accepted
- **Date**: 2026-05-23
- **Supersedes**: —
- **Superseded by**: —

## Context

Earlier ADRs decide *what* the graph contains (ADR-001), *how* it is built in both directions (ADR-002), and *which dimensions* cross-cut every node (ADR-003). None of them yet states what the framework understands by **value** — the thing the whole apparatus exists to enable.

Without that statement, the framework risks reproducing the most common structural failure in software engineering organisations: **measuring outputs as if they were value**. Velocity, story points, features shipped, tickets closed — these are outputs. They are not value. Teams that drift toward measuring them as success metrics produce more output, not more value. The framework's templates (Story / Conditions of satisfaction / Acceptance check) sit at the output layer; if the framework never names what comes after, it implicitly endorses output-as-success.

This ADR records two ideas that are inseparable in the framework's model:

1. **A vertical chain** runs from what the team ships up to value: Output → Outcome → Benefit → Value. Each link is distinct, each can break independently, and value lives only at the end.

2. **The chain is probabilistic, not deterministic.** Even excellent teams complete the chain in a minority of cycles (industry data from Microsoft, Google, Amazon places the figure at 10–30% of features). The framework therefore says **enable value**, not **provide value** — its job is to create the conditions, not guarantee the outcome.

## Decision

The framework recognizes **the value chain** as the vertical lens through which work matures: every node in the spine sits somewhere on the chain, and every cycle (feature build → ship → measure) traverses it.

### The four links

| Link | What it is | How to recognise it |
|---|---|---|
| **Output** | What the team ships — code, UI, configuration, documentation, the tangible product of construction | "We built and deployed X" |
| **Outcome** | A new operational state resulting from the use of the output — behavioral change observed in users or systems | "X% of users now do Y differently because of what we shipped" |
| **Benefit** | A measurable improvement caused by the outcome in a metric that matters to the business or the user | "Because Y is now happening, metric Z moved by N" |
| **Value** | The benefit obtained by someone in proportion to the resources used — a ratio, not an absolute | "The benefit Z, weighed against the cost of building X and producing the outcome Y, is worth the investment" |

The chain composes vertically and links can break at any step:

- **Output without outcome** — the feature shipped but nobody adopted it. Common, often invisible.
- **Outcome without benefit** — users do the new thing, but it doesn't move any metric that matters. Counts as theatre.
- **Benefit without value** — the metric moved, but the cost was higher than the benefit. Negative ROI dressed in green numbers.
- **All four links** — the minority of cycles. The aim of the framework's apparatus is to make this minority *as large as possible*, not to pretend the rest aren't real.

### Probabilistic, not deterministic

The framework **enables** value; it does not **provide** value. The difference is not cosmetic — it is the framework's posture toward the work:

| Provide value (rejected framing) | Enable value (chosen framing) |
|---|---|
| Causal: build → value | Probabilistic: build → maybe value |
| Failure is a defect | Failure is the statistical norm |
| Punish what didn't work | Extract learning from what didn't work |
| The plan should survive | The plan is the starting point of the loop |

Statistical reality: **the value chain completes in roughly 10–30% of cycles even in excellent teams**. The remaining 70–90% produce learning, discoveries, problem identification, or breakthroughs in other directions — provided the team treats the cycle as a learning instrument, not a delivery contract.

### Learning is the guaranteed output

Across every cycle, regardless of whether value materializes, **the framework treats learning as the guaranteed output**. A feature shipped → no adoption observed → clear understanding of *why* (wrong audience, wrong moment, wrong fit, undiscoverable) is a **successful cycle by the framework's standard**, because the project's intent now reflects something it didn't know before.

This is what differentiates the framework's posture from delivery-shop framing: "ship the feature on time" vs "complete the cycle with honesty about what happened".

## Where this is encoded in the framework

### In `framework/SKILL.md` § The graph

A paragraph names the value chain as the vertical lens (alongside holistic dimensions as horizontal lens, alongside hierarchical loop), and articulates "the framework enables value, it does not provide it" with the learning-as-guaranteed-output framing.

### In `node-templates/SKILL.md`

**Feature template** gains a `## Value chain` section, populated post-done, with six slots:

```
- Outputs shipped:    what was actually built (often auto-filled from PRs that closed this)
- Outcomes observed:  behavioral change observed (or 'none — users did not adopt as expected')
- Benefits measured:  metric movements (or 'none — outcome did not move the metrics it should have moved')
- Value assessment:   honest benefit-to-cost ratio. May be negative. The framework asks for honesty, not theatre.
- Learning extracted: what this cycle taught regardless of whether value materialized. THIS IS THE GUARANTEED OUTPUT OF EVERY CYCLE.
- Next cards surfaced: new Issues this evaluation spawned (deprecate this feature? pivot? double down? new experiment?)
```

**Goal template** tightens the comment on `## Outcome statement`: it must state an **outcome** (a new operational state — behavioral / system change), not an output (a thing to be built). A goal that reads "ship the X feature" is mis-stated; a well-stated goal reads "X% of users do Y differently". This is structural — the goal's success criterion is at the outcome layer, not the output layer.

### Status transitions and the chain

The chain does not introduce new statuses. Existing semantics absorb it:

- `done` continues to mean "built and shipped". It does **not** imply value materialized — that is what the Value chain section records.
- `deprecated` is the legitimate state of a feature whose value chain didn't complete and pivoting is the right move. The framework does not punish deprecation; it treats it as the maturation of an honest assessment.
- `supersede` (with the `Supersedes` / `Superseded by` custom fields) is the legitimate state when a feature is replaced by a refined version — the value chain learned something and the next attempt encodes that learning.

The lifecycle `done → measured → either kept-as-is or deprecated or superseded` is therefore expressed:

- `done` (status field) + Value chain section populated honestly (body) → the lifecycle is complete.
- If the assessment surfaces that pivoting is right, the next cycle opens a new Issue that supersedes this one.
- If the assessment surfaces that killing is right, this Issue moves to `deprecated`.
- If the assessment surfaces clear value, the Issue stays `done` and the next cycle builds on it.

## Why this is not methodology

The framework provides:

- The **chain** as a named structure (Output / Outcome / Benefit / Value).
- The **slots** in the feature template that force the assessment.
- The **honest posture** ("the framework asks for honesty, not theatre"; "learning is the guaranteed output").

The framework does not provide:

- *How* to measure outcomes, benefits, value — those are the project's methodology choice (OKRs, leading indicators, NPS, qualitative interviews, A/B testing, etc.).
- *Which* metrics matter for this product — that is project domain knowledge.
- *Which threshold* counts as "value" — project decision, may vary by feature.

Consistent with the framework's posture: the **fixed layer** (the chain, the slots, the posture) is what the framework ships; the **variable layer** (the metric choices, the measurement methodology, the value thresholds) comes from the project's methodology skills or the LLM's training.

## Why probabilistic is encoded as posture, not as quantification

The framework does not require a probability number to be attached to anything (no "this feature has a 30% chance of producing value"). The "probabilistic" framing is **a posture toward how the team treats the cycle**, not a statistical model the framework computes.

This avoids two failure modes:

1. **False precision** — probability numbers attached to feature outcomes are usually invented and produce a sense of rigor where there is none.
2. **Punitive interpretation** — if 30% probability is recorded and the feature fails, that becomes ammunition against the team. The framework wants honesty in retrospect, not forecasts in advance.

Probability is the **lens** through which the team reads the chain ("this might not generate value, and if it doesn't, that is normal — what matters is what we learn"), not a number the framework records.

## Consequences

- `framework/SKILL.md` § The graph gains a paragraph naming the value chain + the enables-not-provides framing.
- `node-templates/SKILL.md` adds the Value chain section to the feature template with the six slots.
- `node-templates/SKILL.md` tightens the goal template's Outcome statement comment.
- Coherence checks (mentioned in ADR-002) can verify that a feature's expected outcomes (when planning) and observed value chain (post-done) align with its parent capability / goal — drift surfaces by comparing chains.
- The `/session-close` skill (pending implementation) naturally prompts the active role to populate the Value chain section of any `done` feature touched during the session, when data is available. If data isn't yet observable (typical immediately after shipping), the section is left with `pending — measure at <date>` markers and revisited in a later session.
- The framework's identity statement gains a line: *the framework's job is to enable value, not provide it; learning is the guaranteed output of every cycle*. This belongs in CLAUDE.md / framework/SKILL.md as posture.

## Alternatives considered

- **Treat value as a single field**, not a chain. Rejected because it collapses the four distinct failure modes (output without outcome, etc.) into one undifferentiated "did it work?" question. The chain is exactly what makes failure modes diagnosable.
- **Add a "value confidence" field at planning time** (the probability number). Rejected per the posture argument above — false precision plus punitive interpretation risk outweigh any benefit.
- **Introduce status `evaluated` after `done`**. Rejected (per the conversation): it imposes universal discipline that the framework's "infrastructure-available, team-decides" posture does not want. The Value chain section is the slot; populating it is the team's choice.
- **Two separate ADRs (chain + probabilistic)**. Rejected: the chain without acknowledging its probabilistic nature degenerates into deterministic framing. The two ideas are inseparable; one ADR keeps them together.
- **Restrict the Value chain section to large features only**. Rejected: at feature granularity the section is always meaningful (even if many slots are N/A for tiny features). At story/spec granularity the value chain lives in the parent feature, not duplicated.

## Status

Accepted. The framework recognizes the Output → Outcome → Benefit → Value chain as its vertical lens, framed as probabilistic. Learning is the guaranteed output of every cycle; value is the desired-but-not-guaranteed end.
