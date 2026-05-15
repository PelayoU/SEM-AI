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

## Artifacts touched

- Created `sessions/2026-05-15-graph-reset.md` — this session doc.
- Created `nodes/adr-015-one-unified-artifact-graph.md`; removed uncommitted `nodes/adr-014` (absorbed).

## Subagent consultations

- (none yet)

## Closing summary

**Outcome:** <pending>.

**Pending / next steps:** <pending>.

**Merge decision:** <pending>.
