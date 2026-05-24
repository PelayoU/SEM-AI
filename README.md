# SEM-AI

**GitHub-native infrastructure for AI-augmented product development.**

Six role-homologous AI agents — PM, Architect, Developer, QA, DevOps, Security Officer — collaborating reactively over a project-intent graph stored as GitHub Issues, with GitHub Actions as the recommended pipeline orchestrator.

The framework ships **infrastructure**, not methodology. The LLM brings methodology from its training; projects layer their own via `.claude/skills/`.

> **Status:** `v0.3.0-pre` — the conceptual model is closed (nine ADRs in `docs/adr/`). Implementation is in progress: framework CI is active, engine MCP backend + hooks + slash commands pending the road to `v0.3.0`.

## Use this template

This repository is a **GitHub template**. The framework is delivered as a clone — no `npm install`, no global packages. The engine and the rest of the framework live in the same repo; you get everything when you click "Use this template".

### Today — `v0.3.0-pre` (no engine yet, 2 commands)

```bash
# 1. Create from template + clone
gh repo create my-product --template owner/sem-ai
gh repo clone owner/my-product
cd my-product

# 2. Provision GitHub structure: 7 Issue Types + labels + Projects v2
./scripts/setup-github-project.sh

# 3. Start working
claude --agent product-manager
```

The agent reads / writes the graph via `mcp__github__*` (native Claude Code integration) and `gh` CLI. **Mechanical enforcement** of parent-type, jurisdiction, lifecycle, etc. is **not active yet** — the engine MCP that performs it ships in `v0.3.0`.

### At `v0.3.0` — engine in the template (3 commands)

```bash
# 1. Create from template + clone
gh repo create my-product --template owner/sem-ai
gh repo clone owner/my-product
cd my-product

# 2. Set up the engine (local venv + minimal Python deps)
./scripts/setup-engine.sh

# 3. Provision GitHub structure
./scripts/setup-github-project.sh

# 4. Start working — engine MCP starts automatically with the session
claude --agent product-manager
```

The engine adds **mechanical enforcement**: the agent that tries to create a `goal` with `parent=feature` gets a hard reject, not a polite suggestion. Hooks fire on graph events (`SessionStart`, `PreCompact`, `PostToolUse` on `transition_status` / `gh pr create` / `gh pr merge`) and auto-invoke role agents to perform semantic CI per [ADR-008 § two layers of CI](docs/adr/008-deployable-framework.md).

The engine code lives in `engine/` inside the template — no pip install. See [ADR-008 § engine in the template](docs/adr/008-deployable-framework.md) for the rationale.

### Beyond `v0.3.0` — optional pip package

Once the adopter base grows and engine updates become routine, the same engine code may also be published as `pip install sem-ai-engine` for adopters who prefer that update model. **Optional**, not the primary distribution.

### The first session

Typically opens a `vision` Issue — the polar star of your product (see [ADR-006](docs/adr/006-features-may-declare-experimental-intent.md) § Value ambition). From there the work cascades: goals, capabilities, features, specs.

## Documentation map

| If you want to… | Read |
|---|---|
| Understand the framework in 5 minutes | [`CLAUDE.md`](CLAUDE.md) |
| See the canonical decisions | [`docs/adr/`](docs/adr/) (nine ADRs, numbered) |
| Understand the contract every agent obeys | [`.claude/skills/framework/SKILL.md`](.claude/skills/framework/SKILL.md) |
| See the body templates for the seven Issue Types | [`.claude/skills/node-templates/SKILL.md`](.claude/skills/node-templates/SKILL.md) |
| See a role's identity + jurisdiction | [`.claude/agents/<role>.md`](.claude/agents/) |
| Copy a reference deployment pipeline | [`examples/.github/workflows/sample-pipeline.yml`](examples/.github/workflows/sample-pipeline.yml) |
| Set up your own GitHub repo for the framework | [`scripts/setup-github-project.sh`](scripts/setup-github-project.sh) |

## Versioning and updates

SEM-AI uses [Semantic Versioning](https://semver.org/) per [ADR-008](docs/adr/008-deployable-framework.md):

- **MAJOR** — break in the catalog of Issue Types, role-jurisdiction matrix, or existing ADR decision.
- **MINOR** — new ADR adding functionality, new skill, new Action example, backward-compatible MCP tool.
- **PATCH** — clarification, refinement, typo, non-functional doc improvement.

When a new version ships, adopters read the changelog (generated from the framework's session docs and ADRs since the previous tag), `git diff` between tags on this repo, and apply relevant changes to their local copy resolving conflicts with their customizations. A `sem-ai upgrade` CLI is deferred.

## Other platforms

SEM-AI is GitHub-first by decision (see [ADR-009](docs/adr/009-github-as-primary-platform.md)). The MCP layer is the framework's real contract and the theoretical extension point for adapters to Jira / Linear / Jenkins / GitLab CI — but those adapters are not ship in `v0.x`. Adopters on non-GitHub stacks can integrate via webhooks at their own adaptation cost.

## License

See [`LICENSE`](LICENSE).
