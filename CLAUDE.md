# SEM-AI

**Software-Engineering-Management infrastructure for working with AI.** Six role-homologous AI agents (PM, Architect, Developer, QA, DevOps, Security Officer) collaborating reactively over a shared project-intent graph stored as GitHub Issues.

The framework ships **infrastructure**, not methodology. The LLM brings methodology from its training; projects layer their own methodology via `.claude/skills/`. **Fixed layer** = Issue Types + custom fields + role contracts + the MCP + the hooks. **Variable layer** = body content + project-supplied methodology skills + project-supplied Actions.

## How to start

You work as **one role at a time**. Pick it at launch:

```
claude --agent <role>            # pm, architect, developer, qa, devops, security-officer
```

The agent's identity is `.claude/agents/<role>.md`; the framework contract is the `framework` skill, preloaded into every agent via the `skills:` frontmatter. With no role active, read `.claude/skills/framework/SKILL.md` first and ask the human which role to take.

## The canonical decisions — read in order if new

| ADR | Decision |
|---|---|
| [001](docs/adr/001-all-nodes-as-github-issues.md) | All graph nodes live as GitHub Issues — 7 Issue Types audited down + native bridges for bug / release / inspection / measurement |
| [002](docs/adr/002-graph-is-hierarchical-but-not-unidirectional.md) | The graph is hierarchical in structure but not unidirectional in construction — 4 modes + anchor-pending pattern |
| [003](docs/adr/003-holistic-product-dimensions-cross-cut-the-spine.md) | Five holistic product dimensions cross-cut the spine — Technology / UX / Monetization / Acquisition / Offline (+ Functionality as base), as both structured slots in the spine and evaluation lens for every role |
| [004](docs/adr/004-invocation-model.md) | Invocation model — hooks primary (framework presumes Claude Code on every dev), MCP for writes, Actions as opt-in examples |

## The seven Issue Types

```
spine:       vision, goal, capability, feature, story, spec
cross-axis:  adr
```

**Concepts that ride on native GitHub objects** (no Issue Type): bugs → label `bug`; release planning → GitHub Milestone; release publication → GitHub Release; code inspection → PR review; non-code inspection → comments on the inspected Issue + label `inspected`; quantitative measurements → CI tooling. See ADR-001 for the full mapping.

## Where things live

| Layer | Location | What |
|---|---|---|
| Role identity | `.claude/agents/<role>.md` (×6) | The role contract — identity, jurisdiction, interaction with other roles. **Methodology-blind.** |
| Framework contract | `.claude/skills/framework/SKILL.md` | The one rule, the graph, the role-jurisdiction map, sessions. Preloaded by every agent. |
| Node templates | `.claude/skills/node-templates/SKILL.md` | Body section templates for the 7 Issue Types (with the Holistic dimensions section in spine templates). |
| Architectural decisions | `docs/adr/NNN-slug.md` | ADRs as markdown for now; will migrate to Issue Type=adr when the engine ships. |
| Graph (the project's plan) | GitHub Issues + Projects v2 | The 7 Types live here; native sub-issue link = parent; "Related" custom field = related; native Issue Type field = type; etc. |
| Releases | GitHub Milestones (planning) + GitHub Releases (publication) | Co-maintained: PM scope, QA quality gate, Security Officer security gate, DevOps pipeline + publish. |
| Session work | `sessions/<id>.md` on `session/*` branches | One markdown doc per work unit. 3-part structure (Context / Decisions / Handoff). |
| Engine MCP | `engine/` *(pending implementation)* | 19 typed graph tools + 3 Milestone/Release bridges + `acting_role` enforcement. |
| Checks library | `engine/checks/` *(pending implementation)* | Shared validation + side-effect logic invoked from hooks and Actions. |
| Hooks | `.claude/settings.json` *(pending implementation)* | The 5 hooks that materialise reactive role auto-invocation (SessionStart, PreCompact, PostToolUse on transition_status, PreToolUse on gh pr create, PostToolUse on gh pr merge). |
| Optional Actions | `examples/.github/workflows/` *(pending shipment)* | 5 YAML examples projects can copy when they need to cover UI editing / external collaborators / async events. |
| Methodology *(project-supplied)* | `.claude/skills/<topic>/SKILL.md` | Surfaced in Claude Code's skill listing; invoked on demand. Not shipped with the framework. |

## Sessions in brief

A session = a `session/<YYYY-MM-DD>-<slug>` branch + a doc `sessions/<id>.md`. One session typically crosses several roles in turn — the active role does its part, hands off via the doc, the next role opens a new Claude Code conversation (`claude --agent <new>` on the same branch) and rehydrates from the doc.

There is no mid-conversation role switch in Claude Code today. Cross-role input mid-conversation uses **consult** (subagent via `Task`, bounded question). Cross-role authorship uses **hand off** (new conversation, same branch, doc bridges the context).

Each session leaves its mark on the graph via Issue comments at three lifecycle points: 📍 in play / ✅ decision (role) / 🏁 closed. The full session model is in `framework/SKILL.md` § Sessions.

## Status (v0.3 — 2026-05-23)

- ✅ Catalog audited down to 7 Issue Types + native bridges (ADR-001)
- ✅ Hierarchical loop + anchor-pending pattern (ADR-002)
- ✅ Holistic product dimensions in spine templates + as evaluation lens (ADR-003)
- ✅ Invocation model: hooks primary, MCP writes, Actions opt-in (ADR-004)
- ✅ Session model on branches (no worktrees) + comments-lifecycle huella en el grafo
- ✅ 6 agent.md methodology-blind; framework + node-templates skills aligned
- ⏳ Engine MCP backend (the 19 + 3 tools) — not yet implemented
- ⏳ `engine/checks/` library — not yet implemented
- ⏳ 5 hooks in `.claude/settings.json` — not yet declared
- ⏳ `/session-open`, `/session-close`, `/catch-up` skills — not yet implemented
- ⏳ `examples/.github/workflows/` — not yet shipped
- ⏳ `scripts/setup-github-project.sh` (provisions the 7 Issue Types + custom fields + saved views + `bug` label) — not yet shipped
