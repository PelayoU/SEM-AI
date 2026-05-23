# ADR-003 — Holistic product dimensions cross-cut the spine

- **Status**: accepted
- **Date**: 2026-05-23
- **Supersedes**: —
- **Superseded by**: —

## Context

A junior product manager tends to think the spine pyramid (vision → goal → capability → feature) in **functional/technical terms only**: what the product does and how it is built. A senior manager carries every level of the pyramid through **multiple holistic dimensions** simultaneously, balancing them, and notices when one is missing.

This is not methodology — it is the practice of mature product management. The framework's catalog of seven Issue Types (ADR-001) and the role-based jurisdiction model give us *who* writes *what*, but they say nothing about the **lens** through which the spine is supposed to be thought. Without naming that lens explicitly, the framework risks reproducing the junior-manager mistake by structural inertia: templates that only ask "what does it do" produce nodes that only describe what they do.

This ADR names the lens and encodes it in two complementary places: structured slots in the spine templates (so the lens cannot be silently skipped) and a conceptual paragraph in the framework SKILL (so every role uses the lens when evaluating impact, not only the PM when authoring the spine).

## Decision

The framework recognizes **five holistic product dimensions** that cross-cut the spine. **Functionality** is the base they complement — the product's reason for being — and the five are the perspectives that, together with functionality, make a holistic product:

| Dimension | What it covers |
|---|---|
| **Technology** | The technology that enables the functionality (architecture, performance, scale, technical stack choices) |
| **UX design** | The design of the user experience (flows, interactions, copy, accessibility, emotional posture) |
| **Monetization** | How the product creates and captures economic value (pricing, business model, unit economics) |
| **Acquisition** | How the product reaches users and customers (channels, growth loops, onboarding funnel) |
| **Offline experience** | The off-screen experiences essential to delivering the product value (support, logistics, partner integrations, human services, physical components) |

These five dimensions are **orthogonal to the role-jurisdiction model**: they do not map one-to-one to roles. A senior PM absorbs most of them when authoring the spine (functionality + monetization + acquisition + UX strategy + offline strategy, consulting Architect for technology). When a project grows large enough to ship dedicated UX Designers or Growth roles, those roles are added project-specifically as agent.md files; the dimensions stay the same.

## Two planes of recognition

The five dimensions are encoded in the framework on **two complementary planes**:

### Plane 1 — Structured slots in spine templates

The templates for `vision`, `goal`, `capability`, and `feature` gain a **"Holistic dimensions"** section with one entry per dimension. The author (PM, since these are spine nodes) is **forced to consider each dimension** because the slots are part of the template. Slots marked `N/A — <reason>` are legitimate when justified; silently omitted slots are not.

For `vision` and `goal` the slots state the **posture** the node commits to in each dimension. For `capability` they state **what the capability does in this dimension**. For `feature` they state **how the feature manifests in this dimension** (concrete enough that the author is forced past the functional-only reflex).

`story` and `spec` do **not** get a dedicated section because at that granularity the dimensions manifest as specific **Acceptance Criteria** (an AC about technology performance, an AC about UX, an AC about monetization metric, etc.) — making the dimensions part of the AC list is cleaner than duplicating slots.

`adr` does not get the section either: an ADR is a single decision with a Consequences section that may impact multiple dimensions, but it is not the place to balance them — it is the place to record the impact.

### Plane 2 — Evaluation lens for every role

Beyond the spine, the five dimensions are the **lens every role uses when evaluating the impact of its own work**:

- **Architect** writing an ADR: this technical decision, what is its impact on UX (latency)? on monetization (infra cost)? on acquisition (time-to-market)? on offline (operability)? The ADR's Consequences section reflects what was found.
- **Developer** implementing a spec: does this code change affect only functionality, or also UX (microcopy), or technology (performance regression), or offline (support cost)?
- **QA** designing tests: what dimension does each test class cover? Pure functional? UX? Performance? Robustness for offline degraded mode?
- **DevOps** planning a release: rollout impact on acquisition (downtime window), on offline (support staffing), on monetization (infra spend during rollout)?
- **Security Officer** auditing: this vulnerability touches which dimensions? Auth → UX; fraud → monetization; data privacy → trust → acquisition; service degradation → offline experience.

All roles use the lens; only PM additionally encodes it as structured slots, because PM authors the spine.

## Why this is infrastructure, not methodology

The framework provides:

- The **slots** (the structural section with five entries in the templates).
- The **lens** (the framework SKILL names the dimensions and says every role applies them).

The framework does not provide:

- The **content** of each slot — how to design UX, how to model monetization, how to architect for offline experience. That is methodology (or the LLM's training, or the project's domain expertise).

This matches the framework's repeated principle: the **fixed layer** (the "frontmatter" — types, fields, structure, slots) is what the framework ships. The **variable layer** (the body content, the methodology that fills each section) comes from the project's skills or the LLM's training.

## Why these five, why functionality as base

The five emerge from the holistic-product practice familiar to senior product organizations (Cagan, Sean Ellis, modern product education). Functionality is treated as the base — the product's reason for being — and the five are the perspectives that, **together with functionality**, prevent the product from being technically excellent but unmonetizable, beautifully designed but undiscoverable, functionally rich but operationally unsupportable.

The framework does not claim these are the only five possible dimensions, but it picks these as the **canonical infrastructure**. A project that needs to add a sixth (e.g. "Compliance" as its own dimension for regulated industries) can extend its templates locally. The framework's set is the default that covers the bulk of product practice.

## What this is not

This ADR does **not** introduce:

- New Issue Types. The catalog of seven from ADR-001 is unchanged.
- New roles. The six roles from the framework SKILL are unchanged. PM is still the authoring hand of the spine; consultations to other roles to fill non-functional slots are the existing `consult` mechanism.
- New status flows or jurisdiction rules. The Engine MCP's enforcement is unchanged.

It introduces structured slots in existing templates and articulates a lens that the framework SKILL names explicitly.

## Consequences

- `node-templates/SKILL.md` gains a "Holistic dimensions" section in the templates of `vision`, `goal`, `capability`, `feature`.
- `framework/SKILL.md` § *The graph* gains a paragraph naming the five dimensions as the evaluation lens every role applies, with a pointer to this ADR.
- The `adr` template's Consequences section is the natural place to reflect cross-dimensional impact when relevant; no new section needed there.
- A node whose Holistic dimensions section has every slot marked `N/A` should trigger review — that is almost certainly a sign the node is misconceived or trivial.
- Coherence checks (mentioned in ADR-002) can include verifying that the spine ancestry is consistent across dimensions — e.g. a feature with a strong monetization slot whose parent capability marks monetization `N/A` is incoherent and either the feature or the capability needs revision.

## Alternatives considered

- **Leave dimensions implicit in the role-jurisdiction model.** Reject because the role model captures *who writes what* but not *what lens is being applied*. Templates that only ask "what does it do" produce uni-dimensional nodes regardless of which role writes them.
- **One Issue Type per dimension.** Considered (e.g. a "UX vision" Issue alongside the regular "vision"). Rejected because dimensions are perspectives on the same node, not separate work artifacts. A vision *has* a UX posture; it doesn't fragment into "the UX vision" and "the functional vision".
- **Slots in every Issue Type including spec and ADR.** Rejected: spec carries the dimensions in its Acceptance Criteria (more concrete and testable); ADR reflects cross-dimensional impact in its Consequences. Forcing dedicated slots there would duplicate without gain.
- **A larger or smaller set of dimensions.** The five chosen are the canonical default. Projects with regulated needs can extend their templates locally (e.g. add a Compliance slot) without changing the framework.

## Status

Accepted. Spine templates carry the five dimensions as structured slots; framework SKILL names them as the lens every role applies.
