#!/usr/bin/env python3
"""Bootstrap dogfood Part 2: create the goal + capability spine under vision #1.

Reads the existing vision Issue, then creates:
  - 8 goals as children of vision (G1..G8)
  - 10 capabilities as children of their primary goal (C1..C10)
  - Cross-axis 'related' links for capabilities serving multiple goals

Idempotent: re-running detects existing nodes by title and skips creation,
but still re-applies related links (safe — the underlying engine.set_related
treats it as a set operation).

Run once, manually:
    SEM_AI_REPO=PelayoU/SEM-AI .venv/bin/python scripts/dogfood/create_spine.py

The resulting Issue numbers are the canonical references going forward.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.adapters import GitHubAdapter, load_config  # noqa: E402
from engine.core import api  # noqa: E402
from engine.core.catalog import NodeType, Status  # noqa: E402
from engine.core.permissions import Role  # noqa: E402


# ============================================================================
# Goal bodies
# ============================================================================


@dataclass(frozen=True)
class GoalSpec:
    code: str  # "G1"
    title: str
    body: str


GOALS: list[GoalSpec] = [
    GoalSpec(
        code="G1",
        title="Sustained, maintainable product lifecycle",
        body="""## Map
- Children: capabilities serving lifecycle persistence (typed graph, sessions, experimentation lifecycle, project-intent evolution)
- Related: vision #1 § Value ambition (lifecycle is the differentiator vs one-shot AI tooling)

## Outcome statement

Software built under SEM-AI remains visible, traceable, maintainable and evolvable months and years after first commit. Releases, pipelines, bugfixes, feature improvements and deprecations all occur within the same framework that produced the initial work. The graph IS the living memory of the product.

Contrast with chat-based AI tooling (Codex / Antigravity / Claude Code standalone): output is generated one-shot, after which the project degrades into an opaque blob nobody can reason about. SEM-AI prevents that degradation structurally.

## Parent vision

#1 — Build SEM-AI: GitHub-native framework for AI-augmented product development

## Horizon

2026–2028. v1.0 condition: at least one downstream project has operated on SEM-AI for ≥3 months without degenerating into ad-hoc maintenance.

## Acceptance check

A project built under SEM-AI can be picked up by a new contributor after 6 months and they can orient + ship within hours, not weeks of code archeology. Concretely: vision + goals are readable in the graph; recent decisions live as `type:adr` Issues; sessions show what was tried; Value chain sections show what was learned.

## Why this goal

The vision's *Why* states: "every line an agent suggests is a line a human has to find, then judge." Without lifecycle infrastructure, AI-augmented work creates a maintainability cliff — fast initial shipping but no ability to evolve. This goal closes that loop: the framework ensures what AI produces remains continuously refactorable, releasable, and debuggable.

## Holistic dimensions

- **Functionality**: every artifact (release / PR / bug / spec) anchors to a graph node; nothing floats orphaned.
- **Technology**: Issues + Projects v2 + Milestones + Releases are durable GitHub-native objects; no parallel DB that could decay.
- **UX design**: PM (and any reader) sees the product state at-a-glance via the graph view; no proprietary dashboard.
- **Monetization**: maintainability reduces total-cost-of-ownership of AI-generated software — the differentiator with measurable willingness-to-pay.
- **Acquisition**: this IS the framework's primary positioning vs chat-based copilots — sustained lifecycle, not one-shot generation.
- **Offline experience**: the graph and its history survive without external services or vendor lock-in.
""",
    ),
    GoalSpec(
        code="G2",
        title="AI authoring is scope-correct and role-coherent",
        body="""## Map
- Children: capabilities preventing AI scope-drift (typed graph, role-bound agents, multi-dimensional evaluation)
- Related: vision #1 § Positioning (distinct from chat-based copilots that leave coherence to luck)

## Outcome statement

AI agents under SEM-AI produce work strictly within the sanctioned scope of the project: no hallucinated features, no role-bleed, no out-of-context decisions. The graph IS the plan, and the agent reads it before authoring. Role identity is mechanically enforced: a Developer cannot author a spec, an Architect cannot transition a feature to done.

## Parent vision

#1

## Horizon

Continuous — not a milestone goal but a steady-state property the framework maintains from v0.3.0 onwards.

## Acceptance check

In adopter projects, the rate of "AI generated something out of scope" defects approaches zero; the rate of "AI did the wrong role's job" similarly. Measured by manual audit on a sample of AI-authored commits in dogfood + first adopters.

## Why this goal

Chat-based AI tools hallucinate because they lack project-intent context and role boundaries. SEM-AI prevents both structurally: the graph is read before authoring (scope context), and jurisdiction is enforced mechanically (role boundaries). These two together convert the AI from a chaotic copilot into a role-correct peer.

## Holistic dimensions

- **Functionality**: graph contains project intent before any authoring; the agent loads it via MCP reads.
- **Technology**: engine MCP validates parent-type, jurisdiction, status at write time — no semantic guessing.
- **UX design**: PM sees role-correct work; doesn't have to police agents.
- **Monetization**: scope-correct AI work = less rework = the customer's saved time is the value claim.
- **Acquisition**: differentiator vs chaotic AI copilots that produce plausible-looking but off-scope code.
- **Offline experience**: enforcement is local (in the engine); doesn't need cloud arbiter.
""",
    ),
    GoalSpec(
        code="G3",
        title="Structural defects caught early in the cycle",
        body="""## Map
- Children: semantic CI capability (engine/checks + hooks + Actions)
- Related: vision #1 § The future product story (mechanical enforcement); G1 (defects early extend lifecycle quality)

## Outcome statement

Structural and semantic defects — missing Security attributes section on an ADR touching auth, role-bleed on an Issue, scope drift in a feature body, missing Learning extracted on a closed feature, supersede chain inconsistency — surface at hook-time (during authoring) or at PR-time (before merge), not in production or post-incident review. AI work reaches human review already structurally sound.

## Parent vision

#1

## Horizon

Continuous from v0.3.0 onwards; surface area grows as more semantic checks are written.

## Acceptance check

In dogfood + adopter projects, ≥80% of structural defects (catalogue-violations + missing-required-section + supersede-chain breaks) are caught by automated checks before human PR review. Measured by counting findings in CI logs vs findings in PR review comments.

## Why this goal

Catching defects late is expensive — late changes ripple. Catching them at authoring time means the agent fixes them while still in context (and still has the role assigned). Two-layer CI (structural push-time + semantic hook/PR-time) is the mechanism.

## Holistic dimensions

- **Functionality**: engine/checks library + 5 hooks + sem-ai-ci.yml + Action examples
- **Technology**: Python checks runnable both from hooks (in-process) and Actions (CI) — same library, two entry points
- **UX design**: developer sees findings inline in their Claude Code session, not 30 minutes later in a PR review
- **Monetization**: less rework = customer time saved per cycle
- **Acquisition**: "CI that thinks before you ship" sells to QA-conscious teams
- **Offline experience**: checks run locally during authoring + remotely during CI; no SaaS dependency
""",
    ),
    GoalSpec(
        code="G4",
        title="Discovery cost collapses into validation cost",
        body="""## Map
- Children: none directly — this goal is served emergently by C1+C2+C3+C4+C5
- Related: vision #1 § Why (the foundational claim); G1 (lifecycle preserves prior discovery)

## Outcome statement

In dogfood and adopter projects, AI-augmented review labor measurably shifts from discovery (searching for what was decided, what's already covered, who owns this, where the spec lives) to validation (reading what's structurally recorded and judging whether it's right). Honest framing: this may not move in all projects; the goal is to observe whether it does and report honestly when it does not.

## Parent vision

#1

## Horizon

12–18 months post-v1.0 (requires adopter data + telemetry instrumentation we do not yet have).

## Acceptance check

In instrumented adopter projects, post-adoption review-time-per-PR shifts ≥30% from "what's the context" (discovery) to "is this correct given the context" (validation). Requires instrumentation: telemetry hook on Claude Code, user studies, or self-reported labor diaries from adopter PMs.

## Why this goal

The vision's *Why* IS this — "collapse discovery cost into validation". This goal makes that measurable rather than aspirational. It also keeps the framework honest: if data shows discovery cost does not actually drop, the value chain is broken and we should learn rather than celebrate.

## Holistic dimensions

- **Functionality**: emergent property of C1+C2+C3+C4+C5; not a single capability
- **Technology**: needs instrumentation we do not yet have — this is the operational gap to close
- **UX design**: the felt experience is "I see the product, not search for it"
- **Monetization**: time saved per cycle is the productivity claim; without data this is a story
- **Acquisition**: hardest goal to demonstrate without reference adopters publishing data
- **Offline experience**: the shift happens locally in the team's flow; no central tracking
""",
    ),
    GoalSpec(
        code="G5",
        title="Enterprise-grade discipline accessible at any scale",
        body="""## Map
- Children: capability — adopter-customizable methodology layer (C10)
- Related: GitHub-native infrastructure capability (C5); vision #1 § Acquisition (template + word of mouth)

## Outcome statement

A freelance developer or 2-person team adopting SEM-AI obtains the same structural discipline (typed graph, role discipline, mechanical CI, semantic validation) that an enterprise team would otherwise build over years of internal tooling. Inversely, large organizations inject their own methodology skills (`.claude/skills/<topic>/SKILL.md`) to enforce house style — corporate-quality practices propagate to AI behavior and humans uniformly.

## Parent vision

#1

## Horizon

2026–2027 (needs ≥2 reference projects per segment to validate both directions of the claim).

## Acceptance check

At least 2 reference projects in each segment — solo/small (≤3 devs) and enterprise (≥1 org with custom methodology skills) — demonstrate distinct usage patterns of the methodology layer. Both report on quality / scope / role coherence outcomes.

## Why this goal

AI-augmented development today has a stratification problem: big-co tooling vs solo-dev improvisation. SEM-AI ships infrastructure once; both segments customize methodology. The framework's "fixed layer + variable layer" architecture (CLAUDE.md) makes this work without forking.

## Holistic dimensions

- **Functionality**: fixed layer (catalog + MCP + hooks + role contracts) is universal; variable layer (skills + body content + Actions) is per-project
- **Technology**: extensibility point is `.claude/skills/` injection — no source changes
- **UX design**: defaults work for solo devs out of the box; orgs override via skills they author
- **Monetization**: same framework serves both markets — broader TAM than enterprise-only or hobbyist-only tools
- **Acquisition**: solo devs discover via GitHub templates; enterprises adopt via internal champions who recognize the methodology fit
- **Offline experience**: works without org-wide SaaS; works inside air-gapped enterprise too
""",
    ),
    GoalSpec(
        code="G6",
        title="External adoption (≥10 projects post-v1.0)",
        body="""## Map
- Children: capability — GitHub-native backend with no extra infrastructure (C5)
- Related: G1-G5 (adoption is the necessary precondition for industry outcomes manifesting outside SEM-AI's own repo)

## Outcome statement

Within 12 months of v1.0, ≥10 independent projects are actively running cycles on SEM-AI (not just clicked-the-template; operating under the model — vision Issue, ≥3 goals, ≥10 features, evidence of sessions and PR closures via the framework). Adoption is the necessary precondition for the industry outcomes (G1-G5) actually manifesting in the world.

## Parent vision

#1 — directly from Value ambition slot ("Adopted by 10+ projects within 12 months of v1.0")

## Horizon

12 months post-v1.0.

## Acceptance check

≥10 projects with substantial graph activity: vision + ≥3 goals + ≥10 features + evidence of session docs and PR closures via the framework. Tracked via GitHub template fork count + community signals (Discussions, Issues on this repo, referrer traffic).

## Why this goal

A framework with no adopters cannot validate its industry-outcome goals. Adoption is the necessary precondition for G1-G5 manifesting in the world. Without external adoption, dogfood (G7) is the only datapoint and it confirms only that the framework's authors can use the framework — circular.

## Holistic dimensions

- **Functionality**: template + 3-command setup must be frictionless; new adopters hit minimum viable graph within 30 minutes
- **Technology**: distribution via GitHub template (no install ritual, no auth setup beyond `gh auth login`)
- **UX design**: README + CLAUDE.md onboarding readable in ≤5 minutes
- **Monetization**: open-source; value to adopters is reduced review labor + structurally enforced graph integrity
- **Acquisition**: GitHub template discovery + word of mouth among AI-augmented teams + 2-3 reference adopters publishing experience
- **Offline experience**: adopter doesn't depend on SEM-AI's own infrastructure; they self-host on their own GitHub
""",
    ),
    GoalSpec(
        code="G7",
        title="Dogfood coherence",
        body="""## Map
- Children: no capability dedicated — dogfood is organizational discipline, not a system capability
- Related: every other goal (the framework dogfoods itself by using its own capabilities on its own development)

## Outcome statement

SEM-AI's own development operates under SEM-AI's model without parallel mechanisms: no markdown ADRs in docs/adr/, no role-bleed in development sessions, no decisions taken outside `type:adr` Issues, no work happening outside session branches. Continuous discipline, not a one-shot achievement.

## Parent vision

#1 — from Value ambition ("The framework can be applied to its own development (dogfood verified)")

## Horizon

Continuous from v0.3.0 onwards. The 2026-05-24 migration of 9 markdown ADRs to Issues #2-#10 is the first major dogfood inflection point; further ones occur each time the framework gains a capability.

## Acceptance check

At any point in time, the SEM-AI repo's graph is queryable and self-consistent: no orphan artifacts; no decisions stored outside Issues; no role-violations in commit history; every substantive work block has an associated session doc. Checkable via the framework's own validators run against itself.

## Why this goal

A framework that cannot run on itself cannot credibly claim to enable others. Dogfood is also the only continuous integration test of the framework's model that exists pre-adoption — every time we use SEM-AI to build SEM-AI we find friction the model needs to address.

## Holistic dimensions

- **Functionality**: every SEM-AI development decision goes through the graph (Issue + spine + Value chain post-done)
- **Technology**: SEM-AI uses its own engine MCP for writes; no bypass
- **UX design**: the framework's PM (me/Pelayo) operates as PM-role under SEM-AI's contract — feels what an adopter would feel
- **Monetization**: dogfood validates that the framework IS usable, which is the entire product proposition
- **Acquisition**: dogfood signals quality to potential adopters — "they use it themselves"; published Value chain sections become reference material
- **Offline experience**: framework operates without depending on its own future versions; v0.3 must be usable without v0.4 to validate this
""",
    ),
    GoalSpec(
        code="G8",
        title="Backend portability viable post-v1",
        body="""## Map
- Children: capability — adapter pattern + stable MCP contract (C6)
- Related: vision #1 § Adopted trends (MCP as lingua franca), Positioning (GitHub-native but not GitHub-locked)

## Outcome statement

A non-GitHub adapter (Jira / Linear / GitLab / private backend) can be contributed without modifying `engine/core/` or any agent / skill code. The abstraction is validated either by shipping a second adapter or by an accepted community RFC describing what the implementation would look like.

## Parent vision

#1 — from Value ambition ("The MCP layer enables future backend adapters (Jira / Linear / GitLab CI) post-v1")

## Horizon

Post-v1.0. No requirement to ship a second adapter before v1.0; the abstraction must merely demonstrate it could.

## Acceptance check

Either: (a) ≥1 community RFC documents a complete BackendAdapter implementation for a non-GitHub backend (Jira / Linear / GitLab) and the SEM-AI maintainers accept it as viable, OR (b) a stub adapter for one non-GitHub backend exists in `engine/adapters/` and demonstrates the BackendAdapter interface holds without engine/core changes.

## Why this goal

Vendor lock-in is a credibility issue at scale. Even if v1.0 ships GitHub-only, the MCP layer must demonstrably support other backends — otherwise the "GitHub-native" positioning becomes a trap that limits TAM and conflicts with G5 (enterprise discipline accessible at any scale, including the enterprises that don't use GitHub).

## Holistic dimensions

- **Functionality**: BackendAdapter abstract class is stable across SemVer minor releases
- **Technology**: engine/core does not import from engine/adapters/github — verified by import-graph analysis
- **UX design**: agent's MCP-facing API does not change between adapters; only the engine cares which backend is wired
- **Monetization**: opens enterprise markets that mandate non-GitHub backends — removes a deal-breaker
- **Acquisition**: portability removes the "we don't use GitHub" objection up front
- **Offline experience**: adapter pattern allows local / private / air-gapped backends as future contributions
""",
    ),
]


# ============================================================================
# Capability bodies
# ============================================================================


@dataclass(frozen=True)
class CapSpec:
    code: str  # "C1"
    title: str
    primary_goal_code: str  # "G1"
    related_goal_codes: tuple[str, ...]  # ("G2", "G3")
    body: str


CAPABILITIES: list[CapSpec] = [
    CapSpec(
        code="C1",
        title="Maintain a typed, mechanically-enforced project graph",
        primary_goal_code="G1",
        related_goal_codes=("G2", "G3"),
        body="""## Map
- Children: features implementing the catalog, validators, MCP API, GitHub adapter (post-v0.3 decomposition)
- Related: G2 (typed graph prevents AI fabrication), G3 (mechanical rejections = defects caught early)

## Statement

Adopters maintain a graph of GitHub Issues where every node has a validated type, parent, status, and acting-role jurisdiction. The engine MCP rejects any operation that violates the catalog: a `goal` cannot have a `feature` as parent; a `vision` cannot be in status `proposed`; only the Architect can write an `adr`. Concepts GitHub already models first-class — bugs, releases, code inspections — ride on native objects (labels, Milestones + Releases, PR reviews), not on additional Issue Types.

## Parent goal

#G1 (sustained, maintainable product lifecycle) — the typed graph IS the living memory of the product

## Two implementations

(a) **Current**: 7 Issue Types + Projects v2 fields (Status, Related, Supersedes / Superseded by) + sub-issue native parent link + role:* labels via `gh` CLI + Projects v2 GraphQL.
(b) **Alternative considered**: generic graph database with similar schema constraints. *Rejected* — adds infra burden (DB hosting, auth, backups) and creates a parallel-source-of-truth problem against GitHub Issues.

## Value analysis

Prevents AI hallucination of impossible project states; enables maintainability over time (the catalog versioning travels with SemVer); supports scope-correctness at write (engine rejects → agent retries within constraints); supports defect catching early (parent-type / jurisdiction violations are immediate, not late).

## Risks

Schema evolution (catalog changes) requires migration discipline across adopters' graphs. Mitigated by catalog versioning + SemVer + machine-readable upgrade notes per release.

## Go / No-Go

Go — shipped in v0.3.0 (22 engine MCP tools, 295 tests passing).

## Holistic dimensions

- **Functionality**: 7 Issue Types + native bridges (bug label, Milestone, Release, PR review) + the per-type contract (parent / status / jurisdiction)
- **Technology**: engine/core/catalog.py (single source of truth) + validators + GitHubAdapter via `gh` CLI
- **UX design**: agents speak typed API via MCP; humans see typed Issues on GitHub's normal UI
- **Monetization**: enforcement = customer's AI agents cannot damage their plan, which is the value-bearing claim
- **Acquisition**: differentiator vs both chat-based tools (chaotic) and traditional planning tools (manual + no AI integration)
- **Offline experience**: validators run locally in the engine; enforcement does not require a central service

## Feature decomposition

Post-v0.3 work will decompose this capability into features: catalog v2 (new types?), Projects v2 Status field via GraphQL (replace label fallback), engine performance, more native bridges (Discussions? Wiki?).
""",
    ),
    CapSpec(
        code="C2",
        title="Operate AI agents that stay in their lane",
        primary_goal_code="G2",
        related_goal_codes=(),
        body="""## Map
- Children: features decomposing role identity, jurisdiction enforcement, reactive auto-invocation (post-v0.3)
- Related: C8 (holistic dimensions help scope-completeness); C10 (methodology layer shapes role behavior)

## Statement

Six role-homologous AI agents (Product Manager, Architect, Developer, QA, DevOps, Security Officer) operate with explicit jurisdiction over distinct node types and activities. Cross-role inputs follow the consult/handoff pattern (consult = subagent returns information, never authorship; handoff = new conversation, new role takes authorship). The engine attaches `acting_role` to every write and rejects writes that violate jurisdiction.

## Parent goal

#G2 (AI authoring is scope-correct and role-coherent)

## Two implementations

(a) **Current**: 6 agent.md identity files + framework SKILL.md jurisdiction map + `acting_role` enforced in engine.api on every write + reactive auto-invocation via 5 hooks.
(b) **Alternative considered**: one unified AI agent with prompted role-switching. *Rejected* — role bleed is invisible without mechanical enforcement; the agent rationalizes its own role transitions and authorship drifts silently.

## Value analysis

Roles prevent AI from authoring outside its scope. Humans can hand off cleanly via sessions. Jurisdiction is checkable mechanically (the role:* label on every Issue carries the audit trail).

## Risks

Rigid roles may not match every team's structure. Mitigated by framework being methodology-blind — orgs customize role behavior via methodology skills (C10) without changing the role-jurisdiction contract.

## Go / No-Go

Go — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 6 agent.md + framework SKILL + the 5 hooks invoking roles reactively at graph events
- **Technology**: `acting_role` is a structured argument on every engine write — not a guess from the agent's prompt
- **UX design**: human picks role at `claude --agent <role>` launch; the role's identity sticks for the conversation
- **Monetization**: role coherence sells to compliance / quality / security-conscious teams who reject chaotic AI tooling
- **Acquisition**: "AI agents that don't step on each other" is a clear differentiator message
- **Offline experience**: role identity loads from local `.claude/agents/*.md` files; no central role registry

## Feature decomposition

Future work: PostToolUse-on-transition spawning the next role via `claude --agent` subprocess; per-role permission scoping; role-aware Action examples.
""",
    ),
    CapSpec(
        code="C3",
        title="Sessions that survive role hand-offs and conversation boundaries",
        primary_goal_code="G1",
        related_goal_codes=("G4",),
        body="""## Map
- Children: features decomposing the session lifecycle (SessionStart hook semantics, /catch-up filters, Value chain post-done templates)
- Related: G4 (sessions reduce re-discovery cost across conversations)

## Statement

A session = a git branch `session/<YYYY-MM-DD>-<slug>` + a doc `sessions/<id>.md` + Issue comments at three lifecycle points (📍 in play / ✅ decision / 🏁 closed) on every affected Issue. Work spans multiple AI conversations and multiple human role-switches without losing context; the SessionStart hook re-hydrates new conversations from the session doc.

## Parent goal

#G1 (sessions are the lifecycle's memory mechanism)

## Two implementations

(a) **Current**: session/<id>.md doc + git branch + Issue comments + 3 slash commands (session-open, session-close, catch-up) + 2 lifecycle hooks (SessionStart, PreCompact).
(b) **Alternative considered**: stateful AI memory backend (vendor's persistent context). *Rejected* — creates vendor lock-in and is not portable across AI providers; the framework should not depend on a single AI vendor's memory feature.

## Value analysis

Enables long-running work without re-discovering context every time. Supports cross-role authorship (PM hands off to Architect via the same branch + updated Handoff). Captures post-done learning via the Value chain section, which is what makes the framework lifecycle-aware rather than ship-aware.

## Risks

Session discipline is human-driven (the Handoff section must be updated). Mitigated by PreCompact hook (refreshes Handoff before context compaction) and /session-close (forces a deliberate close moment).

## Go / No-Go

Go — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 3 slash commands + 5 lifecycle hooks + the session doc 3-part structure (Context / Decisions / Handoff)
- **Technology**: git branch + markdown doc + Issue comments — all GitHub-native, no parallel store
- **UX design**: SessionStart hook re-hydrates fresh conversations; PreCompact ensures Handoff is current before compression
- **Monetization**: continuity is the productivity claim — the customer's team does not start over every conversation
- **Acquisition**: differentiator vs stateless AI tools that lose context on every reset
- **Offline experience**: doc + branch + Issue thread = persistence without cloud; sessions survive a git pull

## Feature decomposition

Future: better /catch-up filters (per-role digest), automatic Handoff drafting from transcript, session linking across branches (epics).
""",
    ),
    CapSpec(
        code="C4",
        title="Catch structural and semantic defects in CI",
        primary_goal_code="G3",
        related_goal_codes=(),
        body="""## Map
- Children: features decomposing each semantic check (architect_coherence, pm_acceptance, security_review, artifacts_derive — and future ones)
- Related: C1 (typed graph rejects parent-type / status / jurisdiction violations mechanically); G7 (dogfood ensures we catch our own defects)

## Statement

Two layers of validation: structural CI (push-time, in GitHub Actions) checks the framework's contracts — catalog integrity, skill frontmatter, agent frontmatter, settings.json. Semantic CI (hook + PR-time, in-process or as Actions) inspects nodes for missing security sections, missing learning extraction, role-bleed, scope drift. Defects surface before merge, not after deployment.

## Parent goal

#G3 (structural defects caught early in the cycle)

## Two implementations

(a) **Current**: sem-ai-ci.yml (structural CI, 3 stages) + engine/checks/ Python library (4 semantic checks: architect_coherence, pm_acceptance, security_review, artifacts_derive) + 5 hooks invoking checks at graph events + planned Action examples for adopters who want Action-time checks too.
(b) **Alternative considered**: post-deployment monitoring + manual review. *Rejected* — too late; defects ripple by then. Catching at authoring is 10-100x cheaper.

## Value analysis

Defects caught at write time are exponentially cheaper to fix. Two-layer architecture means the same Python check runs both in-process (hook) and as a CI step (Action), without duplication.

## Risks

False positives erode trust. Mitigated by surfacing semantic findings as warn-level (do not block writes), letting agents and humans act on them deliberately.

## Go / No-Go

Go — shipped in v0.3.0 with 4 semantic checks. More checks will be added as the framework matures.

## Holistic dimensions

- **Functionality**: 4 semantic checks + 3 structural validators + 5 hooks invoking them at the right moment
- **Technology**: Python library runnable both from hooks (in-process) and Actions (CI) — same code path, two entry points
- **UX design**: developer sees findings inline in their Claude Code session at hook-time; PR reviewers see them at gate-time
- **Monetization**: less rework = customer time saved per cycle; "CI that thinks" sells to mature engineering orgs
- **Acquisition**: "CI catches things you'd otherwise ship" is concrete; can be demonstrated in a 5-minute video
- **Offline experience**: checks run locally during authoring + in CI; no SaaS dependency

## Feature decomposition

Future: per-role review agents invoked by checks (Architect agent for architect_coherence); checks for risk-surface coverage (do all 5 Holistic dimensions have content?); checks for value-chain coherence (post-done sections populated).
""",
    ),
    CapSpec(
        code="C5",
        title="Use GitHub as unified backend with no extra infrastructure",
        primary_goal_code="G6",
        related_goal_codes=("G5",),
        body="""## Map
- Children: features for the GitHub adapter, setup scripts, template-distribution polish
- Related: C6 (the adapter pattern keeps this from becoming lock-in); G5 (no extra infra = accessible at any scale)

## Statement

The system uses GitHub Issues + Projects v2 + Milestones + Releases + PR reviews as the project's storage, plan, release infrastructure, and inspection record. No separate database, no pip install, no cloud service for adopters to deploy or pay for. Distribution is via GitHub template ("Use this template") + 3-command setup (clone, setup-engine, setup-github-project).

## Parent goal

#G6 (external adoption — frictionless onboarding is the adoption hook)

## Two implementations

(a) **Current**: GitHub-native via `gh` CLI + Projects v2 GraphQL + GitHub template distribution.
(b) **Alternative considered**: standalone web app or cloud service. *Rejected* — requires hosting, auth, payments, support; orthogonal to the value proposition; adds substantial adoption friction without proportional benefit.

## Value analysis

Adopter already has GitHub (or can create a free account). SEM-AI piggybacks on infrastructure they already trust, already pay for (or get free), and already operate. The reduction in adoption friction is the primary mechanism by which G6 is achievable.

## Risks

GitHub vendor coupling. Mitigated by C6 — the adapter pattern means a future backend swap is contained to engine/adapters/.

## Go / No-Go

Go — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: Issues + Projects v2 + Milestones + Releases + PR reviews are the storage; native objects (no shadow DB)
- **Technology**: `gh` CLI adapter + GraphQL for Projects v2 fields (Status, Related, Supersedes, Superseded by)
- **UX design**: developer uses tools they already know (gh CLI, Issues page, PR review UI)
- **Monetization**: zero infrastructure cost reduces customer ROI threshold to near-zero — easier "yes"
- **Acquisition**: "no install, no DB, no cloud" is a strong onboarding pitch; the template + setup-script combination delivers it
- **Offline experience**: the graph lives on GitHub; adopters can also git-clone the entire repo (Issues are not in clone but everything else is) and operate offline against a cached graph

## Feature decomposition

Future: setup-github-project.sh should provision `type:*` and `status:*` labels (currently manual); Projects v2 Status field via GraphQL (currently label fallback); per-org template fork tracking for adoption metrics.
""",
    ),
    CapSpec(
        code="C6",
        title="Backend portability via adapter pattern + stable MCP contract",
        primary_goal_code="G8",
        related_goal_codes=(),
        body="""## Map
- Children: features for adapter contract evolution, MCP versioning, RFC process for community adapters
- Related: C5 (the GitHub adapter is the reference implementation that validates the abstraction)

## Statement

The engine speaks to its backend through a swappable adapter — `BackendAdapter` abstract base class with a closed interface (create_issue, update_issue, transition_status, set_related, link_commit, ...). Agents speak only to the MCP; the MCP routes through the active adapter. A non-GitHub adapter (Jira / Linear / GitLab / private backend) can be contributed without modifying `engine/core/` or any agent / skill code.

## Parent goal

#G8 (backend portability viable post-v1)

## Two implementations

(a) **Current**: `BackendAdapter` abstract base + `GitHubAdapter` concrete implementation; engine/core imports only the abstract type.
(b) **Alternative considered**: GitHub-only architecture with no abstraction. *Rejected* — vendor lock = adoption ceiling = conflicts with G5; also closes off the long-term TAM of enterprise / private-backend adopters.

## Value analysis

Enterprise adopters who cannot use GitHub (compliance, legal, on-prem) can use SEM-AI's MCP + their own adapter. The abstraction is also a constraint that keeps engine/core honest — code that violates the abstraction (importing from engine/adapters/github) is caught by code review.

## Risks

The abstraction has not been validated by a second concrete adapter yet — a real risk. Mitigated by the G8 acceptance criterion accepting either a stub adapter OR a community RFC.

## Go / No-Go

Go — shipped in v0.3.0 (abstract base + GitHub implementation).

## Holistic dimensions

- **Functionality**: BackendAdapter ABC with a closed method set + GitHubAdapter as the reference impl
- **Technology**: clean separation of engine/core (logic + types) from engine/adapters (I/O); enforced by code review (and could be enforced by import linting in CI)
- **UX design**: adapter swap is invisible to agents and skills — only the engine's MCP layer cares which backend is wired
- **Monetization**: opens non-GitHub markets without a rewrite; one codebase, multiple backends
- **Acquisition**: removes the "we don't use GitHub" deal-breaker objection
- **Offline experience**: future adapters can target local SQLite, private GitLab, air-gapped Jira — the abstraction allows it

## Feature decomposition

Future: community RFC process documented; stub Linear adapter as integration test; import-lint check in CI; MCP versioning policy (when the contract evolves).
""",
    ),
    CapSpec(
        code="C7",
        title="First-class experimentation lifecycle",
        primary_goal_code="G1",
        related_goal_codes=("G4",),
        body="""## Map
- Children: features for additional experiment sub-types, experiment-specific Value chain reading, label-coherence checks
- Related: G4 (Learning extracted post-done is the discovery → validation shift)

## Statement

Features distinguish explicitly between **delivery intent** (the feature pays off learning already accumulated; success = value chain completes) and **experiment intent** (the feature exists to resolve an uncertainty; success = Learning extracted). The engine MCP auto-applies the native label `experiment` when the feature template's `Uncertainty addressed` slot is populated (and removes it when the slot is cleared). The Value chain section is read differently per intent: delivery → Value assessment is primary; experiment → Learning extracted is primary. Expected final statuses differ by sub-type (prototype → deprecated; A/B → done; spike → usually deprecated; concierge → deprecated).

## Parent goal

#G1 (sustained lifecycle includes experimentation as a first-class workflow)

## Two implementations

(a) **Current**: `Uncertainty addressed` slot in feature template + engine auto-applies `experiment` label + ADR-006 (now Issue #7) codifies sub-type lifecycle expectations.
(b) **Alternative considered**: separate Issue Type for experiments (e.g. `experiment` as a type alongside `feature`). *Rejected* — catalog inflation; intent is per-feature, not per-type; the same feature can transition between intents as learning accumulates.

## Value analysis

Makes shipping prototypes, spikes, A/B tests, and concierge experiments a first-class workflow rather than improvised work. Forces honest assessment ("what was the uncertainty? did we resolve it?") at the moment of closing.

## Risks

Teams may not honestly distinguish intent (everything gets labelled delivery to feel productive). Mitigated by template's mandatory `Uncertainty addressed` slot — `N/A — delivery, not experiment` is itself a forced statement.

## Go / No-Go

Go — shipped in v0.3.0 (slot + label coherence + Value chain post-done sections).

## Holistic dimensions

- **Functionality**: 4 sub-types (prototype, spike, A/B, concierge) + label coherence + post-done Value chain reading per intent
- **Technology**: engine API maintains slot-label invariant (update_node enforces the coherence)
- **UX design**: PM sees experiments distinguished in Issue list / Projects v2 board / `gh issue list` at a glance via the `experiment` label
- **Monetization**: explicit experimentation lifecycle = mature product practice; sells to teams that take discovery seriously
- **Acquisition**: differentiator vs feature trackers that conflate delivery and experiment work
- **Offline experience**: intent encoded in the body slot, label persists locally on the Issue

## Feature decomposition

Future: per-sub-type templates (prototype-specific sections vs A/B-specific sections); auto-suggested status transitions by sub-type; experiment-specific dashboards.
""",
    ),
    CapSpec(
        code="C8",
        title="Multi-dimensional evaluation as structural risk surface",
        primary_goal_code="G2",
        related_goal_codes=("G3",),
        body="""## Map
- Children: features for dimension-specific checks, per-dimension coverage reports
- Related: C1 (templates are part of the typed graph); G3 (risk surfacing is defect-catching at planning time)

## Statement

The system includes five **Holistic Dimensions** — Technology, UX design, Monetization, Acquisition, Offline experience (with Functionality as the base) — as structured slots in vision / goal / capability / feature templates. Each slot is simultaneously a **design slot** (what does this node do in this dimension?) AND a **risk-surface slot** (what risk is absorbed if this dimension is silently omitted?). Silent omission = absorbed risk; marking N/A requires an explicit one-line reason. PMs cannot ship a node with a silently-missing dimension.

## Parent goal

#G2 (planning is scope-complete, not narrow)

## Two implementations

(a) **Current**: structured Holistic dimensions block in each spine template (per node-templates SKILL); reviewable at audit time.
(b) **Alternative considered**: separate "Risk register" document per node. *Rejected* — duplication; risks ARE unvalidated dimensions; the dimensions IS the risk surface.

## Value analysis

Prevents the "we forgot about acquisition" failure mode at the planning level. Makes risk visible structurally rather than in a separate doc nobody reads. Maps directly to the four canonical risk classes (value / usability / viability / business-viability) of the modern product approach.

## Risks

Template overhead may discourage filling — PMs write "N/A" reflexively. Mitigated by the requirement of a one-line reason (forces a moment of consideration) and by the post-done Value chain reading (a dimension marked N/A that later turns out load-bearing is visible as a learning).

## Go / No-Go

Go — shipped in v0.3.0 (templates ship with the dimensions block).

## Holistic dimensions

- **Functionality**: 5 dimensions + Functionality base in spine templates + risk class mapping (Monetization↔value risk · UX↔usability · Technology↔viability · Acquisition+Offline↔business viability)
- **Technology**: enforced via node-templates skill content (the template IS the contract); could be checkable via a future engine/check
- **UX design**: PM fills slots; any reader sees coverage at a glance
- **Monetization**: dimensional thinking catches monetization gaps that pure feature work misses
- **Acquisition**: same — catches acquisition / GTM gaps before launch, not after silence
- **Offline experience**: explicit slot forces explicit thinking about the off-screen / off-network path

## Feature decomposition

Future: dimension-coverage check in engine/checks (warn if a Holistic dimensions block has zero substantive content); per-dimension Projects v2 view (Risk surface view per dimension).
""",
    ),
    CapSpec(
        code="C9",
        title="Project intent evolves: bottom-up emergence + supersede chains",
        primary_goal_code="G1",
        related_goal_codes=("G4",),
        body="""## Map
- Children: features for anchor-pending tooling, supersede UI, evolution-aware queries
- Related: G4 (no rework loss; past attempts inform current decisions)

## Statement

The graph accommodates emergent project work: top-down construction (greenfield from vision), bottom-up creation with **anchor-pending** (a feature that emerged from user signals before its capability has crystallized), and in-place evolution via **supersede** chains (replace a decision while preserving history via the supersedes / superseded-by custom fields). Construction direction is the human manager's call, not a framework rule.

## Parent goal

#G1 (lifecycle dynamics — the product evolves; the graph supports it)

## Two implementations

(a) **Current**: anchor-pending pattern documented in node-templates + framework SKILL; supersedes/superseded-by custom fields available on every node type; engine.api.supersede enforces the link consistency.
(b) **Alternative considered**: strict top-down only (vision must crystallize before goals, goals before capabilities, etc.). *Rejected* — does not match real product work; bottom-up emergence is the normal way capabilities emerge from feature patterns and goals from capability patterns.

## Value analysis

The graph tracks discovery, not just upfront design. Decisions can evolve (supersede) without losing history; bottom-up observations can land in the graph immediately (anchor-pending) and be properly anchored later. This is what makes the lifecycle goal achievable rather than aspirational.

## Risks

Bottom-up nodes may stay orphaned if their parent never crystallizes. Mitigated by anchor-pending visibility (the Map section's `- Parent: anchor pending` line surfaces them at audit).

## Go / No-Go

Go — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 4 construction modes (top-down / bottom-up / mixed / anchor-pending) + supersede chains across all node types
- **Technology**: parent edge is mutable (update_node can re-parent); supersede fields are available at zero structural cost on every type
- **UX design**: PM can capture observations now, anchor properly later — the framework does not force premature crystallization
- **Monetization**: matches how real teams discover their product — adoption fit
- **Acquisition**: differentiator vs rigid top-down planning tools (Jira waterfall feel) and against ad-hoc bottom-up tools (no parent edge at all)
- **Offline experience**: anchor-pending notes are local body text; supersede chains are local custom-field values

## Feature decomposition

Future: anchor-pending dashboard (find all bottom-up nodes waiting for parent crystallization); supersede chain visualizer; deprecation propagation rules.
""",
    ),
    CapSpec(
        code="C10",
        title="Adopter-customizable methodology layer",
        primary_goal_code="G5",
        related_goal_codes=("G2",),
        body="""## Map
- Children: features for skill discovery, methodology pointer resolution, per-org skill packs
- Related: C2 (methodology shapes AI role behavior); G2 (methodology shapes scope-correct authoring)

## Statement

The framework ships **infrastructure** (catalog, MCP, hooks, role contracts, semantic CI library) but **no methodology** (no specific way to do value analysis, requirements discovery, story decomposition, security threat modelling). Adopters install `.claude/skills/<topic>/SKILL.md` files for their house style. Node templates carry `→ method:` pointers indicating where adopter methodology skills fill each section. Fixed layer (framework) + variable layer (project methodology) = customization without forking.

## Parent goal

#G5 (enterprise-grade discipline accessible at any scale)

## Two implementations

(a) **Current**: `→ method:` pointers in node-templates spine + Claude Code's skill listing mechanism + injectable `.claude/skills/` per project + CLAUDE.md documenting the fixed / variable layer split.
(b) **Alternative considered**: framework ships opinionated methodology defaults. *Rejected* — alienates teams with existing established practice; forces the framework into religious wars over methodology that have no canonical answer; conflicts with G5's enterprise-customization goal.

## Value analysis

Large orgs inject their enterprise methodology (specific value-analysis frameworks, security threat models, requirements templates) and the AI immediately uses them. Small teams use defaults from training. Both run on the same framework; updating the framework does not destroy methodology customization.

## Risks

Skill discovery / quality varies across orgs (the framework cannot validate adopter-supplied methodology). Out of framework scope by design — this is the adopter's responsibility.

## Go / No-Go

Go — shipped in v0.3.0 (template pointers + injection mechanism).

## Holistic dimensions

- **Functionality**: fixed layer + variable layer architecture + `→ method:` pointer convention
- **Technology**: skill listing via Claude Code's built-in skill discovery; no special infra
- **UX design**: agent invokes methodology skill at the `→ method:` pointer; falls back to training when no matching skill installed
- **Monetization**: large orgs can buy or develop methodology-skill packs (or community can publish OSS ones); same framework, different customer segments
- **Acquisition**: enterprises adopt because they can preserve their established practice; solo devs adopt because defaults work out of the box
- **Offline experience**: skills are local markdown files in the adopter's repo; no remote skill store

## Feature decomposition

Future: skill-pack discovery convention (where do community methodology packs live?); per-org methodology validation hooks; methodology-skill schema (frontmatter conventions).
""",
    ),
]


# ============================================================================
# Mapping helpers
# ============================================================================


def _by_code(items, code):
    for it in items:
        if it.code == code:
            return it
    raise KeyError(code)


# ============================================================================
# Main
# ============================================================================


def main() -> int:
    cfg = load_config()
    adapter = GitHubAdapter(cfg)

    print(f"Target repo: {cfg.repo}")
    print()

    # ----- Find vision #1 (must already exist) -----
    visions = adapter.query_issues(type=NodeType.VISION)
    if not visions:
        print("FAIL: no vision Issue found. Run migrate_to_issues.py first.")
        return 1
    vision = visions[0]
    print(f"==> Vision: {vision.id} ({vision.title!r})")
    print()

    # ----- Step 1: Goals (idempotent by title) -----
    print(f"==> Creating {len(GOALS)} goals as children of {vision.id}")
    existing_goals = adapter.query_issues(type=NodeType.GOAL)
    existing_goal_titles = {g.title: g for g in existing_goals}

    goal_id_by_code: dict[str, str] = {}
    for spec in GOALS:
        if spec.title in existing_goal_titles:
            node = existing_goal_titles[spec.title]
            print(f"    [exists] {spec.code} {spec.title!r} → {node.id}")
        else:
            print(f"    [..] {spec.code} {spec.title!r}", end=" ", flush=True)
            try:
                node = api.create_node(
                    adapter,
                    type=NodeType.GOAL,
                    parent_id=vision.id,
                    title=spec.title,
                    body=spec.body,
                    status=Status.ACTIVE,
                    acting_role=Role.PM,
                )
            except Exception as e:
                print(f"FAILED: {e}")
                return 1
            print(f"→ {node.id}")
        goal_id_by_code[spec.code] = node.id

    print()

    # ----- Step 2: Capabilities (idempotent by title) -----
    print(f"==> Creating {len(CAPABILITIES)} capabilities under their primary goal")
    existing_caps = adapter.query_issues(type=NodeType.CAPABILITY)
    existing_cap_titles = {c.title: c for c in existing_caps}

    cap_id_by_code: dict[str, str] = {}
    for spec in CAPABILITIES:
        parent_goal_id = goal_id_by_code[spec.primary_goal_code]
        if spec.title in existing_cap_titles:
            node = existing_cap_titles[spec.title]
            print(
                f"    [exists] {spec.code} → {node.id}  "
                f"(parent {spec.primary_goal_code}={parent_goal_id})"
            )
        else:
            print(
                f"    [..] {spec.code} {spec.title[:60]!r}  "
                f"(parent {spec.primary_goal_code}={parent_goal_id})",
                end=" ",
                flush=True,
            )
            try:
                node = api.create_node(
                    adapter,
                    type=NodeType.CAPABILITY,
                    parent_id=parent_goal_id,
                    title=spec.title,
                    body=spec.body,
                    status=Status.ACTIVE,
                    acting_role=Role.PM,
                )
            except Exception as e:
                print(f"FAILED: {e}")
                return 1
            print(f"→ {node.id}")
        cap_id_by_code[spec.code] = node.id

    print()

    # ----- Step 3: Related cross-axis links -----
    print("==> Applying cross-axis 'related' links")
    related_applied = 0
    for spec in CAPABILITIES:
        if not spec.related_goal_codes:
            continue
        cap_id = cap_id_by_code[spec.code]
        related_ids = tuple(
            goal_id_by_code[g] for g in spec.related_goal_codes
        )
        try:
            api.set_related(
                adapter,
                node_id=cap_id,
                related_ids=related_ids,
                acting_role=Role.PM,
            )
        except Exception as e:
            print(
                f"    [warn] could not set related on {cap_id}: {e}"
            )
            continue
        print(
            f"    {spec.code} {cap_id} → related: "
            f"{', '.join(spec.related_goal_codes)} "
            f"({', '.join(related_ids)})"
        )
        related_applied += 1

    print()
    print("==> Summary")
    print(f"    vision: {vision.id}")
    print(f"    goals created/kept: {len(goal_id_by_code)}")
    print(f"    capabilities created/kept: {len(cap_id_by_code)}")
    print(f"    related links applied: {related_applied}")
    print()
    print("Goal → Issue mapping:")
    for spec in GOALS:
        print(f"    {spec.code} = {goal_id_by_code[spec.code]}  {spec.title}")
    print()
    print("Capability → Issue mapping:")
    for spec in CAPABILITIES:
        print(
            f"    {spec.code} = {cap_id_by_code[spec.code]}  "
            f"(parent {spec.primary_goal_code}={goal_id_by_code[spec.primary_goal_code]})  "
            f"{spec.title}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
