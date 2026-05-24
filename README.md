# SEM-AI

**GitHub-native infrastructure for AI-augmented product development.**

Six role-homologous AI agents — PM, Architect, Developer, QA, DevOps, Security Officer — collaborating reactively over a project-intent graph stored as GitHub Issues, with GitHub Actions as the recommended pipeline orchestrator.

The framework ships **infrastructure**, not methodology. The LLM brings methodology from its training; projects layer their own via `.claude/skills/`.

> **Status:** `v0.3.0-pre` — the conceptual model is closed (nine ADRs in `docs/adr/`). Implementation is in progress: framework CI is active, engine MCP backend + hooks + slash commands pending the road to `v0.3.0`.

## Use this template

This repository is a **GitHub template**. To adopt the framework in a new project:

1. Click **"Use this template"** → **"Create a new repository"** on the GitHub page of this repo.
2. Clone your new repo locally.
3. Run the provisioning script to set up Issue Types, labels, Projects v2, and custom fields:
   ```bash
   ./scripts/setup-github-project.sh
   ```
4. Open Claude Code at the repo root with a role: `claude --agent product-manager` (or `architect`, `developer`, `qa`, `devops`, `security-officer`).
5. The first session typically opens a `vision` Issue — the polar star of your product (see [ADR-006](docs/adr/006-features-may-declare-experimental-intent.md) § Value ambition).

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
