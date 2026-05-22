---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-14
updated: 2026-05-22
maintained_by_role: architect
---

# ADR 008 — Markdown body + YAML frontmatter is the canonical data format for every node

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — operating across every node in `nodes/`, every session document in `sessions/`, every skill file in `.claude/skills/`, every agent identity in `.claude/agents/`, and every template in `_obsidian/templates/`. The format is not declared as a top-level decision in CLAUDE.md but is everywhere implicit; this ADR surfaces and records the decision.

## Context

The substrate must pick a data format for every node — vision, goal, capability, feature, story, spec, ADR, session — and for every framework artifact (skills, agents, templates). The choice constrains every other decision downstream: what tools can read the data, what schemas the data can encode, how the data version-controls, how an AI agent reads and writes it. Three forces are in tension:

1. **The format must be human-readable directly.** A reader (auditor, contributor, AI agent) should be able to open any node in a plain text editor and understand it without rendering, decoding, or special tooling. The vision's *"audit becomes inspection of the substrate"* claim requires this: substrate inspection is reading text, not running queries.
2. **The format must carry structured metadata.** Frontmatter (parent edges, status, dates, IDs, type-specific fields like `horizon`, `mvp`, `supersedes`) must be machine-parseable for tooling, schema-checkable for discipline, and human-readable when opened directly. A pure-prose format loses the structural property; a pure-data format loses the human-readability property.
3. **The format must compose with git and with line-oriented tools.** Diff, merge, grep, sed, line-numbered editing — these are the daily tools of software work. A format that breaks line-orientation (e.g., a binary container, a single-line JSON blob) defeats the toolchain SEM-IA inherits from its host environment.

A fourth tension: an AI agent (LLM) reads text most reliably and writes text most predictably. Formats that require an LLM to produce well-formed XML, JSON, or DSL output introduce a class of failure modes (malformed brackets, escape-character bugs, indentation drift) that markdown does not have. The substrate's data format also constrains agent reliability.

## Decision

We adopt **markdown body + YAML frontmatter** as the canonical data format for every node, every session document, every skill file, every agent identity file, and every template in the substrate. The convention:

1. **YAML frontmatter is the first content of every file**, delimited by `---` on its own line at the top and `---` on its own line ending the block. Frontmatter carries structured fields (per CLAUDE.md § *Frontmatter*): `category`, `id`, `parent`, `status`, `created`, `updated`, and type-specific optional fields.
2. **Markdown body follows the frontmatter**, in standard CommonMark with the Obsidian wikilink extension (`[[id]]`) per ADR 002. Body sections are template-defined; the templates encode required sections per node type.
3. **One file = one node = one artifact.** No multi-node files, no node-fragments-across-files, no encoded sub-objects. The unit of authorship and the unit of versioning are the same.
4. **Filenames carry the node identity.** `nodes/<type>-<id>-<slug>.md` per CLAUDE.md § *The graph*; the filename's stem matches the frontmatter `id` field. Stories include a letter suffix to trace acceptance criteria into the sibling spec (`story-007-A-...` → `AC-A1`, `AC-A2`).
5. **No alternative format is permitted for substrate-authored artifacts.** A future need for richer data (graph queries, structured indices) is satisfied by *deriving* views (e.g., Obsidian `.base` files, `bibliography/skill-references.md`) from the canonical markdown, not by substituting the canonical format with anything else.

## Consequences

**Positive:**

- **Universal readability.** Every file in the framework opens in any text editor, on any operating system, without special tooling. The reader gets full content; the AI agent gets full content; the auditor gets full content. The vision's substrate-inspection claim is structurally honoured.
- **Native git semantics.** Markdown + YAML diffs cleanly, merges reasonably, and survives copy-paste between branches. The framework inherits git's full toolchain (diff, blame, bisect, rebase, cherry-pick) for free.
- **Frontmatter is schema-enforceable.** YAML's key-value structure makes schema-checking straightforward (the field's existence, its type, its value range). Tooling that wants to validate "every node has a `parent` field linking to an existing node" reads YAML and walks the wikilinks; no parser engineering required.
- **Obsidian-native.** The recommended editor (ADR 007) renders markdown + frontmatter natively; wikilinks become navigable; frontmatter fields appear in the file metadata pane and drive search and queries.
- **LLM-friendly.** Markdown is the most reliably produced text format from LLMs. The substrate's choice of format reduces agent failure modes (malformed output) at the data layer.
- **No format lock-in.** Markdown + YAML are ISO-publishable, decades-stable, and outside any single vendor's roadmap. The substrate's data layer outlives the editor, the harness, and the LLM provider.
- **Citation pattern composes naturally.** The inline citation pattern (ADR 003) is plain text within markdown body; no special escape, no separate annotation channel. The citation discipline operates entirely within the format.

**Negative:**

- **No native schema validation.** Markdown editors render YAML frontmatter without enforcing schema; a malformed `parent:` or a misspelled `status:` value is caught only at audit time or by a custom linter (currently not present). The discipline is convention-enforced, not structurally enforced.
- **Frontmatter and body can drift.** A node's body might claim properties the frontmatter doesn't carry (or vice versa); the format does not force reconciliation. Templates mitigate this by structuring the body in parallel with the frontmatter, but the drift risk is real.
- **Wikilink resolution is editor-specific.** `[[id]]` resolves correctly in Obsidian, plain text everywhere else. A reader on plain GitHub web sees the wikilink as text; a search for "incoming links to this node" requires either Obsidian or custom tooling. This is the ADR 002 negative consequence in its data-format form.
- **No native typed relationships.** Frontmatter carries `parent:` as a single string; the value is *conventionally* a wikilink (`"[[id]]"`) but YAML doesn't know that. Typed-edge semantics live in the framework's reading conventions, not in the data format. A custom relationship type (e.g., "this spec implements that capability") cannot be machine-typed without inventing a new frontmatter field or new tooling.
- **Markdown's structural expressiveness is limited.** Heading levels, lists, tables, code blocks. Anything beyond these requires plain prose or extensions (Mermaid diagrams, math syntax) that not every renderer supports. For most SEM-IA artifacts this is enough; for the rare case (a complex diagram, a structured table that wants joins) the format is a constraint.

**Neutral:**

- **The choice is conventional, not Jones-anchored.** Jones (Ch 7 topic 2 — data structure) speaks of hierarchical / relational / row-oriented / column-oriented / object-oriented data architectures. Markdown + YAML doesn't fit cleanly into these categories — it is *document-oriented* with metadata. The decision is grounded in the human-readability + git-composability + LLM-friendliness tensions, not in Jones taxonomy directly. Flagged as practitioner convention.
- **Frontmatter dialect is conservative.** YAML, not JSON (JSON would also work but reads worse); YAML's looser typing is acceptable at the framework's scale.
- **Filename convention is part of the data format in this framework.** `<type>-<id>-<slug>.md` carries semantic information (the type) outside the file contents. A reader inspecting a directory listing already learns the node's category. The convention is load-bearing; renaming files breaks `parent:` references.
- **The format is not unique to SEM-IA.** Markdown + YAML frontmatter is the *de facto* standard for static-site generators (Hugo, Jekyll, Eleventy), for Obsidian, for Foam, for Logseq. SEM-IA's data layer composes naturally with this ecosystem; an export to a static site is trivial.

## Alternatives considered

- **JSON or YAML for nodes (no markdown body).** Rejected. Loses human-prose narrative; turns every node into a record; defeats the *audit-by-reading* property. The vision's "audit is substrate inspection" reduces to "audit is record traversal".
- **A custom DSL for nodes.** Rejected. Requires a parser; couples the framework to its own parser's continued maintenance; loses git diff/merge ergonomics; loses LLM reliability.
- **Markdown body without frontmatter; metadata in a separate manifest file.** Rejected. Splits the node across two files; introduces a synchronisation requirement (manifest must match files); doubles the parse surface; loses the property *"one file = one node"*.
- **AsciiDoc or reStructuredText instead of markdown.** Rejected. Better structural expressiveness, worse tool support, worse LLM familiarity, worse Obsidian ecosystem fit. The trade is wrong for this framework's needs.
- **Org-mode (Emacs-flavoured) for nodes.** Rejected. Excellent structural expressiveness, narrow editor support (effectively Emacs-only), poor Obsidian fit. Loses portability across editors.
- **A graph database (Neo4j, etc.) as the data layer.** Rejected. Tremendous structural expressiveness; rich query semantics; but breaks all four forces — not human-readable, not git-native, not LLM-friendly, not tool-composable. Considered by [[cap-01-vision-to-code-audit]] as an alternative implementation; not adopted.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Materially affected. Every artifact in the substrate is a markdown + YAML file; the structure of the framework *as files on disk* is a direct consequence of this choice.
- **2. Data structure:** Materially affected. This is the principal topic the decision addresses. The data architecture is document-oriented (markdown body) with metadata (YAML frontmatter); the schema lives in the templates; the format is uniform across all node categories. Jones's hierarchical / relational / row-oriented / column-oriented / OO catalog does not include document-oriented as a first-class option — flagged as the practitioner convention that fills this gap.
- **3. Interfaces to outside world:** Affected. Any external consumer of the framework's data — a static-site generator, a custom dashboard, an audit tool — reads markdown + YAML. The interface is a widely-supported standard, not a SEM-IA-specific format.
- **4. Decomposition into functional components:** Affected. The substrate decomposes into files; each file is one node; the partition is at the file boundary. Functional components do not span files.
- **5. Linkage / information transmission among components:** Affected. Linkage is carried by frontmatter `parent:` (formal) and by wikilinks in the body (narrative). Both are textual; both survive in any markdown reader. The transmission channel is the file format itself.
- **6. Performance attributes:** Not materially affected. File-system reads are cheap; markdown parsing is cheap; YAML parsing is cheap. At SEM-IA's scale, performance is uninteresting. If the framework ever scaled to 10,000+ nodes, file-system enumeration time would warrant attention; not applicable today.
- **7. Security attributes:** Indirectly affected. Plain-text files inherit the repository's secrecy posture; no opaque containers; no hidden state. A reviewer can audit any node directly. This transparency is a security property: nothing can be hidden inside an encoded blob.

## Source

- Skill: `architect-architecture-design`.
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics, especially topic 2 (data structure). Jones's data-architecture catalog (hierarchical / relational / row-oriented / column-oriented / OO) does not include document-oriented; the gap is filled by practitioner convention.
- CLAUDE.md § *Frontmatter*, § *The graph*, § *Repo structure* — the substrate sections that operationalise this format.
- `_obsidian/templates/*.md` — the eight templates that encode the per-node-type schema.
- CommonMark specification (commonmark.org) — markdown standard, **not in audited `bibliography/sources/`**; cited as standard.
- YAML 1.2 specification — frontmatter standard, **not in audited `bibliography/sources/`**; cited as standard.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**.
- Related: ADR 002 (the wikilink + parent-edge linkage rides on this format), ADR 003 (the citation pattern is plain text within markdown), ADR 007 (Obsidian renders this format natively).
