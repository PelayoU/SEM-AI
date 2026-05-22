# ADR-001 — All graph nodes live as GitHub Issues

- **Status**: accepted
- **Date**: 2026-05-23
- **Supersedes**: —
- **Superseded by**: —

## Context

The framework's substrate is a typed project-intent graph: vision → goal → capability → feature → story → spec, plus cross-axis ADRs. The roles read and write this graph through a typed engine MCP, on artifacts the human and the AI agents share.

Earlier iterations explored multiple storage models for these nodes:
- v0.1: SQLite + custom MCP + React UI (custom storage, custom UX)
- v0.2: markdown files in `sem-ai/<type>/<slug>.md` + `docs/adr/<slug>.md` (storage in repo files)
- v0.2 hybrid: markdown spine + GitHub Issues for operational tier

Through extended design discussion the framework converged on a single uniform storage model: **all graph nodes live as GitHub Issues**. A subsequent audit then reduced the catalog to the minimum that GitHub does not already cover natively. This document records the decision and the audited catalog.

## Decision

Every graph node — regardless of type — lives as a **GitHub Issue** with a distinguishing **Issue Type**. The framework ships **seven** Issue Types:

```
spine:       vision, goal, capability, feature, story, spec
cross-axis:  adr
```

Other concepts the framework cares about (bugs, releases, code inspections, deliberation) ride on GitHub's native first-class objects rather than being modelled as additional Issue Types. The full mapping is in *Catalog audit* below.

Session logs remain as markdown files in `sessions/<id>.md` on a `session/*` branch — they record cross-Issue work narrative for one work session, distinct from any single Issue.

Code lives in the repo as files on branches, with PRs that close Issues via `Closes #N` — unchanged from any normal GitHub workflow.

## Why this storage model

**1. Maximum native UX.** GitHub Projects v2 indexes Issues + PRs natively; it does **not** index arbitrary repo files. To get kanban boards, table-grouped-by-parent views, roadmap timelines, custom fields per node, native sub-issue hierarchy with expand / collapse — all over the full graph (Vision → Spec) — the nodes have to be Issues. Markdown in the repo gets the file browser and grep; it does not get Projects v2.

**2. Jurisdiction enforced by construction eliminates the conflict problem branches were designed to solve.** The framework's role-jurisdiction matrix is mechanical: PM only writes vision / goal / capability / feature / story / spec; Architect only ADRs; QA contributes inspections via PR review comments and opens `bug`-labelled Issues; Developer writes code and opens `bug`-labelled Issues for self-found defects; DevOps owns Milestones / Releases; Security Officer only contributes sections into other roles' Issues. Two roles can never write the same Issue simultaneously. Branches for node storage become redundant.

**3. Live visibility is a feature, not a bug.** When the Architect approves an ADR right now, every other role needs to see it AT ONCE, not at the next git pull. Issues update in real time; markdown on a branch hides work until merge. The framework's role-coordination model depends on real-time visibility of decisions.

**4. PR review survives where it matters most.** Code is still files on branches, PR-reviewed line-by-line. PRs implementing a Spec close the Spec Issue on merge. The PR-review-as-gate is preserved for code. Node body edits use the Issue's edit history (version-vs-version, suitable for prose where line-by-line diff is not the right shape).

**5. One uniform storage model is structurally cleaner.** One mental model, one backend, one API surface for the engine MCP. The agent calls `create_node(type="spec", parent="feature-12", ...)` and never has to know which storage tier this node lives in — there is one tier.

## Catalog audit principle

**Before adding an Issue Type, check whether GitHub already has a first-class object for that thing.** If GitHub has it (its own API, its own URL, its own UI, its own integration with Projects v2), use the native object and, where the agent needs to operate it, expose a thin bridge in the engine MCP. Do not duplicate. Reasons:

- Duplication creates two places where the same concept lives, which drift.
- Native objects get GitHub's UX investment for free (progress bars, native filters, search index, notifications, mobile app).
- A reduced catalog is faster to learn and harder to misuse.

The seven Issue Types that survived the audit are the ones GitHub does **not** model natively — they are pure intent-of-product objects whose semantics the framework defines.

## Native GitHub objects we don't duplicate

| Concept | What GitHub gives natively | What that replaces |
|---|---|---|
| **Bug** | Issue + label `bug` + native `open`/`closed` state | A would-be `defect` Issue Type. The lifecycle granularity (triaged / in-progress / verified) is left to project methodology — the framework only requires the label. Linked PRs via `Closes #N` resolve the close. |
| **Release planning** | **GitHub Milestone** (title, markdown description, due_on, state, assigned Issues, progress bar, own URL) | A would-be `release` Issue Type. The Milestone body holds Scope / Sizing / Estimate / Risk register / Quality gate / Security gate sections. Issues assigned to the Milestone are its scope (no `related` field needed). |
| **Release publication** | **GitHub Release** (git tag + release notes + binaries) | The publication moment of the Milestone. When the Milestone closes, DevOps publishes the Release with `publish_release(milestone, tag, notes)`. |
| **Code inspection** | **PR review** (reviewer, threaded line-by-line comments, approve / request-changes / comment, branch protection) | A would-be `inspection` Issue Type for code. Code inspections live entirely in PR reviews. |
| **Spec / ADR inspection** | Comments on the spec or ADR Issue itself + label `inspected` when complete | A would-be `inspection` Issue Type for non-code artifacts. Defects raised by the inspection are opened as separate `bug`-labelled Issues linked from the inspection comment. |
| **Quantitative measurements** | CI artifacts, codecov, sonar, dashboards | A would-be `measurement` Issue Type. Numbers live in tooling, not in the graph. |
| **Pre-formal deliberation** | Issue comments on the ADR while in `proposed` state (the conversation that matures it to `accepted`) | A would-be `discussion` recognition. Discussions as a GitHub feature exist; the framework neither requires nor forbids them — if a team uses them, it's outside the framework's concern. |

## How it works (the "frontmatter equivalent" in Issues)

Every concept the v0.2 YAML frontmatter encoded maps to a native Issue mechanism:

| Concept | Mechanism in Issues |
|---|---|
| `type` | **Issue Type** (native GitHub feature, single-select; first-class field per Issue) |
| `parent` (one, canonical) | **sub-issue** (native parent / child relationship via the `sub_issue_write` API) |
| `related` (N, cross-axis) | **custom field** "Related" (multi-issue-reference) + native cross-references (`#42` in body) |
| `status` (per-type values) | **Projects v2 custom field "Status"** (single-select with the union of all states); the engine MCP enforces per-type which values are legal |
| `created` / `updated` | native Issue timestamps |
| `maintained_by_role` | label `role:<role-id>` — set by the engine on every write from the `acting_role` parameter |
| `labels` | native Issue labels (1:1) |
| `supersedes` / `superseded-by` | **custom fields** "Supersedes" (multi-issue-reference) / "Superseded by" (single-issue-reference); available across all node types but used canonically for ADRs |
| `artifacts` (files this node touches) | **derived automatically** from the PRs that close the Issue (`Closes #N` in PR description). Each linked PR contributes its `changed_files`; the engine MCP query `get_node_artifacts(node)` returns the union. No anticipated / predicted artifacts — only post-hoc, mechanical record |

The engine MCP's API surface includes 19 typed tools for graph operations (`create_node`, `update_node`, `transition_status`, `link_commit`, `set_related`, `add_label`, `remove_label`, `supersede`, `query_nodes`, `search_nodes`, `get_node`, `children_of`, `ancestors_of`, `get_related`, `get_tree`, `estimate_size`, `validate_node`, `get_project_map`, `get_instance_config`) **plus three Milestone/Release bridges** introduced by this ADR (see *Milestone and Release operations* below).

## Status validation per type

GitHub Projects v2 exposes one "Status" single-select field at board level — its option values are the **union** of all states any node type can hold. The engine MCP enforces per-type which subset is legal:

- `vision`: `active` / `deprecated` (rarely changes)
- `goal`: `draft` → `active` → `done` / `deprecated`
- `capability`: `draft` → `active` → `done` / `deprecated`
- `feature`, `story`: `backlog` → `in-progress` → `review` → `done` / `deprecated`
- `spec`: `draft` → `ready-for-implementation` → `in-implementation` → `done` / `deprecated`
- `adr`: `proposed` → `accepted` → `superseded` / `deprecated`

Bugs use the native Issue `open`/`closed` state — no Status custom field, no enforced granularity. Milestones use the native `open`/`closed` state.

Projects v2 shows all values in the single "Status" dropdown; the engine MCP rejects `create_node(type="vision", status="proposed")` because `proposed` is not in vision's legal set. The user sees a sensible error.

## Milestone and Release operations

The engine MCP adds three bridges to operate Milestones and Releases without leaving the MCP, with `acting_role` enforcement:

| Tool | `acting_role` required | Purpose |
|---|---|---|
| `create_milestone(title, due_date, body)` | `pm` | Opens a new Milestone for a release; body holds Scope / Sizing / Estimate / Risk register sections |
| `assign_to_milestone(node_id, milestone)` | `pm` | Adds a feature / spec / story to the Milestone's scope (native milestone assignment) |
| `publish_release(milestone, tag, notes)` | `devops` | Closes the Milestone and publishes the GitHub Release (native tag + release notes) |

Milestones are **co-maintained** objects:

| Body section | Maintained by |
|---|---|
| Scope, Sizing, Estimate, Risk register | PM |
| Quality gate | QA (consulted by PM) |
| Security gate | Security Officer (consulted by PM) |
| Pipeline / deployment | DevOps |

The MCP enforces the split: `update_milestone` accepts a section identifier and only allows the role that owns that section to write it.

## Read patterns

- `children_of(node)`: returns sub-issues native to the parent + Issues with `related` cross-reference where appropriate (by current convention, secondary parents go to `related` instead of duplicating the sub-issue link).
- `parents_of(node)`: returns the single sub-issue parent (or none if root).
- `related_to(node)`: returns the "Related" custom field references + native cross-references.
- `query_nodes(type=, status=, parent=, milestone=, label=, ...)`: filters via Issue search; `milestone=` filters by Milestone assignment.
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
- **Maximalist catalog (11 Issue Types: vision/goal/capability/feature/story/spec/adr/release/defect/measurement/inspection).** The first version of this ADR. Rejected after audit because `release`, `defect`, `measurement`, and `inspection` (for code) duplicate GitHub-native objects (Milestone+Release, label, CI tooling, PR review). The seven that survived are the ones GitHub does not model natively.

## Consequences

- All Issue-backed node types replace markdown-file-backed nodes for the strategic spine + ADR cross-axis.
- The `sem-ai/` and `docs/adr/` markdown directories from v0.2 are not part of v0.3 (except for this ADR which lives as markdown until the Issues backend is wired and we migrate it as an Issue with Type=ADR).
- A one-shot migration script will create Issues from any historical markdown nodes (none in the current repo since the clean-slate commit removed them).
- A `scripts/setup-github-project.sh` script provisions the Projects v2 board with the 7 Issue Types + custom fields + saved views + the `bug` label needed.
- The engine MCP backend reads / writes via the GitHub MCP (`mcp__github__*`) for Issue operations; via `gh milestone` + `gh release` CLI (wrapped) for the Milestone/Release bridges.
- The `framework` skill and `node-templates` skill need updating to reflect the reduced 7-type catalog and the native-mechanism bridges (separate commits follow this ADR).

This ADR itself lives as `docs/adr/001-all-nodes-as-github-issues.md` for now. Once the engine MCP + Issue-backed storage ship, it will be migrated to an Issue with Type=ADR (eat-our-own-dogfood marker); the markdown file stays in git history as the original record.
