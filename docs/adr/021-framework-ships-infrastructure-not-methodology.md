---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-22
updated: 2026-05-22
maintained_by_role: architect
supersedes:
  - adr-020-skills-reduction-methodology-as-instance
---

# ADR 021 — The framework ships infrastructure, not methodology

## Context & forces

ADR-020 ("Reduce skills · methodology lives in the instance", same-day, earlier in this session) framed the v0.2 reframe as *"move the methodology from `.claude/skills/<role>-<topic>/` into `instance/methodology/<sub-discipline>.md` and reference it from agent.md."* That framing was wrong in two ways the user surfaced immediately:

- **The framework should not ship methodology at all.** Cagan / Jones / Cohn / Patton / Fagan / Humble & Farley / Nygard / ANSI-IEEE are SEM-AI's *current dogfood choice*, not part of what the framework offers to downstream products. A SAFe shop, a Modern-Agile shop, or a custom-methodology shop shouldn't have to first scrape the framework's methodology assumptions out before installing.
- **The methodology layer's natural home is Claude Code's `.claude/skills/` mechanism.** Inventing a parallel `instance/methodology/` folder duplicated what skills already exist for, and put two file trees in tension with each other.

There is a deeper reason: **LLMs already carry the SEM literature in their training.** A PM agent prompted to "draft a vision" applies vision discipline by default — Cagan's principles, GISF's construction, the 2-10 year horizon — because the training data contains these methods. The framework does not need to *teach the LLM* the methodology; it needs to give the LLM the *infrastructure within which to apply whatever methodology fits the work*. Roles, jurisdiction, the substrate, the engine MCP, the interaction model — these are portable across methodologies; the methodology itself rides on the LLM's training (and optionally on project-supplied skills).

## Decision

**The framework ships infrastructure, not methodology.**

What the framework provides:
- 6 role-homologous agents (`.claude/agents/<role>.md`) — role identity, jurisdiction, the 7-step workflow, the interaction-with-other-roles table. **No methodology criteria, no bibliographic citations, no sub-discipline tables.**
- The `framework` skill (`.claude/skills/framework/SKILL.md`) — the contract.
- The engine MCP (`engine/`) — methodology-blind mechanism.
- The engine's config data (`instance/*.yaml`) — node types schema, lifecycle, jurisdiction matrix, validator rules. *Default values are tuned for the SEM-AI dogfood; any project can override.*
- The SessionStart hook + `.mcp.json` registration + GitHub Actions for self-maintenance.

What the framework does **not** provide:
- No `instance/methodology/` directory.
- No `.claude/skills/<role>-<topic>/` skills shipping methodology content.
- No `## Discipline` mega-section in agent.md.
- No `Sub-disciplines you cover` table in agent.md pointing at methodology files.

What downstream projects bring:
- Their own `.claude/skills/<topic>/SKILL.md` if they want a particular methodology surfaced in Claude Code's skill listing. The Skill tool invokes them when the description matches the work.
- Their own values for `instance/*.yaml` if they want different thresholds, sections, or forbidden patterns.
- Or *nothing* — operate from the LLM's training; the agent names the methodology it is applying so the human can accept or substitute.

## Overall structure

Three layers — framework (infrastructure) · methodology (project's choice, optional) · LLM (default methodology source from training).

```
Layer 1 (framework, always present):
  .claude/agents/<role>.md × 6     — methodology-blind role contracts
  .claude/skills/framework/SKILL.md — the contract
  engine/ + instance/*.yaml         — engine + its config data
  hooks + .mcp.json + Actions       — self-maintenance

Layer 2 (project methodology, optional):
  .claude/skills/<topic>/SKILL.md   — project's chosen methodology, in
                                       Claude Code's native mechanism

Layer 3 (LLM training, always available):
  Cagan, Jones, Cohn, Patton, Fagan, Humble & Farley, Nygard,
  ANSI-IEEE 1471, IFPUG, COSMIC, ISBSG, SAFe, Modern Agile, OKRs, OWASP,
  NIST, STRIDE, … — the agent names what it's applying
```

## Data structure

agent.md retains the 5-section structure (Identity / Jurisdiction / How you work / Interaction / Gotchas) but every sub-section is methodology-blind. The "How you work" workflow includes step 3 explicitly: *"Pick the methodology you'll apply — from a project skill if one matches, otherwise from training. State it out loud (e.g., 'I'll apply SMART for this goal' / 'I'll size this with light function-points')."*

## Interfaces to the outside world

Agents read `.claude/agents/<role>.md` at session start. They use the Skill tool's listing to discover project skills. They use `mcp__sem_ai_engine__*` for substrate writes. The methodology layer is invisible to the engine — the agent decides which methodology to apply and audits its own work against the methodology's criteria.

## Decomposition into functional components

Three independent layers (framework / project methodology / LLM training) compose without coupling. The framework does not import project skills; project skills do not import framework agent.md content; the LLM training does not depend on either.

## Linkage / information transmission

The agent reads project skills *on demand* via the Skill tool — not preloaded — so context economy is preserved. Project skills are discoverable via the skill listing but not consuming context until invoked.

## Performance attributes

Context per session start: 6 agent.md files × ~70 lines + `framework` skill ~120 lines + project map from SessionStart hook + any project skills the agent invokes during the work. Compared to v0.1's preloaded 41 skills × ~250 lines, the context footprint drops ~7× without losing methodology access (training carries it, skills carry it on demand).

## Security attributes

Dispatched to Security Officer.

- Removing the `.claude/skills/security-officer-*` skills does **not** weaken the Security Officer role: the LLM's training carries Jones BP #38, ISO 17799, OWASP, STRIDE, NIST SP 800-x, MITRE ATT&CK, capability-based security, the Principle of Least Authority, etc. The Security Officer agent.md retains its identity, jurisdiction, and the section-contribution + release-stop authority, methodology-blind.
- A project that wants a specific security methodology enforced (e.g., HIPAA-specific, PCI-DSS-specific, automotive ASIL-D-specific) ships its own `.claude/skills/<security-topic>/SKILL.md` — Claude Code's mechanism, surfaced via the Skill listing, invoked on demand.

## Style: chosen + rejected

- **Chosen**: framework = infrastructure only; methodology = LLM training + optional project skills.
- **Rejected** (ADR-020's position): methodology absorbed into agent.md ## Discipline + duplicated in `instance/methodology/<sub-discipline>.md`. Conflated framework with this project's dogfood; locked downstream products into our bibliography; duplicated what `.claude/skills/` already exists for.
- **Rejected**: ship methodology in the framework but let the user override per-file. Trains the framework's authors into thinking *they* own the methodology choice; gradient toward methodology lock-in.
- **Rejected**: minimal agent.md with no role-discipline language at all (just "use your training"). Loses the *role's* identity-as-discipline contract — the "you are primary in your dimension; release-stop authority; symmetric primacy" framing is framework-level role contract, not methodology.

## Consequences

- `instance/methodology/` deleted entirely (the 5 files created earlier this session: README, fp-sizing, fagan-inspections, pm-discipline, architect-discipline).
- `.claude/skills/<role>-<topic>/` × 41 (the cherry-picked methodology skills) deleted from `main`. Preserved on `archive/v0.1-sqlite-experiment` as historical reference.
- 6 agent.md rewritten as truly framework-blind: 73 + 68 + 71 + 73 + 70 + 78 = **433 lines total** (was 1 046 after the previous absorption attempt, 70 × 6 = 420 in v0.1 with skills preloaded).
- `framework/SKILL.md` rewritten to reflect v0.2 substrate + the engine MCP + the new role table (no methodology references).
- README.md and CLAUDE.md updated to remove `instance/methodology/` references and to surface the three-layer model.
- ADR-020 superseded by this ADR. Its title and framing ("methodology lives in the instance") was incorrect — the methodology lives in the LLM's training and optionally in project skills, not in the framework.

## Design inspection

The negative verification test from TESTING.md (PM attempts to create a `measurement` → engine hard-rejects via jurisdiction) is unchanged and still passes. The mechanical enforcement is in the engine + jurisdiction matrix, not in agent.md text — so stripping methodology from agent.md does not weaken enforcement. The pytest suite (28 tests) is unchanged and stays green.
