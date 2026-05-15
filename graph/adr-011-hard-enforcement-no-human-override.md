---
category: adr
id: adr-011-hard-enforcement-no-human-override
parent: "[[cap-01-vision-to-code-audit]]"
artifacts:
  - "[[CLAUDE.md]]"
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[.claude/settings.json]]"
status: superseded
created: 2026-05-15
updated: 2026-05-15
supersedes:
superseded-by: "[[adr-015-one-unified-artifact-graph]]"
---

# ADR 011 — Node-before-artifact is hard-enforced with no human override

> One decision = one ADR. The ADR format (Context / Decision / Consequences) is Michael Nygard convention — **not in audited `bibliography/sources/`**, cited as convention. Architect-scope audit grid: Jones Ch 7 § Software Architecture (seven fundamental topics).

## Status

accepted (human-confirmed at session close 2026-05-15).

## Context

SEM-IA's enforcement was soft context only. Empirically demonstrated null: an agent with the entire contract + 37 skills + bootstrap session loaded, having just articulated the node-before-artifact rule, still edited `CLAUDE.md` with no governing node on a single "do it". The failed escape was exactly *"the human told me to"*. **Relates to / operationalises** [[adr-004-substrate-content-separation]] (this enforces the substrate/content split), and extends [[adr-005-subagent-dispatch-not-authority-transfer]] and [[adr-010-human-directed-ai-maintained]] (human still directs — by authoring/approving the governing node, not by ordering an ungoverned write). Conceptual lineage: configuration-control / locked-master discipline (Capers Jones BP #33 practice 2; SQA non-coercion, Jones Ch 5 p. 282) — named here once, not turned into a per-node citation apparatus.

## Decision

The node-before-artifact invariant is enforced at the Claude Code `PreToolUse` tool boundary by `.claude/hooks/enforce-node-before-artifact.sh`. There is **no per-prompt human override, no permission-mode bypass, and no `--dangerously-skip-permissions` escape**. The only legitimate way to change substrate is to first author (or extend) a management node whose `artifacts:` lists the path. "Human directs" is preserved as *authoring/approving the governing node*, never as ordering an ungoverned write.

## Consequences

**Positive:** rigor becomes a structural effect of the system, not a virtue the agent may forget; the demonstrated failure is made physically impossible; audit becomes validation, not discovery.

**Negative:** every substrate change requires a node first (friction by design); a residual Bash-write bypass surface exists (`python -c`, `perl -i`, editors) — heuristic verb parsing cannot be complete; defended in depth by the soft CLAUDE.md/agent layer and accepted, not papered over.

**Neutral:** `nodes/`, `sessions/`, `bibliography/`, `/tmp`, `.git`, `.obsidian/` are out of scope by design; `.claude/.active-role` is gate-ignored runtime state.

## Alternatives considered

- **Soft prompt-only enforcement** — rejected: empirically null (the originating failure).
- **Human break-glass flag** (env var / permission bypass) — rejected: reintroduces the exact failed coercion path; Jones BP #33 practice 2 forbids side-channel edits, Ch 5 p. 282 requires the rule be non-coercible.
- **Deny-by-default with no governance path** — rejected: would block all legitimate work, contradicting [[adr-010-human-directed-ai-maintained]].

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **3. Interfaces to outside world:** the hook is the gate on the tool→filesystem interface.
- **5. Linkage / information transmission:** node `artifacts:` ↔ substrate path is the enforced link.
- **7. Security attributes:** non-bypassable by permission mode; fail-safe-closed.
- Others: not materially affected.

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics audit grid.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* — convention, not in audited `bibliography/sources/`.
