# Examples

Opt-in YAML workflows and templates that adopting projects can copy into their own `.github/workflows/` directory and customize. **None of these is shipped or activated by default in an adopting project** — they are reference templates you copy when you need them.

The framework presumes Claude Code on every developer (see ADR-004); hooks in `.claude/settings.json` cover most of the reactive surface. These examples cover the cases hooks can't (UI editing, external collaborators without Claude Code, asynchronous events) and the orchestrator of the project's own pipeline (per ADR-009).

## What's here

| File | Purpose | When you want it |
|---|---|---|
| [`.github/workflows/sample-pipeline.yml`](.github/workflows/sample-pipeline.yml) | Reference end-to-end deployment pipeline for an adopting project: build → test → static analysis → package → deploy-staging → e2e → deploy-production → 🏁 notify-graph. Heavily commented as a starter kit. | Always (this is the canonical pipeline shape per ADR-009). Copy, replace the placeholders with your actual build/test/deploy tools. |

The framework will also ship in `.github/workflows/`:

| File *(pending)* | Purpose | When you want it |
|---|---|---|
| `sem-ai-validate-posthoc.yml` | Validates Issues structurally (parent type, status legal, jurisdiction) after they are edited from the GitHub UI. | When humans edit Issues from the web UI without going through Claude Code |
| `sem-ai-security-review.yml` | Invokes the Security Officer role on PR opened, reviewing security implications. | When you have external collaborators (forked PRs without Claude Code) and want pre-merge security review as a backstop |
| `sem-ai-artifacts.yml` | Derives artifacts from PRs that merge with `Closes #N` linkage. | When merges sometimes happen outside Claude Code (auto-merge, web UI merge, external merger) |
| `sem-ai-sync-project.yml` | Adds newly-created Issues to the Projects v2 board with default custom fields set. | When humans create Issues from the UI / mobile app and you want them in the board automatically |
| `sem-ai-status-transition.yml` | Auto-transitions `ready-for-implementation → in-implementation → done` based on PR events. | Optional automation; explicit transitions remain the alternative |

## How to use these

1. **Browse the file**, read the comments.
2. **Copy** to your own project's `.github/workflows/` directory (preserve the filename so future updates from the framework merge cleanly).
3. **Customize** the placeholders for your stack — build tool, test runner, static-analysis tools, deploy targets, etc.
4. **Configure secrets** (e.g. `ANTHROPIC_API_KEY` for role-invocation Actions, deploy tokens, third-party scanner tokens) in your repo's Settings → Secrets.
5. **Configure environments** (`staging`, `production`) with required reviewers in Settings → Environments if the pipeline includes manual approval gates.
6. **Commit** the customized workflow to your default branch. It activates on the next push / PR.

## Updates

When SEM-AI ships a new version with changes to these examples (per ADR-008 + the changelog), your project's local copy does **not** automatically update — these are templates you own. To pick up changes:

1. Read the changelog for the SEM-AI version you're upgrading to.
2. `git diff` the framework's `examples/` directory between your adopted tag and the new tag.
3. Apply the relevant changes to your local copy, resolving conflicts with your customizations.

A `sem-ai upgrade` CLI is deferred (per ADR-008) until the patterns stabilize across 3+ downstream adoptions.

## Customization that's safe vs unsafe

- **Safe to change**: build commands, test commands, deploy targets, secret names, environment names, conditional logic in `if:` clauses, additional stages you add, extra notifications you wire (Slack/Teams/PagerDuty).
- **Unsafe to break**: the `notify-graph` job's contract — it parses `Closes #N` in PR descriptions and posts 🏁 lifecycle comments. If you change that contract (e.g. remove the comment, or rename the marker), the framework's `get_node_artifacts` (per ADR-001 § Native objects) will miss this session's mark in the Issue thread. Keep the contract; change the comment text only if you understand the consequences.

## Related framework pieces

- `.claude/settings.json` — hooks declared by the framework, the primary reactive layer (per ADR-004). Hooks cover Claude-Code-active scenarios; these Actions cover the rest.
- `engine/checks/` — shared validation + side-effect logic the hooks and Actions both invoke (per ADR-004 — pending implementation).
- `docs/adr/004-invocation-model.md` — the rationale for "hooks primary, Actions opt-in".
- `docs/adr/009-github-as-primary-platform.md` — the rationale for GitHub Actions as the recommended pipeline orchestrator.
