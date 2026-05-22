---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-22
updated: 2026-05-22
maintained_by_role: architect
supersedes:
  - adr-008-markdown-frontmatter-data-format
---

# ADR 019 — Markdown body + tiny YAML frontmatter as canonical data format

## Context & forces

v0.1 stored the spine in SQLite. Branching was impossible; PRs could not diff intent; the `body` column was opaque markdown that the SQL layer could not query without parsing.

For v0.2 we need:

- Branching (sessions on `session/*` branches).
- PR-friendly diffs (the discovery → validation collapse requires reviewers seeing the change).
- Machine-readable structural queries (parent / status / role / labels) without parsing the whole body.
- Body content that humans author conversationally (markdown).

## Decision

**Markdown body + tiny YAML frontmatter** as canonical data format for the strategic spine.

Frontmatter ≈ 7 fields, all queryable by the engine without parsing the body:

```yaml
---
type: <vision | goal | capability | feature | adr>
parent: <parent-slug>            # absent for vision
status: <draft | active | ready-for-implementation | in-implementation | done | superseded | deprecated>
created: YYYY-MM-DD
updated: YYYY-MM-DD
maintained_by_role: <role-id>
labels:                           # optional
  - mvp:go
  - horizon:release
# ADR-only extras
supersedes:                       # ADR chain integrity
  - adr-NNN-slug
superseded-by:
  - adr-NNN-slug
---
```

Body: markdown, templated section headers per `instance/node_types.yaml`. Validators parse body via `mistune` AST only for warn-level findings (sections present, required fields, forbidden patterns, security cross-section). Determinism comes from frontmatter.

## Overall structure

Two-zone file: frontmatter (machine-queried) + body (human-authored, lightly validated).

## Data structure

| Field | Type | Source | Indexed |
|---|---|---|---|
| type | enum-string | filename folder | yes (file path) |
| parent | string (slug) | frontmatter | yes |
| status | enum-string | frontmatter | yes |
| created / updated | ISO date | frontmatter | yes |
| maintained_by_role | enum-string | frontmatter | yes |
| labels | list[string] | frontmatter | yes |
| supersedes / superseded-by | list[string] | frontmatter | yes |
| body | markdown | file body | no (AST-parsed for warnings) |

The id is **derived from the file path**, not stored in frontmatter. `sem-ai/goals/01-self-bootstrap-validation.md` → id `goal-01-self-bootstrap-validation`. Removing redundancy keeps the schema honest: there is one place that names the node (its path).

## Interfaces to the outside world

`engine.graph_walker.parse_node_file(path, instance)` is the canonical reader. PyYAML for the frontmatter; mistune (AST) for body-level warn parsing.

## Decomposition into functional components

`engine/graph_walker.py` parses frontmatter; `engine/validators.py` operates on body via regex (current) or AST (future). The two are decoupled — a body that fails warn-level checks still has a valid Node.

## Linkage / information transmission

Frontmatter `parent` is the spine's only authoritative edge. Children are *queried*, never stored as a second source. The cross-axis `supersedes`/`superseded-by` for ADRs is the only exception, and lives on the ADR itself (the chain root).

## Performance attributes

Frontmatter parse: ~0.1 ms per file (PyYAML). Body AST parse: ~5 ms per file (mistune). Full spine walk on 100 nodes: ~50 ms. Cache via in-memory dict on the MCP server if the spine grows beyond ~10 000 nodes.

## Security attributes

Dispatched to Security Officer.

- PyYAML uses `safe_load` only (no `Loader=`); no Python-object construction via YAML tags.
- Body content is markdown, not executed code; the validators read text only.
- The mistune AST is structural; we never `eval` or template-render body text.

## Style: chosen + rejected

- **Chosen**: markdown + tiny YAML frontmatter. Branchable, PR-friendly, machine-queryable.
- **Rejected**: SQLite (v0.1). No branching; no PR diff.
- **Rejected**: pure YAML for nodes (no markdown). Body content (vision narrative, ADR consequences, feature stories) is prose; forcing it into YAML strings is hostile to authors.
- **Rejected**: rich YAML frontmatter (deep nested objects for queryable fields). Forces the body to lose its semantic structure (## Section headers carry meaning); the user pushed back on this directly in the design discussion ("pero entonces para qué necesitamos yaml?").
- **Rejected**: JSON frontmatter. YAML's comments + multi-line strings make it more author-friendly.

## Consequences

- Every spine change is a markdown diff; PRs show meaningful change.
- Branches name sessions; multiple humans can work in parallel without merging conflicts in a shared DB.
- File renames carry semantic change (the id is the path); a rename is a deliberate act.
- Loss: the schema is enforced lazily (at write time, by the engine validators). A malformed frontmatter is detected only when the file is read — not at "schema commit" time. Mitigation: `sem-ai-validate` GitHub Action validates every PR before merge.

## Design inspection

This very file is a worked example: the frontmatter is the 7 + 2 ADR-only fields, the body is templated per `instance/node_types.yaml::adr.sections`, and the file path encodes the id (`adr-019-markdown-yaml-frontmatter-canonical`).
