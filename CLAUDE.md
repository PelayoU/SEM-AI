# SEM-AI

**Software-Engineering-Management infrastructure for working with AI.** Six role-homologous AI agents (PM, Architect, Developer, QA, DevOps, Security Officer) sharing a typed project-intent substrate. The framework ships **infrastructure** — roles, jurisdiction, the engine MCP, the interaction model. It **does not ship a methodology**: the LLM's training carries decades of SEM literature, and any project can layer its own methodology on top via Claude Code's `.claude/skills/`.

You work as **one role at a time.** Pick it with `claude --agent <role>` (PM, architect, developer, qa, devops, security-officer). With no role active, read `.claude/skills/framework/SKILL.md` first, then ask the human which role to take. The framework contract is the **`framework` skill**; every agent preloads it via `skills:` frontmatter, so the contract is present in both primary (`claude --agent <role>`) and dispatched-subagent (Task) modes.

## Where things live

| Layer | Location | What |
|---|---|---|
| Role identity | `.claude/agents/<role>.md` (×6) | The role contract — identity, jurisdiction, the 7-step workflow, interaction with other roles, gotchas. **Methodology-blind.** |
| Framework contract | `.claude/skills/framework/SKILL.md` | The one rule, the substrate, the role-jurisdiction map, the engine MCP, sessions. The only always-on skill. |
| Strategic spine | `sem-ai/{vision,goals,capabilities,features}/*.md` | Markdown nodes with v0.2 7-field frontmatter (`type · parent · status · created · updated · maintained_by_role · labels`). Read / written through the engine MCP. |
| Decision history | `docs/adr/NNN-slug.md` | ADRs; supersede chain in frontmatter. |
| Operational tier | GitHub Issues + sub-issues (`feature/story/spec/defect/measurement/inspection`) | Kanban-style work; labels link issues to spine nodes. |
| Releases | GitHub Releases | Native; `## Sizing` / `## Quality gate` / `## Security gate` sections in the body. |
| Engine | `engine/` (Python package) | Methodology-blind mechanism over the spine + GitHub. Exposed as `mcp__sem_ai_engine__*`. |
| Engine config | `instance/{instance,lifecycle,jurisdiction,node_types}.yaml` | What the engine needs to operate: project metadata · status state-machine · role × type write-authority matrix · 11 node types with parent rules + **section templates** + storage targets. The section templates are the only methodology the framework ships; everything else here is pure infrastructure. |
| Methodology extensions *(optional, project-supplied)* | `instance/{thresholds,forbidden,required_fields,sizing}.yaml` if a project wants the engine's warn-level validators populated | The engine treats these as optional — missing = no rules of that kind apply, structural validators (parent-type, section presence, lifecycle, jurisdiction) keep enforcing unchanged. Numerical thresholds (DRE bands, FP tiers, …), warn-level forbidden patterns, required-field regexes, FP sizing coefficients. **Not shipped.** |
| Methodology *(optional, project-supplied)* | `.claude/skills/<topic>/SKILL.md` if a project wants one | Surfaced in Claude Code's skill listing; invoked on demand by the agent. **Not shipped with the framework.** If a project ships nothing here, agents operate from the LLM's training and name the methodology they apply out loud. |

## Status (v0.2 — 2026-05-22)

- ✅ v0.1 SQLite + custom MCP + 9-lens React UI archived on `archive/v0.1-sqlite-experiment` (reachable for offline / regulated deployments via `git worktree add ../sem-ai-v0.1 archive/v0.1-sqlite-experiment`).
- ✅ v0.2 layout: `sem-ai/` + `docs/adr/`; 74 markdown nodes (the 69 self-bootstrap + 6 v0.2 ADRs) on the 7-field frontmatter.
- ✅ Engine MCP: 19 typed tools (`read 8 · write 8 · compute 2 · config 1`) in `engine/`; pytest green.
- ✅ Methodology YAMLs (`thresholds`/`forbidden`/`required_fields`/`sizing`) **not shipped**; engine treats them as optional. The framework's single methodology opinion is the section templates in `node_types.yaml`.
- ✅ 6 agent.md framework-blind (no methodology references; the LLM brings the school it's applying).
- ✅ 3 GitHub Actions wired (`sem-ai-validate` on PRs · `sem-ai-tree` on push · `sem-ai-sync` on issues + spine push).
- ⏳ Branch protection on `main` requires one `gh api` admin call (documented in `README.md`).
