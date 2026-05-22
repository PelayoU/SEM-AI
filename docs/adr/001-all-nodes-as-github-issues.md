# ADR-001 — All graph nodes live as GitHub Issues

- **Status**: accepted
- **Date**: 2026-05-23
- **Supersedes**: —
- **Superseded by**: —

## Context

The framework's substrate is a typed project-intent graph: vision → goal → capability → feature → story → spec, plus cross-axis ADRs, plus operational nodes (defect, measurement, inspection), plus release deliveries. The roles read and write this graph through a typed engine MCP, on artifacts the human and the AI agents share.

Earlier iterations explored multiple storage models for these nodes:
- v0.1: SQLite + custom MCP + React UI (custom storage, custom UX)
- v0.2: markdown files in `sem-ai/<type>/<slug>.md` + `docs/adr/<slug>.md` (storage in repo files)
- v0.2 hybrid: markdown spine + GitHub Issues for operational tier

Through extended design discussion the framework converged on a single uniform storage model: **all graph nodes live as GitHub Issues**. This document records that decision and the rationale.

## Decision

Every graph node — regardless of type — lives as a **GitHub Issue** with a distinguishing **Issue Type** (Vision / Goal / Capability / Feature / Story / Spec / ADR / Defect / Measurement / Inspection / Release).

GitHub Releases (native git tag + release notes) remain as a separate artifact for the publication moment of a release; the **Release** Issue Type tracks the planning + scope + quality / security gates while the release is being built, and links to the eventual GitHub Release as the published artifact.

Session logs remain as markdown files in `sessions/<id>.md` on a `session/*` branch — they record cross-Issue work narrative for one work session, distinct from any single Issue.

Code lives in the repo as files on branches, with PRs that close Issues via `Closes #N` — unchanged from any normal GitHub workflow.

## Why this storage model

**1. Maximum native UX.** GitHub Projects v2 indexes Issues + PRs natively; it does **not** index arbitrary repo files. To get kanban boards, table-grouped-by-parent views, roadmap timelines, custom fields per node, native sub-issue hierarchy with expand / collapse — all over the full graph (Vision → Spec) — the nodes have to be Issues. Markdown in the repo gets the file browser and grep; it does not get Projects v2.

**2. Jurisdiction enforced by construction eliminates the conflict problem branches were designed to solve.** The framework's role-jurisdiction matrix is mechanical: PM only writes vision / goal / capability / feature / story / spec / release; Architect only ADRs; QA only measurement / inspection / defect-inspection-origin; Developer only code + defect-static-analysis-origin; Security Officer only contributes sections into other roles' Issues. Two roles can never write the same Issue simultaneously. Branches for node storage become redundant.

**3. Live visibility is a feature, not a bug.** When the Architect approves an ADR right now, every other role needs to see it AT ONCE, not at the next git pull. Issues update in real time; markdown on a branch hides work until merge. The framework's role-coordination model depends on real-time visibility of decisions.

**4. PR review survives where it matters most.** Code is still files on branches, PR-reviewed line-by-line. PRs implementing a Spec close the Spec Issue on merge. The PR-review-as-gate is preserved for code. Node body edits use the Issue's edit history (version-vs-version, suitable for prose where line-by-line diff is not the right shape).

**5. One uniform storage model is structurally cleaner.** One mental model, one backend, one API surface for the engine MCP. The agent calls `create_node(type="defect", parent="spec-001", ...)` and never has to know which storage tier this node lives in — there is one tier.

## Trade-offs accepted

- **No `git diff` line-by-line on node body edits.** Replaced by Issue edit history (each save creates a version; comparison is full-text version-vs-version). Acceptable because node bodies are prose where full-version comparison is more legible than line diffs.
- **No branch + PR for individual node changes.** Acceptable because jurisdiction enforcement eliminates the concurrency conflict branches solve. Rare large restructures coordinate via Discussion + an ordered series of edits.
- **GitHub Releases sit outside Projects v2 boards.** Acceptable because the Release Issue Type provides the kanban / planning visibility; the GitHub Release is the publication artifact (user-facing tag + notes), which is the right tool for that role.
- **Some industry convention is bent.** ADRs traditionally live in `docs/adr/` markdown (Nygard 2011). Making them Issues with Issue Type=ADR is unusual. The bend is acceptable because (a) the supersede chain still works via custom fields, (b) the body content stays the same prose, (c) the gain in unified board UX outweighs the convention.

## How it works (the "frontmatter equivalent" in Issues)

Every concept the v0.2 YAML frontmatter encoded maps to a native Issue mechanism:

| Concept | Mechanism in Issues |
|---|---|
| `type` | **Issue Type** (native GitHub feature, single-select; first-class field per Issue) |
| `parent` (one, canonical) | **sub-issue** (native parent / child relationship via the `sub_issue_write` API) |
| `related` (N, cross-axis) | **custom field** "Related" (multi-issue-reference) + native cross-references (`#42` in body) |
| `status` (per-type values) | **Projects v2 custom field "Status"** (single-select with the union of all states); the engine MCP enforces per-type which values are legal — e.g. `defect` accepts `open / triaged / in-progress / fixed / verified / closed`; `vision` accepts only `draft / active / deprecated / superseded` |
| `created` / `updated` | native Issue timestamps |
| `maintained_by_role` | label `role:<role-id>` (or custom field) — set by the engine on every write from the `acting_role` parameter |
| `labels` | native Issue labels (1:1) |
| `supersedes` / `superseded-by` | **custom fields** "Supersedes" (multi-issue-reference) / "Superseded by" (single-issue-reference); available across all node types but used canonically for ADRs |
| `artifacts` (files this node touches) | **derived automatically** from the PRs that close the Issue (`Closes #N` in PR description). Each linked PR contributes its `changed_files`; the engine MCP query `get_node_artifacts(node)` returns the union. No anticipated / predicted artifacts — only post-hoc, mechanical record |

The engine MCP's API surface is unchanged from prior iterations (the 19 typed tools: `create_node`, `update_node`, `transition_status`, `link_commit`, `set_related`, `add_label`, `remove_label`, `supersede`, `query_nodes`, `search_nodes`, `get_node`, `children_of`, `ancestors_of`, `get_related`, `get_tree`, `estimate_size`, `validate_node`, `get_project_map`, `get_instance_config`). The backend changes from "markdown files + frontmatter parser" to "GitHub Issues + sub-issue API + Projects v2 custom fields", but the agent calling `create_node(type="defect", parent="spec-001", origin="coding", severity="sev-3", acting_role="developer")` sees no difference.

## Status validation per type

GitHub Projects v2 exposes one "Status" single-select field at board level — its option values are the **union** of all states any node type can hold. The engine MCP enforces per-type which subset is legal:

- `vision`: `active` / `deprecated` (rarely changes)
- `goal`: `draft` → `active` → `done` / `deprecated`
- `capability`: `draft` → `active` → `done` / `deprecated`
- `feature`, `story`: `backlog` → `in-progress` → `review` → `done` / `deprecated`
- `spec`: `draft` → `ready-for-implementation` → `in-implementation` → `done` / `deprecated`
- `defect`: `open` → `triaged` → `in-progress` → `fixed` → `verified` → `closed`
- `measurement`, `inspection`: `recorded` (terminal — facts do not have a lifecycle)
- `adr`: `proposed` → `accepted` → `superseded` / `deprecated`
- `release`: `planning` → `in-development` → `in-testing` → `released` / `cancelled`

Projects v2 shows all values in the single "Status" dropdown; the engine MCP rejects `create_node(type="vision", status="open")` because `open` is not in vision's legal set. The user sees a sensible error.

## Read patterns

- `children_of(node)`: returns the union of (a) sub-issues native to the parent, (b) Issues with label `parent:<node-id>` (for cases where multi-parent might be modelled via labels — by current convention, secondary parents go to `related` instead), (c) cross-referenced Issues for related semantics.
- `parents_of(node)`: returns the single sub-issue parent (or none if root).
- `related_to(node)`: returns the "Related" custom field references + native cross-references.
- `query_nodes(type=, status=, parent=, ...)`: filters via Issue search.
- `search_nodes(query)`: substring search via GitHub's native Issue search API.

## Read cost honest expectation

Reading nodes via the GitHub API is ~5–50× slower per call than reading markdown files locally (API latency ~100–500 ms vs file read ~5–20 ms). For typical agent sessions (5–30 reads), the absolute latency stays under 5 seconds total — noticeable but functional. Mitigations:
- The `SessionStart` hook pre-loads the at-minimum project map in one batched `list_issues` call.
- The engine MCP keeps an in-process cache within a single MCP session.
- Heavy operations (full tree walks, broad searches) batch via `list_issues --search <filter>` rather than per-node fetches.

If sustained operation reveals latency as a real friction, a local cache layer (`.cache/sem-ai-issues/` mirroring Issue contents on disk) can be added as a transparent optimisation without changing the storage model. Deferred until the friction is observed.

## Alternatives considered

- **Markdown spine in repo (no Issues).** Diff-friendly + PR-reviewable but loses Projects v2 visibility entirely. Rejected for the operational tier; the strategic spine was considered but losing Projects v2 board for the whole graph defeats the team UX argument.
- **Hybrid (markdown spine + Issues operational).** The natural compromise. Rejected because (a) the dual storage model imposes a mental tax, (b) Projects v2 boards then only show half the graph, (c) jurisdiction enforcement already removes the diff/branch advantage of markdown for nodes.
- **Projects v2 draft items (no backing Issues).** Lightweight but no URL outside the Project, no labels, no native search, no sub-issues, no PR linkage. Rejected.
- **External tracker (Jira / Linear / Azure DevOps).** Forces every adopter onto a specific platform. Rejected — the framework should be installable on a GitHub repo without further licensing or vendor commitment.

## Consequences

- All Issue-backed node types replace markdown-file-backed nodes for the strategic spine + operational tier.
- The `sem-ai/` and `docs/adr/` markdown directories from v0.2 are not part of v0.3 (except for this ADR which lives as markdown until the Issues backend is wired and we migrate it as an Issue with Type=ADR).
- A one-shot migration script will create Issues from any historical markdown nodes (none in the current repo since the clean-slate commit removed them).
- A `scripts/setup-github-project.sh` script provisions the Projects v2 board with the Issue Types + custom fields + saved views needed.
- The engine MCP backend reads / writes via the GitHub MCP (`mcp__github__*`) for Issue operations; via `gh release` CLI for the GitHub Release publication step.
- The `framework` skill and `node-templates` skill need rewriting to reflect Issue-backed storage instead of markdown frontmatter.

This ADR itself lives as `docs/adr/001-all-nodes-as-github-issues.md` for now. Once the engine MCP + Issue-backed storage ship, it will be migrated to an Issue with Type=ADR (eat-our-own-dogfood marker); the markdown file stays in git history as the original record.
