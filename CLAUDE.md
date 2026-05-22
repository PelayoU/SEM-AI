# SEM-AI

A Software-Engineering-Management framework for working with AI — six role-homologous AI agents (PM, Architect, Developer, QA, DevOps, Security Officer) that share a typed project-intent substrate. The framework is **a discipline and an infrastructure**, not a methodology: each role's identity is in `.claude/agents/<role>.md`, the methodology this project applies (Cagan / Jones / Fagan / Humble & Farley / Jones-SRD) is configured per *instance* in `instance/`.

You work as **one role at a time.** Pick it with `claude --agent <role>` (PM, architect, developer, qa, devops, security-officer). With no role active, read `.claude/skills/framework/SKILL.md` first, then ask the human which role to take. The framework contract — the one rule, the substrate, the role-jurisdiction map — is the **`framework` skill**; every agent preloads it via `skills:` frontmatter, so the contract is present in both primary (`claude --agent <role>`) and dispatched-subagent (`Task`) modes.

## Where things live

| Layer | Location | What |
|---|---|---|
| Strategic spine | `sem-ai/{vision,goals,capabilities,features}/*.md` | Markdown nodes with v0.2 frontmatter (`type · parent · status · created · updated · maintained_by_role · labels`). Read/written through the engine MCP. |
| Decision history | `docs/adr/NNN-slug.md` | ADRs; sequence stable, supersede chain in frontmatter. |
| Operational tier | GitHub Issues + sub-issues (`feature/story/spec/defect`) | Kanban-style work, labels link issues to capabilities. |
| Releases | GitHub Releases | Native; the `## Quality gate` / `## Security gate` sections live in the release notes body. |
| Role identity | `.claude/agents/<role>.md` (×6) | The role contract — identity, jurisdiction, workflow, interaction with other roles, gotchas. Each absorbs generic role discipline (the framework); methodology specifics are in `instance/methodology/*.md`. |
| Methodology instance | `instance/*.yaml` + `instance/methodology/*.md` | The opinion: node types, parent rules, lifecycle, jurisdiction matrix, thresholds, forbidden patterns, sizing coefficients, reference playbooks. *This* repo configures the SEM-AI methodology (Jones / Cagan / Fagan / Jones-SRD). A different product would carry a different instance against the same engine. |
| Engine | `engine/` (Python package) | The mechanism — methodology-blind read / write / validate / estimate over the spine + GitHub. Exposed as the `sem_ai_engine` MCP server (`mcp__sem_ai_engine__*`). |

## Status (v0.2 transition — 2026-05-22)

- ✅ v0.1 SQLite + custom MCP + 9-lens React UI archived in branch `archive/v0.1-sqlite-experiment` (not deleted — reachable for offline / regulated deployments).
- ✅ v0.2 file layout in place: `sem-ai/` + `docs/adr/`, all 69 inherited nodes migrated to the 7-field frontmatter.
- ⏳ Agent.md absorption (Day 1.9), engine MCP (Day 2), GitHub Actions (Day 3) — in flight per `.claude/plans/merry-plotting-cosmos.md`.
- 📄 v0.2 design rationale: `PIVOT-TO-GITHUB.md` (will be superseded by `docs/adr/016-…` to `docs/adr/020-…` once the ADRs are authored on Day 3).
