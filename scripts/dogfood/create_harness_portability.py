#!/usr/bin/env python3
"""Bootstrap dogfood Part 7: create G9 (harness portability) + ADR.

Surfaces a real architectural gap: the framework is Claude Code-first by
default but the boundary between harness-agnostic substrate (engine/) and
harness-specific binding (.claude/) was implicit until now. This commit:

  - Creates G9 as a new goal under vision #1, analogous to G8 (backend
    portability) but on the harness axis.
  - Creates an ADR (type:adr) as child of G9 recording the deliberate
    choice: Claude Code-first for v0.x; engine/ stays harness-agnostic;
    per-harness bindings (.cursor/, .windsurf/, .codex/, etc.) deferred
    to post-v1 with the same shape as .claude/.

Idempotent: skips creation if a node with the same title already exists.

Run once:
    SEM_AI_REPO=PelayoU/SEM-AI .venv/bin/python scripts/dogfood/create_harness_portability.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.adapters import GitHubAdapter, load_config  # noqa: E402
from engine.core import api  # noqa: E402
from engine.core.catalog import NodeType, Status  # noqa: E402
from engine.core.permissions import Role  # noqa: E402


GOAL_TITLE = "Harness portability viable post-v1"

GOAL_BODY = """## Map

- Children: none directly — this goal is satisfied by maintaining engine/ harness-agnostic; per-harness bindings (future capabilities) added when external demand pulls them
- Related: vision #1 § Adopted trends (MCP as lingua franca of tool-AI integration); G8 #18 (analogous portability axis for backends); the ADR child below recording the boundary

## Outcome statement

A non-Claude-Code adopter (Cursor / Windsurf / Codex CLI / private internal harness) can use SEM-AI by adding a thin harness binding without modifying `engine/` or any other harness's binding. The engine substrate (MCP server + checks + adapters + catalog) is harness-agnostic and verifiably so via import-clean discipline.

## Stakeholder

Two segments: **non-Claude-Code-using adopter** — enterprise teams or individuals whose AI tooling is Cursor / Windsurf / Codex / a private harness; they need SEM-AI to work in their environment without forking. Plus **SEM-AI maintainers** responsible for keeping `engine/` free of Claude-Code-specific imports; without this discipline maintained continuously, future portability becomes infeasible without rewrite.

## Parent vision

#1

## Horizon

Continuous discipline from v0.3 onwards (engine/ stays harness-agnostic). Time-bound checkpoint: **post-v1.0 release** for the first non-Claude-Code binding (community RFC or stub binding accepted by maintainers).

## Acceptance check

Either: (a) ≥1 community RFC documents a complete harness binding for a non-Claude-Code AI host (Cursor / Windsurf / Codex / etc.) and SEM-AI maintainers accept it as viable, OR (b) a stub binding directory (e.g. `.cursor/`) exists demonstrating the harness boundary holds without `engine/` changes. **Continuous lifetime gate**: `grep -r "from \\.claude\\|import .*claude" engine/` returns empty (verifiable in CI; trivial to enforce).

## Why this goal

Vendor lock-in to a single AI host limits TAM and mirrors G8's concern at a different architectural axis. Even if v1.0 ships Claude Code-only, the engine substrate must demonstrably support other harnesses or the "MCP-native" positioning becomes a trap that closes off enterprise adopters whose tooling is fixed (Cursor in many startups, Codex in others, private harnesses in regulated industries).

The discipline must start now — engine/ is already mostly harness-agnostic by design (MCP is the protocol surface); enforcing it explicitly costs almost nothing and prevents painting into a corner. The cost of fixing harness-leakage *after* it accumulates would be a rewrite.

## Holistic dimensions

- **Functionality**: engine/ surface stays harness-agnostic; .claude/ is the v0.x reference binding; per-harness bindings sit as siblings of .claude/, never as variants inside engine/
- **Technology**: MCP protocol is the harness boundary — engine speaks MCP, harness binding translates between MCP and host-specific mechanisms (skill loading, hook registration, agent identity, slash commands)
- **UX design**: agent-interaction shape is harness-specific (each host has its own UX surface) — the framework provides typed graph + role contracts + reactive substrate uniformly underneath
- **Monetization**: opens enterprise markets locked to non-Claude-Code tooling — removes a deal-breaker for buyers whose AI tooling decisions are made elsewhere in the org
- **Acquisition**: "MCP-native, harness-portable" — concrete positioning for buyers wary of AI vendor lock-in; analogous to the "GitHub-native, backend-portable" positioning that G8 backs
- **Offline experience**: engine MCP server runs locally regardless of harness; bindings are local files; no network dependency on any specific host's cloud services
"""


ADR_TITLE = "Claude Code is the primary AI harness; engine/ stays harness-agnostic; bindings post-v1"

ADR_BODY_TEMPLATE = """## Map

- Parent: {goal_id} (G9 — Harness portability viable post-v1)
- Related: #10 (ADR-009 — GitHub is the primary platform; this ADR is the harness-axis sibling); #28 (C10 — Adopter-customizable methodology layer; harness bindings are a layer of customization); #29 (ADR — methodology boundary; analogous discipline at the harness boundary)

## Status

accepted

## Context

SEM-AI through v0.3 has used Claude Code as its only AI harness. The engine MCP server (`engine/mcp_server.py`) is harness-agnostic by design — MCP is a protocol, and any compatible host (Cursor, Claude Desktop, Windsurf, internal tools) can load the server unchanged. But the framework's *agent operating surface* — agents, skills, hooks, slash commands — all live under `.claude/` and use Claude Code-specific mechanisms (skill loading, agent identity, settings.json hook declarations, slash command registration, event names like `SessionStart` / `PreCompact` / `PostToolUse` / `PreToolUse`).

This creates an asymmetry: the *engine substrate* is portable today; the *framework affordances* are Claude Code-bound. An adopter whose AI tooling is Cursor / Windsurf / Codex CLI / a private internal harness can load the MCP server today but loses the reactive layer (auto-invoked checks, session continuity, role-correct agent invocation, slash commands) until per-harness bindings exist.

Two concerns were unaddressed until this ADR:

1. **Vendor lock-in to a single AI host** mirrors the GitHub-first concern that ADR-009 (#10) addresses for backends. Without an explicit harness portability stance, the framework's "MCP-native" positioning becomes a trap that closes off enterprise adopters whose AI tooling is fixed elsewhere in the org.

2. **Without an explicit boundary** between harness-agnostic and harness-specific code, future contributors might leak Claude Code-isms into `engine/` (importing from `.claude/`, encoding Claude-specific event names, assuming Claude-specific config shapes). Once leaked, future portability becomes a rewrite, not a binding.

## Decision

**Adopt Claude Code-first as a deliberate v0.x choice**, analogous to GitHub-first per ADR-009. The engine substrate stays harness-agnostic via MCP. Harness bindings (`.claude/`) are the v0.x reference; other-harness bindings (`.cursor/`, `.windsurf/`, `.codex/`, etc.) are deferred to post-v1 with the same shape: per-harness directory with that harness's agent definitions, skill loading mechanism, hooks (mapped to its event model), and command registration.

**The boundary:**

- **`engine/`** — pure Python, MCP-protocol-only, no imports from `.claude/` or any other harness binding, no Claude Code-specific assumptions (event names, config keys, skill discovery rules)
- **`.claude/`** — Claude Code-specific binding: agents, skills, hooks declared via Claude Code's `settings.json`, slash commands
- **`scripts/`** — shell scripts invoked by `.claude/` machinery; the scripts themselves should be generic (no Claude-specific code), only their *invocation* is Claude Code-shaped
- **Future per-harness bindings** — e.g. `.cursor/`, `.windsurf/`, `.codex/` — live as siblings of `.claude/`, each one mapping the framework's reactive contract (when-to-invoke-which-role, when-to-run-which-check) to its host's specific mechanisms

**For non-Claude-Code adopters today:**

- The engine MCP server (`python -m engine.mcp_server`) is loadable by any MCP-compatible host today; the typed graph + structural enforcement + role-bound writes all work
- They lose the framework's reactive affordances (auto-invoked checks, session continuity, lifecycle Issue comments) until a per-harness binding exists
- This is acceptable for v0.x — the *value proposition* is intact (typed graph + mechanical enforcement + role-coherent agents) even without the reactive layer; the reactive layer is *amplification*, not the substrate

**Enforcement:**

- CI lint check: `grep -r "from \\.claude\\|import .*\\.claude" engine/` must return empty
- New engine/ contributions are reviewed against this boundary
- Harness-specific additions go to the appropriate binding directory, never to engine/

## Consequences

**What becomes easier:**

- Clear boundary for contributors — no Claude Code-isms allowed in `engine/`, no ambiguity about where new code goes
- A future Cursor / Windsurf / Codex binding contributor knows exactly what scope they're implementing — implement the same reactive contract that `.claude/` covers, using their host's mechanisms
- The portability claim is honest — `engine/` *already* works without Claude Code via MCP; the only missing pieces are per-host reactive bindings
- Marketing positioning is coherent — "MCP-native engine + Claude Code-first reference binding; other harnesses welcome post-v1"

**What becomes harder:**

- The framework now ships with "missing parts" for non-Claude-Code adopters (no agents, no hooks, no slash commands until their host's binding exists); the value proposition becomes "typed graph + structural enforcement now, reactive affordances when your host's binding ships"
- Contributors might want to add harness-specific convenience features in `engine/` (e.g. "add a hook helper for Claude Code's PostToolUse event format") — must be vigilant about rejecting these and routing them to `.claude/` or future binding directories
- The CI lint check adds a small maintenance overhead; worth it

**What is now locked in:**

- `engine/` stays import-clean of `.claude/` from this commit forward (verifiable via grep / CI lint)
- Per-harness bindings always live as siblings of `.claude/`, never as variants inside `engine/` or `scripts/`
- The MCP protocol is the canonical agent-facing contract; harness bindings translate between MCP and host-specific mechanisms — they do not bypass MCP to talk directly to engine internals
- Adding a non-Claude-Code binding is a framework-level contribution (likely a new ADR + capability) — not an adopter customization

## Security attributes

N/A — portability boundary, no security surface. Per-harness bindings inherit the security posture of their host (Claude Code, Cursor, etc.); the framework does not introduce new security responsibilities at the boundary.

## Alternatives considered

- **Design a "framework binding spec" abstract layer with per-harness translators now.** Rejected: premature without a second harness in scope; the MCP protocol is already the abstraction at the engine-agent boundary, and another layer on top would duplicate. The spec emerges from the second binding's needs, not from speculation.

- **Acknowledge silently — no goal, no ADR, just operational reality.** Rejected: enterprise adopters and contributors both ask "what about Cursor?" / "where would I add Windsurf support?" — the framework needs a documented answer, even if the answer is "post-v1 via community binding".

- **Commit to multi-harness shipping in v1.0** (Claude Code + Cursor + ≥1 other). Rejected: stretches v1.0 scope without proof that any non-Claude-Code adopter wants it; better to ship Claude Code-first and let demand pull a second binding. Pre-building bindings without a real adopter usually over-fits to imagined needs.

- **Lift the .claude/ machinery into engine/ and add per-host adapter shims at the boundary.** Rejected: would couple the engine to specific reactive-event models (Claude Code's hook event names, Cursor's analogues); the cleaner factorization is the reverse — engine stays substrate, bindings live near their host's mechanisms.
"""


def main() -> int:
    cfg = load_config()
    adapter = GitHubAdapter(cfg)

    print(f"Target repo: {cfg.repo}")
    print()

    # ----- Step 1: Find vision -----
    visions = adapter.query_issues(type=NodeType.VISION)
    if not visions:
        print("FAIL: no vision Issue found. Run migrate_to_issues.py first.")
        return 1
    vision = visions[0]
    print(f"==> Vision: {vision.id}")

    # ----- Step 2: Create G9 (idempotent) -----
    existing_goals = {g.title: g for g in adapter.query_issues(type=NodeType.GOAL)}
    if GOAL_TITLE in existing_goals:
        goal = existing_goals[GOAL_TITLE]
        print(f"    [exists] G9 = {goal.id} ({goal.title!r})")
    else:
        print(f"    [..] creating G9 {GOAL_TITLE!r}", end=" ", flush=True)
        try:
            goal = api.create_node(
                adapter,
                type=NodeType.GOAL,
                parent_id=vision.id,
                title=GOAL_TITLE,
                body=GOAL_BODY,
                status=Status.ACTIVE,
                acting_role=Role.PM,
            )
        except Exception as e:
            print(f"FAILED: {e}")
            return 1
        print(f"→ {goal.id}")

    # ----- Step 3: Create the ADR as child of G9 (idempotent) -----
    existing_adrs = {a.title: a for a in adapter.query_issues(type=NodeType.ADR)}
    if ADR_TITLE in existing_adrs:
        node = existing_adrs[ADR_TITLE]
        print(f"    [exists] ADR = {node.id} ({node.title!r})")
    else:
        print(f"    [..] creating ADR under {goal.id}", end=" ", flush=True)
        adr_body = ADR_BODY_TEMPLATE.format(goal_id=goal.id)
        try:
            node = api.create_node(
                adapter,
                type=NodeType.ADR,
                parent_id=goal.id,
                title=ADR_TITLE,
                body=adr_body,
                status=Status.ACCEPTED,
                acting_role=Role.ARCHITECT,
            )
        except Exception as e:
            print(f"FAILED: {e}")
            return 1
        print(f"→ {node.id}")

    print()
    print("==> Done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
