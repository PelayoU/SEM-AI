# ADR-008 — SEM-AI as a deployable framework: versioning, distribution, CI/CD, dogfood

- **Status**: accepted
- **Date**: 2026-05-24
- **Supersedes**: —
- **Superseded by**: —

## Context

So far, every architectural decision in this repository has been about **what SEM-AI is** — its catalog of seven Issue Types (ADR-001), its hierarchical loop (ADR-002), its holistic dimensions (ADR-003), its invocation model (ADR-004), its value chain (ADR-005), its experimental intent (ADR-006), its risk surface (ADR-007). None has been about **how SEM-AI itself is delivered to teams that want to use it**.

That gap matters now for two reasons:

1. The framework is conceptually closed (the seven ADRs above describe a coherent model). The next steps are implementation — code under `engine/`, hooks in `.claude/settings.json`, skills like `/session-open` — and the implementation needs a release model so that adopting teams can pull stable versions and know what changed between them.

2. The framework necessarily distinguishes **the deployment pipeline of an adopting project** (the team using SEM-AI to manage their product, with their own Jenkins / GitHub Actions / GitLab CI / whatever) from **the deployment pipeline of SEM-AI itself** (how the framework gets to the adopting team in the first place). The two are very different concerns, often conflated. This ADR records both.

## Decision — two pipelines, two scopes

### Pipeline 1 — The adopting project's pipeline (NOT framework infrastructure)

The deployment pipeline of an adopting project — its CI/CD stages, its orchestrator, its environments, its quality gates, its compliance validations, its dual control, its notifications — is **methodology**, chosen by the adopting team. The framework does **not** impose:

- The orchestrator (Jenkins, GitHub Actions, GitLab CI, CircleCI, Buildkite, Argo, …)
- The stages (unit tests, integration, smoke, canary, blue-green, dark launch, …)
- The tools (SonarQube vs Coverity, Nexus vs Artifactory, Trivy vs Snyk, …)
- The criteria (coverage thresholds, severity gates, performance budgets, …)
- The notification topology (email vs Slack vs Teams vs PagerDuty)
- The compliance validations (SOC2, ISO 27001, AEAT certification, HIPAA, …)

What the framework provides at the boundary between graph and pipeline is **already decided** in earlier ADRs:

- **Hook integration** (ADR-004): `PostToolUse on Bash(gh pr merge *)` derives artifacts from `Closes #N` linkage; `PreToolUse on Bash(gh pr create *)` triggers pre-emptive security/PM reviews; the engine's `triggered_by` parameter restricts agents invoked by hooks/Actions to read+comment.
- **Action examples** (ADR-004): `examples/.github/workflows/sem-ai-artifacts.yml` and friends, for teams whose merges happen outside Claude Code; copy-paste opt-in.
- **Closure convention** (ADR-001): PRs close Issues via `Closes #N`; merge triggers artifact derivation; Milestones aggregate releases; the GitHub Release native object publishes.
- **Status semantics** (ADR-001/005): `done` means "shipped"; the pipeline of the adopting project defines what "shipped" concretely entails; the framework does not.

The adopting team configures their pipeline to fire the framework's hooks/Actions when relevant graph events happen, and to interpret `done`/`deprecated` according to their conventions. That is the entire interface.

### Pipeline 2 — SEM-AI's own pipeline (framework infrastructure)

The pipeline that delivers SEM-AI itself to adopting teams **is** framework concern, and is articulated here.

#### Distribution

| Channel | What ships | When |
|---|---|---|
| **GitHub template repository** (primary) | The full `.claude/agents/` + `.claude/skills/` + `docs/adr/` + `examples/` + `scripts/` + `CLAUDE.md` + `README.md` + `LICENSE`. Adopting teams click "Use this template" and get a copy of the framework as the seed of their own repo. | From the first stable release onward. |
| **pip package `sem-ai-engine`** (when the engine exists) | The Python package implementing the 19 + 3 MCP tools + the `engine/checks/` library. Imported by the adopting team's `.claude/settings.json` hooks and by their opt-in `.github/workflows/` Actions. | When the engine ships (post v0.3.0). |
| **Claude Code marketplace plugin** | *(deferred)* — when the marketplace is mature enough to host frameworks of this shape. Not blocking. | Future. Not v1. |

The template repository is the primary canal because (a) it is native to GitHub, (b) it gives the adopting team a working copy they edit, (c) it does not require any tooling beyond `git clone` + `gh repo create --template`. The pip package follows only when the engine has executable code.

#### Versioning — SemVer

The framework uses **Semantic Versioning** with explicit semantics per increment:

| Increment | Triggered by |
|---|---|
| **MAJOR** (`X.0.0`) | A break in the catalog of seven Issue Types (adding/removing a Type, changing its parent rule or status set); a change in the role-jurisdiction matrix that affects an existing role's ownership; a decision in an existing ADR that is superseded by an incompatible one. Adopting teams need to plan a migration. |
| **MINOR** (`0.X.0`) | A new ADR that adds functionality (a new lens, a new mechanism, a new skill); a new framework-shipped skill (e.g. `/session-open`); a new Action example in `examples/`; a backward-compatible MCP tool addition. Adopting teams gain a new capability they can opt into. |
| **PATCH** (`0.0.X`) | A clarification or refinement of an existing SKILL.md or template comment; a fix in CLAUDE.md / README; a typo; an update inside an existing ADR (like the "Update — label experiment" added to ADR-006 in 2026-05-24); a non-functional documentation improvement. No behavioral change for adopting teams. |

The current state of the repository corresponds to `v0.3.0-pre` (the conceptual model is closed across ADRs 001–008, implementation is pending). The first stable release will be tagged when the implementation pending list (engine + hooks + skills + examples + setup script) reaches a usable minimum — that target is `v0.3.0`. The route to `v1.0.0` requires the framework to be successfully adopted in at least one downstream project for a meaningful period; absent that, calling it 1.0 would be premature.

#### CI — Continuous Integration on the framework repo itself

The framework's own CI lives in `.github/workflows/sem-ai-ci.yml` (to be created) and runs on every PR. Its stages:

1. **ADR coherence** — every ADR file has the canonical header (Status / Date / Supersedes / Superseded by); every link to another ADR exists; no dangling references to deleted files; the `Supersedes` chain is acyclic and consistent.
2. **Skill frontmatter** — `framework/SKILL.md` and `node-templates/SKILL.md` have valid `name:` and `description:` frontmatter; the skill names match the directory names.
3. **Agent frontmatter** — the six `agent.md` files have valid `name:` / `description:` / `model:` / `color:` / `skills:` frontmatter; each lists `framework` and `node-templates` in `skills:`; the role names match the filenames.
4. **Settings.json** — `.claude/settings.json` is valid JSON; the hooks declared correspond to documented events (per ADR-004).
5. **Markdown lint** — basic prose / formatting check on `docs/` + `CLAUDE.md` + `README.md` + all `*.md` in `.claude/`.
6. **Engine tests** — `pytest engine/` when the engine exists. No-op until then.
7. **Validators self-test** — `engine/checks/` library has its own unit tests (when implemented).

Stage 7 is interesting because it eats its own dogfood: the same validators that `engine/checks/` provides for adopting projects also validate the framework's own repository. The framework validates itself with its own tools.

CI failure blocks merge.

#### CD — Continuous Delivery of the framework

CD lives in `.github/workflows/sem-ai-release.yml` (to be created) and triggers on `git tag` push matching `v[0-9]+.[0-9]+.[0-9]+`.

Stages:

1. **Re-run CI** on the tagged commit (defense in depth).
2. **Generate changelog**:
   - List ADRs added or modified since the previous tag.
   - List `*/SKILL.md` files modified.
   - List `*/agent.md` files modified.
   - List session docs (`sessions/*.md`) closed since the previous tag, with their Decisions section quoted (this gives the changelog a narrative shape, not just a file diff).
3. **Create GitHub Release** with the tag, the generated changelog as release notes, and the source archive.
4. **Publish pip package** (when the engine exists) to PyPI with the same tag.
5. **Notify** — comment on any open Issue referencing the release; optionally post to the project's Discussions feed if it exists.

The changelog format ties the release narrative to the actual session work that produced it. This is dogfood: the framework's release notes are generated from the same Decisions / Handoff sections that the framework asks adopting teams to maintain.

### Dogfood — the framework develops by applying itself

The framework's own development follows the framework's own model. Concretely:

- **Every major change starts with an ADR.** This is already happening — ADRs 001–008 are the literal record.
- **Sessions are documented** in `sessions/<id>.md` per the framework's session contract (branch + doc + 3-part structure + Decisions + Handoff). When the framework ships `/session-open` and `/session-close`, those skills will be used by the framework's own team to run the framework's own development.
- **PRs close Issues via `Closes #N`** once the framework's own graph is provisioned in its repository (Issue Types + custom fields + saved views, per the future `scripts/setup-github-project.sh`).
- **The catalog of 7 Issue Types applies to the framework itself.** The framework's vision is a `vision` Issue; its goals are `goal` Issues; its capabilities (e.g. "engine MCP backend") are `capability` Issues; the development of each capability decomposes into `feature`s, etc. The framework's roadmap will eventually live as a Milestone with the relevant Issues assigned.
- **Coherence enforcement applies to the framework's own repo.** When `engine/` exists and the MCP is wired, the framework will be the first adopting project — and the validators will validate it. Failures in the framework's own graph are bugs in the framework, addressed like any other.

This is not symbolic — it is the only way to ensure the framework is genuinely usable. A framework that cannot be applied to its own development is not a framework, it is a proposal.

### Extensibility — what an adopting project can and cannot change

The boundary between **fixed layer** and **variable layer** (per the principle the design discussions converged on) is encoded as follows:

| Can change | Cannot change |
|---|---|
| **Methodology skills** added under `.claude/skills/<topic>/` | The **catalog of seven Issue Types** (ADR-001) |
| **Project-specific agent.md files** under `.claude/agents/` (e.g. a `ux-designer.md` if the project has that role; an `growth-pm.md` for growth teams) | The **six canonical roles** (PM / Architect / Developer / QA / DevOps / Security Officer) — they ship as-is |
| The **body content of the project's own graph nodes** (vision, goals, etc.) | The **structure of the spine templates** in `node-templates/SKILL.md` — body sections (Story, Acceptance check, Holistic dimensions, Value chain, …) are framework-shipped |
| **Project-specific saved views** in Projects v2 | The **decisions of the canonical ADRs** (001–008) — they evolve via new ADRs or via inline `Update —` sections, never by silent edits in adopting projects |
| **`examples/.github/workflows/`** Actions copied into the project's `.github/workflows/` and modified | The **engine MCP API surface** (the 19 + 3 tools, the `acting_role` / `triggered_by` enforcement) — adopters consume it, do not modify it |
| **Settings overrides** in `.claude/settings.local.json` for personal preferences | The **5 ship hooks** declared in the framework's `.claude/settings.json` — adopters inherit them; can extend with their own hooks but not remove the shipped ones |
| **Their own `instance/<project>.yaml`** (when the engine supports project config) for project-specific thresholds / labels / sizing coefficients | The **framework's own `instance/`** if it exists (it currently doesn't) — that's the engine's default behavior, not for adopter override |

When an adopting team wants a change that falls in the "cannot change" column, the correct path is **contributing back to the framework** via PR — propose a new ADR that justifies the change, debate it, and if accepted, it lands in a Major or Minor version that the adopter can then upgrade to.

### Update model — manual with changelog, CLI deferred

When a new version of SEM-AI is released, an adopting project updates manually:

1. The team reads the changelog (generated per the CD stages above).
2. The team decides which changes to absorb. Patch releases are usually safe; minor releases add capability the team can opt into; major releases require migration planning.
3. The team `git diff`s the relevant changed files between the adopted version and the new version, in the SEM-AI template repository (via GitHub's compare view between tags).
4. The team applies the relevant changes to its own copy, resolving conflicts with their local customizations (methodology skills, project agent.md files, etc.).

A future `sem-ai upgrade` CLI tool is **deferred**: the upgrade pattern is not yet stable enough across versions to automate without risk of bad merges into customized files. Once SEM-AI has been adopted in 3+ downstream projects across a few minor versions, the upgrade patterns can be reified into a CLI. Until then, manual + good changelog.

## Alternatives considered

- **Single distribution channel (only template repo OR only pip package).** Rejected. The template repo is the right vehicle for the markdown + skills + agent.md layer; the pip package is the right vehicle for the engine code. Each does what the other can't well. When both exist, both ship; until then, just the template.
- **CalVer (`YYYY.MM.DD`) instead of SemVer.** Rejected. The framework will have breaks in its catalog (a Type change is a structural break for adopters); SemVer signals that clearly. CalVer hides the difference between a typo fix and a Type removal.
- **Marketplace plugin from day one.** Rejected as the primary channel for v0.3 / v1.0. Deferred until Claude Code marketplace is mature enough; not blocking.
- **`sem-ai upgrade` CLI from day one.** Rejected. Premature automation against unstable evolution patterns risks bad merges into customized files. Manual + clear changelog is honest and sufficient for early versions.
- **Templating with placeholder variables** (e.g. `{{PRODUCT_NAME}}` in CLAUDE.md, replaced when the adopter clones). Rejected. Adds a templating layer; the adopter simply edits the few places where their product name appears (CLAUDE.md opening + README). The simplicity of "clone and edit" beats the convenience of templating for a low number of substitutions.
- **No versioning, evolve in place.** Rejected. Without versioning, adopters cannot pin to a known-good state; every upgrade becomes a surprise. SemVer is mandatory for any framework intended to be adopted.
- **Combining this ADR with ADR-004** (which already mentions distribution lightly). Rejected. ADR-004 is about the invocation model (hooks vs MCP vs Actions); this ADR is about the framework as a deliverable. Separate concerns, separate ADRs.

## Consequences

- A `.github/workflows/sem-ai-ci.yml` is created in a follow-up commit, implementing the seven CI stages (initially with stages 1–5 active; stages 6–7 become active when `engine/` exists).
- A `.github/workflows/sem-ai-release.yml` is created when the framework approaches its first stable tag; for now, the CD logic lives only in this ADR.
- The framework's own repository starts using SemVer git tags. The current state corresponds to `v0.3.0-pre`. The first tag `v0.3.0` is pushed when implementation pending reaches a usable minimum.
- `scripts/setup-github-project.sh` (already pending per earlier ADRs) provisions not only the 7 Issue Types + custom fields + `bug` and `experiment` labels, but also the saved Projects v2 views (`Discovery` filter on `experiment` label, `Delivery` filter excluding it, etc.).
- `CLAUDE.md` gains a line in its status section pointing at this ADR for the deployment model.
- `README.md` (when minimal version is created) opens with "This is SEM-AI v<X>. Use this template to start your project." with link to release notes.
- The pip package `sem-ai-engine` becomes part of the engine implementation work; its `setup.py` / `pyproject.toml` is part of the engine ship.
- Adopting projects discover updates by watching the framework's release feed (subscribe to GitHub Releases on the SEM-AI repo) — there is no push notification mechanism beyond GitHub's native one. Sufficient for v0.x; can be enhanced later if the user base grows.

## Status

Accepted. SEM-AI distinguishes the deployment pipeline of adopting projects (methodology, not framework concern) from its own deployment pipeline (framework infrastructure). The framework distributes as a GitHub template repository (primary) with a future pip package for the engine; uses SemVer; ships CI for self-validation; releases via tag-driven CD with narrative changelog. The framework develops by applying itself (dogfood). Adopting projects can change methodology, project-specific roles, body content, and their own pipelines — but cannot change the canonical catalog, the canonical roles, or the canonical ADRs; for those, the path is contribution upstream.
