# SEM-AI

**GitHub-native infrastructure for AI-augmented product development.** Six role-homologous AI agents (PM, Architect, Developer, QA, DevOps, Security Officer) collaborating reactively over a shared project-intent graph stored as GitHub Issues, with GitHub Actions as the recommended pipeline orchestrator (see ADR-009).

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
| [005](docs/adr/005-value-chain-probabilistic.md) | Value chain Output → Outcome → Benefit → Value — probabilistic, not deterministic; the framework enables value, does not provide it; learning is the guaranteed output of every cycle |
| [006](docs/adr/006-features-may-declare-experimental-intent.md) | Features may declare experimental intent — delivery (pay off learning) or experiment (resolve uncertainty); vision as polar-star with Value ambition, features as steps toward it |
| [007](docs/adr/007-holistic-dimensions-as-risk-surface.md) | Holistic dimensions are also the risk surface — an unvalidated dimension is a risk assumed without knowing; the four canonical risk classes (value / usability / viability / business viability) map to the dimensions |
| [008](docs/adr/008-deployable-framework.md) | SEM-AI as a deployable framework — SemVer, distribution as GitHub template repo + future pip package, CI/CD pipeline, dogfood, extensibility boundary |
| [009](docs/adr/009-github-as-primary-platform.md) | GitHub is the primary platform — backend, orchestrator (GitHub Actions recommended), distribution; the MCP layer is the real contract and the theoretical extension point for Jira / Linear / Jenkins / GitLab adapters post-v1 |

## The seven Issue Types

```
spine:       vision, goal, capability, feature, story, spec
cross-axis:  adr
```

**Concepts that ride on native GitHub objects** (no Issue Type): bugs → label `bug`; release planning → GitHub Milestone; release publication → GitHub Release; code inspection → PR review; non-code inspection → comments on the inspected Issue + label `inspected`; quantitative measurements → CI tooling. See ADR-001 for the full mapping.

## The bare-minimum cycle

Every cycle of work — regardless of granularity (a vision being articulated, a feature being shipped, a spec being tested) — traverses the same five steps. They are the framework's process spine, distributed across the components above. **As an agent, follow them; do not skip them silently — each skip has a cost, and skipping changes what the framework can do next.**

| # | Step | Where it lives in the framework | What happens here |
|---|---|---|---|
| 1 | **Card** | An Issue is opened (vision / goal / capability / feature / story / spec) | A unit of work is captured. The Issue is a placeholder for the conversation, not the conversation itself. |
| 2 | **Conversation** | A session of work begins — `claude --agent <role>` opens a Claude Code conversation; the human and the agent talk, explore, validate. Issue comments + the session doc's Decisions section are the conversation's traces. | The knowledge that will inform construction is generated here. The body of the node will destila this conversation. |
| 3 | **Confirmation** | The Issue body is updated with the destilada result — sections filled, Acceptance check stated, spec's Acceptance Criteria written, binding decisions logged in the session doc's Decisions section, ✅ comments posted on affected Issues | What the team agreed becomes recorded. The Issue body is the destilado of step 2, not its replacement. |
| 4 | **Construction** | A PR is opened that closes the Issue via `Closes #N`. Code is reviewed line-by-line in the PR. Artifacts are derived automatically from `Closes #N` on merge. | The work materializes. Construction may surface new findings that loop back to step 2 — that is normal, not a failure. |
| 5 | **Consequences** | The feature's `## Value chain` section is populated post-done: Outputs shipped, Outcomes observed, Benefits measured, Value assessment, **Learning extracted** (always populated; the guaranteed output of every cycle — see ADR-005), Next cards surfaced | The cycle closes by recording what actually happened along the chain Output → Outcome → Benefit → Value. The chain is probabilistic; honesty matters more than celebration. New cards surfaced here become step 1 of the next cycle. |

The framework provides the infrastructure for each step; the agent operates them. Direction-of-construction is not strictly 1→5 — bottom-up cycles, anchor-pending patterns, and pivots are explicitly recognized (ADR-002). What is not negotiable is that **each step has its place; silently collapsing the cycle into fewer steps produces specific failure modes** (skipping Conversation → builds the wrong thing; skipping Confirmation → ambiguous construction; skipping Consequences → no learning, no loop, one-way pipeline).

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

## Status (v0.3.0 — 2026-05-24)

Conceptual model — closed across nine ADRs:

- ✅ Catalog audited down to 7 Issue Types + native bridges (ADR-001)
- ✅ Hierarchical loop + anchor-pending pattern (ADR-002)
- ✅ Holistic product dimensions in spine templates + as evaluation lens (ADR-003)
- ✅ Invocation model: hooks primary, MCP writes, Actions opt-in (ADR-004)
- ✅ Value chain Output→Outcome→Benefit→Value, probabilistic; learning as guaranteed output (ADR-005)
- ✅ Features may declare experimental intent; vision as polar-star with Value ambition (ADR-006); label `experiment` as visibility complement
- ✅ Holistic dimensions are also the risk surface; modern approach principles 1-3 covered (ADR-007)
- ✅ SEM-AI as a deployable framework — SemVer, distribution, CI/CD, dogfood (ADR-008)
- ✅ GitHub as the primary platform — backend + orchestrator + distribution; MCP as extension point (ADR-009)
- ✅ Session model on branches (no worktrees) + comments-lifecycle huella en el grafo
- ✅ 6 agent.md methodology-blind; framework + node-templates skills aligned

Implementation — `v0.3.0` feature complete:

- ✅ Engine MCP backend — 22 typed tools (19 graph + 3 Milestone/Release bridges) with `acting_role` + `triggered_by` enforcement, layered as `engine/core/` + `engine/adapters/github.py` (gh CLI)
- ✅ `engine/checks/` semantic CI library — security_review, architect_coherence, pm_acceptance, artifacts_derive
- ✅ 5 hooks declared in `.claude/settings.json` — SessionStart, PreCompact, PostToolUse on transition_status / gh pr merge, PreToolUse on gh pr create
- ✅ 3 slash commands shipped — `/session-open`, `/session-close`, `/catch-up` (in `.claude/skills/` + `scripts/skills/`)
- ✅ `scripts/setup-engine.sh` + `scripts/setup-github-project.sh` — adopter setup in 3 commands
- ✅ `examples/.github/workflows/sample-pipeline.yml` — reference end-to-end pipeline
- ✅ Framework's own CI in `.github/workflows/sem-ai-ci.yml` — 5 stages: ADRs, skills, agents, settings, markdown lint
- ✅ 295 tests passing in 0.08s

Deferred to v0.4 / later:

- ⏳ 5 opt-in Action examples (`sem-ai-validate-posthoc.yml`, `sem-ai-security-review.yml`, etc.) — useful only when humans edit Issues from the GitHub UI or external collaborators open PRs without Claude Code
- ⏳ Agent-invoking-agent pattern from hooks (e.g. `PostToolUse on transition_status` spawning `claude --agent security-officer` for deeper review) — pattern needs more design
- ⏳ MCP adapters for Jira / Linear (per ADR-009 § theoretical extension point)
- ⏳ Projects v2 Status field via GraphQL (currently encoded as `status:<value>` label)
- ⏳ Optional pip distribution of `engine/` (per ADR-008 update — deferred until adopter base grows)
