---
category: session
id: 2026-05-15-graph-reset
date: 2026-05-15
participants: [architect]
related-nodes: []
artifacts: []
---

# Graph reset — one unified artifact-graph; generic slim CLAUDE.md

## Context

281 nodes (1 vision / 3 goals / 13 caps / 77 features / 96 stories / 77 specs / 14 ADRs) + a 341-line doctrine-heavy CLAUDE.md were bloat from self-hosting applying product-decomposition to prose. Converged model: **one rooted artifact graph; one rule (no artifact without a parent node referencing it, every node→vision); doctrine carried by mechanism (gate/hook/agents/skills), not CLAUDE.md prose; CLAUDE.md is the framework's GENERIC project-agnostic contract — no "SEM-IA" self-reference, no Obsidian (an interchangeable personal visual layer, not framework)**. Keep: vision, 3 goals, 37 skills, 5 agents, 3 hooks (incl. the load-bearing role-scope-union gate), role-scope.json, sessions as history. Delete: all story/spec wrappers, cap bloat, obsolete ADRs' doctrine, the 3-layer/mirror/substrate-trichotomy, `_obsidian/templates/`. **Safety: branch-only, history fully preserved, `main` untouched, reversible.** Branched off the current state (keeps the gate code from the portability work; that branch's now-obsolete doctrine is superseded by this rebuild).

**Reversibility anchor:** pre-teardown SHA `1b92365` (281 nodes). `git show 1b92365:nodes/<file>` recovers any old node forever.

## Log

### 2026-05-15 — architect

Opened `session/2026-05-15-graph-reset` off `session/2026-05-15-gate-portability` HEAD (1b92365). `/role architect`. Plan approved (teardown→rebuild to the unified one-rule model; generic slim CLAUDE.md; Obsidian-not-framework; history-preserving). Untracked `.claude/commands/session-log.md` flagged (pre-existing, separate concern, not adopted); untracked `nodes/adr-014` will be absorbed into the single unified-model ADR then removed.

Skills applied: `architect-architecture-design`.
Artifacts: this session doc.
Next: author the ONE unified-model ADR (nodes-first) before any deletion.

### 2026-05-15 — architect (Reset-B: unified ADR)

Authored `adr-015-one-unified-artifact-graph` (nodes-first, before any deletion): one rooted artifact graph + one rule; doctrine in mechanism; **identity framework-first, role-second** ("You are this framework, in the <role> role" — discipline as identity, not memory); generic project-agnostic contract (no "SEM-IA"); Obsidian is an interchangeable personal visual layer (not framework); feature=skill, no story/spec wrappers. Supersedes adr-004/007/012/013; absorbs the uncommitted adr-014 (removed — its substance is in adr-015); keeps adr-001/002/003/009/010/011 in force. `artifacts:` governs CLAUDE.md + the 5 agents + gate + role-scope.json.

Skills applied: `architect-architecture-design`.
Artifacts: `nodes/adr-015-one-unified-artifact-graph.md`; removed uncommitted `nodes/adr-014`; this session doc.
Next: Reset-C — mass prune (delete story/spec, feature=skill, prune caps, supersede ADRs, drop _obsidian/templates, gitignore .obsidian).

### 2026-05-15 — architect (Reset-C: prune + feature=skill)

281 → **68 nodes** (1 vision + 3 goals + 13 caps + 14 ADRs + 37 features). Deleted all 96 `story-*`, 77 `spec-*`, 77 old `feature-*` (recoverable: `git show 1b92365:nodes/<f>`). Created **37 lean skill-features**, one per skill, `parent:`=its role-discipline cap (cap-03..07), `artifacts:`=that `SKILL.md` — no story/spec wrapper (the SKILL.md is the spec, adr-009/015). Superseded adr-004/007/012/013 (`status: superseded`, `superseded-by: adr-015`; kept as history). Removed `_obsidian/templates/` (node structure carried by authoring skills); `.obsidian/` added to `.gitignore` (personal visual layer, not framework). **Plan deviation, stated:** kept all 13 caps + 14 ADRs rather than pruning caps — deleting caps would orphan ADR parents and the real bloat was features/stories/specs; this hits the ~60–70 target safely without risky cap-reparenting (graph-integrity > rigid plan adherence). Integrity verified: exactly 1 rootless (`vision-sem-ia`), 0 orphans, 0 story/spec, feature count == skill count (37). The strategic backbone the human said "no están mal" is untouched.

Skills applied: `architect-architecture-design`, `po-feature-decomposition` (feature=skill mapping).
Artifacts: 37 new `nodes/feature-*`; 4 superseded ADRs; deleted 250 nodes + `_obsidian/templates/`; `.gitignore`; this session doc.
Next: Reset-D — generic slim CLAUDE.md + agent-opener reframe.

### 2026-05-15 — architect (Reset-D: generic slim CLAUDE.md + agent openers)

`CLAUDE.md`: **341 → 57 lines**. Framework-first identity ("**You are this framework.** … You are this before you are any role"), the one rule stated once, generic/project-agnostic (zero "SEM-IA"), zero Obsidian, sections only: graph conventions / how to operate / enforcement-as-pointers / portability / local prefs. Deleted entirely: Orient 3-layer block, `## Roles`+`## Role jurisdiction` table, `## Terminology`, `## The triangle`, `## Operating principles` essay, `## Templates`, `## Repo structure`. The word "substrate" removed; "jurisdiction" remains only as a one-word pointer to `role-scope.json` (not the deleted doctrine table). The 5 `agents/*.md` openers reframed: each opens *"You are this framework, in the **<role>** role… the role is your current scope, not your identity"* (bodies/skills/handoffs untouched). Governed by adr-015 (`artifacts:` lists CLAUDE.md + the 5 agents).

Skills applied: `architect-architecture-design`.
Artifacts: `CLAUDE.md` (rewrite + header-corruption fix), 5 `.claude/agents/*.md` (opener); this session doc.
Next: Reset-E — verify gate (no regression) + graph integrity + reversibility + close.

### 2026-05-15 — architect (Reset-E: verify + close)

Verified by direct hook invocation + scripts: gate no-regression (ungoverned `.claude/skills/architect-zzz/SKILL.md` → deny; CLAUDE.md/agents/gate-hook/nodes governed-by-adr-015 → allow; no-role + wrong-role → deny); graph integrity (68 nodes, exactly 1 rootless `vision-sem-ia`, 0 orphans, 37 features == 37 skills, 0 story/spec); reversibility (`git show 1b92365:nodes/spec-072` returns old content — full 281-node graph recoverable); `main` untouched at `0c8431e`. Fixed a committed CLAUDE.md header corruption (`# CL`→`# CLAUDE.md`, commit `ae284d0`) from the recurring stray gremlin. Closing; merge + adr-015 acceptance deferred to the human.

Skills applied: `architect-architecture-design`.
Artifacts: this session doc.
Next: human picks merge / PR / discard; confirm adr-015.

## Artifacts touched

- Created `sessions/2026-05-15-graph-reset.md` — this session doc.
- Created `nodes/adr-015-one-unified-artifact-graph.md`; removed uncommitted `nodes/adr-014` (absorbed).

## Subagent consultations

- (none yet)

## Closing summary

**Outcome:** Teardown→rebuild to the unified model, done & verified, history intact. **281 → 68 nodes** (1 vision + 3 goals + 13 caps + 14 ADRs + 37 lean skill-features). One rooted artifact graph, one rule, doctrine carried by mechanism. `adr-015` is the single conceptual ADR (supersedes adr-004/007/012/013, absorbs adr-014). `CLAUDE.md` **341 → 57 lines**: framework-first identity ("You are this framework… before you are any role"), generic/project-agnostic (zero "SEM-IA"), zero Obsidian, no doctrine essays. 5 agent openers reframed framework-first. `_obsidian/templates/` removed; `.obsidian/` gitignored (interchangeable personal visual layer, not framework). Verified: gate no-regression (ungoverned deny / governed-by-adr-015 allow / no-role+wrong-role deny / nodes ignored); graph integrity (1 rootless `vision`, 0 orphans, feature==skill==37); old 281-node graph fully recoverable (`git show 1b92365:nodes/…`); `main` untouched at `0c8431e`.

**Pending / next steps:**
- `adr-015` is `status: proposed` — set `accepted` on human confirmation at merge.
- **Environmental issue (flag, important):** a recurring stray corruption hit `CLAUDE.md`'s top lines ~4× this conversation (`/`, `. `, `# CL`); the last one reached commit `8981a5f` (truncated `# CLAUDE.md`→`# CL`) and was fixed in `ae284d0`. Something outside the work is mutating that file between write and commit — worth investigating (editor/plugin/hook on the human side).
- Superseded ADRs (004/007/012/013) kept as history with `superseded-by:`. The portability branch's gate *code* (role-scope union + always-ignore guard) is retained and is what makes the unified model work; that branch's obsolete doctrine is superseded here.
- Branch deletion of prior merged session branches = independent housekeeping.

**Merge decision:** <pending — human decides: merge / PR / discard; confirm adr-015 acceptance>.
