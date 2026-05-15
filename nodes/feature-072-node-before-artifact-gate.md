---
category: feature
id: feature-072-node-before-artifact-gate
parent: "[[cap-01-vision-to-code-audit]]"
artifacts:
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[.claude/settings.json]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Feature 072 — Hard node-before-artifact enforcement gate

> Authored via `po-feature-decomposition`. Delivers the structural mechanism that turns cap-01's "every code-affecting artifact traces to a node" from a *navigable* property into an *enforced* one. Relates to [[adr-004-substrate-content-separation]] (it enforces that split) and the `2026-05-14` session's deferred *graph-vs-substrate operating rule* candidate.

## What it delivers

A Claude Code `PreToolUse` hook that **denies** any `Write`/`Edit`/`Bash` that creates or mutates a substrate path unless a management node in `nodes/` references that path in its `artifacts:` frontmatter. No "the human told me to" escape; not overridable by permission mode or `--dangerously-skip-permissions`. The only legitimate path to a substrate change is authoring the governing node first ("van primero los nodos").

## Story Map position (Patton via slide 132)

- **Activity (Epic):** structural enforcement of traceability.
- **Task:** this feature.
- **Release slice:** walking skeleton of the hard-enforcement layer.

## Stories (children)

- `[[story-072-A-deny-ungoverned-substrate-write]]` — As the framework, I want an ungoverned substrate Write/Edit denied, so node-before-artifact is enforced, not audited.
- `[[story-072-B-deny-bash-side-channel-write]]` — As the framework, I want Bash side-channel writes into substrate denied likewise.
- `[[story-072-C-allow-governed-and-ignore-nonsubstrate]]` — As a contributor, I want governed substrate writes and all non-substrate writes to pass without friction.

## Spec sibling

- `[[spec-072-node-before-artifact-gate]]`

## Notes

C0 search-before-create: `.claude/settings.json` had no governing node (pre-existing gap) — this feature closes it by listing it in `artifacts:`. The hook script path is shared with [[feature-075-hard-role-jurisdiction]] (same file, both checks). Bash-write parsing is heuristic; the residual bypass surface is documented in [[adr-011-hard-enforcement-no-human-override]].

## Source

- Skill: `po-feature-decomposition`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54 (feature definition) + slide 56 (5 Cs). Governance node — light `## Source` per template; conceptual lineage (configuration-control discipline) is recorded in the ADR `## Context`, not duplicated here.
