# SEM-AI

> Software-Engineering-Management infrastructure for working with AI.
>
> Six role-homologous AI agents (PM, Architect, Developer, QA, DevOps, Security Officer) share a typed project-intent substrate. The framework absorbs the review cost AI generates — *discovery* collapses to *validation* — so the engineer keeps authorship and judgement, not the discovery cost.

## What this is

Three years from now, working with AI in software development is no longer something an engineer pays for in review labour. Around the engineer lives an infrastructure of role-homologous AI agents — one per dimension classical SEM separates into a role (scope, architecture, code, quality, operations, security). Each agent operates in its jurisdiction over a shared typed substrate of project intent: the same artifacts the human roles read, write, and validate against later. Human review collapses from *discovery* — searching for what drifted — to *validation* — confirming what was already recorded as compliant.

The framework's full statement is in [`sem-ai/vision/001-sem-ai.md`](sem-ai/vision/001-sem-ai.md).

## Architecture (v0.2)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  Claude Code agent (PM | Architect | Developer | QA | DevOps | Security)     │
│                                                                              │
│    reads:  .claude/agents/<role>.md  +  .claude/skills/framework/SKILL.md    │
│    uses:   mcp__sem_ai_engine__*  (typed read / write / validate / estimate) │
│    hooks:  SessionStart → at-minimum project map injected                    │
└──────────────────────────────────────────────────────────────────────────────┘
        │                              │                              │
        ▼                              ▼                              ▼
┌────────────────────┐    ┌──────────────────────────┐    ┌──────────────────────┐
│ engine/  (Python)  │    │ instance/  (YAML + MD)   │    │ GitHub.com           │
│  • mcp_server.py   │    │  • instance.yaml         │    │  • repo files        │
│  • validators.py   │    │  • node_types.yaml       │    │  • Issues + sub-     │
│  • graph_walker.py │    │  • thresholds.yaml       │    │    issues            │
│  • estimator.py    │◀───│  • forbidden.yaml        │    │  • Releases          │
│  • tree_renderer.py│    │  • required_fields.yaml  │    │  • Actions (validate │
│  • config_loader.py│    │  • lifecycle.yaml        │    │    · sync · tree)    │
│  • lifecycle.py    │    │  • jurisdiction.yaml     │    │  • Branch protection │
│  • jurisdiction.py │    │  • sizing.yaml           │    │    on main           │
│                    │    │  • methodology/*.md      │    │                      │
│  ~1100 lines       │    │                          │    │                      │
│  methodology-blind │    │  ~ 800 lines YAML + MD   │    │                      │
└────────────────────┘    └──────────────────────────┘    └──────────────────────┘
```

**Engine = mechanism. Instance = opinion. GitHub = storage + UX. Agent = judgement.** Each layer replaceable in isolation.

## Where things live

| Layer | Location | What |
|---|---|---|
| Vision | `sem-ai/vision/NNN-slug.md` | The 2–10 year future-as-system + positioning statement |
| Strategic spine | `sem-ai/{goals,capabilities,features}/*.md` | Markdown with v0.2 7-field frontmatter |
| Decision history | `docs/adr/NNN-slug.md` | ADRs; supersede chains in frontmatter |
| Operational tier | GitHub Issues + sub-issues | `feature` / `story` / `spec` / `defect` — kanban-shaped |
| Releases | GitHub Releases | Body has `## Sizing` / `## Quality gate` / `## Security gate` |
| Role identity | `.claude/agents/<role>.md` | Absorbs the role's generic discipline + Interaction table |
| Methodology | `instance/*.yaml` + `instance/methodology/*.md` | This instance's opinion (Jones / Cagan / Cohn / Patton / Fagan / Humble & Farley / Nygard) |
| Engine | `engine/` Python package | 19 typed MCP tools exposed as `sem_ai_engine` |

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
#    Read .claude/agents/<role>.md for the role's discipline + workflow.

# 4. Enable branch protection on main (admin one-off):
gh api -X PUT repos/{owner}/{repo}/branches/main/protection \
  --field 'required_status_checks[strict]=true' \
  --field 'required_status_checks[contexts][]=sem-ai-validate' \
  --field 'required_pull_request_reviews[required_approving_review_count]=1' \
  --field 'enforce_admins=true' \
  --field 'restrictions=null'
```

## The six roles (one paragraph each)

- **Product Manager** ([`.claude/agents/product-manager.md`](.claude/agents/product-manager.md)) — owns scope, business analysis, project management. Absorbs PO + BA + PM functions (Cagan-empowered). Authors vision · goals · capabilities · features · stories · specs · releases. 15 sub-disciplines from vision to change control.
- **Architect** ([`.claude/agents/architect.md`](.claude/agents/architect.md)) — owns the technical dimension. The 7 fundamental architecture topics. Authors ADRs. Dispatches Security Officer for Topic 7 (Security attributes).
- **Developer** ([`.claude/agents/developer.md`](.claude/agents/developer.md)) — owns code. Coding practices · static analysis · unit testing · certified reuse · legacy maintenance. Authors code commits linked to specs via `link_commit`; opens defects found by static analysis / unit tests.
- **QA** ([`.claude/agents/qa.md`](.claude/agents/qa.md)) — owns the quality dimension, **independent of the development chain**. SQA programme · measurements · inspections · testing strategy · DRE projection. Authors `measurement` · `inspection` · `defect` (inspection-found). Release-stop authority on quality grounds.
- **DevOps** ([`.claude/agents/devops.md`](.claude/agents/devops.md)) — owns operations. Configuration control · deployment pipeline · releases · post-release change · maintenance ops · customer support · legacy retirement.
- **Security Officer** ([`.claude/agents/security-officer.md`](.claude/agents/security-officer.md)) — owns security, **independent of the development chain**. Security programme · SRD · the 7th architecture topic · security test portfolio (testing 65% / ethical hacking 85% / SAST 25%) · threat catalogue. Contributes sections (Security AC in spec, Security gate in release, Security attributes in ADR). Release-stop authority on security grounds.

Each role agent.md ends with an **Interaction with other roles** table — the symmetric primacy contract (consult for 1–3 turns; hand off for 4+).

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
1. Hard-rejects on parent-type or jurisdiction violation (`ValueError` → MCP returns error).
2. Returns `warnings: list[str]` for missing sections, missing required fields, forbidden patterns, security cross-section findings — the write proceeds, the agent acts on the warnings.

The full engine API is in [`engine/mcp_server.py`](engine/mcp_server.py); the methodology configuration that drives it is in [`instance/`](instance/).

## Verifying the framework works

The proof the methodology is *mechanically enforced* — not aspirational — is in [`TESTING.md`](TESTING.md). Four agent-dispatch tests cover:

1. **QA** authors a `measurement` node via the engine MCP (positive test).
2. **Developer** authors a `defect` node from a static-analysis finding (positive test).
3. **Architect** authors an ADR, dispatching Security Officer for Topic 7 (positive test, cross-role).
4. **PM** attempts to author a `measurement` — the engine MCP **hard-rejects** via jurisdiction matrix (negative test; this is the strongest proof of mechanical enforcement).

Plus a pytest suite (`tests/`) exercising the engine modules directly.

## Decision history

The v0.2 pivot is recorded in:

- [`docs/adr/016-pivot-to-github-backed.md`](docs/adr/016-pivot-to-github-backed.md)
- [`docs/adr/017-engine-instance-split.md`](docs/adr/017-engine-instance-split.md)
- [`docs/adr/018-symmetric-role-primacy.md`](docs/adr/018-symmetric-role-primacy.md)
- [`docs/adr/019-markdown-yaml-frontmatter-canonical.md`](docs/adr/019-markdown-yaml-frontmatter-canonical.md)
- [`docs/adr/020-skills-reduction-methodology-as-instance.md`](docs/adr/020-skills-reduction-methodology-as-instance.md)

The v0.1 codebase (custom MCP + React UI) lives on `archive/v0.1-sqlite-experiment` for reference. To restore for an offline / regulated deployment:

```bash
git worktree add ../sem-ai-v0.1 archive/v0.1-sqlite-experiment
```

## License

[LICENSE](LICENSE).
