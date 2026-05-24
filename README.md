# SEM-AI

**GitHub-native infrastructure for AI-augmented product development.**

Six role-homologous AI agents — PM, Architect, Developer, QA, DevOps, Security Officer — collaborating reactively over a project-intent graph stored as GitHub Issues, with GitHub Actions as the recommended pipeline orchestrator.

The framework ships **infrastructure**, not methodology. The LLM brings methodology from its training; projects layer their own via `.claude/skills/`.

> **Status:** `v0.3.0` — feature complete. Engine MCP, semantic CI library, 5 reactive hooks, 3 slash commands, both setup scripts, sample pipeline, framework CI — all shipped. 295 tests passing. Ready for adoption.

## Use this template

This repository is a **GitHub template**. The framework is delivered as a clone — no `npm install`, no global packages. The engine and the rest of the framework live in the same repo; you get everything when you click "Use this template".

### Setup — 3 commands

```bash
# 1. Create from template + clone
gh repo create my-product --template owner/sem-ai
gh repo clone owner/my-product
cd my-product

# 2. Set up the engine (local venv + minimal Python deps + verify)
./scripts/setup-engine.sh

# 3. Provision GitHub structure (Issue Types + labels + Projects v2)
export SEM_AI_REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
./scripts/setup-github-project.sh

# 4. Start working — engine MCP + 5 hooks start automatically
claude --agent product-manager
```

The engine provides **mechanical enforcement**: an agent that tries to create a `goal` with `parent=feature` gets a hard reject, not a polite suggestion. Hooks fire on graph events (`SessionStart`, `PreCompact`, `PostToolUse` on `transition_status` / `gh pr merge`, `PreToolUse` on `gh pr create`) and run `engine/checks/` for semantic CI. The framework runs two layers of validation: structural CI on every push (catalog + skills + agents + settings), and semantic CI inside Claude Code sessions (hooks invoke role-coherence checks).

The engine code lives in `engine/` inside the template — no pip install. The rationale: the framework is one cohesive artifact; splitting the engine into a separately-versioned package would force adopters to track two version axes for no clear gain at this stage.

### Inside a session

```
/session-open <slug>     creates session branch + doc + posts 📍 on each in-play Issue
/session-close           finalizes Handoff + posts 🏁 + prompts merge/PR/discard
/catch-up [--since 7d]   digest of graph changes since last invocation (or custom window)
```

### Beyond `v0.3.0` — optional pip package

Once the adopter base grows and engine updates become routine, the same engine code may also be published as `pip install sem-ai-engine` for adopters who prefer that update model. **Optional**, not the primary distribution.

### The first session

Typically opens a `vision` Issue — the polar star of your product. The vision encodes both identity (Positioning) and ambition (Value ambition — the destination of the value chain). From there the work cascades: goals, capabilities, features, specs.

## Documentation map

| If you want to… | Read |
|---|---|
| Understand the framework in 5 minutes | [`CLAUDE.md`](CLAUDE.md) |
| See the canonical decisions | The SEM-AI project's Issues filtered by `type:adr` — the framework's own decisions live in its own graph |
| Understand the contract every agent obeys | [`.claude/skills/framework/SKILL.md`](.claude/skills/framework/SKILL.md) |
| See the body templates for the seven Issue Types | [`.claude/skills/node-templates/SKILL.md`](.claude/skills/node-templates/SKILL.md) |
| See a role's identity + jurisdiction | [`.claude/agents/<role>.md`](.claude/agents/) |
| Use the slash commands inside a session | [`.claude/skills/session-open/SKILL.md`](.claude/skills/session-open/SKILL.md) · [`session-close`](.claude/skills/session-close/SKILL.md) · [`catch-up`](.claude/skills/catch-up/SKILL.md) |
| See how the engine works inside | [`engine/`](engine/) — `core/` (catalog, validators, api) + `adapters/github.py` (gh CLI) + `checks/` (semantic CI) + `mcp_server.py` |
| Copy a reference deployment pipeline | [`examples/.github/workflows/sample-pipeline.yml`](examples/.github/workflows/sample-pipeline.yml) |
| Set up your own GitHub repo for the framework | [`scripts/setup-engine.sh`](scripts/setup-engine.sh) + [`scripts/setup-github-project.sh`](scripts/setup-github-project.sh) |

## Versioning and updates

SEM-AI uses [Semantic Versioning](https://semver.org/):

- **MAJOR** — break in the catalog of Issue Types, role-jurisdiction matrix, or existing ADR decision.
- **MINOR** — new ADR adding functionality, new skill, new Action example, backward-compatible MCP tool.
- **PATCH** — clarification, refinement, typo, non-functional doc improvement.

When a new version ships, adopters read the changelog (generated from the framework's session docs and ADRs since the previous tag), `git diff` between tags on this repo, and apply relevant changes to their local copy resolving conflicts with their customizations. A `sem-ai upgrade` CLI is deferred.

## Other platforms

SEM-AI is GitHub-first by decision. The MCP layer is the framework's real contract and the theoretical extension point for adapters to Jira / Linear / Jenkins / GitLab CI — but those adapters do not ship in `v0.x`. Adopters on non-GitHub stacks can integrate via webhooks at their own adaptation cost.

## License

See [`LICENSE`](LICENSE).
