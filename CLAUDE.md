# SEM-IA

A framework for software engineering management at scale — vision through code, fully traceable. The human assumes a role (Product Owner, Architect, QA, Developer, DevOps); each role is an AI agent grounded in audited bibliography and a curated catalog of skills. The project lives as a navigable graph of markdown nodes in `nodes/`, browsable as an Obsidian vault rooted at the repo.

**This file is the project's universal contract.** It is loaded into every Claude session in this repo, including `claude --agent <role>` invocations. Role-specific identity lives in `.claude/agents/<role>.md`. Skill criteria live in `.claude/skills/<role>-<skill>/SKILL.md`.

The framework has two layers:

- **Layer A — the framework** (*what* and *why*): roles, skills, bibliography, the graph, templates. Universal, audited, citation-anchored.
- **Layer B — operating the framework** (*how* and *when*): sessions as git branches, the session bootstrap, slash commands, subagent dispatch.

Both layers are documented below. Layer A first, Layer B second.

---

## Roles

5 core roles. Tier-3 specialised roles (Security, Designer) are planned but not yet built. Tier-4 emergence cases (separate BA / PM) are documented in `.claude/sem-role-catalog.md`.

| Role          | Custody                                                                                    | Skills | Agent file                          | Tier |
| ------------- | ------------------------------------------------------------------------------------------ | ------ | ----------------------------------- | ---- |
| Product Owner | Product + business analysis + project management (super-PO fusing PM/PL/BA/PM-project)     | 15     | `.claude/agents/product-owner.md`   | 1    |
| Developer     | Production code + reuse application + static analysis + unit testing + maintenance         |  5     | `.claude/agents/developer.md`       | 1    |
| Architect     | Architectural decisions + methodology selection + reusability strategy + performance       |  5     | `.claude/agents/architect.md`       | 2    |
| QA            | Quality program (SQA independence) + measurements + inspections + testing + DRE            |  5     | `.claude/agents/qa.md`              | 2    |
| DevOps        | Configuration control + deployment pipeline + releases + customer support + maintenance ops + legacy retirement |  7     | `.claude/agents/devops.md`          | 2    |

**Default entry: Product Owner.** For new product work, `claude --agent product-owner` is the natural starting point — PO is the integrator and routes to specialists when needed. Direct entry with another role is appropriate for work that does not need product framing (refactor, incident response, infrastructure ADR).

**Invocation modes:**

- **Role-as-agent (human)** — `claude --agent <role>` starts a session where Claude assumes that role for the duration.
- **Subagent dispatch (Claude)** — from another role, use the `Task` tool with `subagent_type: <role>`. The response is consultation, not authority transfer (see Layer B § *Subagent dispatch*).

Both modes load this `CLAUDE.md` + the role's `agent.md`. The agent.md `description` field triggers correct dispatch.

---

## Repo structure

```
SEM-AI/
├── .claude/
│   ├── agents/<role>.md                Role identity + skill catalog.
│   ├── skills/<role>-<skill>/SKILL.md  Skill = canonical method for one operation, anchored verbatim in primary sources.
│   ├── commands/<name>.md              Slash commands (Layer B ceremony moments).
│   ├── templates/
│   │   ├── agent.md.template           Pattern for new role files.
│   │   └── SKILL.md.template           Pattern for new skill files.
│   ├── sem-role-catalog.md             Design doc: roles, tiering, BP↔skill mapping.
│   └── settings.json                   Claude Code config (project-level).
├── _obsidian/
│   ├── bases/                          (Future) Filtered views as `.base` queries.
│   └── templates/                      Authoritative node-structure templates.
├── nodes/                              The project graph. Each `<type>-<id>-<slug>.md` is one artifact.
├── sessions/                           Session documents (`YYYY-MM-DD-<topic>.md`).
├── bibliography/
│   ├── sources/                        Audited PDFs. Skills cite these.
│   ├── INDEX.md                        Navigable bibliographic index.
│   └── skill-references.md             Per-skill traceability for academic audit.
├── CLAUDE.md                           This file.
└── LICENSE
```

**Obsidian vault = repo root.** Opening Obsidian on this directory makes the graph, backlinks, and (future) bases views available.

---

# Layer A — the framework

## The graph

Backbone hierarchy (GISF UC3M `gisf-life-cycle.pdf` slide 53):

```
vision → goals → capabilities → features → stories → specs
                                                  ↘ adrs (architectural decisions can hang off anywhere)
```

**Node naming.** `nodes/<type>-<id>-<slug>.md` where `<type>` ∈ `{vision, goal, cap, feature, story, spec, adr}`. Stories include a letter suffix to trace acceptance criteria in the sibling spec: `story-007-A-password-step.md` → spec `Scenario` labelled `AC-A1`, `AC-A2`, …

**Session naming.** `sessions/<YYYY-MM-DD>-<topic-slug>.md` — distilled record of a meaningful conversation between the human and one or more roles.

## Wikilinks `[[id]]`

For narrative cross-references inside a node body, use Obsidian wikilinks:

```markdown
This feature derives from [[cap-03-multirole-agents]] and produces the spec [[spec-007-login-multifactor]].
```

Wikilinks activate Obsidian's backlinks pane and graph view. They are **narrative references**, not the formal hierarchical edge — `parent:` in frontmatter is the formal edge. Use the two consistently.

## Frontmatter

**Minimal required fields** for every node:

| Field      | Meaning                                                       | Required for                |
| ---------- | ------------------------------------------------------------- | --------------------------- |
| `category` | Node type (`vision`, `goal`, `capability`, `feature`, `story`, `spec`, `adr`, `session`). Drives `.base` filters and tooling. | Every node                  |
| `id`       | Stable unique identifier matching the filename                | Every node                  |
| `parent`   | Wikilink to the parent node in the backbone hierarchy         | Every node except `vision`  |
| `status`   | One of the canonical values below                             | Every node except `session` |
| `created`  | `YYYY-MM-DD`                                                  | Every node                  |
| `updated`  | `YYYY-MM-DD`                                                  | Every node                  |

**Type-specific optional fields** appear in the relevant templates: `horizon:` (goal), `mvp:` (capability), `artifacts:` (feature / story / spec / adr — when wrapping a concrete substrate artefact, see § Substrate traceability below), `supersedes` / `superseded-by` (adr), `date` / `participants` / `related-nodes` (session).

**Not used in this project** (eliminated by design): `also-relates-to`, `depends-on`, `dimensions-affected`. Horizontal cross-references live as wikilinks in node bodies, not as frontmatter fields.

**Substrate traceability** (operationalises Capers Jones BP #11 practice 7 via the management-graph format). Management nodes that wrap a concrete substrate artefact — a feature describing a specific skill or agent or template; a story or spec verifying a specific artefact's behaviour; an ADR affecting specific code — carry an explicit `artifacts:` field in frontmatter:

```yaml
artifacts:
  - .claude/skills/po-vision/SKILL.md
  - .claude/agents/product-owner.md
```

Paths are relative to repo root and point at items in this repository (`.claude/...`, `_obsidian/...`, `bibliography/sources/...`, `CLAUDE.md`, `LICENSE`). External / conventional references (Cagan books, Nygard ADRs, etc.) stay in `## Source`, not in `artifacts:`. The field is **optional** — a feature describing an abstract property without a single artefact owner (e.g., *"parent-pointer convention"*, *"backbone hierarchy"*) may omit it — but **strongly preferred** when a concrete substrate path exists, because it makes the management↔substrate link **machine-queryable**, not just narrative-mention in `## Source`.

## Canonical status values

| Status                     | Meaning                                              | Applies to                     |
| -------------------------- | ---------------------------------------------------- | ------------------------------ |
| `draft`                    | Under construction in a session                      | All nodes                      |
| `active`                   | Completed and in force                               | `vision`, `goal`, `capability` |
| `ready-for-implementation` | Backlog-ready for a Developer to pick up             | `feature`                      |
| `in-implementation`        | Developer / team working on it                       | `feature`, `story`             |
| `implemented`              | All stories done, spec satisfied, tests pass         | `feature`, `story`             |
| `deprecated`               | Consciously retired (no longer applies)              | All nodes                      |
| `superseded`               | Replaced by a later artifact (keep `superseded-by:`) | `adr`                          |

## Templates

The eight node templates in `_obsidian/templates/` are the canonical structure for each node category in the management graph, derived from the corresponding Layer-A skill where applicable (`session.md` is an operational convention, not skill-anchored):

| Template                            | Anchored in skill               | Primary sources                                                                  |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------- |
| `_obsidian/templates/vision.md`     | `po-vision`                     | Cagan 10 principles via GISF `gisf-discovery.pdf` slides 82, 84, 86, 89          |
| `_obsidian/templates/goal.md`       | `po-goals`                      | SMART (GISF slide 95), multilevel horizons (GISF slide 150), why-stack (slide 96)|
| `_obsidian/templates/capability.md` | `po-capabilities`               | GISF `gisf-life-cycle.pdf` slides 54, 64, 69; `gisf-discovery.pdf` slides 97–99  |
| `_obsidian/templates/feature.md`    | `po-feature-decomposition`      | Cohn slide 124, INVEST slide 128, 5 Cs slide 56, Story Map slide 132             |
| `_obsidian/templates/story.md`      | `po-feature-decomposition`      | Cohn slide 124, INVEST slide 128, 5 Cs (`agile-story-essentials.pdf`)            |
| `_obsidian/templates/spec.md`       | `po-spec-gherkin`               | Cucumber `gherkin-reference.pdf` pp. 1–9, GISF slides 54, 126                    |
| `_obsidian/templates/adr.md`        | `architect-architecture-design` | Jones Ch 7 § Software Architecture pp. 470–475 (Nygard ADR format as convention) |
| `_obsidian/templates/session.md`    | (used by every role)            | (operational convention; no single bibliographic anchor)                         |

**Application.** Templates are instantiated either by a human (via Templater plugin in Obsidian) or by an agent (via `Read` + `Write` tools), copying the template's structure into a new file under `nodes/<...>.md` and filling the placeholders. Both paths produce structurally conformant nodes; the choice is operational, not architectural.

**To create a new role or skill,** use the meta-templates at `.claude/templates/agent.md.template` and `.claude/templates/SKILL.md.template`.

## Skills convention

Each skill lives at `.claude/skills/<role>-<name>/SKILL.md` with frontmatter (`name`, pushy `description`) and a body of ≤ ~500 lines (Anthropic skill-creator). Body sections are fixed:

`## Purpose` · `## When this skill applies` · `## Formal criteria` · `## How you proceed` · `## Pitfalls to avoid` · `## Source`

**Citation mandate.** Every authoritative claim in a skill (criteria, thresholds, anti-patterns) cites a primary source: Jones BP # / page; GISF PDF slide #; Cucumber reference page. No criterion is stated without a citation. **Read-before-write:** the constructor reads the source firsthand (or a `pdftotext` extract) before writing the skill.

**Out-of-bibliography handling.** Practitioner frameworks not in `bibliography/sources/` (Cagan, Sinek, Doerr, Adzic, Patton, Cohn, Nygard ADRs, ITIL, CMMI, ISO/IEEE standards, SOLID, Clean Code, DORA, etc.) may be referenced as convention but are flagged with a disclaimer in the skill's `## Source` section — never cited as anchored authority.

## Bibliography

`bibliography/sources/` holds the audited primary sources skills cite:

- `se-best-practices.pdf` — Capers Jones (McGraw-Hill 2010). 28 of 50 Best Practices currently used + Ch 1 § Critical Topics + Ch 5 § SQA Organizations + Table 5-1 + Table 5-2 + Ch 7 § Software Architecture + Ch 8 § Forms of Defect Prevention + Ch 9 Tables 9-22 and 9-23.
- 8 GISF UC3M PDFs: `gisf-discovery.pdf`, `gisf-life-cycle.pdf`, `gisf-agile-teams-and-roles.pdf`, `gisf-delivery-planning.pdf`, `gisf-delivery-backlog-management.pdf`, `gisf-delivery-control-and-monitoring.pdf`, `gisf-delivery-review-and-retrospectives.pdf`, `gisf-pipeline-devops.pdf`.
- `gherkin-reference.pdf` — Cucumber official Gherkin syntax.
- `user-story-mapping.pdf` — Patton story-map concepts (Comakers 2013 handout).
- `agile-story-essentials.pdf` — Comakers / Patton 2013 (Kent Beck origin attribution).

`bibliography/INDEX.md` is the navigable map. `bibliography/skill-references.md` is the per-skill traceability record for academic audit (TFM defence, etc.).

**Citation pattern.** Skills cite sources inline: `(Jones BP #14, p. 76)` · `(GISF gisf-discovery.pdf slide 89)` · `(Cucumber gherkin-reference.pdf p. 1)`. A statement without such a citation is not a statement from this framework.

---

# Layer B — operating the framework

## The triangle

Three pillars hold the operating model together. Each leg removes a class of friction that traditional Working Agreements try (and usually fail) to handle:

1. **Traceability** — every artifact in `nodes/` has an explicit `parent:` chain and `[[wikilinks]]`. The graph itself answers *"what exists and how does it relate?"*. Replaces *"where is X documented?"* friction.
2. **Scope discipline** — each role operates only the skills listed in its `## Skills` section. Work falling outside the role's scope is escalated via subagent consultation or session handoff. Scope violations are visible at audit time via the session doc's `participants` field. Replaces *"whose job is this?"* friction.
3. **Sessions as shared context** — a thread of work lives as a git branch + a session document in `sessions/`. Multiple roles may participate; anyone entering the session inherits full context. Replaces *"let me catch you up"* friction.

The triangle replaces a Working Agreement. There are no team rules to memorise — the infrastructure makes the right path the natural path.

## Sessions = git branch

A **session** is a thread of work materialized as two coupled artifacts:

1. A **git branch** named `session/<YYYY-MM-DD>-<topic-slug>`.
2. A **session document** at `sessions/<YYYY-MM-DD>-<topic-slug>.md` — narrative log of what happened, who contributed, what nodes were touched.

**Branch state is session state.** No `status:` field on the session doc. A session is open as long as its branch exists; it closes when the branch is merged or deleted. The currently checked-out branch is the session you are inside (or `main` if you are between sessions). To list open sessions: `git branch --list 'session/*'`.

A session is **agnostic of role**. Multiple roles may participate in the same session — by subagent consultation or by sequential role invocation in the same branch. The session document records who contributed when.

## Session bootstrap

**Before any work in a new conversation, the active role runs this bootstrap.** It is the single canonical entry point — there is no `/session-open` command, no startup hook, no other mechanism.

1. **Detect current branch** — run `git branch --show-current`.

2. **If on a `session/*` branch** — read `sessions/<id>.md` with the `Read` tool, acknowledge briefly (*"Resuming session `<id>`."*), proceed with the human's request. If the doc does not exist (orphan branch), say so and offer to either re-create it from `_obsidian/templates/session.md` or `git checkout main`.

3. **If on `main`** — list open sessions with `git branch --list 'session/*'`. Then:
   - **No open sessions** — ask: *"There are no open sessions. Do you want to open one for this work, or work directly on `main`?"*
   - **One or more open sessions** — list them and ask: *"You have these open sessions: `<list>`. Resume one, open a new one, or work on `main`?"*

4. **Act on the answer:**
   - **Resume existing** — `git checkout session/<id>`, then read `sessions/<id>.md`.
   - **Open new** — ask for a topic slug (kebab-case). Compute `id = <today>-<slug>`. Then `git checkout -b session/<id>`, create `sessions/<id>.md` from `_obsidian/templates/session.md` (fill `id`, `date`; leave `participants: []` and `related-nodes: []`), commit with message `open session: <id>`.
   - **Work on main** — proceed without opening a session. Appropriate for trivial fixes, exploration, or work outside the product model.

The role drives this conversationally. The triangle's "sessions as shared context" pillar is enforced by the role asking, not by syntax.

## Writing to the session doc

The session doc is the shared context for every role that touches the session. Each role appends to it as work progresses, so the next contributor (same role later, or a different role) inherits a complete record. This is the mechanism that makes role handoffs possible without ceremony.

**Sections and who writes them:**

| Section                    | When                                                                       | Who              |
| -------------------------- | -------------------------------------------------------------------------- | ---------------- |
| `## Context`               | Once, right after the session is opened.                                   | Opening role     |
| `## Log`                   | Append a new entry at every significant moment (see triggers below).       | Active role      |
| `## Artifacts touched`     | Kept in sync as nodes are created or modified.                             | Active role      |
| `## Subagent consultations`| Append after every `Task` tool dispatch to another role.                   | Consulting role  |
| `## Closing summary`       | Filled by `/session-close` only.                                           | Closing role     |

**Log entry triggers** — append to `## Log` when any of the following happens:

1. A significant decision is made (architecture choice, scope cut, framework selection).
2. An artifact is created or modified in `nodes/`.
3. A subagent consultation yields a non-trivial outcome.
4. **Before stepping away** — end of conversation, role switch, branch checkout, or invoking `/session-close`. This is the most important trigger: it is how the next contributor inherits state.

**Log entry format:**

```
### YYYY-MM-DD HH:MM — <role>

<1–2 paragraph narrative of what was done.>
Skills applied: `<role>-<skill>`, `<role>-<skill>`.
Artifacts: [[node-id]], [[node-id-2]].
Next: <what the next contributor should pick up, or "—">.
```

**Role tag.** The role tag is the role active in the conversation that produced the entry. When subagents are dispatched via `Task`, the consulting role authors the Log entry (the subagent's response is summarised in `## Subagent consultations`, not in `## Log`).

**Handoff discipline.** Before the human closes a conversation with one role to open another with a different role on the same branch (cross-conversation handoff), the outgoing role appends a final Log entry stating (a) the current state of the work, (b) what the next role should pick up, (c) any open questions. The incoming role runs the bootstrap, reads the doc, sees this entry, and is oriented.

The convenience command `/session-log` collapses this into one invocation (see below).

## Slash commands

Slash commands cover only the explicit ceremony moments. Opening and resuming are conversational (bootstrap above).

- `/session-log [optional note]` — appends a Log entry to the current session doc, datestamped and role-tagged. Use at every Log entry trigger; especially before stepping away or handing off to another role.
- `/session-context` — re-reads the current session doc into context. Useful in long sessions when context has drifted.
- `/session-close` — appends a final summary to the session doc; the human decides merge to `main` / open PR / discard.

No other commands exist.

## Subagent dispatch ≠ authority transfer

When a role invokes another role via the `Task` tool, the response is **information**, not authority. PO consulting Architect about feasibility does *not* mean Architect now owns the feature — PO retains scope authority and uses Architect's input as data. This keeps roles from quietly bleeding into each other's scopes; it is the operational form of pillar 2 of the triangle.

If full ownership transfer is what's needed (rare), the human closes the conversation with the first role and opens a new one with the second, in the same session / same branch.

## Direct work on `main`

Working directly on `main` is permitted but discouraged for product-driven work. Appropriate for trivial fixes, exploration, or work explicitly outside the session model (typo fixes, repo hygiene). The framework does not enforce a no-direct-commits-to-main rule by default.

---

## Operating principles

- **Human directs; AI maintains.** A role proposes; the human confirms before anything is written. Authorship is always the human's.
- **Citation is mandatory.** Every authoritative claim traces to a primary source. *"INVEST fails the Independent criterion because …"* — not *"this isn't a good story"* without anchor.
- **Read-before-write per skill.** A new skill is not written without first reading the binding source verbatim. The same discipline applies when extending a skill.
- **Out-of-bibliography is named, not borrowed silently.** If a useful framework isn't in `bibliography/sources/`, the skill flags it as convention with a disclaimer.
- **Obsidian is the UI surface.** The human opens the repo as a vault to browse the graph (graph view, backlinks). When `_obsidian/bases/` populates with `.base` files, filtered views (backlog, in-flight, etc.) appear.

---

## Local preferences

Personal settings that should not be checked in (sandbox URLs, personal shortcuts, machine-local instructions) belong in `CLAUDE.local.md` at the repo root. That file is gitignored and is loaded after this one with local-priority semantics.
