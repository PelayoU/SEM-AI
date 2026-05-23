# ADR-002 — The graph is hierarchical but not unidirectional

- **Status**: accepted
- **Date**: 2026-05-23
- **Supersedes**: —
- **Superseded by**: —

## Context

ADR-001 established the catalog of seven Issue Types (vision, goal, capability, feature, story, spec, adr) with a `parent` chain that runs vision → goal → capability → feature → story → spec. The structure is unambiguously hierarchical.

A natural misreading of that structure is **"the graph is built top-down"** — first the vision, then goals, then capabilities, then features, then stories, then specs. As if construction order had to mirror parent direction.

But the reality of product management — at any seriousness, not as methodology, just as practice — is that the graph is built **in both directions at once, and the dominant direction varies by moment**. A manager who only ever works top-down builds the wrong things; a manager who only ever works bottom-up loses coherence with intent. Real management oscillates.

This ADR records that the framework recognizes this explicitly, and the patterns that follow from it.

## Decision

The graph is **hierarchical in structure** (the `parent` chain encodes the intent ancestry, vision is the root) but **not unidirectional in construction**. Work flows in both directions depending on the moment.

**Four modes are explicitly recognized**, and switching between them is normal:

| Mode | Dominant direction | Trigger |
|---|---|---|
| **Greenfield** | Initial top-down, immediately iterating with bottom-up validation | Starting a new product from a vision; first weeks/months |
| **Feature-in-flight** | Bottom-up | A new feature emerges from user signals (complaints, data, opportunities) in a running product; it is captured first, then validated against the existing capability/goal/vision above |
| **Strategic planning** | Top-down | Annual or quarterly cycle deriving capabilities from agreed goals and vision |
| **Steady state** | Mixed continuous | Day-to-day team work: stories and AC at the bottom, coherence checks against goals and vision at the top, feedback in both directions |

**Direction-of-construction is the human manager's call**, based on the moment. The framework does not enforce one. The Engine MCP accepts node creation in any order — it does not require the parent to be in any particular status before a child can be created.

## The "anchor pending" pattern

When a node emerges bottom-up before its parent has crystallized — typical of the feature-in-flight mode — the framework's pattern is:

1. **Set `parent` to the closest meaningful ancestor that already exists**, even if loosely fitting.
2. **The parent stays in `status: draft`** while the bottom-up signals continue to clarify what it really is.
3. **The child's Map section carries the note "anchor pending"** so any reader knows the parent link is provisional.
4. **When the higher level crystallizes**, the parent link is corrected via `update_node`, the parent's status advances, and the "anchor pending" note is removed.

This is the normal way capabilities emerge from feature patterns, and goals emerge from capability patterns. It is not an exception; it is the bottom-up half of the loop made explicit.

## Why this is not a violation of "context is the project"

The framework's One Rule (from `framework/SKILL.md`) says: *before you create or change anything — code, a skill, config, a node — a graph node must already reference it*. This might seem to forbid bottom-up creation (how can you create a feature when its capability doesn't exist yet?).

But the rule is satisfied. The feature created bottom-up **does have a parent** — the loosely fitting capability that already existed, or the goal one level up if no capability fits. The graph node referencing the work is in place. The fact that the parent is `draft` and may be revised does not break the rule; it makes the *intent* part of the rule visible (the parent is still being clarified) without blocking the work below.

If literally **nothing** above fits — not even a goal — that is a signal that the work shouldn't be done yet. Stop and clarify the higher levels first. The rule still holds.

## Why the framework recognizes this explicitly

Three reasons:

1. **Realism.** Senior managers oscillate between directions. A framework that pretends the graph is built top-down only contradicts how product work actually happens, and that contradiction trains the agent (and the human) to misread the graph.

2. **Permission.** Junior managers, faced with a strictly top-down model, force every new feature through a full ancestry rebuild. That is slow and often wrong (the new feature reveals what its capability should be, not the other way around). Recognizing bottom-up gives explicit permission to capture the signal first and clarify intent after.

3. **Coherence checks become explicit.** When the graph admits both directions, the framework can name the **coherence check** as its own operation: at the end of a bottom-up cycle, walk up the parent chain and confirm the new node's ancestry still makes sense; if not, revise (via supersede) the upper levels rather than silently incoherently leaving them.

## Consequences

- `framework/SKILL.md` § *The graph* gains a paragraph naming the four modes and the anchor-pending pattern, with a pointer to this ADR.
- `node-templates/SKILL.md` § *How to use a template* gains a point on the anchor-pending pattern: when creating a node whose ancestry isn't fully clear, parent to the closest meaningful ancestor, mark its status `draft`, write "anchor pending" in the Map section, correct via `update_node` later.
- The Engine MCP's validators do **not** reject a node whose parent is in `draft`. That is a legitimate state during anchor-pending. The validators do reject jurisdiction violations, parent-type violations, and illegal status transitions — those remain mechanical.
- Coherence walks (parent chain validation at session close or before declaring a node `done`) become an explicit operation the team can run; not part of the ship initially, but documented as a pattern.
- The four modes are **not** new node types or new statuses. They are descriptions of how the same seven Issue Types and their lifecycles are operated in different moments.

## Alternatives considered

- **Force top-down construction.** Reject creation of any node whose parent is not yet `active`. Rejected because it contradicts how senior product work actually flows; it would force every bottom-up signal to wait for a complete ancestry rebuild before being captured.
- **Allow free creation but stay silent about it.** The framework already allows it (nothing rejects bottom-up creation); not articulating the modes would leave junior users to discover it ad hoc and likely misuse it. Rejected because the value of the framework is in naming the practice, not in hiding it.
- **Introduce a separate "draft-orphan" node type.** Considered for capturing the bottom-up signal explicitly. Rejected because the existing types + `draft` status + the "anchor pending" note in Map already cover it without inflating the catalog.

## Status

Accepted. The framework recognizes four modes of construction and the anchor-pending pattern as the bottom-up half of the loop.
