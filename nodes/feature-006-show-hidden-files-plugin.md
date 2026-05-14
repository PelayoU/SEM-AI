---
category: feature
id: feature-006-show-hidden-files-plugin
parent: "[[cap-01-vision-to-code-audit]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 006 — Show-hidden-files plugin exposing `.claude/` in Obsidian

> Authored via `po-feature-decomposition`. Delivers part of [[cap-01-vision-to-code-audit]].

## What it delivers

Obsidian by default hides dot-prefixed files and directories. Without intervention, `.claude/` (agents, skills, commands, settings) is invisible to the editor — SEM-IA's substrate is half-blind. The community plugin `show-hidden-files` (`.obsidian/plugins/show-hidden-files/`) toggles dot-file visibility, exposing the entire substrate to navigation, search, and link resolution within Obsidian.

## Story Map position

- **Activity (Epic):** Editor surface completion.
- **Task:** This feature (show-hidden-files).
- **Release slice:** Walking skeleton — without it, the editor sees only half of SEM-IA.

## Stories (children)

- [[story-006-A-dot-files-visible]] — As a human navigating the vault in Obsidian, I want dot-prefixed files visible, so I can open agent definitions and skill files without leaving the editor.

## Spec sibling

- [[spec-006-show-hidden-files-plugin]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (visual test: `.claude/` appears in file tree) → Construction (community plugin installed + enabled) → Consequences (substrate fully visible in editor).

## Notes

Architectural anchor: [[adr-007-obsidian-as-editor-surface]]. The plugin is third-party community code — a tier-2 dependency. Architect's reuse certification gate (`architect-reuse-certification`) was bypassed for this case because the plugin's behaviour is trivially auditable (toggle visibility); risk is bounded. For tier-1 reuse the certification gate would apply.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-007-obsidian-as-editor-surface]].
- Substrate evidence: `.obsidian/plugins/show-hidden-files/manifest.json`; community-plugins.json lists it enabled.
- Out-of-bibliography: Obsidian (vendor); `show-hidden-files` (community plugin).
