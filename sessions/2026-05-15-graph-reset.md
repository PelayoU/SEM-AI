---
category: session
id: 2026-05-15-graph-reset
date: 2026-05-15
participants: [architect, product-manager]
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

### 2026-05-15 — architect (Reset-F: artifact/node ontology + `nodes/`→`graph/`)

Human flagged that CLAUDE.md conflated *node* and *artifact* and that "the project lives in nodes/" misleads. Fixed: CLAUDE.md now states the ontology plainly — **everything created is an artifact; a *node* is the structured kind (template, lives in `graph/`, carries `parent:`/`artifacts:`) and is what *governs* the rest; a capability/goal/vision is a level of thinking whose written form is a node artifact**; rule restated ("if it's itself a node → `graph/`; else a node in `graph/` lists it in `artifacts:` first"). Folder **renamed `nodes/` → `graph/`** (`git mv`, 68 files, history preserved — the folder *is* the graph, its files are node-artifacts). Patched the gate hook (`always_ignore` `graph/*`, the node grep, deny text), `role-scope.json` + `role-scope.example.json` `_comment`, and adr-015 (body + a Clarification block). Verified: `graph/` write → allow (no deadlock); ungoverned → deny; governed (CLAUDE.md/hook via adr-015, architect) → allow; rootless=1, orphan=0, 68 nodes, 37 features; `git show 1b92365:nodes/…` still recovers the pre-rename history; adr-015 confirmed valid UTF-8 (no corruption). `.claude/commands/session-log.md` (only non-mechanism file mentioning `nodes/`) left untouched — pre-existing untracked cruft, flagged not adopted.

Skills applied: `architect-architecture-design`.
Artifacts: `git mv nodes→graph` (68); `CLAUDE.md`, `.claude/hooks/enforce-node-before-artifact.sh`, `.claude/role-scope.json`, `.claude/role-scope.example.json`, `graph/adr-015-*`; this session doc.
Next: human picks merge / PR / discard; confirm adr-015.

### 2026-05-15 — architect (Reset-G: role-decision table in CLAUDE.md)

Human asked that CLAUDE.md state what each role decides so a role can self-recognise straying into another's scope (a PO cannot avoid Architect territory if it cannot see what the Architect owns). **Derived, not invented:** read all 5 `.claude/agents/*.md`; each table row = that agent's *"custodian of…"* identity line (Owns) + the direction of its own "Interaction with other roles" hand-offs (what it *supplies to* another = not its call). Added a compact 5-row `What each role decides` block to CLAUDE.md's `## Working as roles` section. Security/Designer excluded (Tier-3, not built — their agent.md rows point at non-existent roles). Governed by adr-015 (CLAUDE.md ∈ its `artifacts:`); no new doctrine — a faithful cross-role surface of agent files adr-015 already governs, so node-before-artifact holds without amending the ADR. The separate piece (multi-role review at `/session-close` over the diff) is a *genuinely new* decision and is NOT done here — it will need its own decision in adr-015 (still `proposed`, amendable) before `/session-close` is rewritten.

Skills applied: `architect-architecture-design`.
Artifacts: `CLAUDE.md` (added role-decision table); this session doc.
Next: (a) author the `/session-close` multi-role-review decision into adr-015 + rewrite `/session-close`; (b) reshape each agent.md "Interaction with other roles" table into trigger + consult-vs-handoff form; human picks merge / PR / discard; confirm adr-015.

### 2026-05-15 — architect (Reset-H: session-close multi-role review; how-to-operate clarifications)

Node-first: amended `adr-015` (still `proposed`) — added decision 6 (session close runs an advisory multi-role review; command not hook, because the review is agentic and a shell hook cannot read a diff / dispatch roles / write findings; consultation only per ADR-005; never blocks) + a Neutral consequence + added `[[.claude/commands/session-close.md]]` to its `artifacts:` so the command rewrite is governed. Then: `CLAUDE.md` `## How to operate` — two clarifications (one session may pass through several roles, the human does the switch on the same branch, never silently do another role's work; log continuously to the session doc as you go, not reconstructed at close) — clarifications of already-governed content, no further ADR change. Then rewrote `.claude/commands/session-close.md`: generic (dropped all "SEM-IA" per adr-015 decision 3), inserted step 3 = compute `git diff main...HEAD`, dispatch the relevant built roles as `Task` subagents (review-only, ADR-005), findings → new `## Session review (multi-role)` section; and made the branch-decision step strictly neutral — **no default, no recommendation, wait for explicit human choice** (was: "default to merge for solo workflows"; corrected to honour the standing constraint).

Skills applied: `architect-architecture-design`.
Artifacts: `graph/adr-015-one-unified-artifact-graph.md` (decision 6 + artifacts: + consequence), `CLAUDE.md` (how-to-operate), `.claude/commands/session-close.md` (rewrite); this session doc.
Next: reshape each agent.md "Interaction with other roles" table into trigger + consult-vs-handoff form (drop Security/Designer — Tier-3, not built); human picks merge / PR / discard; confirm adr-015.

### 2026-05-15 — architect (Reset-I: agent.md step-6 rewrite — rot fix + exit-trigger)

Rewrote step 6 of `## Workflow` in all 5 `agent.md` (identical paragraph, verbatim across files; each file's distinct closing line preserved). Removed teardown rot: dead `/role <name>`, dead `.claude/hooks/enforce-node-before-artifact.sh` + "cannot be overridden" (contradicted adr-015's unenforced-discipline decision), dead cross-ref "§ Role jurisdiction" → "§ Working as roles". Preserved the load-bearing thesis intact (scope check; out-of-scope refused even on explicit "do it", Jones Ch 5 p.282; subagent = consultation-only never authoring, ADR-005; "a bare 'do it' is verified, not blindly executed"). Added **(c)**: role-local exit-trigger recognition — when completed work satisfies a hand-off in this role's own `## Interaction with other roles` table, name it and surface to the human (the missing relay; local/pairwise → respects the contamination invariant). Governed by adr-015 (`artifacts:` lists all 5 agents) — node-before-artifact satisfied.

**Provenance caveat (flagged for the multi-role review, honest record):** authored by a contaminated, role-less instance after the human, with full knowledge of the contamination/recursion objection (which the human originated), explicitly and repeatedly directed it under the existing governing node. Verification was performed exhaustively and surfaced before acting (not blindly executed); the human made the scope determination (human-directed model, adr-010 lineage). This is exactly the kind of provenance a fresh-role `/session-close` review should re-examine — recorded here deliberately so it can.

Skills applied: `architect-architecture-design`.
Artifacts: `.claude/agents/{product-owner,architect,qa,developer,devops}.md` (step-6 rewrite ×5); this session doc.
Next: reshape each agent.md "Interaction with other roles" table into trigger + consult-vs-handoff form (drop Security/Designer — Tier-3, not built); the wrapper rot still pending (`/session-open` dead template path, "SEM-IA" strings, no adoption doc); human picks merge / PR / discard; confirm adr-015.

### 2026-05-17 — product-manager (close)

Human entered as Product Manager, then asked to "close the branch — shouldn't have been opened" and exit. Clarified that `session/2026-05-15-graph-reset` is pre-existing **Architect** work (opened 2026-05-15, not this session, not by Product Manager) carrying the completed graph reset + `adr-015` + `CLAUDE.md` rewrite — discarding would abandon all of it. Surfaced the choice neutrally with the irreversibility of discard stated; human chose **leave the branch intact and exit**. No Product Manager work performed; no nodes/artifacts touched. Multi-role diff review intentionally skipped — no new work this session and the branch is preserved untouched (neither merged nor discarded), so an advisory review has no object.

Skills applied: (none — close only).
Artifacts: this session doc.
Next: Architect's pending items stand unchanged (accept `adr-015`; agent.md table reshape; wrapper rot; merge / PR / discard). Human decides.

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

**Merge decision:** pending — human decides. Session closed by Product Manager 2026-05-17 on the human's instruction to leave the branch intact and exit; **branch preserved untouched, nothing merged or discarded**. The Architect's merge / PR / discard choice and `adr-015` acceptance remain open and deferred to the human in a future session.
