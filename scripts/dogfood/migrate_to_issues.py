#!/usr/bin/env python3
"""Bootstrap dogfood — create the SEM-AI repo's first Issues via the engine.

Steps:
 1. Create the vision Issue (project = building SEM-AI).
 2. For each docs/adr/NNN-*.md, create a corresponding Issue with
 type=adr, parent=vision, status=accepted, acting_role=architect.

Run once, manually:
 SEM_AI_REPO=PelayoU/SEM-AI .venv/bin/python scripts/dogfood/migrate_to_issues.py

Idempotence: this script is NOT idempotent. Running twice creates duplicate
Issues. It is a one-shot bootstrap; the resulting Issue numbers are the
canonical references going forward.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.adapters import GitHubAdapter, load_config # noqa: E402
from engine.core import api # noqa: E402
from engine.core.catalog import NodeType, Status # noqa: E402
from engine.core.permissions import Role # noqa: E402


VISION_TITLE = "Build SEM-AI: GitHub-native framework for AI-augmented product development"

VISION_BODY = """## Why

Working with AI in software development is no longer a curiosity — it is the new normal. But the new normal carries a hidden tax: every line an agent suggests is a line a human has to *find*, then *judge*. Discovery cost. SEM-AI's reason for being is to collapse that discovery cost into validation — the engineer reads what was already recorded as compliant by a typed substrate of project intent, not searches for what drifted.

## The future as a context

Teams adopting AI seriously are converging on three patterns: agents acting through MCPs, GitHub as the unified platform for code + project intent, and CI/CD where validation is structural before it is semantic. SEM-AI lives at the intersection of those three.

## The future product story

Six role-homologous AI agents (PM, Architect, Developer, QA, DevOps, Security Officer) operating over a shared project-intent graph stored as GitHub Issues, with mechanical enforcement of parent-type, jurisdiction, lifecycle, and triggered_by — so the agent that tries to break the model can't.

## One-breath narrative

GitHub-native infrastructure for AI-augmented product development: the framework absorbs discovery cost so engineers keep authorship and judgement.

## Positioning

For development teams adopting AI agents seriously, SEM-AI is GitHub-native infrastructure that turns six role-homologous agents into a coherent product organization — distinct from chat-based copilots that leave coherence to luck.

## Value ambition

- Adopted by 10+ projects within 12 months of v1.0
- Measurably reduces AI-driven review labor from discovery to validation
- The framework can be applied to its own development (dogfood verified)
- The MCP layer enables future backend adapters (Jira / Linear / GitLab CI) post-v1

## Horizon

2026–2028. v0.3.0 ships the conceptual model + engine; v0.4 brings dogfood-driven refinements; v1.0 is reached when at least one downstream project has operated on the framework for a meaningful period.

## Adopted trends

- AI agents become first-class co-authors of project work, not just code-suggesters
- Project graphs migrate to managed platforms (GitHub Issues + Projects v2) rather than custom databases
- MCP becomes the lingua franca of tool-AI integration; framework-as-MCP-server is a viable distribution model

## Holistic dimensions

- **Functionality**: six role-homologous AI agents collaborating reactively over a project-intent graph stored as GitHub Issues
- **Technology**: Python engine MCP server + `gh` CLI adapter + minimal dependencies (pyyaml, requests, mcp)
- **UX design**: 3-command setup (clone → setup-engine.sh → setup-github-project.sh); skills as slash commands invoked by the agent
- **Monetization**: open-source framework; value to adopters is reduced review labor + structurally enforced graph integrity
- **Acquisition**: GitHub template + word of mouth among AI-augmented teams + reference adopters
- **Offline experience**: documentation in the repo + community Discussions; no external service to call
"""


def parse_adr_title(text: str) -> tuple[str, str]:
 """Extract title from the first '# ADR-N — title' line; return (title, body_after_title)."""
 lines = text.splitlines()
 if not lines:
 return ("(untitled ADR)", text)
 first = lines[0]
 m = re.match(r"^#\s+(.+?)\s*$", first)
 title = m.group(1) if m else first
 body = "\n".join(lines[1:]).lstrip("\n")
 return (title, body)


def main() -> int:
 cfg = load_config()
 adapter = GitHubAdapter(cfg)

 print(f"Target repo: {cfg.repo}")
 print()

 # ----- Step 1: Vision (idempotent) -----
 print("==> Vision Issue")
 existing_visions = adapter.query_issues(type=NodeType.VISION)
 if existing_visions:
 vision = existing_visions[0]
 print(f" [exists] vision = {vision.id} ({vision.title!r})")
 else:
 vision = api.create_node(
 adapter,
 type=NodeType.VISION,
 parent_id=None,
 title=VISION_TITLE,
 body=VISION_BODY,
 status=Status.ACTIVE,
 acting_role=Role.PM,
 )
 print(f" [created] vision = {vision.id} ({vision.title!r})")
 print()

 # ----- Step 2: ADRs -----
 adr_dir = REPO_ROOT / "docs" / "adr"
 adr_files = sorted(adr_dir.glob("[0-9][0-9][0-9]-*.md"))
 print(f"==> Migrating {len(adr_files)} ADRs as Issues (idempotent)")

 existing_adrs = adapter.query_issues(type=NodeType.ADR)
 existing_titles = {n.title: n for n in existing_adrs}

 created_adrs: list[tuple[str, str]] = []
 for adr_file in adr_files:
 text = adr_file.read_text(encoding="utf-8")
 title, body = parse_adr_title(text)
 if title in existing_titles:
 adr = existing_titles[title]
 print(f" [exists] {adr_file.name} → {adr.id}")
 created_adrs.append((adr_file.name, adr.id))
 continue
 print(f" [..] {adr_file.name}", end=" ", flush=True)
 try:
 adr = api.create_node(
 adapter,
 type=NodeType.ADR,
 parent_id=vision.id,
 title=title,
 body=body,
 status=Status.ACCEPTED,
 acting_role=Role.ARCHITECT,
 )
 except Exception as e:
 print(f"FAILED: {e}")
 return 1
 print(f"→ {adr.id}")
 created_adrs.append((adr_file.name, adr.id))

 print()
 print("==> Summary")
 print(f" vision: {vision.id}")
 for fname, issue_id in created_adrs:
 print(f" {fname} → {issue_id}")
 print()
 print("Save these Issue numbers — they are the canonical references")
 print("going forward. The markdown files in docs/adr/ can now be removed.")
 return 0


if __name__ == "__main__":
 sys.exit(main())
