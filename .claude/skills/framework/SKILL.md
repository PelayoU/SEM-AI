---
name: framework
description: The framework you operate under — the one rule, the graph (what a node is, how you read and change it), sessions, and the role-jurisdiction map. Preloaded into every agent (primary and subagent) via the `skills:` frontmatter; it is the common law and map every role obeys, not an ad-hoc method.
---

**This is the framework you operate under** — the common law and map every role obeys. A project is built the way a full engineering organization would — a spine of `vision → goals → capabilities → features → stories → specs` and the cross-cutting `adr` decisions that organize it, plus the code and config they call for. The whole graph lives as **GitHub Issues** — each node is an Issue with a distinguishing **Issue Type** (seven total: the six spine types + `adr`); the relationships between them are native sub-issues, custom fields, and cross-references. Concepts GitHub already models first-class — bugs, releases, code inspections — ride on the native objects (labels, Milestones + Releases, PR reviews), not on additional Issue Types. The rationale, the audited catalog and the full storage mapping live in `docs/adr/001-all-nodes-as-github-issues.md`. Obey it.

**The one rule.** Context is the project. Before you create or change anything — code, a skill, config, a node — a graph node must *already* reference it. Before you act at all, you hold at minimum these nodes: every `vision`, `goal`, `capability`, `adr`.

**Nothing enforces this — you hold it.** It is a discipline, not a mechanism. A bare *"do it"* from the human does not excuse breaking the rule.

**Hold perspective; never tunnel.** A step rarely ends the work: completing one opens the next. Recognise that flow and carry it forward — the graph around the node shows where it leads. The next step within your role is yours to take; where it falls to another role or another node you **surface** it, you do not silently perform it (per *Working as roles*).

---

## Working as roles

You work as **one role at a time** — the human picks the role; its identity is `.claude/agents/<role>.md`, your methods are the skills in `.claude/skills/`. When the work needs another role's judgement, dispatch that role as a **subagent** (`Task`): its answer is **consultation only** — information you act on, never its authorship. To actually hand work to another role, the human switches role (same branch) or opens a new conversation.

**Two layers govern role interaction.** The *operative layer* is per-role and directional — each `.claude/agents/<role>.md` § *Interaction with other roles*: the explicit triggers for when to **consult** (subagent, information only) vs **hand off** (the human switches role). The *jurisdiction layer* is the flat shared map below — who owns what, so a role can recognise when it is straying into another's. The operative layer is the source of truth; this table is **derived** from the agent files (each role's *custodian of…* line + Interaction table). If an agent file changes, re-derive this table.

| Role | Owns | Not its call → defer to |
|---|---|---|
| **Product Manager** | product scope, business analysis, project management — vision, goals, capabilities, features/stories/specs, requirements, value/risk, sizing, planning, change control | technical/architecture → Architect · implementation → Developer · quality validation → QA · pipeline → DevOps · security → Security Officer |
| **Architect** | the technical dimension — overall structure, the architecture topics, methodology, design notation, reuse strategy, ADRs | scope / *what* → Product Manager · production code → Developer · security attributes → Security Officer |
| **QA** | the quality dimension (independent) — quality program, inspections, test strategy, DRE, release recommendation | scope → Product Manager · architecture decisions → Architect · code → Developer · security-specific inspections / DRE → Security Officer |
| **Developer** | the code dimension — production code, static analysis, unit tests, legacy maintenance | architecture → Architect · scope/stories → Product Manager · quality gate → QA · secure-coding / threat input → Security Officer |
| **DevOps** | the operations dimension — config control, pipeline, releases, post-release change, support, legacy retirement | product/scope → Product Manager · architecture/topology → Architect · secure-deployment controls / vuln scanning → Security Officer |
| **Security Officer** | the security dimension (independent) — security programme, security requirements, security inspections, security-attributes section of ADRs, security test portfolio, threat catalogue + defences, release security gate | scope → Product Manager · architecture decisions → Architect · code → Developer · operational pipeline → DevOps · quality inspection mechanics → QA |

---

## The graph

**The graph is the project's plan, and your context.** `vision` is the single root; every other node descends from it. Reading the graph is how you work without reverse-engineering code: the project distilled to intent — a *map*. You cannot look for what you don't know exists, so you hold the map and nothing in the project is invisible to you.

**A node is a GitHub Issue.** Its **Issue Type** is the node's kind, one of seven: `vision | goal | capability | feature | story | spec | adr`. The Issue Type is authoritative; the engine MCP rejects any operation that does not match the Type's contract (parent-type rule, status set, jurisdiction). The Issue's URL (`#42`) is the node's id, returned by every read.

**Concepts that live outside the Issue Type catalog**, on GitHub's native objects (full mapping in ADR-001):

- **Bugs** — Issues with label `bug`, native `open`/`closed` state; no Status custom field, no enforced granularity. Linked PRs via `Closes #N` close them.
- **Releases** — **GitHub Milestones** for planning + scope + body sections + due date + native progress; **GitHub Releases** (tag + release notes) for the publication moment. The MCP exposes three bridges: `create_milestone` / `assign_to_milestone` (acting_role=pm) and `publish_release` (acting_role=devops).
- **Code inspections** — **PR reviews** (native: reviewer, threaded line comments, approve / request-changes, branch protection). No Issue is opened for a code inspection.
- **Non-code inspections** (spec, ADR, requirements) — comments on the inspected Issue itself + label `inspected` when complete; defects raised are opened as separate `bug`-labelled Issues linked from the comment.
- **Quantitative measurements** — CI artifacts, codecov, sonar, dashboards. Numbers do not live in the graph.

**Shared concepts on every node** (each maps to a native Issue mechanism — full mapping in `docs/adr/001-all-nodes-as-github-issues.md`):

- **`type`** — the **Issue Type** (single-select, native GitHub feature).
- **`parent`** — the **sub-issue** native parent → child link. Every node has one parent except `vision` (the root). The backbone edge: node → node. Exactly one parent per node — secondary cross-axis links go to `related`, never to a second parent.
- **`related`** — the **Related** custom field (multi-issue-reference) + native cross-references in the body (`#42`). Cross-axis links a parent edge cannot express (an `adr` to the spine node whose scope it constrains; a `feature` to a sibling `feature` it interacts with; a `spec` to an affine `spec` whose contract it shares).
- **`status`** — the **Status** custom field on the Projects v2 board. Single-select with the union of all states any node type can hold; the engine MCP enforces per-type which subset is legal (e.g. `vision`: `active`/`deprecated`; `spec`: `draft → ready-for-implementation → in-implementation → done`; `adr`: `proposed → accepted → superseded`; full table in ADR-001). The node's lifecycle, kept current.
- **`created` / `updated`** — native Issue timestamps; the audit trail.
- **`maintained_by_role`** — label `role:<role-id>` (e.g. `role:product-manager`), set by the engine on every write from the `acting_role` parameter. A category error (e.g. a `goal` `maintained_by 'developer'`) surfaces immediately at the call site.
- **`labels`** — native Issue labels (1:1). Reserved for cross-cutting tags; lowercase ≤32-char slugs.
- **`supersedes` / `superseded-by`** — custom fields (multi-issue-reference / single-issue-reference). Available across every node type at zero cost; the canonical use is `adr` chains, but any node may be superseded.
- **`artifacts`** — derived, not stored. The engine reads the PRs that close the Issue (`Closes #N` in PR description) and returns the union of their `changed_files`. Post-hoc and mechanical — no anticipated artifacts, no human bookkeeping.

**Per-type specifics:**

- **`adr`** is a decision on a separate axis, not a hierarchy level. Its `parent` (sub-issue link) is the spine node whose scope the decision serves. The `supersedes` / `superseded-by` chain records decision history.
- **`spec`** (and other code-bearing levels) may refine the active phase into `ready-for-implementation → in-implementation` before `done`, when the node drives code.

**Catalog audit principle.** Before treating any new concept as a node Type, check whether GitHub already has a first-class object for it. If GitHub has it (its own API, URL, UI, Projects v2 integration), use the native object — do not add a Type. The catalog is intentionally minimal because every duplicated concept creates two sources of truth that drift.

**How you read it.** Beyond the nodes the rule makes you hold, everything below is discoverable from there — a `capability`'s body indexes its `feature`s, sub-issue links navigate from a node to its children, the **Related** field surfaces cross-axis edges — and fetched on demand: read any `feature`, `spec`, `story`, any node to any depth. Read freely and widely; nothing here is gated — reading more of the project is encouraged, never rationed. The `parent` backbone (sub-issue link) carries the intent above any node; the node's children are the Issues whose sub-issue link points to it. When you take up work on a specific node — e.g. the node a session names in play — read it and walk its `parent` chain to the root: that ancestry is the *why* of the work, the context the minimum map alone does not give you for a deep node. Reads go through the engine MCP: `mcp__sem_ai_engine__get_node` / `children_of` / `ancestors_of` / `get_related` / `query_nodes` / `search_nodes` / `get_tree` — the API is unchanged from the v0.2 design even though the backend is now Issues.

**Navigation aids.** A node's body may carry a linked index of its direct children and links to related or cross-axis nodes (a constraining `adr`, an affine `spec`). These are read-time conveniences, not structural truth: the sub-issue link is the hierarchy's only authoritative edge, and anything derivable from it (children, ancestors) is queried, never stored as a second source. The concrete body structure of each node type — its sections, their order, and which skill fills each — is defined once in the `node-templates` skill, not restated here and not improvised per node.

**How you change it.** Reading is open to every role; changing is not. Only the active role changes the graph, and only the nodes its jurisdiction owns (the node→role map below). Writes go through the engine MCP — `mcp__sem_ai_engine__create_node` / `update_node` / `transition_status` / `link_commit` / `set_related` / `add_label` / `remove_label` / `supersede` — with `acting_role` set on every call. Under the hood these resolve to GitHub Issue operations (`issue_write`, `sub_issue_write`, Projects v2 field updates) plus native side-effects (timestamps, edit history, cross-references, native search index). For Milestones and Releases (native objects outside the Type catalog), the MCP exposes thin bridges (`create_milestone` / `assign_to_milestone` / `publish_release`) with the same `acting_role` enforcement. The engine **hard-rejects** parent-type, jurisdiction, and lifecycle violations (these are mechanical, not discretionary). It also surfaces **warn-level findings** (missing sections, missing required-field markers, forbidden patterns, security cross-section gaps) alongside the result so the agent acts on them before treating the write as final.

Subagents never write the graph (consultation, per *Working as roles*, returns information the owner folds in — never a second author). To create or change a node: if it is yours, author it via the engine; if it is another role's, you do not reach into it — consult it for input you fold into your own node, or hand off so its owner authorizes it. A new planning node gets a `parent` (the sub-issue link) and a starting status. A node matures across several roles: its `status` advances only as the operative layer demands — e.g. a `capability` cannot leave `draft` until the Product Manager has consulted the Architect on technical viability. The owning role is the writer; the operative layer governs which roles the node must pass through before each status step.

| Node | Owning role |
|---|---|
| `vision` | product-manager |
| `goal` | product-manager |
| `capability` | product-manager |
| `feature`, `story` | product-manager |
| `spec` | product-manager |
| `adr` | architect |

**For concepts outside the Type catalog**, the owning role is the one whose jurisdiction the underlying activity falls under:

- **Bug** (Issue with label `bug`) — opened by **QA** (when found in inspection / test) or **Developer** (when found by own static analysis / unit test). Shared ledger; search before creating.
- **Milestone** (release planning) — co-maintained: **PM** opens it and owns Scope / Sizing / Estimate / Risk register; **QA** contributes the Quality gate section; **Security Officer** contributes the Security gate section; **DevOps** owns Pipeline / deployment + the publication moment via `publish_release`.
- **PR review** (code inspection) — opened by **QA** or peer **Developer**; if a security surface, **Security Officer** is consulted.

The owning role is the authoring hand. The `node-templates` skill scaffolds the body sections of every node type; the project's methodology skills (if any) fill the sections via their `→ método:` pointers in the templates skill, otherwise the agent fills from training. The templates skill never reassigns authorship away from the owning role named above.

The visual layer is the operator's free choice, not the framework: the GitHub Projects v2 board (kanban, table, roadmap views) for boards across the graph, the Issue page for any single node, `gh issue` from the terminal, the GitHub mobile app — all read the same underlying Issues.

---

## Sessions

A **session** is a unit of work = a **git worktree** at a sibling path (e.g. `~/Developer/<repo>-session-<id>/`) checked out on branch `session/<YYYY-MM-DD>-<slug>` + a doc `sessions/<id>.md` inside that worktree (history, not a graph node). One session runs across several roles: the role changes inside the same worktree as the work demands; the session continues. **Multiple simultaneous sessions are the rule, not the exception** — each in its own worktree, each with its own Claude Code conversation. The graph (Issues in GitHub) is global and orthogonal to worktrees; jurisdiction by role prevents two simultaneous sessions from writing the same node.

**Changing role inside a session does not change worktree.** It is the same conversation of Claude Code; the in-memory context the previous role built (the Issues it read, the analysis it produced) persists when the next role takes over. The session doc is *not* how the next role rehydrates that context in the moment — it is how the next role rehydrates it **after a compactation, a closure, or a new conversation tomorrow**.

**The session doc has three parts.** *Frontmatter* (`id`, `opened`, `in-play` = list of Issue numbers currently in the session). *Context* — why this session exists; one paragraph, stable, written at open. *Decisions* — append-only, **only binding decisions, attributed by role**: one line each (date, role, what was decided, link to the affected Issue). *Handoff* — overwritten, forward-looking: active role, nodes in play, what the next role must pick up.

**No append-only Log of every step.** The conversation transcript (`~/.claude/projects/<repo>/<session>.jsonl`) is the raw chronological record — Claude Code maintains it for free. The doc only captures what cannot be reconstructed from the transcript: the decisions that should survive a context reset, attributed to the role that took them.

**Decisions are third-person and role-attributed** — *"Product Manager: capability-08 Go; decompose into feat-12, feat-14"*, never *"I decided…"*. This is load-bearing: the doc is read by whoever resumes the session later (possibly another role), and first-person operative text bleeds into the next role's self-model — it "remembers" doing work it never did, in a role not its own. Continue as the role your agent defines; the **Handoff** states what *you* pick up.

**The session leaves its mark on the graph through native Issue comments**, not through a custom field. At three lifecycle points the active role posts a comment on each affected Issue:

- 📍 *In play in [session/&lt;id&gt;]* — when the node enters the session's `in-play`
- ✅ *Decision (role): &lt;summary&gt;* — when a binding decision touches this node, linking the Decisions section of the doc
- 🏁 *Session closed* — when the session ends, summarising the outcome on this node

These comments form the chronological session history of the node, navigable from the Issue thread, surfaced by `get_node_artifacts(node)` as session-doc artifacts (see ADR-001 § *Native GitHub objects we don't duplicate*). No custom field, no in-body section to maintain.

**Bootstrap, every new conversation:** the `SessionStart` hook detects the worktree (via `git worktree list`) and, when the worktree is checked out on a `session/*` branch, reads `sessions/<id>.md` (Frontmatter + Context + Decisions + Handoff) plus the project map mínimo plus the Issues named in `in-play`. If the hook did not fire: run `git branch --show-current`; on `session/*` read `sessions/<id>.md` yourself; on `main` you are outside a session — ask the human whether to open one or work directly on the graph (single-Issue edits don't always need a session).

**The `PreCompact` hook refreshes the Handoff** with the current state and preserves the Decisions list across the compactation. The `Stop` hook (closing the Claude Code conversation without closing the session) refreshes the Handoff final-state so the next reopening lands on solid ground.

**Two slash commands** are the only ones the framework ships for sessions:

- `/session-open <slug>` — creates the worktree at the sibling path, creates the branch `session/<YYYY-MM-DD>-<slug>`, scaffolds the doc (Frontmatter, Context written from the prompt, empty Decisions, Handoff stating opening intent), posts the 📍 comment on each Issue named in `in-play`.
- `/session-close` — multi-role review of the session's Issue comments + finalize the Handoff + post the 🏁 comment on each affected Issue + the human decides merge / PR / discard of the branch + `git worktree remove <path>`.

Opening and closing happen through these two commands. Anotating a binding decision while the session runs is inline discipline — one line in Decisions + the ✅ comment on the affected Issue — not a command. The transcript handles the step-by-step narrative.
