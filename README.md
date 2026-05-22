# SEM-AI

> **Software-Engineering-Management infrastructure for working with AI.**
>
> Six role-homologous AI agents (PM, Architect, Developer, QA, DevOps, Security Officer) share a typed project-intent substrate. The framework absorbs the review cost AI generates — *discovery* collapses to *validation* — so the engineer keeps authorship and judgement, not the discovery cost.

## What this is

Three years from now, working with AI in software development is no longer something an engineer pays for in review labour. Around the engineer lives an infrastructure of role-homologous AI agents — one per dimension classical SEM separates into a role (scope, architecture, code, quality, operations, security). Each agent operates in its jurisdiction over a shared typed substrate of project intent: the same artifacts the human roles read, write, and validate against later. Human review collapses from *discovery* — searching for what drifted — to *validation* — confirming what was already recorded as compliant.

The framework's full statement is in [`sem-ai/vision/001-sem-ai.md`](sem-ai/vision/001-sem-ai.md).

## What the framework ships — and what it doesn't

**Ships (infrastructure):**

- 6 role-homologous agents — methodology-blind role contracts.
- The `framework` skill — the always-on contract.
- The engine MCP (Python) — methodology-blind mechanism with 19 typed tools.
- The engine's infrastructure config — `instance/{instance,lifecycle,jurisdiction,node_types}.yaml`: status state-machine + role × type write-authority matrix + the 11 node types with parent rules + **section templates** + storage targets.
- SessionStart hook + `.mcp.json` + 3 GitHub Actions (validate · sync · tree).

**Does not ship at all:**

- No Cagan / Jones / Fagan / Cohn / Patton / Humble & Farley / Nygard playbooks.
- No `instance/methodology/` folder.
- No `.claude/skills/<role>-<topic>/` skills carrying methodology criteria.
- No `instance/thresholds.yaml` / `forbidden.yaml` / `required_fields.yaml` / `sizing.yaml` — these YAML slots exist in the engine as **optional extension points**. If a project wants the engine's warn-level validators populated (DRE bands, FP tiers, anti-patterns, regex markers, sizing coefficients), it creates the file and fills it in. The engine treats missing files as "no rules of that kind apply" — structural validators (parent-type, section presence, lifecycle, jurisdiction) keep enforcing unchanged.

The framework's single methodology shipment is the **node body templates** (the section headers per node type in `instance/node_types.yaml`) — without templates the engine cannot enforce body structure at all, so this is the minimum opinion the framework carries. A project tunes templates to its own taste.

For everything else: the LLM already carries the SEM literature in its training (Cagan / Jones / Cohn / Patton / Fagan / Humble & Farley / Nygard / ANSI-IEEE / IFPUG / COSMIC / ISBSG / SAFe / Modern Agile / OKRs / OWASP / NIST / STRIDE / …). The framework constrains the *infrastructure* within which any methodology operates; the methodology itself rides on the LLM's training, on the project's filled-in `instance/*.yaml` stubs, and optionally on project-supplied skills in `.claude/skills/` — Claude Code's native mechanism.

## Architecture (v0.2)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  Claude Code agent (PM | Architect | Developer | QA | DevOps | Security)     │
│                                                                              │
│    reads:  .claude/agents/<role>.md   ← methodology-blind role contract      │
│            .claude/skills/framework/SKILL.md   ← the always-on contract      │
│    uses:   mcp__sem_ai_engine__*  (19 typed tools)                           │
│    hooks:  SessionStart → at-minimum project map injected                    │
└──────────────────────────────────────────────────────────────────────────────┘
        │                                                              │
        ▼                                                              ▼
┌────────────────────────────────┐                  ┌──────────────────────────┐
│ engine/  (Python)              │                  │ GitHub.com               │
│  • mcp_server.py · 19 tools    │                  │  • repo files (spine)    │
│  • config_loader · graph_walker│                  │  • Issues (operational)  │
│  • validators · estimator      │◀─reads YAML──┐   │  • Releases              │
│  • lifecycle · jurisdiction    │              │   │  • Actions (validate ·   │
│  • tree_renderer               │              │   │    sync · tree)          │
│  ~1100 lines, methodology-blind│              │   │  • Branch protection    │
└────────────────────────────────┘              │   └──────────────────────────┘
                                                │
                       ┌────────────────────────┴───────┐
                       │  instance/  (engine config)    │
                       │   • instance.yaml              │
                       │   • node_types.yaml            │
                       │   • lifecycle.yaml             │
                       │   • jurisdiction.yaml          │
                       │   • required_fields.yaml      │
                       │   • forbidden.yaml             │
                       │   • thresholds.yaml            │
                       │   • sizing.yaml                │
                       │  default values = SEM-AI       │
                       │  dogfood; project can override │
                       └────────────────────────────────┘

Methodology — three sources, project's choice:
  ① the LLM's training (always available, no install)
  ② project-supplied `.claude/skills/<topic>/SKILL.md` (optional, surfaced
     in Claude Code's skill listing, invoked on demand)
  ③ never shipped with the framework itself
```

## Where things live

| Layer | Location | What |
|---|---|---|
| Vision | `sem-ai/vision/NNN-slug.md` | The 2–10 year future-as-system + positioning statement |
| Strategic spine | `sem-ai/{goals,capabilities,features}/*.md` | Markdown with v0.2 7-field frontmatter |
| Decision history | `docs/adr/NNN-slug.md` | ADRs; supersede chains in frontmatter |
| Operational tier | GitHub Issues + sub-issues | `feature` / `story` / `spec` / `defect` / `measurement` / `inspection` — kanban-shaped |
| Releases | GitHub Releases | Body has `## Sizing` / `## Quality gate` / `## Security gate` |
| Role identity | `.claude/agents/<role>.md` | Methodology-blind role contract (Identity / Jurisdiction / How you work / Interaction / Gotchas) |
| Engine | `engine/` Python package | 19 typed MCP tools exposed as `sem_ai_engine` |
| Engine config | `instance/*.yaml` | Engine's data layer (schema · lifecycle · jurisdiction matrix · validator rules · thresholds) |
| Methodology *(optional)* | `.claude/skills/<topic>/SKILL.md` | Project's chosen methodology in Claude Code's native skill mechanism. **Not shipped.** |

## Quick start

```bash
# 1. Clone + scaffold the Python workspace (one-off).
git clone <this-repo> && cd <repo>
python3 -m venv .venv
.venv/bin/pip install PyYAML mistune mcp

# 2. Open a role-active Claude Code session.
claude --agent product-manager        # most sessions start here
# OR
claude --agent architect              # when work is structural
claude --agent developer              # when work is code
claude --agent qa                     # when work is quality
claude --agent devops                 # when work is operational
claude --agent security-officer       # when work is security

# 3. The SessionStart hook injects the at-minimum project map.
#    The engine MCP exposes 19 typed tools as mcp__sem_ai_engine__*.
#    The agent uses its training for the methodology; if you want a
#    specific methodology surfaced, add it as a skill under .claude/skills/.

# 4. Enable branch protection on main (admin one-off):
gh api -X PUT repos/{owner}/{repo}/branches/main/protection \
  --field 'required_status_checks[strict]=true' \
  --field 'required_status_checks[contexts][]=sem-ai-validate' \
  --field 'required_pull_request_reviews[required_approving_review_count]=1' \
  --field 'enforce_admins=true' \
  --field 'restrictions=null'
```

## The six roles (one paragraph each)

- **Product Manager** ([`.claude/agents/product-manager.md`](.claude/agents/product-manager.md)) — owns scope, business analysis, project management. Absorbs PO + BA + PM functions. Authors vision · goals · capabilities · features · stories · specs · releases.
- **Architect** ([`.claude/agents/architect.md`](.claude/agents/architect.md)) — owns the technical dimension. Authors ADRs. Dispatches Security Officer for Topic 7 (Security attributes).
- **Developer** ([`.claude/agents/developer.md`](.claude/agents/developer.md)) — owns code. Authors code commits linked to specs via `link_commit`; opens defects found by own static analysis / unit tests.
- **QA** ([`.claude/agents/qa.md`](.claude/agents/qa.md)) — owns the quality dimension, **independent of the development chain**. Authors `measurement` · `inspection` · `defect` (inspection-found). Release-stop authority on quality grounds.
- **DevOps** ([`.claude/agents/devops.md`](.claude/agents/devops.md)) — owns operations. Contributes operational sections into PM-owned releases (`advisory_update`). Opens defects with operational origin.
- **Security Officer** ([`.claude/agents/security-officer.md`](.claude/agents/security-officer.md)) — owns security, **independent of the development chain**. Contributes sections (Security AC in spec, Security gate in release, Security attributes in ADR) into nodes owned by other roles. Authors security defects. Release-stop authority on security grounds.

Each role agent.md ends with an *Interaction with other roles* table — the symmetric primacy contract (consult for 1–3 turns; hand off for 4+).

## Engine MCP — 19 tools

```
READ (8)    get_project_map · get_node · children_of · ancestors_of ·
            query_nodes · search_nodes · get_related · get_tree
WRITE (8)   create_node · update_node · transition_status · link_commit ·
            set_related · add_label · remove_label · supersede
COMPUTE (2) estimate_size · validate_node
CONFIG (1)  get_instance_config
```

Every write:
1. **Hard-rejects** on parent-type or jurisdiction violation (`ValueError` → MCP returns error). The engine enforces, not the agent's good intentions.
2. Returns `warnings: list[str]` for missing sections, missing required-field patterns, forbidden patterns, security cross-section findings. The write proceeds; the agent acts on the warnings.

The full engine API is in [`engine/mcp_server.py`](engine/mcp_server.py); the engine's config that drives the validators is in [`instance/`](instance/).

## Verifying the framework works

The proof the framework's discipline is *mechanically enforced* — not aspirational — is in [`TESTING.md`](TESTING.md).

- **Engine pytest** (`tests/`, 28 tests, all green): the engine's mechanics — config loading, graph walking, validators, jurisdiction matrix, lifecycle, estimator, tree renderer.
- **4 agent-dispatch tests** (manual; run with real `claude --agent <role>` sessions): three positive (QA records a measurement · Developer opens a defect · Architect authors an ADR and dispatches Security Officer for Topic 7) and one **negative** — PM attempts to create a `measurement` and the engine hard-rejects via jurisdiction matrix. *The negative is the strongest proof of mechanical enforcement: discipline an agent could violate on a "do it" without consequence is aspiration; discipline the engine refuses is infrastructure.*

## Decision history

The v0.2 pivot is recorded in `docs/adr/`:

- [`016-pivot-to-github-backed.md`](docs/adr/016-pivot-to-github-backed.md) — substrate from SQLite to GitHub-backed files + Issues + Releases.
- [`017-engine-instance-split.md`](docs/adr/017-engine-instance-split.md) — engine (mechanism) vs engine config (opinion).
- [`018-symmetric-role-primacy.md`](docs/adr/018-symmetric-role-primacy.md) — no orchestrator; each role primary in its dimension.
- [`019-markdown-yaml-frontmatter-canonical.md`](docs/adr/019-markdown-yaml-frontmatter-canonical.md) — 7-field frontmatter + markdown body as canonical format.
- [`021-framework-ships-infrastructure-not-methodology.md`](docs/adr/021-framework-ships-infrastructure-not-methodology.md) — the framework does not ship methodology; supersedes ADR-020.

The v0.1 codebase (custom MCP + React UI) lives on `archive/v0.1-sqlite-experiment` for reference. To restore for an offline / regulated deployment:

```bash
git worktree add ../sem-ai-v0.1 archive/v0.1-sqlite-experiment
```

## License

[LICENSE](LICENSE).
