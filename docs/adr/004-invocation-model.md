# ADR-004 — Invocation model: hooks + MCP + Actions as opt-in examples

- **Status**: accepted
- **Date**: 2026-05-23
- **Supersedes**: —
- **Superseded by**: —

## Context

The framework is, in its own framing, **infrastructure for working with AI**: six role-homologous agents that read and write a shared project-intent graph, with roles that **invoke each other automatically** as events on the graph warrant it. A Security Officer reviewing a spec when it is marked `ready-for-implementation` is not a methodology choice — it is the mechanism by which the roles' independence becomes useful. Without that auto-invocation, the six agents are just six dispatch-on-demand personas.

But "auto-invoke a role on an event" can be implemented in several places, each with different reach and cost:

| Mechanism | Where it runs | When it fires | Who sees it |
|---|---|---|---|
| **MCP tool** | in the agent (Claude Code process) | the agent calls it | only the agent |
| **Hook** (Claude Code) | in the agent (Claude Code process) | a CLI event (PreToolUse, PostToolUse, SessionStart, PreCompact, Stop, UserPromptSubmit, …) | only when Claude Code is being used in this repo right now |
| **GitHub Action** | on a GitHub runner VM | a GitHub event (push, PR, issues, milestone, schedule) | everyone, always, regardless of who provoked the event |

Picking one without an explicit decision means defaulting badly. This ADR records the decision: **hooks first, Actions as opt-in examples, MCP for writes**.

## Decision

### Premise

**The framework presumes Claude Code (or an equivalent CLI with the same hook surface — OpenCode, future tools) on every developer of the project.** This is the asymmetry that makes hooks viable as the primary mechanism. If a project cannot assume that, it falls back to Actions (covered as opt-in below); but the canonical adoption pattern is "everyone uses Claude Code".

### Three mechanisms, three roles

| Mechanism | Role in the framework |
|---|---|
| **MCP** (engine tools) | The agent's *hand* — synchronous writes to the graph (`create_node`, `update_node`, `transition_status`, …) + the three bridges to Milestones/Releases (`create_milestone`, `assign_to_milestone`, `publish_release`). Initiated by the agent. |
| **Hooks** (Claude Code) | The framework's *reactive nervous system* — local, runs in the agent's process, fires on CLI events, can invoke role-agents automatically as reactions. Initiated by Claude Code events. |
| **GitHub Actions** | The *bridge from outside the agent* — runs on GitHub runners, fires on GitHub events. Necessary only when something happens outside Claude Code that the framework needs to react to (a human edits an Issue from the web UI; a colaborator without Claude Code opens a PR; an event fires when no dev is running the CLI). Initiated by GitHub events. |

### What the framework ships

**Shipped (in the framework's `.claude/settings.json` and skills):**

- **The MCP** with the full graph tool set (19 typed tools, from ADR-001) **plus** the three bridges to Milestones/Releases (`create_milestone`, `assign_to_milestone`, `publish_release`, with `acting_role` enforcement, from ADR-001 § *Milestone and Release operations*).

- **Five hooks** — the minimum that materialises the framework's auto-invocation contract:

  | Hook | Event | Action |
  |---|---|---|
  | `SessionStart` | new Claude Code conversation | When on a `session/*` branch, read `sessions/<id>.md` (Frontmatter + Context + Decisions + Handoff) + project map mínimo + Issues in `in-play`. |
  | `PreCompact` | before compactation | Refresh the Handoff with current state; preserve Decisions across the compact. |
  | `PostToolUse` on `mcp__sem_ai_engine__transition_status` | a node transitions status | Invoke the role that owns the next step (spec→`ready-for-implementation` invokes security-officer review; adr→`accepted` invokes architect coherence check). |
  | `PreToolUse` on `Bash(gh pr create *)` | the agent opens a PR | Invoke security-officer review + pm acceptance check pre-emptive; block on critical findings. |
  | `PostToolUse` on `Bash(gh pr merge *)` | the agent merges a PR | Derive artifacts from the PR's `Closes #N` references into the affected Issues. |

- **One skill** — `/catch-up`:

  | Skill | Use |
  |---|---|
  | `/catch-up [since <X>]` | On-demand digest of graph changes since the last invocation (or since X). Filters native GitHub notifications, groups by node type, surfaces decisions and new nodes. Defaults to "since last invocation" via state file `.sem-ai/last-catch-up.json`. |

  Pull-mode, not push: not in `SessionStart`, because the project map already shows current state; redundant to push notifications at every bootstrap.

- **The `engine/checks/` library** — the validation + side-effect logic the hooks invoke. One source of truth, callable from a hook (in Claude Code), from an Action (in a runner), or from a manual CLI run. Examples: `security_review.py`, `architect_coherence.py`, `pm_acceptance.py`, `artifacts_derive.py`.

**Not shipped (in `examples/.github/workflows/`, opt-in per project):**

- **`sem-ai-validate-posthoc.yml`** — fires on `issues.opened` / `issues.edited` / `pull_request.opened`. Invokes the same `engine/checks/` library that the hook would, post-hoc. **For repos where humans edit Issues from the GitHub UI** without going through Claude Code.

- **`sem-ai-security-review.yml`** — fires on PR opened. Invokes security review against the diff. **For repos with external collaborators** (without Claude Code installed) whose PRs need to be reviewed structurally.

- **`sem-ai-artifacts.yml`** — fires on PR merged. Same logic as the `PostToolUse on gh pr merge` hook, but catches merges that happen outside Claude Code (auto-merge, UI merge, external merge). **For repos where merges don't always go through Claude Code.**

- **`sem-ai-sync-project.yml`** — fires on Issue opened from the UI. Adds the Issue to the Projects v2 board with default custom fields set. **For repos where humans create Issues from the UI.**

- **`sem-ai-status-transition.yml`** — auto-transitions `ready-for-implementation → in-implementation → done` based on PR events. **For projects that want the automation; explicit transitions remain the alternative.**

A project enables any of these by copying the YAML from `examples/` to its own `.github/workflows/` and configuring the API key as a GitHub secret. The framework ships the library + the examples; the activation is the project's call.

### Coordination between hooks and Actions

The hook and the equivalent Action share the same `engine/checks/` logic — they are thin adapters that call the same function. **Dedup mechanism**: when a hook executes a check successfully, it leaves a marker (a label `checked:<check-name>@<commit-sha>` on the Issue or a commit trailer). The Action looks for the marker first; if present, it skips. Result: in repos where Claude Code is the dominant path, hooks pre-empt and Actions are nearly silent; in repos with external traffic, Actions catch what hooks miss without duplicating work.

### Permissions for agents invoked by hook/Action

A role agent invoked by a hook or Action runs **with restricted permissions**:

- **Reads** the graph freely.
- **Posts comments** on Issues (its findings, summaries, references).
- **Opens new Issues** with label `bug` or label `security-finding` if it discovers something.
- **Does NOT transition status** on existing Issues.
- **Does NOT edit body** of Issues it didn't create.

This preserves "the human confirms" while allowing reactive automation. Findings are always visible (as comments or new Issues); decisions that change state remain with the human in front of a Claude Code session, with the relevant role active.

The MCP enforces this via the `triggered_by` parameter, set automatically by hooks/Actions when they invoke a role. `triggered_by=action` (or `triggered_by=hook`) restricts the available operations. `triggered_by=human` (the default when a human prompts a role in a Claude Code conversation) gives full operations subject to the normal jurisdiction rules.

## Why hooks not Actions as primary

Four reasons:

1. **Pre-emptive vs reactive.** A hook fires before the PR leaves the dev's machine. An Action fires after. For security-critical reviews, pre-empting is structurally better — the bad code never reaches main.

2. **Cost.** Hooks consume the dev's already-active Claude Code session. Actions consume GitHub Action minutes + API tokens stored as secrets. For a small / medium team, hooks are nearly free; Actions add a per-PR cost line.

3. **Latency.** Hooks run instantly. Actions wait for a runner.

4. **Coverage where it matters most.** Hooks cover everyone who uses Claude Code; if the team standardises on it, that's everyone. Actions are necessary only for the residual cases (external collaborators, UI editing).

If `(team uses Claude Code) ⇒ True` for the project, hooks are the right primary mechanism.

## Why Actions still exist as opt-in

Three residual cases where hooks alone are insufficient:

1. **External collaborators** (open-source projects, contractor PRs, etc.) without Claude Code installed.
2. **Humans editing Issues from the GitHub UI / mobile app** without going through Claude Code.
3. **Asynchronous events** like auto-merge, scheduled tasks (cron), or events that fire when no dev is in front of the CLI.

For these the project enables the corresponding Action from `examples/`. The framework provides the library + the YAML examples; the team activates them per their needs.

## What the framework does NOT do (related work)

- **Mid-conversation agent switching.** Not available in Claude Code today (verified). A role change requires a new conversation (`claude --agent <new>` on the same branch); the SessionStart hook bootstraps the new agent from the doc. See `framework/SKILL.md` § *Sessions*.

- **Webhook receivers.** The framework does not run a server that receives webhooks. All reactive work goes through hooks (CLI events) or Actions (GitHub events). Anything else is out of scope.

- **Notification routing** (Slack / Teams / email). Project-supplied if needed; the framework's notification primitive is the GitHub Issue comment + the `/catch-up` skill that digests changes on demand.

## Alternatives considered

- **Actions as primary, hooks as opt-in.** The inverse of this decision. Rejected because (a) most teams adopting an AI-augmented workflow are already going to standardise on a CLI like Claude Code; (b) Actions have non-trivial per-event cost in tokens + runner minutes; (c) hook latency / pre-emptive behaviour wins where it matters most.

- **MCP-only, no hooks no Actions.** Considered. Rejected: the MCP is synchronous-from-the-agent only. It cannot fire reactions; the agent has to explicitly request the cross-role consult. Auto-invocation of role-agents on graph events would be impossible. The whole "six roles watching each other" model collapses to "six roles waiting to be called".

- **Build a webhook receiver server.** Considered for routing GitHub events to local hooks. Rejected: adds a server to maintain; out of scope for an installable framework. If a team needs it, they build it on top.

- **Ship all five Action examples activated by default.** Rejected: most projects don't need most of them. Token cost is non-trivial. Better to ship the library + examples and let each project enable what it needs.

- **Conversation transcript replay between roles.** Considered for cross-role context (so the new role sees the previous role's transcript). Rejected: the transcript is per-conversation and Claude Code doesn't expose it across conversations; the session doc is the explicit bridge (ADR-001 / framework SKILL § *Sessions*).

## Consequences

- The framework's `.claude/settings.json` declares the five hooks above. They are present from `/init` onwards.
- `.claude/skills/catch-up/SKILL.md` ships with the framework.
- `engine/checks/` is part of the framework's code package, importable from hooks and from Actions.
- `examples/.github/workflows/` ships with the five YAML examples + a README that lists them and the criteria for enabling each.
- The `/session-open` and `/session-close` skills (pending implementation) interact with the hook system at their entry/exit points.
- The MCP's `triggered_by` parameter is documented as a write-time argument; hooks and Actions set it; humans default to `human`.
- The framework's status as "infrastructure for working with AI" is materially supported by this ADR: the auto-invocation of roles by graph events is what makes it more than a set of agent.md files. Without this, the framework would be six agents waiting to be called; with this, the framework is the agents collaborating reactively over the graph.

This ADR's implementation (the actual hooks, the engine/checks/ library, the Actions YAML examples) is deferred to subsequent commits; this records the decision and the contracts.
