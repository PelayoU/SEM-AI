# ADR-009 — GitHub as the primary platform: backend, orchestrator, pipeline

- **Status**: accepted
- **Date**: 2026-05-24
- **Supersedes**: —
- **Superseded by**: —

## Context

ADR-001 decided that the graph lives in GitHub Issues, using GitHub's native objects (sub-issue, Projects v2 custom fields, Milestones, Releases, labels, PR reviews). ADR-004 added that the framework presumes Claude Code on every dev and ships hooks + MCP + opt-in Actions. ADR-008 articulated that the deployment pipeline of an adopting project is methodology — the framework does not impose the orchestrator.

That neutrality is honest at the contract level but **operationally ambiguous**: an adopting team reads ADR-008 and asks "fine, but what orchestrator should we actually use? You expect hooks on `Bash(gh pr merge *)`, Action examples in `.github/workflows/`, native GitHub objects across the board. Are you really neutral, or is GitHub Actions implicitly required?".

The honest answer is: **operationally we are already GitHub-first**. Pretending otherwise costs clarity without buying real neutrality. The framework relies natively on:

- GitHub Issues + sub-issues + custom fields (for the graph)
- GitHub Projects v2 (for boards / saved views / Status field)
- GitHub Milestones (for release planning, per ADR-001 § native bridges)
- GitHub Releases (for publication, per ADR-001)
- GitHub native labels (for `bug`, `experiment`, `role:*`, etc.)
- GitHub PR reviews (for code inspection)
- GitHub native cross-references (for the session lifecycle 📍/✅/🏁)
- `gh` CLI in hooks (per ADR-004 hook list)

Refusing to name GitHub Actions as the recommended orchestrator after committing to all of the above is denial. This ADR closes the denial.

At the same time, the underlying truth that the framework's contract is the **MCP** (and the MCP could in principle adapt to other backends) is preserved as a theoretical extension point.

## Decision

**GitHub is the framework's primary platform** — the platform on which the framework ships, recommends adoption, and itself develops (dogfood per ADR-008). This applies to three concerns simultaneously:

| Concern | GitHub mechanism | Status |
|---|---|---|
| **Backend of the graph** | Issues + sub-issues + Projects v2 + Milestones + Releases + labels + PR reviews | Primary supported (ADR-001) |
| **Orchestrator of the project's pipeline** | GitHub Actions | **Primary recommended** (this ADR) |
| **Distribution of the framework itself** | GitHub template repository + GitHub Releases for SEM-AI's own versioning | Primary (ADR-008) |

The framework gives adopters one **coherent platform** for the full product lifecycle — intent (graph), build (CI), deploy (CD), publish (Releases) — without integration tax across vendors.

### Why GitHub-first is honest

Five reasons, in order of weight:

1. **Native end-to-end coherence.** Every primitive the framework relies on is a GitHub native object. Adding GHA as the recommended orchestrator completes the stack: the graph and the pipeline share the same platform, the same auth, the same event model, the same labels and cross-references. No glue code, no third-party integrations to maintain.

2. **Zero integration tax for adopters.** A team that adopts the framework already has GitHub. They don't need to provision a separate CI service, set up cross-tool auth, or maintain webhook bridges to keep their orchestrator and their graph in sync. `Closes #N` in a PR description, fired by their GHA pipeline, updates the graph natively.

3. **Marketplace coverage.** GitHub Marketplace hosts thousands of Actions for AWS / GCP / Azure / Docker / Kubernetes / Maven / Gradle / npm / pytest / Trivy / Snyk / SonarCloud / etc. The framework does not invent build/deploy automation; the adopting team picks from the existing marketplace and the framework integrates natively because everything happens in the same platform.

4. **Dogfood consistency.** SEM-AI's own CI/CD pipeline (per ADR-008) is GHA. If adopters are recommended GHA, the framework's own development is operating exactly as it asks adopters to operate. The framework is genuinely usable to itself.

5. **Adoption velocity.** Frameworks that try to be vendor-neutral from day one rarely finish v1. The first adoption case requires committing to a platform; otherwise every decision has to be re-validated against N backends. GitHub-first lets v1.0 happen.

### The MCP layer as the theoretical extension point

The framework's contract — the surface that an adopter actually talks to — is the engine MCP (the 19 graph tools + 3 Milestone/Release bridges + `acting_role` / `triggered_by` enforcement, per ADR-001 / ADR-004). The MCP is the abstraction; GitHub is its primary implementation.

**In principle**, the same MCP contract could be implemented against:

| Backend / orchestrator | Hypothetical MCP |
|---|---|
| Jira | `mcp__jira__*` — maps Issues + Sub-tasks + Epics to the graph types |
| Linear | `mcp__linear__*` — maps Issues + Projects to the graph types |
| GitLab | `mcp__gitlab__*` — maps Issues + Epics + Releases to the graph types |
| Azure DevOps | `mcp__azdevops__*` — maps Work Items to the graph types |
| Jenkins | as an orchestrator alternative to GHA, integrated via webhooks → MCP |
| GitLab CI | same — alternative orchestrator via webhooks |
| CircleCI / Buildkite / Argo | same |

**In practice**, the framework does NOT ship these adapters in v0.x. They are:

- **Theoretically possible**, because the MCP layer is the real contract.
- **Operationally unsupported**, because the framework's validators / hooks / Action examples assume the GitHub primitives.
- **Future work**, when the framework has reached v1.0 with at least one stable downstream adoption on GitHub, and demand from teams locked into other platforms justifies the engineering cost of porting the MCP and the examples.

This is the honest position: GitHub is the chosen home; the MCP layer keeps the option open without committing to it.

### Pipeline of the adopting project — GHA recommended, alternatives via webhooks

The pipeline of the adopting project (build, test, static analysis, package, publish, deploy to staging, deploy to production, notify) is **methodology** (per ADR-008), not framework concern at the level of which stages exist. But on the matter of *what platform runs the pipeline*, this ADR recommends:

**Primary recommendation: GitHub Actions.** The framework ships:

- A **sample pipeline** in `examples/.github/workflows/sample-pipeline.yml` (when implementation lands) demonstrating end-to-end integration: triggers on push / PR, runs build + tests + static analysis, deploys to a configurable target, fires the framework's hooks at the right moments, posts the 🏁 lifecycle comment on Issues that close.
- A short guide in the same `examples/` directory naming the points where the adopter customizes the sample (deploy target, build tool, test framework, secrets).

**Alternative: external orchestrator via webhooks.** Teams locked into Jenkins / GitLab CI / CircleCI / Buildkite can integrate by:

- Configuring their orchestrator to invoke the MCP at relevant pipeline events (build started, tests passed, deployed to staging, etc.) — likely via `gh api` calls from inside their pipeline steps, or via Issue comments that the MCP reads.
- Configuring webhook receivers (out of scope for the framework) that translate their orchestrator's events into MCP calls.
- This integration is **documented but unsupported**: the framework does not ship adapters for external orchestrators in v0.x. Adopters who choose this path own the integration.

The cost of the alternative path is honestly recognized — adopters with mature Jenkins / GitLab CI setups have a real adaptation tax. The framework does not pretend this tax is zero.

### What this ADR does NOT change

- **The catalog of seven Issue Types** (ADR-001) stays unchanged.
- **The role-jurisdiction matrix** (framework SKILL) stays unchanged.
- **The hook model** (ADR-004) stays unchanged — hooks remain primary; Actions remain opt-in extensions for cases hooks cannot cover (UI editing, external PRs without Claude Code, etc.).
- **The session model** (framework SKILL § Sessions) stays unchanged.
- **The neutral framing of ADR-008** about the *stages* of the adopting project's pipeline (the adopter chooses build/test/deploy stages, the framework does not impose them) stays unchanged. This ADR is about the *platform that runs the pipeline*, not about which stages it has.

## Alternatives considered

- **Maintain strict vendor neutrality.** Reject the recommendation of GHA and keep ADR-008's framing as final. Rejected because (a) the framework is operationally GitHub-first already; (b) pretending otherwise costs clarity for adopters without buying real neutrality; (c) frameworks that refuse to commit to a platform rarely reach v1.0; (d) the recommendation does not preclude alternatives — it acknowledges the natural fit while keeping the door open.

- **Make GHA required (not just recommended).** Adopters who can't use GHA cannot adopt the framework. Rejected because some adopters (regulated industries with on-prem Jenkins, organizations with corporate GitLab) cannot move to GHA in the near term. Requiring would exclude them entirely from a framework they could otherwise use with adaptation tax. Recommendation is the honest middle ground.

- **Ship MCP adapters for Jira / Linear / GitLab in v0.x.** Rejected. Each adapter is engineering work that requires testing against a backend whose semantics differ from GitHub's (Jira's parent/child model is not identical to GitHub sub-issues; Linear's Projects do not match Projects v2; etc.). Doing this work before v1 is reached on GitHub fragments the team's attention. Future work post v1.

- **Treat the orchestrator question separately from the backend question.** Two ADRs: one confirming GitHub backend, one recommending GHA orchestrator. Rejected because the two concerns reinforce each other — the value of GitHub-first is precisely the unified platform; splitting them into two ADRs would lose the coherence argument. One ADR, one decision.

- **Include the sample pipeline implementation in this ADR's commit.** Rejected. The ADR is the decision; the sample pipeline is implementation that lives in `examples/.github/workflows/sample-pipeline.yml`. Separate commits per ADR-008's distribution model (ADRs record decisions; implementation follows in dedicated commits).

## Consequences

- The framework's identity becomes more concrete: **SEM-AI is a GitHub-native framework** for AI-augmented product development. Adopters who use GitHub get the full benefit out of the box; adopters on other platforms can adapt at their own cost.
- `CLAUDE.md` will mention GitHub as the primary platform in its opening (next time it gets a refresh).
- `README.md` (when minimal version is created) opens with "SEM-AI is a GitHub-native framework. Use this template if your team works on GitHub. For other platforms, the MCP layer is the extension point — see ADR-009 for the theoretical adaptation path".
- `examples/.github/workflows/` gains, in a follow-up commit, a `sample-pipeline.yml` demonstrating end-to-end pipeline orchestration with GHA + integration with the graph via `Closes #N` and lifecycle comments.
- The framework's marketing/positioning (when it gets to that stage) is "GitHub-native AI product framework", not "platform-neutral product framework". Honest positioning.
- For adopters: the path of least resistance is clear. Use GitHub. The framework was designed for that.
- For future contributors: if demand for Jira / Linear / Jenkins / GitLab adapters emerges post-v1, the MCP layer is the extension point — adapters can be contributed without breaking the GitHub-native core.
- The "feature on the roadmap" of multi-backend support is **explicitly recognized as future**, not abandoned. Documenting it as theoretical-extension-point keeps the option alive.

## Status

Accepted. SEM-AI is GitHub-first: GitHub for the graph backend (ADR-001), GitHub Actions as the primary recommended pipeline orchestrator (this ADR), GitHub for distribution (ADR-008). The MCP layer is the framework's real contract and the theoretical extension point for future adapters to Jira / Linear / Jenkins / GitLab CI — but those adapters are not ship in v0.x. Adopters on non-GitHub stacks can integrate via webhooks + MCP at their own cost; the framework documents but does not ship the alternative paths.
