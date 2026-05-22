---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-22
updated: 2026-05-22
maintained_by_role: architect
supersedes:
  - adr-004-substrate-content-separation
  - adr-007-obsidian-as-editor-surface
---

# ADR 016 — Pivot the substrate to GitHub-backed (files + Issues + Releases)

## Context & forces

v0.1 shipped a SQLite-backed substrate with a custom 18-tool TypeScript MCP and a 9-lens React UI (`mcp/` + `ui/`). 81 / 81 tests green; 11 node types; FP auto-estimate; 4 hooks; 6 agents. **But the architecture was wrong**: SEM-AI was reimplementing storage + UI that GitHub already provides — ~6 000 lines of TS+React with no business existing.

Forces converging on the pivot:

- Branching. SQL has no branching; intent could not fork. Markdown + git does.
- PR-forced review. The vision's *"discovery → validation"* collapse needs every spine change to face a reviewer. PRs do this natively; SQL writes do not.
- Operational kanban. Feature / story / spec / defect are kanban-shaped — Issues with labels match the data shape; SQL rows did not.
- Releases. GitHub Releases already exist with notes, tags, attachments; the v0.1 `release` node type duplicated all of it.
- Ecosystem. GitHub gives free CI (Actions), Discussions, ProjectsV2, sub-issues — every layer of our UI was a worse version of these.
- Token economy. 9 React lenses re-rendered for every interaction; reading markdown costs zero.

## Decision

**Adopt GitHub as the substrate** for the strategic spine + the operational tier.

- Strategic spine — `sem-ai/{vision,goals,capabilities,features}/*.md` and `docs/adr/*.md`. Read/written through the engine MCP (`mcp__sem_ai_engine__*`).
- Operational tier — GitHub Issues + sub-issues (`feature` / `story` / `spec` / `defect`).
- Releases — GitHub Releases (the body carries `## Sizing`, `## Quality gate`, `## Security gate` sections, populated by PM + QA + Security Officer).
- PR-forced workflow — branch protection on `main` requires a PR + the `sem-ai-validate` check.
- Self-maintenance — GitHub Actions for validate / sync / tree.

The v0.1 TypeScript + React stack is preserved on `archive/v0.1-sqlite-experiment` for reference and as an optional `--backend=local` mode for offline / regulated deployments.

## Overall structure

Four-layer architecture: agent (Claude Code) → engine MCP (Python) → instance YAML (methodology config) → GitHub (storage + UX). Each layer replaceable in isolation.

## Data structure

Markdown frontmatter is the source of truth for structural queries (parent, status, dates, role, labels). Body is markdown with templated sections per type. See ADR 019 for the schema.

## Interfaces to the outside world

- Engine MCP exposes 19 typed tools (`mcp__sem_ai_engine__*`).
- Existing GitHub MCP (`mcp__github__*`) handles Issue / Release writes (no modification).
- Claude Code hooks (`SessionStart`) inject the project map.

## Decomposition into functional components

Engine modules: `config_loader · graph_walker · validators · estimator · lifecycle · jurisdiction · tree_renderer · mcp_server` (~1100 LoC Python).

## Linkage / information transmission

Engine MCP reads/writes spine markdown + ADR markdown directly. For GitHub Issues / Releases, the engine delegates writes to the GitHub MCP through agent dispatch (the agent calls one MCP, gets a result, then calls another).

## Performance attributes

Markdown reading is O(n) per file; the spine is typically < 200 files. The engine's `iter_spine_nodes` is uncached and re-reads each tool call; cache via in-memory dict can land in v0.3 if the spine exceeds ~10 000 nodes (Jones Enterprise tier).

## Security attributes

Dispatched to Security Officer.

- Authorization model: GitHub native (write requires PR + reviewer approval + the `sem-ai-validate` check on branch protection).
- Threat surface: no new endpoints introduced by the pivot; reduces vs v0.1 (the React UI was a previously-exposed surface).
- Supply chain: PyYAML + mistune + mcp; certified-reuse gate per `architect-reuse-certification` is the audit point.
- Boundary control: validators run on PR; jurisdiction matrix is hard-rejected at MCP write time.

## Style: chosen + rejected

- **Chosen**: GitHub-backed file substrate + typed engine MCP. Adopts a settled ecosystem; minimizes custom code.
- **Rejected**: Continue v0.1's custom MCP + UI. Costs ~6 000 LoC of work to maintain a worse storage + UX than GitHub.
- **Rejected**: Obsidian vault as substrate. Single-user; no branching at scale; no CI.
- **Rejected**: Jira + Confluence + bespoke ADR tooling. Three vendors; no native branching; no native PR.

## Consequences

- v0.1's custom MCP and React UI archived; framework is methodology-blind engine + GitHub.
- Single human operator can scale to a team without rebuild (each developer pairs with their role-agent; the substrate is repo-shared).
- PR review on every spine change → the discovery-to-validation collapse becomes mechanical, not aspirational.
- Loss: offline-first behaviour. Mitigation: archive branch carries the SQLite backend for offline / regulated deployments.

## Design inspection

PR with this ADR triggers a sem-ai-validate run + a peer review per the new branch protection.
