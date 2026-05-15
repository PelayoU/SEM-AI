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

## Artifacts touched

- Created `sessions/2026-05-15-graph-reset.md` — this session doc.
- Created `nodes/adr-015-one-unified-artifact-graph.md`; removed uncommitted `nodes/adr-014` (absorbed).

## Subagent consultations

- (none yet)

## Closing summary

**Outcome:** <pending>.

**Pending / next steps:** <pending>.

**Merge decision:** <pending>.
