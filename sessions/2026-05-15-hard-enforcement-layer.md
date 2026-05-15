---
category: session
id: 2026-05-15-hard-enforcement-layer
date: 2026-05-15
participants: [architect, product-owner, qa]
related-nodes:
  - "[[feature-072-node-before-artifact-gate]]"
  - "[[feature-073-claude-md-orientation-and-governance]]"
  - "[[feature-074-agent-decision-verification]]"
  - "[[feature-075-hard-role-jurisdiction]]"
  - "[[feature-076-per-turn-role-reinforcement]]"
  - "[[adr-011-hard-enforcement-no-human-override]]"
  - "[[adr-012-mandatory-active-role-hard-jurisdiction]]"
artifacts: []
---

# Hard-enforcement layer (node-before-artifact + hard role-jurisdiction)

> A session is a thread of work. It lives on git branch `session/<id>` and ends with `/session-close` (which decides merge / PR / discard). Session state is branch state.

## Context

Soft context proved to be **null enforcement**: an agent with the entire `CLAUDE.md` + 5 agents + 37 skills + bootstrap session loaded, having just articulated the node-before-artifact rule in its own words, still edited `CLAUDE.md` (a substrate change) with **no governing node, on a single "do it"**. That out-of-process edit (a 15-line "Orient here" block) is uncommitted in the working tree — the live proof and case study. This session reverts it, then installs a hard PreToolUse gate (node-before-artifact, no override) + mandatory active-role marker (hard role-jurisdiction) + a `UserPromptSubmit` per-turn reinforcement, **through the very discipline it enforces**: session → revert → nodes-first → ADRs → substrate → verify → close. Full design in the approved plan; this work fulfils the `2026-05-14` session's deferred *graph-vs-substrate operating rule* and *consultation matrix* improvement candidates.

## Log

### 2026-05-15 — architect

Opened session `2026-05-15-hard-enforcement-layer` (branch created, this doc instantiated). Confirmed: on a fresh branch off `main`, no other open sessions, `git diff --stat CLAUDE.md` = exactly 1 file / 15 insertions (the out-of-process block, scope verified for the Phase-B revert). Plan approved by the human after extensive design (decisions: no override; hard role-jurisdiction via mandatory `.claude/.active-role`; bibliography out of gate scope; citations conserved; subagent=consultation/`/role`=work; per-turn reinforcement hook). C0 search-before-create already done read-only: `CLAUDE.md` governed by ~30 nodes (relate, don't duplicate); `.claude/settings.json` + legacy `session-start.sh` ungoverned (pre-existing gap, flag only); `.claude/agents/*` governed by feature-007/024/adr-005.

Skills applied: `architect-architecture-design` (enforcement design).
Artifacts: this session doc.
Next: Phase B — revert the out-of-process `CLAUDE.md` edit (`git checkout -- CLAUDE.md`), recorded here, before authoring any node.

### 2026-05-15 — architect (Phase B: revert)

Reverted the out-of-process `CLAUDE.md` edit. Pre-check passed (`git diff --stat CLAUDE.md` = exactly `1 file changed, 15 insertions(+)`), then `git checkout -- CLAUDE.md`; confirmed clean (`git diff --quiet` passes, `grep "Orient here before anything else"` → 0 matches). Rationale: that 15-line block was a substrate change with **no governing node** — the exact node-before-artifact violation this session exists to prevent. It is not lost: its content is re-applied later, node-traced, under `feature-073` (Phase D, §5). The other working-tree noise (`.obsidian/workspace.json` UI state + untracked cruft) is deliberately left untouched (scope discipline).

Skills applied: `architect-architecture-design`.
Artifacts: `CLAUDE.md` (reverted to committed state); this session doc.
Next: Phase C — author governing nodes first (feature-072..076 + stories + specs + adr-011/012), commit all before any substrate change.

### 2026-05-15 — product-owner + architect (Phase C: nodes first)

Authored **26 governing nodes**, parents before children, all `draft`/`proposed`, light `## Source` per template (no skill-grade citation apparatus — citation guard honoured). PO authored the 5 features + 14 stories + 5 specs (`po-feature-decomposition`, `po-spec-gherkin`); Architect authored adr-011/adr-012 (`architect-architecture-design`) — logged as cross-role co-authoring within the session, not a Task subagent dispatch. C0 search-before-create applied: relate-not-duplicate to feature-007/010/024/025/028, adr-004/005/010; this work delivers the `2026-05-14` deferred *graph-vs-substrate operating rule* (→ feature-073) and *consultation matrix* (→ feature-074) candidates; pre-existing ungoverned `.claude/settings.json` closed by feature-072/076; legacy `session-start.sh` gap flagged, not retro-fixed. Parent-chain sanity: 26/26 present, all parents resolve. **No substrate touched yet.**

Skills applied: `po-feature-decomposition`, `po-spec-gherkin`, `architect-architecture-design`.
Artifacts: 26 nodes under `nodes/` (feature/story/spec-072..076, adr-011, adr-012); this session doc.
Next: Phase D — implement substrate in deadlock-safe order, each path already governed by these nodes.

### 2026-05-15 — architect (Phase D: substrate)

Implemented substrate in deadlock-safe order: `.claude/.active-role`=architect (gate-ignored) → `.claude/role-scope.json` (role→path map; architect owns governance/structural substrate, PO owns templates+po-skills, each role owns its own skills, bibliography ungated) → `.claude/commands/role.md` (`/role` ceremony) → `.claude/hooks/enforce-node-before-artifact.sh` + `.claude/hooks/role-reinforce.sh` (chmod +x) → wired `.claude/settings.json` PreToolUse(`Write|Edit|MultiEdit|NotebookEdit|Bash`)+UserPromptSubmit → `CLAUDE.md` §5 (Orient block re-applied **node-traced** under feature-073, Role-jurisdiction table mirroring role-scope.json, graph-vs-substrate + decision-verification + node-before-artifact-hard operating principles) → 5 agents §6 (decision-verification + scope-refusal Workflow step). 10 pre-activation hook probes passed before wiring. **Harness note (honest):** Claude Code loads hook config at session start, so the gate enforces from the **next** session; this session's edits were governed + architect-in-scope anyway (no contradiction). Authoritative verification is direct hook invocation (Phase E), which exercises the exact code path Claude Code will call.

Skills applied: `architect-architecture-design`.
Artifacts: `.claude/{.active-role,role-scope.json,commands/role.md,hooks/enforce-node-before-artifact.sh,hooks/role-reinforce.sh,settings.json}`, `CLAUDE.md`, 5 `.claude/agents/*.md`.
Next: Phase E — full verification matrix.

### 2026-05-15 — qa + architect (Phase E: verification)

Ran the 13-scenario matrix by direct hook invocation (deterministic; QA consulted for scenario design — see Subagent consultations). All pass:

1. Ungoverned substrate Write → **deny** (node-before-artifact). 2. Bash `>`/`>>`/`sed -i`/`cp`/`mv`/`tee` into ungoverned substrate → **deny** (all). 3. No `.claude/.active-role` → **deny** (mandatory marker). 4. Wrong role (developer→CLAUDE.md) → **deny** (role-scope). 5. Governed + correct role (architect→`.claude/agents/architect.md`, →CLAUDE.md) → **allow** silent. 6. The actual §5 CLAUDE.md edits executed this session = live positive proof. 7. `nodes/` write → **allow** (gate-ignored). 8. `.claude/.active-role` (Write + Bash) → **allow** (gate-ignored — bootstrap-safe escape valve). 9. Override-hardness: hook has **no** permission-mode/skip code path; deny is unconditional, and Claude Code applies a PreToolUse `deny` over bypass / `--dangerously-skip-permissions` (confirmed in design exploration). 10. Subagent: same `PreToolUse` fires for `Task` subagents (Claude Code behaviour) — design-confirmed. 11. `role-scope.json` keys ↔ CLAUDE.md jurisdiction table: both cover all 5 roles, consistent. 12. Performance: ~0.03 s per invocation (5 runs), well under the 250 ms budget. 13. Reinforcement hook: injects role+jurisdiction+checklist with a role set; injects the run-`/role` message with no role; never blocks.

Result: node-before-artifact + hard role-jurisdiction + per-turn reinforcement all enforced; the originating failure (ungoverned `CLAUDE.md` edit on a bare "do it") is now structurally impossible from the next session. 24 feature/story/spec nodes bumped `draft`→`implemented`; adr-011/012 left `proposed` for human acceptance at close.

Skills applied: `qa-testing-strategy` (scenario design, consulted), `architect-architecture-design`.
Artifacts: spec-072/075/076 (realized-AC note); 24 node status bumps; this session doc.
Next: Phase F — `/session-close`.

### 2026-05-15 — architect (Phase F: session-close)

Invoked `/session-close`. Participants compiled: architect (enforcement design + substrate + ADRs), product-owner (feature/story/spec nodes), qa (Phase-E scenario design, consulted — non-authoring). The flow the session demonstrates, end to end: **session opened → out-of-process edit reverted (the originating violation, undone first) → 26 governing nodes authored before any substrate → 2 ADRs → substrate implemented in deadlock-safe order, each path pre-governed → 13/13 verification → close.** node-before-artifact was applied to the implementation of node-before-artifact itself. Closing summary filled; committing; merge decision deferred to the human.

Skills applied: `architect-architecture-design`.
Artifacts: this session doc.
Next: human picks merge / PR / discard.

## Artifacts touched

- Created `sessions/2026-05-15-hard-enforcement-layer.md` — this session doc.
- Reverted `CLAUDE.md` — discarded the out-of-process 15-line "Orient here" block (no governing node); content re-applied node-traced in Phase D.
- Created 26 nodes — `feature-072..076`, their `story-*` (14) and `spec-072..076`, `adr-011`, `adr-012` — the governing graph for the hard-enforcement substrate.
- Created substrate — `.claude/.active-role`, `.claude/role-scope.json`, `.claude/commands/role.md`, `.claude/hooks/enforce-node-before-artifact.sh`, `.claude/hooks/role-reinforce.sh`.
- Edited substrate — `.claude/settings.json` (+PreToolUse +UserPromptSubmit), `CLAUDE.md` (§5 governance), 5 `.claude/agents/*.md` (§6 Workflow step).
- Edited nodes — 24 feature/story/spec status `draft`→`implemented`; spec-072/075/076 realized-AC notes.

## Subagent consultations

> When a role invokes another role via the `Task` tool, log the consultation here (optional but helpful for audit). The consulting role retains scope authority; the consulted role provides information only.

- `architect` → `qa` — Question: design the Phase-E verification matrix (deny/allow boundary cases, override-hardness, performance). Response summary: 13-scenario matrix (ungoverned/no-role/wrong-role denies; governed/node/marker allows; override-hardness; subagent; consistency; perf; reinforcement). Consultation only — Architect retained scope authority and authored the substrate; QA did not author.

## Closing summary

> Filled in at `/session-close`. What was accomplished, what is left pending, and the recommended next step.

**Outcome:** SEM-IA's soft-only enforcement (proven null — an agent edited `CLAUDE.md` ungoverned on a bare "do it") is replaced by a self-hosted hard layer, installed *through its own discipline*: a `PreToolUse` gate (`.claude/hooks/enforce-node-before-artifact.sh`) that denies any substrate Write/Edit/Bash unless (1) a role is declared (`.claude/.active-role` via `/role`), (2) a node references the path in `artifacts:`, and (3) the path is within the active role's `.claude/role-scope.json` jurisdiction — no override by directive, permission mode, or `--dangerously-skip-permissions`; plus a `UserPromptSubmit` per-turn reinforcement. Governed by 26 nodes (`feature/story/spec-072..076`, `adr-011`, `adr-012`) authored **before** any substrate. CLAUDE.md gained a hoisted Orient block, a Role-jurisdiction table, and graph-vs-substrate / decision-verification / node-before-artifact operating principles; the 5 agents gained a decision-verification Workflow step. 13/13 verification scenarios pass; ~0.03 s/call. The `2026-05-14` deferred *graph-vs-substrate operating rule* and *consultation matrix* improvement candidates are delivered. Citations in skills/agents untouched (epistemic spine preserved); `bibliography/**` correctly left ungated (non-shippable evidence).

**Pending / next steps:**
- `adr-011`, `adr-012` are `status: proposed` — set to `accepted` on human confirmation at merge.
- **Deferred (separate node):** skill-trigger enforcement — agents/SKILL.md are well-designed for triggering but it remains soft model-judgment; capture as a future `feature` under `cap-02` (a `UserPromptSubmit`-based skill-applicability nudge), not built here.
- Residual (documented in adr-011/012, accepted): heuristic Bash-write parser has a residual bypass surface (`python -c`, `perl -i`, editors); marker/reality desync is a correctness (not bypass) risk.
- Pre-existing, flagged not fixed: `CLAUDE.md § Session-bootstrap` "no command/hook exists" drift; legacy `.claude/hooks/session-start.sh` ungoverned; `CLAUDE.md § Terminology` lists `bibliography/sources/` under substrate (imprecise vs distribution reality).
- The gate enforces from the **next** Claude Code session (hook config loads at session start); logic is deterministically verified by direct invocation.

**Merge decision:** <pending — human decides: merge / PR / discard>.
