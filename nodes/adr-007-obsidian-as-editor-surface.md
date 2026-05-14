---
category: adr
id: adr-007-obsidian-as-editor-surface
parent: "[[cap-01-vision-to-code-audit]]"
status: accepted
created: 2026-05-14
updated: 2026-05-14
supersedes:
superseded-by:
---

# ADR 007 — Obsidian is the recommended editor surface; the data layer remains editor-agnostic

> Documents an architectural decision significant enough to be cross-cutting, reversible only with effort, and questioned by future readers. **One decision = one ADR**. Inmutable once accepted: if the decision changes, create a new ADR that `supersedes` the previous one.
>
> The ADR format (Context / Decision / Consequences) is widely-adopted industry convention (Michael Nygard) but is **not in audited `bibliography/sources/`** — it is cited here as practitioner convention. The Architect role's authoritative criteria live in `architect-architecture-design` (Jones BP #14 + Ch 7 § Software Architecture). When an architectural decision is recorded as an ADR, the seven fundamental topics (Jones Ch 7 p. 470: structure / data / interfaces / decomposition / linkage / performance / security) are the audit grid.

## Status

**accepted** — Obsidian is configured in the substrate as the recommended editor surface. `.obsidian/` lives at repo root (graph view, workspace, show-hidden-files plugin); CLAUDE.md § *Operating principles* names Obsidian as *"the UI surface"*; the eight node templates live under `_obsidian/templates/` and are designed for Obsidian's Templater plugin. The data layer (markdown + YAML frontmatter + Obsidian-syntax wikilinks) remains readable in any markdown viewer.

## Context

Once the framework adopts a navigable graph of markdown nodes (ADR 002) and a substrate-vs-content partition (ADR 004), a question arises: *what does the human use to read, edit, and navigate the graph?* Three forces are in tension:

1. **The graph property demands a viewer that exposes it.** A backbone hierarchy plus narrative wikilinks (ADR 002) without a viewer that renders the graph as a graph reduces SEM-IA's audit claim to *"read the markdown files in alphabetical order"*. The vision's *"audit becomes inspection of the substrate"* claim requires a viewer that shows the graph as a graph and the backlinks as backlinks.
2. **Editor lock-in is a portability risk.** Naming a specific editor as required couples the framework to that editor's continued availability, license terms, and feature stability. A new contributor without that editor cannot operate the framework. This compounds with [[cap-13-portability]].
3. **The framework is engineering-grade, not data-science-grade.** Available choices for a graph-view-capable markdown editor include Obsidian, Logseq, Foam (VS Code extension), Dendron, plain text + custom tooling, and a handful of others. The choice should be one that lives well alongside a software engineering workflow (git, branching, CI/CD), not one that fights it.

A fourth tension: the framework's substrate already includes `.claude/` (hidden by default in most file viewers) and `_obsidian/` (named for Obsidian but containing plain markdown). The framework must accommodate this visibility asymmetry — Obsidian by default hides dot-directories, so `.claude/` requires explicit configuration to expose. The bootstrap session must produce the configuration; this is itself part of the decision.

## Decision

We adopt the rule **Obsidian is the recommended editor surface for the human; the data layer remains editor-agnostic**, with the following corollaries:

1. **The repo root *is* the Obsidian vault.** Opening Obsidian on `<sem-ia-repo>/` makes the graph view, backlinks pane, and Templater plugin available without additional configuration beyond what the substrate already ships.
2. **The substrate ships Obsidian configuration as part of the framework.** `.obsidian/` at repo root carries `workspace.json`, `graph.json`, and the show-hidden-files plugin configuration. This exposes `.claude/` and other dot-prefixed substrate to Obsidian's file view, making the framework readable from within the editor.
3. **The data layer is portable across markdown viewers.** Every node is plain markdown with YAML frontmatter. Wikilinks (`[[id]]`) are Obsidian-syntax but are widely supported (Logseq, Foam, plain GitHub web renders them as text). Templates use the Templater syntax for variable insertion but produce inert markdown once instantiated. A reader without Obsidian can still read every node, every session document, and every skill file.
4. **The slash-command interface (Layer B operating model) is editor-independent.** `/session-log`, `/session-context`, `/session-close` execute in Claude Code regardless of which editor the human uses for reading. Obsidian is for *reading and navigating* the graph; Claude Code is for *operating* the framework. The two surfaces are orthogonal.
5. **`_obsidian/` directory name acknowledges the recommendation.** The templates directory carries the recommended-editor name because the templates use Templater-flavoured placeholders. Re-targeting templates to a different editor's templating engine (Dendron, Foam, Logseq) is a substrate change, not a content change; the data the templates produce is editor-neutral.

## Consequences

**Positive:**

- **The graph property has a natural visual surface.** Obsidian's graph view shows the backbone hierarchy and wikilinks as a navigable graph; the backlinks pane shows incoming references on any node. The audit claim of the vision becomes operational and not just structural.
- **Configuration ships with the substrate.** A new contributor cloning the repo and opening Obsidian on it gets the graph view, the file-list view, and the hidden-files-visible state without manual setup. Cognitive load for first-time use is low.
- **The editor is free, multiplatform, and offline.** Obsidian runs on macOS, Linux, Windows; no server; no account required for core features. The "anyone can run SEM-IA" property of the vision survives at the editor layer.
- **Plugin ecosystem covers extension cases.** Templater (template instantiation), Dataview (queries over frontmatter — relevant for future `_obsidian/bases/`), Show Hidden Files (the substrate-exposure plugin) — all are stable, widely-used plugins with established maintainer bases.
- **The recommendation is decoupled from the data layer.** A future migration off Obsidian (to Foam, to a custom viewer, to a graph DB) does not require rewriting nodes — only re-targeting the templates and re-configuring the substrate's editor directory. The data is preserved.

**Negative:**

- **Obsidian is closed-source.** Its core editor is proprietary, even though the data format (markdown + frontmatter) is open. A regulatory or organisational policy that forbids proprietary editors would force the framework onto an alternative. The decision acknowledges this risk; the open-data property is the mitigation.
- **Configuration sprawl is real.** `.obsidian/workspace.json` carries layout state that drifts as the human uses the editor; small spurious changes appear in `git status` constantly. The substrate ships a baseline configuration, but per-contributor drift remains a low-grade friction.
- **Wikilink syntax is Obsidian-flavoured (community convention, not standard).** `[[id]]` is widely supported but not part of CommonMark or any standardised markdown variant. A renderer that doesn't resolve wikilinks displays them as literal text, which is a graceful degradation but not a clean rendering.
- **Templater is plugin-dependent.** Templates use Templater placeholders (`<% ... %>`); a contributor without Templater installed cannot instantiate a template from within the editor. Workaround: instantiate the template by hand by copying the file and filling the placeholders. The friction is real for first-time setup.
- **The substrate now contains editor-specific configuration.** `.obsidian/` is a substrate directory by location (ADR 004 partition) but its contents are editor-specific. A project that adopts SEM-IA and uses a different editor must either retain the `.obsidian/` directory dormant or remove it; either way, the substrate's editor-recommendation surfaces as a thing to opt out of, not opt into.

**Neutral:**

- **The choice is a recommendation, not a mandate.** A contributor preferring VS Code with Foam, or Logseq, or a plain markdown editor + custom CLI tooling can operate the framework — they lose Obsidian's graph view and backlinks pane but retain everything else. The framework documents the recommendation; it does not enforce it.
- **The data layer's portability is the load-bearing property.** Editor choice is downstream of data portability. If the data weren't editor-neutral, the recommendation would *be* a mandate; because the data is neutral, the recommendation is genuinely a recommendation.
- **Future `_obsidian/bases/` will deepen the recommendation.** `.base` files (Obsidian's filtered-views format) are planned for backlog views, in-flight queries, etc. When those land, the value of Obsidian as the recommended surface grows; switching editors would lose access to those filtered views. This is anticipated, not yet realised.
- **The editor choice does not affect agent behaviour.** Claude Code's agents read and write the data layer directly; they do not depend on any editor. The framework operates the same regardless of which editor the human uses.

## Alternatives considered

- **No editor recommendation; users pick whatever they want.** Rejected. Loses the configuration-shipped-with-substrate property; new contributors face cognitive setup cost; the graph property has no recommended visualisation surface, weakening the audit claim's operational form.
- **VS Code + Foam extension as the recommended editor.** Considered seriously. Real benefits: open-source, IDE-grade, lives natively in the same surface developers use for code. Real costs: Foam's graph view is less mature than Obsidian's; backlinks support is weaker; no Templater-equivalent of comparable ergonomics; no out-of-the-box hidden-files plugin. **Deferred, not rejected** — if Foam reaches parity, the recommendation could shift; the data layer would survive the migration.
- **Logseq as the recommended editor.** Considered. Real benefits: open-source, block-based. Real costs: opinionated about journal-first workflow; less well-suited to the hierarchical-backbone model SEM-IA uses; markdown export is lossy in some cases. Rejected as default.
- **Custom web-based viewer shipped with the framework.** Rejected. Adds infrastructure cost (build, host, maintain); breaks the offline property; reinvents wheels that mature editors already provide.
- **Mandate Obsidian; declare the framework Obsidian-only.** Rejected. Couples the framework's adoption to one editor's continued availability and license terms; defeats portability claim; conflicts with the *"anyone can run SEM-IA"* surface of the vision.

## Seven fundamental topics — touchpoints (Jones Ch 7, p. 470)

- **1. Overall structure:** Affected. The `.obsidian/` directory at repo root is a top-level substrate component; the choice to ship editor configuration with the framework is a structural decision about *where the recommended UX lives*.
- **2. Data structure:** Indirectly affected. The data layer itself is editor-neutral (markdown + frontmatter); but template syntax (Templater placeholders) is editor-specific until templates are instantiated. The data flows through an editor-specific gateway at authoring time, then becomes neutral.
- **3. Interfaces to outside world:** Materially affected. This is the principal topic the decision addresses. The interface between the framework and the human reader / author *is* the editor surface. The decision names Obsidian as the recommended interface and the data layer as the editor-neutral contract underneath.
- **4. Decomposition into functional components:** Affected. The framework decomposes into a data layer (universal), an editor layer (Obsidian-recommended), and an operating layer (Claude Code slash commands). Each layer is independently replaceable; the decomposition is intentional.
- **5. Linkage / information transmission among components:** Affected. The wikilink syntax is a piece of editor-flavoured linkage that survives editor change because it degrades gracefully to text. The recommendation preserves the linkage's *displayed* richness in the recommended editor while keeping the *underlying* linkage portable.
- **6. Performance attributes:** Not materially affected. Obsidian's graph rendering is performant for graphs of SEM-IA's scale. At very large scale (10k+ nodes) the graph view becomes unwieldy; not applicable today; would warrant attention only if the framework scaled to that order.
- **7. Security attributes:** Indirectly affected. Obsidian is closed-source; trust in the editor is required at runtime. The mitigation is that the data layer is open and inspectable; a compromised editor cannot fabricate data without leaving a trace in the markdown files visible to any other tool.

## Source

- Skill: `architect-architecture-design` (Jones Ch 7 seven fundamental topics, especially topic 3 — interfaces to outside world).
- Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), Ch 7 § Software Architecture (pp. 470–475) — seven fundamental topics, used here as the audit grid.
- CLAUDE.md § *Operating principles* (*"Obsidian is the UI surface"*), § *Repo structure* (`_obsidian/` is named in the substrate table).
- `.obsidian/` directory at repo root — the substrate's editor configuration.
- `_obsidian/templates/` — the templates, written in Templater syntax for the recommended editor.
- ADR format: Michael Nygard, *Documenting Architecture Decisions* (industry convention) — **not in audited `bibliography/sources/`**.
- Obsidian (Obsidian.md), Templater plugin, Show Hidden Files plugin — community tools, **not in audited `bibliography/sources/`**; cited as convention.
- Capability anchor: [[cap-01-vision-to-code-audit]] (the audit-by-navigation property the editor surface materialises operationally).
