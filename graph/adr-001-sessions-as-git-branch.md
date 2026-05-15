---
category: adr
id: adr-001-sessions-as-git-branch
parent: "[[goal-01-self-bootstrap-validation]]"
artifacts:
  - "[[CLAUDE.md]]"
  - "[[.claude/commands/session-log.md]]"
  - "[[.claude/commands/session-context.md]]"
  - "[[.claude/commands/session-close.md]]"
  - "[[_obsidian/templates/session.md]]"
status: accepted
created: 2026-05-14
updated: 2026-05-14
supersedes:
superseded-by:
---

# ADR 001 — Sessions are git branches; session documents are the shared context

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — the decision is operating in the substrate as of session `2026-05-14-sem-ia-self-bootstrap`. The branch carrying this very conversation is `session/2026-05-14-sem-ia-self-bootstrap`, which is the operational evidence the decision is in force. CLAUDE.md Layer B § *Sessions = git branch* encodes the contract; the three slash commands (`session-log`, `session-context`, `session-close`) cover the ceremony moments.

## Context

A unit of work in SEM-IA (a multi-step elaboration, a cross-role thread, a milestone push) must survive interruption, role switch, and contributor change without context loss. Three forces are in tension:

1. **Persistence with versioning.** Whatever container holds session state must be diffable, revertable, mergeable, and inspectable historically. A unit of work has the same change-control needs as code.
2. **Branchable concurrency.** Several units of work may proceed in parallel. The substrate must allow concurrent sessions without one trampling another, and must allow merge of completed sessions back into the main line.
3. **Zero new infrastructure.** Adding a session database, a server, a workflow engine, or a custom CLI raises the cost of adopting SEM-IA on a new project. The existing infrastructure of any software project already contains a tool that solves all three forces: git.

A session is also semantically richer than a branch: it has participants, a narrative log, references to nodes touched, and a closing summary. That semantic richness needs a home that is human-readable, AI-readable, and in the same versioning substrate. The natural home is a markdown document committed alongside the work the session produced.

Capability [[cap-09-session-continuity]] declares the property; this ADR records the structural decision that materialises it.

## Decision

We adopt **two coupled artifacts per session**:

1. A **git branch** named `session/<YYYY-MM-DD>-<topic-slug>`. The branch's existence *is* the session's open/closed state — there is no separate `status:` field on the session document.
2. A **session document** at `sessions/<YYYY-MM-DD>-<topic-slug>.md`, derived from `_obsidian/templates/session.md`, with fixed sections (Context, Log, Artifacts touched, Subagent consultations, Closing summary).

The currently checked-out branch is the session you are inside; `main` means between sessions. Listing open sessions is `git branch --list 'session/*'`. Closing is either a merge to `main`, a PR, or branch deletion — decided at `/session-close` time.

Role information is captured as the `participants` array of the session document and as the role tag on each Log entry; the session itself is role-agnostic and may carry contributions from several roles in sequence or via subagent dispatch.

## Consequences

**Positive:**

- **Zero new infrastructure.** Every developer environment already has git; no session server, no database migration, no auth layer.
- **Branch state IS session state.** No drift possible between *"is the session open?"* and *"does the branch exist?"*. Removing one field that can lie removes one source of bugs.
- **Native diff and history.** Every change made within a session is reviewable via `git log` / `git diff` on the branch. The session document and the artifacts the session produced share the same audit history.
- **Concurrency for free.** Several sessions can be open at once on the same repo with no coordination cost.
- **Merge semantics for closing.** Closing a session merges its work into `main` using existing git workflow; the team's conflict-resolution and code-review practices apply unchanged.
- **Substrate portability.** A new project lifting the SEM-IA substrate (per [[cap-13-portability]]) inherits session continuity for free, because the underlying mechanism is git, not a SEM-IA-specific service.

**Negative:**

- **git literacy required.** A user who does not know git cannot operate the session model. SEM-IA is not usable by non-engineers under this decision. This is consistent with the framework's target audience (software engineering effort) but it is a real exclusion.
- **Branch hygiene becomes session hygiene.** Stale branches, abandoned sessions, orphan session documents (a `sessions/...md` whose branch is gone, or a branch whose document is missing) are now possible failure modes. The bootstrap procedure addresses them conversationally rather than structurally.
- **No central session registry.** Listing open sessions requires a git command; there is no dashboard view without additional tooling. For a solo author this is acceptable; for a multi-contributor team without shared remote access this becomes friction.
- **Session merging is not session locking.** Two contributors can open sessions touching the same node; the conflict only surfaces at merge time. This matches git's optimistic-concurrency model; it is a deliberate trade-off against pessimistic locking.

**Neutral:**

- **The "session" concept is not a Jones-anchored construct.** The bibliographic anchors for project planning (Jones BP #15) speak of milestones, work packages, releases — not sessions. The session concept is operational scaffolding for AI-mediated work; it is documented in CLAUDE.md Layer B as project convention. This ADR does not claim the concept is in the audited bibliography.
- **Branch-naming convention is conventional, not enforced.** `session/<YYYY-MM-DD>-<topic-slug>` is a convention; no hook today rejects branches that don't follow it. The convention is enforced socially via the bootstrap procedure.
- **Session document templating is decoupled from branch creation.** The bootstrap procedure performs both in sequence; nothing structural binds them together. A future tightening (a git hook, a slash command) would close this gap if needed.

## Alternatives considered

- **Session = database row in a session service.** Rejected. Adds infrastructure cost, breaks portability, requires auth, and creates a second source of truth alongside git. Diff and revert semantics would have to be reinvented.
- **Session = long-running LLM context window with checkpoints.** Rejected. Couples session persistence to a specific LLM harness and to its context-window API; defeats portability across harnesses (already a non-goal of G3 but a future direction); the substrate must not depend on a vendor's runtime.
- **Session = a tag plus a JSON manifest at repo root.** Rejected. Tags are not branches; tagged work cannot accumulate further commits without ambiguity. The concurrency story is weaker than branches'.
- **Session = git worktree (one filesystem directory per session).** Rejected as the default mechanism, though worktrees remain available as an *advanced* affordance. Worktrees solve the "I want to swap sessions without losing local state" problem but add directory-tree complexity that most contributors don't need; branches are the simpler default.
- **No sessions; work directly on `main` always.** Rejected. Loses the shared-context property (pillar 3 of the Layer B operating triangle), forces every conversation to start cold, and removes the audit trail that ties cross-role work together.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Materially affected. The substrate has two top-level work modalities — *on main* and *in a session* — and the session modality is the dominant one. The branch becomes the principal structural unit of work-in-progress.
- **2. Data structure:** Materially affected. Session documents are first-class markdown nodes with a defined template (`_obsidian/templates/session.md`) and required sections (Context, Log, Artifacts touched, Subagent consultations, Closing summary). The session schema is part of the framework's data architecture.
- **3. Interfaces to outside world:** Materially affected. The interface to the contributor (human or AI) for opening/resuming/closing a session is conversational — the bootstrap procedure in CLAUDE.md Layer B — supplemented by three slash commands. There is no GUI; the surface is the terminal + the editor.
- **4. Decomposition into functional components:** Affected. The Layer-B operational components are: the bootstrap procedure, the three slash commands, the session template, the role agents that write into the session, and git itself. Each is independently replaceable; the session contract is the integration point.
- **5. Linkage / information transmission among components:** Materially affected. The session document is the *shared context* across roles within a thread — the mechanism by which information transmits from role to role (via subagent dispatch logged in `## Subagent consultations`) or across time (via Log entries with role tags). This linkage is the operational substrate of pillar 3 of the triangle.
- **6. Performance attributes:** Not materially affected. Session-document size grows with Log entries but bounded in practice (one session, one topic, one or two months at most). No performance budget is set; none is expected to be needed below the >100,000 FP tier where Jones (BP #39) would require specialist instrumentation. Above that tier, session-document length and read-time become a concern; not applicable at SEM-IA's current scale.
- **7. Security attributes:** Indirectly affected. Branch-protection and access-control on `main` apply transitively to session merges — a session's work only lands in `main` via the same merge-review path as any other change. Session documents inherit the repository's secrecy posture (private repo = private sessions). No additional security control specific to sessions is introduced.

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics, used here as the audit grid.
- CLAUDE.md Layer B § *Sessions = git branch*, § *Session bootstrap*, § *Writing to the session doc*, § *Slash commands* — the substrate that operationalises this decision.
- `_obsidian/templates/session.md` — the session-document schema.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**; adopted as convention.
- Capability anchor: [[cap-09-session-continuity]] (the property this decision materialises).
