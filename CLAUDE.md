# SEM-IA

A framework for software engineering management at scale — vision through code, fully traceable. The human assumes a role (Product Owner, Architect, QA, Developer, DevOps); each role is an AI agent grounded in audited bibliography and a curated catalog of skills. The whole project lives as a navigable graph of markdown nodes in `nodes/`, browsable as an Obsidian vault rooted at the repo.

**This file is the project's universal contract.** It is loaded into every Claude session in this repo, including invocations like `claude --agent product-owner`. Role-specific identity lives in `.claude/agents/<role>.md`. Skill criteria live in `.claude/skills/<role>-<skill>/SKILL.md`.

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

**Invocation.** Two modes:

- **Role-as-agent (human)** — `claude --agent <role>` starts a session where Claude assumes that role for the duration.
- **Subagent dispatch (Claude)** — from another role, use the `Task` tool with `subagent_type: <role>`. The response is consultation, not authority transfer (see Layer B below).

Both modes load this `CLAUDE.md` + the role's `agent.md`. The agent.md `description` field is what triggers correct dispatch.

---

## Repo structure

```
SEM-AI/
├── .claude/
│   ├── agents/<role>.md                Role identity + skill catalog (frontmatter Anthropic-compliant, body CLAUDE.md-style).
│   ├── skills/<role>-<skill>/SKILL.md  Skill = canonical method for one operation, anchored verbatim in primary sources.
│   ├── templates/
│   │   ├── agent.md.template           Pattern for new role files.
│   │   └── SKILL.md.template           Pattern for new skill files.
│   ├── sem-role-catalog.md             Source-of-truth design doc: roles, tiering, BP↔skill mapping.
│   └── settings.json                   Claude Code config (project-level).
├── _obsidian/
│   ├── bases/                          (Future) Filtered views of the graph as `.base` queries.
│   └── templates/                      Authoritative node-structure templates (vision/goal/cap/feature/story/spec/adr/session).
├── nodes/                              The project graph. Each `<type>-<id>-<slug>.md` is one artifact (currently empty).
├── sessions/                           Conversation records (`YYYY-MM-DD-<topic>.md`).
├── bibliography/
│   ├── sources/                        Audited PDFs (Capers Jones, GISF UC3M, Cucumber, etc.). Skills cite these.
│   ├── INDEX.md                        Navigable bibliographic index.
│   └── skill-references.md             Per-skill traceability for academic audit.
├── CLAUDE.md                           This file.
└── LICENSE
```

**Obsidian vault = repo root.** Opening Obsidian on this directory makes the graph, backlinks, and (future) bases views available.

---

## Skills convention

Each skill lives at `.claude/skills/<role>-<name>/SKILL.md` with frontmatter (`name`, pushy `description`) and a body of ≤ ~500 lines (Anthropic skill-creator). Body sections are fixed:

`## Purpose` · `## When this skill applies` · `## Formal criteria` · `## How you proceed` · `## Pitfalls to avoid` · `## Source`

**Citation mandate.** Every authoritative claim in a skill (criteria, thresholds, anti-patterns) cites a primary source: Jones BP # / page; GISF PDF slide #; Cucumber reference page. No criterion is stated without a citation. **Read-before-write:** the constructor reads the source firsthand (or `pdftotext` extract) before writing the skill.

**Out-of-bibliography handling.** Practitioner frameworks not in `bibliography/sources/` (Cagan books, Sinek, Doerr, Adzic, Patton book, Cohn book, Bass, Ford, Ousterhout, Martin, Nygard ADRs, ITIL, CMMI, ISO 9000/10007, IEEE 828/1028, Six Sigma, Crosby, Tom Gilb, Humble & Farley book, Three Ways DevOps, DORA, xUnit, GoF, SOLID, Clean Code, Strangler Fig, etc.) may be referenced as convention but are flagged with a disclaimer in the skill's `## Source` section — never cited as anchored authority.

---

## The graph

Backbone hierarchy (GISF UC3M `gisf-life-cycle.pdf` slide 53):

```
vision → goals → capabilities → features → stories → specs
                                                  ↘ adrs (architectural decisions can hang off anywhere)
```

**Naming.** `nodes/<type>-<id>-<slug>.md` where `<type>` ∈ `{vision, goal, cap, feature, story, spec, adr}`. Stories include a letter suffix to trace acceptance criteria in the sibling spec: `story-007-A-password-step.md` → spec `Scenario` labelled `AC-A1`, `AC-A2`, …

**Sessions** live in `sessions/YYYY-MM-DD-<topic-slug>.md` — distilled records of a meaningful conversation between the human and a role.

---

## Templates

The eight node templates in `_obsidian/templates/` are the canonical structure for each artifact type, derived directly from the corresponding Layer-A skill:

| Template                            | Anchored in skill            | Primary sources                                                                  |
| ----------------------------------- | ---------------------------- | -------------------------------------------------------------------------------- |
| `_obsidian/templates/vision.md`     | `po-vision`                  | Cagan 10 principles via GISF `gisf-discovery.pdf` slides 82, 84, 86, 89          |
| `_obsidian/templates/goal.md`       | `po-goals`                   | SMART (GISF slide 95), multilevel horizons (GISF slide 150), why-stack (slide 96)|
| `_obsidian/templates/capability.md` | `po-capabilities`            | GISF `gisf-life-cycle.pdf` slides 54, 64, 69; `gisf-discovery.pdf` slides 97–99  |
| `_obsidian/templates/feature.md`    | `po-feature-decomposition`   | Cohn slide 124, INVEST slide 128, 5 Cs slide 56, Story Map slide 132             |
| `_obsidian/templates/story.md`      | `po-feature-decomposition`   | Cohn slide 124, INVEST slide 128, 5 Cs (`agile-story-essentials.pdf`)            |
| `_obsidian/templates/spec.md`       | `po-spec-gherkin`            | Cucumber `gherkin-reference.pdf` pp. 1–9, GISF slides 54, 126                    |
| `_obsidian/templates/adr.md`        | `architect-architecture-design` | Jones Ch 7 § Software Architecture pp. 470–475 (Nygard ADR format as convention) |
| `_obsidian/templates/session.md`    | (used by every role)         | (operational convention; no single bibliographic anchor)                          |

**Application.** The human applies a template via Templater (Obsidian); an agent reads it via the `Read` tool, copies the structure, fills the placeholders, writes to the appropriate `nodes/<...>.md`.

**To create a new role or skill,** use the meta-templates at `.claude/templates/agent.md.template` and `.claude/templates/SKILL.md.template`.

---

## Frontmatter

**Minimal required fields** for every node:

| Field      | Meaning                                                      | Required for |
| ---------- | ------------------------------------------------------------ | ------------ |
| `category` | Node type (`vision`, `goal`, `capability`, `feature`, `story`, `spec`, `adr`, `session`). Drives `.base` filters and tooling. | Every node   |
| `id`       | Stable unique identifier matching the filename               | Every node   |
| `parent`   | Wikilink to the parent node in the backbone hierarchy        | Every node except `vision` |
| `status`   | One of the canonical values below                            | Every node except `session` |
| `created`  | `YYYY-MM-DD`                                                 | Every node   |
| `updated`  | `YYYY-MM-DD`                                                 | Every node   |

**Type-specific optional fields** appear in the relevant templates: `horizon:` (goal), `mvp:` (capability), `supersedes` / `superseded-by` (adr), `date` / `role` / `participants` (session).

**Not used in this project** (eliminated by design): `also-relates-to`, `depends-on`, `dimensions-affected`. Horizontal cross-references live as wikilinks in node bodies, not as frontmatter fields.

---

## Canonical status values

| Status                   | Meaning                                                | Applies to              |
| ------------------------ | ------------------------------------------------------ | ----------------------- |
| `draft`                  | Under construction in a session                        | All nodes               |
| `active`                 | Completed and in force                                 | `vision`, `goal`, `capability` |
| `ready-for-implementation` | Backlog-ready for a Developer to pick up            | `feature`               |
| `in-implementation`      | Developer / team working on it                         | `feature`, `story`      |
| `implemented`            | All stories done, spec satisfied, tests pass           | `feature`, `story`      |
| `deprecated`             | Consciously retired (no longer applies)                | All nodes               |
| `superseded`             | Replaced by a later artifact (keep `superseded-by:`)   | `adr`                   |

---

## Wikilinks `[[id]]`

For narrative cross-references inside a node body, use Obsidian wikilinks:

```markdown
This feature derives from [[cap-03-multirole-agents]] and produces the spec [[spec-007-login-multifactor]].
```

Wikilinks activate Obsidian's backlinks pane and graph view. They are **narrative references**, not the formal hierarchical edge — `parent:` in frontmatter is the formal edge. Use the two consistently.

---

## Layer B — operating the graph

This section codifies *how* the framework is used. Layer A (roles + skills + bibliography + templates) provides the *what* and *why*; Layer B provides the *how* and *when*.

### The triangle

Three pillars hold the operating model together. Each leg removes a class of friction that traditional Working Agreements try (and usually fail) to handle:

1. **Traceability** — every artifact in `nodes/` has an explicit `parent:` chain and `[[wikilinks]]`. The graph itself answers *"what exists and how does it relate?"*. Replaces *"where is X documented?"* friction.
2. **Scope discipline** — each role operates only the skills listed in its `## Skills` section. Work falling outside the role's scope is escalated via subagent consultation or session handoff. Scope violations are visible at audit time via the session doc's `participants` field. Replaces *"whose job is this?"* friction.
3. **Sessions as shared context** — a thread of work lives as a git branch + a session document in `sessions/`. Multiple roles may participate; anyone entering the session inherits full context. Replaces *"let me catch you up"* friction.

The triangle replaces a Working Agreement. There are no team rules to memorise — the infrastructure makes the right path the natural path.

### Sessions = git branch

A **session** is a thread of work materialized as two coupled artifacts:

1. A **git branch** named `session/<YYYY-MM-DD>-<topic-slug>`.
2. A **session document** at `sessions/<YYYY-MM-DD>-<topic-slug>.md` — narrative log of what happened, who contributed, what nodes were touched.

**Branch state is session state.** No `status:` field in the session frontmatter. If the branch exists, the session is open. On `main`, no session is active. To list open sessions: `git branch | grep ^\ \ session/`.

A session is **agnostic of role**. Multiple roles may participate in the same session — by subagent consultation or by sequential agent invocation in the same branch. The session document records who contributed when.

### Subagent dispatch ≠ authority transfer

When a role invokes another role via the `Task` tool, the response is **information**, not authority. PO consulting Architect about feasibility does *not* mean Architect now owns the feature — PO retains scope authority and uses Architect's input as data. This distinction keeps roles from quietly bleeding into each other's scopes, and is the operational form of pillar 2 of the triangle.

If full ownership transfer is what's needed (rare), the human closes the conversation with the first role and opens a new one with the second, in the same session / same branch.

### Slash commands

Custom commands live in `.claude/commands/`. The Layer B set:

- `/session-open <topic-slug>` — creates branch `session/<date>-<topic-slug>` + initial session doc from `_obsidian/templates/session.md`.
- `/session-close` — appends final summary to session doc; the human decides merge to `main` / open PR / discard.
- `/session-context` — re-reads the current session doc into context. Useful in long sessions when context has drifted.

### SessionStart hook

A `SessionStart` hook in `.claude/hooks/` checks `git branch --show-current` when Claude starts. If on a `session/*` branch, the hook surfaces the corresponding session doc as context. On `main`, the hook is silent.

This is the mechanism that makes "any role can pick up where another left off" work without ceremony: switch to the session branch (or already be on it), launch the role you need, the session context is loaded.

### Direct work on `main`

Working directly on `main` without opening a session is permitted but discouraged for product-driven work. It is appropriate for trivial fixes, exploration, or work explicitly outside the session model (one-line typo fixes, repo hygiene). The framework does not enforce a no-direct-commits-to-main rule by default; if you want it, add a pre-commit hook locally.

---

## Bibliography and citation discipline

`bibliography/sources/` holds the audited primary sources skills cite:

- `se-best-practices.pdf` — Capers Jones (McGraw-Hill 2010). 28 of 50 Best Practices currently used + Ch 1 § Critical Topics + Ch 5 § SQA Organizations + Table 5-1 + Table 5-2 + Ch 7 § Software Architecture + Ch 8 § Forms of Defect Prevention + Ch 9 Tables 9-22 and 9-23.
- 6 GISF UC3M PDFs (`gisf-discovery.pdf`, `gisf-life-cycle.pdf`, `gisf-delivery-planning.pdf`, `gisf-delivery-backlog-management.pdf`, `gisf-pipeline-devops.pdf`, `gisf-delivery-control-and-monitoring.pdf`).
- `gherkin-reference.pdf` — Cucumber official Gherkin syntax.
- `user-story-mapping.pdf` — Patton story-map concepts (Comakers 2013 handout).
- `agile-story-essentials.pdf` — Comakers / Patton 2013 (Kent Beck origin attribution).

`bibliography/INDEX.md` is the navigable map of these sources.
`bibliography/skill-references.md` is the per-skill traceability record for academic audit (TFM defence, etc.).

**Pattern.** Skills cite sources inline: `(Jones BP #14, p. 76)` · `(GISF gisf-discovery.pdf slide 89)` · `(Cucumber gherkin-reference.pdf p. 1)`. A statement without such a citation is not a statement from this framework.

---

## Operating principles

- **Human directs; AI maintains.** A role proposes; the human confirms before anything is written. Authorship is always the human's.
- **Citation is mandatory.** Every authoritative claim traces to a primary source. *"INVEST fails the Independent criterion because …"* — not *"this isn't a good story"* without anchor.
- **Read-before-write per skill.** A new skill is not written without first reading the binding source verbatim. The same discipline applies when extending a skill.
- **Out-of-bibliography is named, not borrowed silently.** If a useful framework isn't in `bibliography/sources/`, the skill flags it as convention with a disclaimer — never as anchored authority.
- **Layer A vs Layer B.** **Layer A** (roles + skills + bibliography + canonical templates) defines the *what* and *why* of every operation: what a role does, what criteria it applies, what artifact it produces. **Layer B** (sessions as git branches + slash commands + the SessionStart hook, documented above) defines the *how* and *when*: how work is opened, threaded across roles, and closed. Together they replace what a Working Agreement would try to legislate.
- **Obsidian is the UI surface.** The human opens the repo as a vault to browse the graph (graph view, backlinks). When `_obsidian/bases/` populates with `.base` files, filtered views (backlog, in-flight, etc.) appear.

---

## Local preferences

Personal settings that should not be checked in (sandbox URLs, personal shortcuts, machine-local instructions) belong in `CLAUDE.local.md` at the repo root. That file is gitignored and is loaded after this one with local-priority semantics.
