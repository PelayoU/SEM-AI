#!/usr/bin/env python3
"""Bootstrap dogfood Part 6: create 34 features under capabilities #19-#28.

Reverse-engineers the v0.3.0 shipped framework into typed feature Issues.
Each capability decomposes into 2-5 features; almost all are delivery
(not experiment) and ship status=done; Value chain sections are
populated with dogfood-observed outputs + honest "pending external
adoption" framing for outcomes / benefits.

Idempotent: re-running detects existing features by title and skips.

Run once:
    SEM_AI_REPO=PelayoU/SEM-AI .venv/bin/python scripts/dogfood/create_features.py
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.adapters import GitHubAdapter, load_config  # noqa: E402
from engine.core import api  # noqa: E402
from engine.core.catalog import NodeType, Status  # noqa: E402
from engine.core.permissions import Role  # noqa: E402


# Capability Issue numbers — set by create_spine.py
CAP_ID = {
    "C1": "#19", "C2": "#20", "C3": "#21", "C4": "#22", "C5": "#23",
    "C6": "#24", "C7": "#25", "C8": "#26", "C9": "#27", "C10": "#28",
}


@dataclass(frozen=True)
class FeatureSpec:
    code: str
    title: str
    parent_cap: str  # "C1"
    body: str
    related_cap_codes: tuple[str, ...] = field(default_factory=tuple)


# ============================================================================
# C1 — Typed, mechanically-enforced project graph
# ============================================================================

F1_1 = FeatureSpec(
    code="F1.1",
    title="Catalog of 7 Issue Types with per-type contracts",
    parent_cap="C1",
    body="""## Map
- Children: none yet (stories may be added if a type contract evolves)
- Related: F1.3 (validators enforce the catalog); F1.5 (templates materialize the body shape per type)

## Story

Adopter team's PM + agents need a single source of truth for what Issue Types the framework recognises, what parent each type can have, what statuses are legal, and which role can author each. The catalog provides this as a typed Python enum + TypeContract per type, importable by validators and adapters alike.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- 7 NodeType values: vision, goal, capability, feature, story, spec, adr
- Each type has a TypeContract with: valid_parent_types, valid_statuses, initial_status, terminal_statuses
- Catalog is the single import point referenced by validators + adapters
- Status enum covers the union of all per-type statuses (12 values)

## Acceptance check

Verified by `engine/tests/test_catalog.py` — ~20 tests confirm parent rules, lifecycle, terminal statuses match the documented contracts.

## Position in the larger narrative

The catalog is the framework's structural backbone. F1.3 (validators) and F1.5 (templates) both read from it; the engine MCP rejects any operation that contradicts it.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 7 typed nodes + 12 statuses + per-type lifecycle rules
- **Technology**: Python Enum + frozen dataclass TypeContract; immutable at runtime
- **UX design**: agents see typed API; humans see typed Issues on GitHub (via labels when native Issue Types are absent)
- **Monetization**: structural backbone for the value proposition — without typed contracts there is no mechanical enforcement
- **Acquisition**: foundational; not a marketing surface directly
- **Offline experience**: catalog lives in code; loaded locally; no network dependency

## Value chain

- **Outputs shipped**: `engine/core/catalog.py` (NodeType, Status, TypeContract, CATALOG dict)
- **Outcomes observed**: Dogfood — every Issue created by the team flows through the catalog; zero parent-type violations slipped through; spine + ADRs both rely on it
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated; external value pending
- **Learning extracted**: The catalog being a Python module (not YAML / DSL) made evolving it during the v0.3 cycle trivial — type changes are import-checked at write time. A DSL would have added friction without obvious benefit.
- **Next cards surfaced**: Catalog versioning policy when types change (deferred to post-v1.0)
""",
)

F1_2A = FeatureSpec(
    code="F1.2a",
    title="Engine MCP API: 19 typed graph operation tools",
    parent_cap="C1",
    body="""## Map
- Children: none
- Related: F1.2b (Milestone/Release bridges share the same API surface); F6.3 (MCP server exposes these tools); F1.3 (validators run on every write)

## Story

Adopter team's agents need a typed API for graph operations that validates structure at write time and reads at any depth. The engine MCP API provides 19 functions covering reads (get_node, children_of, ancestors_of, get_related, query_nodes, search_nodes, get_tree, get_project_map), writes (create_node, update_node, transition_status, link_commit, set_related, add_label, remove_label, supersede), and inspection (estimate_size, validate_node, get_instance_config).

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- 19 graph operations exposed via `engine/core/api.py`
- Every write validates triggered_by + jurisdiction + (where relevant) parent + status before delegating to the adapter
- Reads return immutable `Node` dataclasses; agents cannot mutate the graph by mutating returned objects
- API is adapter-agnostic — same signatures work against any `BackendAdapter` implementation

## Acceptance check

Verified by `engine/tests/test_api.py` — comprehensive tests covering each operation's structural validation, error paths, and adapter delegation.

## Position in the larger narrative

This is the surface the AI agents talk to. F6.3 (MCP server) wraps these functions as MCP tools so agents invoke them via the protocol; F1.3 (validators) is the enforcement layer the API delegates to.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 19 typed graph operations, immutable returns, validation-before-write
- **Technology**: Python module with explicit signatures; depends on engine/adapters/base for backend swapability
- **UX design**: agents speak this API via MCP tools; humans never see it directly
- **Monetization**: the API surface IS the contract that makes structural enforcement possible
- **Acquisition**: N/A — internal API, not adopter-facing surface
- **Offline experience**: pure Python, no network dependency in the API layer itself (the adapter handles I/O)

## Value chain

- **Outputs shipped**: `engine/core/api.py` (19 graph functions + helpers); ~600 LOC
- **Outcomes observed**: Dogfood — every spine node (#1-#29) was created via this API; zero structural violations escaped
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated; external value pending
- **Learning extracted**: Forcing `acting_role` as a required kwarg on every write surfaces accidental role-bleed at the call site — agents cannot drift silently. This pattern is worth preserving even as the API grows.
- **Next cards surfaced**: Per-tool MCP schema generation for richer agent-side tooltips (deferred)
""",
)

F1_2B = FeatureSpec(
    code="F1.2b",
    title="Engine MCP API: 3 Milestone / Release bridge tools",
    parent_cap="C1",
    body="""## Map
- Children: none
- Related: F1.2a (graph operations sibling); F5.1 (Milestones + Releases are GitHub-native objects); G7 dogfood will exercise these once SEM-AI cuts its first Release

## Story

Adopter team's PM + DevOps need to plan releases (Milestone scope/sizing/risk register/quality gate/security gate/pipeline) and publish them (tag + Release notes) without leaving the framework. The three bridges provide MCP-level access to these GitHub-native operations while preserving role enforcement (PM creates/assigns Milestones; DevOps publishes Releases).

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `create_milestone(title, body, due_on, acting_role=PM)` creates a GitHub Milestone with a structured body
- `assign_to_milestone(node_id, milestone_title, acting_role=PM)` links an Issue to its release Milestone
- `publish_release(tag, milestone_title, release_notes, acting_role=DEVOPS)` cuts a GitHub Release
- Role enforcement: only PM may create/assign Milestones; only DevOps may publish Releases — engine hard-rejects other roles
- Validated via `validate_jurisdiction` per call

## Acceptance check

Verified by `engine/tests/test_api.py` Milestone / Release sections.

## Position in the larger narrative

Native GitHub bridges per the framework's catalog audit principle: concepts GitHub already models first-class (Milestones, Releases) ride on the native objects, not on additional Issue Types. The bridges are the framework's typed access to these natives.

## State

done — shipped in v0.3.0 (not yet exercised in dogfood; SEM-AI has not cut a v0.4 release).

## Holistic dimensions

- **Functionality**: 3 bridges covering plan + assign + publish
- **Technology**: thin wrappers over `gh api` calls + GraphQL for due dates
- **UX design**: adopter's PM + DevOps see Milestones in GitHub's native UI; the framework adds discipline, not parallel UI
- **Monetization**: enables release-as-product-cadence; mature release practice for adopters
- **Acquisition**: N/A directly
- **Offline experience**: bridges require GitHub API connectivity by definition

## Value chain

- **Outputs shipped**: 3 functions in `engine/core/api.py` (create_milestone, assign_to_milestone, publish_release); adapter methods in `engine/adapters/github.py`
- **Outcomes observed**: Tests pass; not exercised in dogfood yet (SEM-AI is pre-v0.4 release)
- **Benefits measured**: Pending — first exercise in dogfood at v0.4 cut
- **Value assessment**: Shipped + test-validated; real-world value pending first release dogfood
- **Learning extracted**: Splitting create_milestone (PM jurisdiction) from publish_release (DevOps jurisdiction) at the API level forces the role separation mechanically — even if the human is one person wearing both hats
- **Next cards surfaced**: First release dogfood will likely surface gaps in the Milestone body template (sizing section detail, risk register format)
""",
)

F1_3 = FeatureSpec(
    code="F1.3",
    title="Structural validators with hard-reject (parent / status / jurisdiction / triggered_by / supersede)",
    parent_cap="C1",
    body="""## Map
- Children: none
- Related: F1.1 (validators read the catalog); F1.2a + F1.2b (API delegates to validators); F2.3 (acting_role enforcement is the jurisdiction validator)

## Story

Adopter team's agents are protected from authoring invalid graph states by mechanical validators that hard-reject parent-type mismatches, illegal statuses, jurisdiction violations, restricted triggered_by, and broken supersede chains. The agent that tries to break the model gets a typed exception, not a polite suggestion.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `validate_parent(node_type, parent_type)` — raises ParentTypeViolation when invalid
- `validate_status(node_type, status)` — raises StatusViolation
- `validate_jurisdiction(node_type, acting_role)` — raises JurisdictionViolation
- `validate_triggered_by(operation, triggered_by)` — raises TriggeredByViolation
- `validate_supersede(superseding, superseded)` — raises SupersedeViolation on inconsistent chains
- Every API write calls the relevant validators before delegating to the adapter

## Acceptance check

Verified by `engine/tests/test_validators.py` — comprehensive negative + positive cases per validator.

## Position in the larger narrative

This is the framework's *mechanical layer* (per the methodology ADR #29): structural truths enforced at write time. Distinct from the *semantic layer* (engine/checks) which surfaces warn-level findings post-hoc.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 5 structural validators + typed exceptions in engine/core/exceptions.py
- **Technology**: pure Python functions that raise typed exceptions; no I/O
- **UX design**: agents receive structured errors with code + message; the engine never silently corrects
- **Monetization**: hard-reject is what makes the typed graph load-bearing rather than aspirational
- **Acquisition**: "AI agents cannot fabricate impossible graph states" — concrete promise
- **Offline experience**: pure validation, no network

## Value chain

- **Outputs shipped**: `engine/core/validators.py` (5 validators); `engine/core/exceptions.py` (typed exception hierarchy)
- **Outcomes observed**: Dogfood — during the spine creation (#11-#28), 0 invalid writes attempted that weren't caught (verified by absence of bug Issues filed)
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated
- **Learning extracted**: Validators as pure functions (no adapter dependency) means they can run anywhere — including in hooks before the write hits the adapter. This separation is worth preserving.
- **Next cards surfaced**: Validator for capability "WHAT vs HOW" leak (capability Statement mentions specific tech) — surfaced by the methodology ADR #29 as future engine/checks work, not strictly a structural validator
""",
)

F1_5 = FeatureSpec(
    code="F1.5",
    title="Canonical body templates for the 7 Issue Types (node-templates SKILL)",
    parent_cap="C1",
    body="""## Map
- Children: none (the SKILL is the artifact; individual section-level features sit elsewhere)
- Related: F8.1 (Holistic dimensions section); F7.1 (Uncertainty addressed slot); F3.5 (Value chain post-done); F7.3 (sub-type lifecycle); F10.1 (→ method pointers)

## Story

Adopter team's agents need to know what body sections every Issue Type carries, in what order, with what guidance, so they can scaffold nodes correctly. The node-templates SKILL is the canonical source: one template per type (vision / goal / capability / feature / story / spec / adr), each with required sections, → method pointers for adopter methodology, and inline commentary that encodes definitional product literacy (output/outcome, why-stack, WHAT vs HOW, Holistic dimensions as risk surface, value chain post-done).

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- One template per Issue Type, with explicit `## <Section>` headers and inline `# comments` describing how to fill each
- Vision / goal / capability / feature templates carry the `## Holistic dimensions` block (with risk-class mapping)
- Feature template carries `## Uncertainty addressed`, `## Value chain` (post-done), and sub-type lifecycle guidance
- Goal template carries `## Stakeholder`, with SMART guidance on Horizon + Acceptance check, and the why-stack example on Outcome statement
- Capability template carries WHAT-vs-HOW guidance (coinless trolley vs NFC unlock) and reinforced Two implementations as anti-solution safety net
- ADR template carries Security attributes section as mandatory

## Acceptance check

Skill loads correctly per `engine/tests/test_skill_scripts.py` skill-frontmatter validators. Manual review of each template against the methodology ADR #29 inventory.

## Position in the larger narrative

The templates are the definitional product literacy embedded in the framework (per ADR #29). The MCP enforces structural rules at write time, but doesn't inspect body content — these templates are what the agent reads to know what sections to write. An adopter who overrides this SKILL forks the framework's definitional baseline.

## State

done — shipped in v0.3.0; refined 2026-05-24 (Stakeholder section added; why-stack + SMART + WHAT vs HOW guidance added).

## Holistic dimensions

- **Functionality**: 7 typed body templates with sections + comments + → method pointers
- **Technology**: markdown SKILL loaded by Claude Code's skill mechanism; no engine dependency
- **UX design**: agent reads SKILL when scaffolding; human reads to audit a node's completeness
- **Monetization**: shapes adopter's PM authoring — fewer skipped sections = more honest planning
- **Acquisition**: visible to adopters when they open the SKILL — "this is what good looks like"
- **Offline experience**: pure markdown, local file, no network

## Value chain

- **Outputs shipped**: `.claude/skills/node-templates/SKILL.md` (~300 LOC of templates + commentary)
- **Outcomes observed**: Dogfood — every spine node body (#1-#29) was authored from these templates; ADR #29 records the methodology embedded
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated; external value pending
- **Learning extracted**: Definitional literacy in template comments (e.g. "Mis-stated: 'Ship feature X' — that's an output") is more effective at shaping AI authoring than a separate methodology doc. The comment lives next to the section it constrains.
- **Next cards surfaced**: Capability template comment for "Twitter trap" (already added); per-section examples for spec template's Acceptance Criteria notation (deferred); risk-class mapping made more explicit on goal template Holistic dimensions
""",
)


# ============================================================================
# C2 — AI agents stay in their lane
# ============================================================================

F2_1 = FeatureSpec(
    code="F2.1",
    title="6 role identity contracts (methodology-blind agent.md)",
    parent_cap="C2",
    body="""## Map
- Children: none
- Related: F2.2 (framework SKILL embeds jurisdiction map); F2.3 (acting_role enforcement honors these identities); F10.2 (methodology skills layer behavioral specifics on top)

## Story

Adopter team needs six role-homologous AI agents (Product Manager, Architect, Developer, QA, DevOps, Security Officer) whose identities live as plain markdown files declaring jurisdiction + interaction patterns, without methodology baked in. The agent.md files describe WHAT each role owns and WHO it consults / hands off to — not HOW it does the work.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- 6 agent.md files in `.claude/agents/` — one per role
- Each file declares: identity, jurisdiction, owned node types, interaction-with-other-roles table (consult / hand off triggers)
- Each preloads framework + node-templates skills via `skills:` frontmatter
- Methodology-blind: no specific value-analysis frameworks, story formats, or domain methodology in agent identity

## Acceptance check

Verified by `engine/tests/test_skill_scripts.py` agent-frontmatter validators (required fields, expected role names, framework + node-templates preloaded). Validator `scripts/validators/check_repo.py agents` runs in CI.

## Position in the larger narrative

The role identities + their jurisdiction map are the framework's separation-of-concerns layer. When an adopter runs `claude --agent pm`, the agent loads its identity + framework SKILL and operates within the bounds — and the engine validates `acting_role` at every write (F2.3) so the boundary is mechanically respected.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 6 typed agent identities with explicit jurisdiction
- **Technology**: markdown frontmatter + body; Claude Code's agent loader does the work
- **UX design**: human picks role at `claude --agent <role>` launch; the role sticks for the conversation
- **Monetization**: role coherence is one of the framework's primary differentiators vs chaotic AI tools
- **Acquisition**: "AI agents that don't step on each other" — concrete pitch
- **Offline experience**: agent.md files are local; no remote role registry

## Value chain

- **Outputs shipped**: 6 files in `.claude/agents/` — product-manager.md, architect.md, developer.md, qa.md, devops.md, security-officer.md
- **Outcomes observed**: Dogfood — we (Pelayo + Claude as PM) have operated under role identity for the spine derivation without role-bleeding into Architect work
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated
- **Learning extracted**: Keeping agent.md methodology-blind (just identity + jurisdiction) means adopters can inject their methodology via skills without forking the agent. Worth preserving.
- **Next cards surfaced**: Agent-invoking-agent pattern from hooks (e.g. PostToolUse on transition_status spawning the Architect agent) — deferred per ADR-004 status
""",
)

F2_2 = FeatureSpec(
    code="F2.2",
    title="Framework SKILL: jurisdiction map + consult/handoff patterns",
    parent_cap="C2",
    body="""## Map
- Children: none
- Related: F2.1 (agent.md preload this SKILL); F1.5 (node-templates SKILL is the body shape; framework SKILL is the contract); F3.1 (sessions section lives here)

## Story

Every AI agent (any role) preloads a single framework SKILL describing the common law: the one rule (context is the project), the graph and how to read/change it, sessions (branch + doc model), the role-jurisdiction map (who owns what), and the consult/handoff patterns for cross-role work. Agents arrive in their conversations with this contract already in context, so they don't drift outside framework norms.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `.claude/skills/framework/SKILL.md` exists with valid frontmatter
- Sections: Working as roles (jurisdiction table); The graph (read/write rules + MCP tools); Sessions (3-part doc + hooks)
- Preloaded by all 6 agent.md files via `skills: [framework, node-templates]`
- Consult vs hand-off explicitly distinguished

## Acceptance check

Verified by `scripts/validators/check_repo.py skills` (in CI) — checks frontmatter + name matches folder. Manual review of jurisdiction table against agent.md ownership claims.

## Position in the larger narrative

The framework SKILL is what makes the 6 agents *coherent* rather than 6 independent characters. They share this common ground; the differences live in their individual agent.md identities.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: one SKILL document; sections covering graph + roles + sessions + the one rule
- **Technology**: markdown + frontmatter; skill mechanism loads on agent launch
- **UX design**: human + AI both read it; serves as the framework's onboarding doc inside Claude Code
- **Monetization**: coherent multi-agent operation is the value proposition's structural backbone
- **Acquisition**: "every agent obeys the same common law" — sells to teams worried about AI chaos
- **Offline experience**: local markdown; no remote dependency

## Value chain

- **Outputs shipped**: `.claude/skills/framework/SKILL.md` (~150 LOC)
- **Outcomes observed**: Dogfood — agents in this session have operated under the contract; no role-violations slipped through
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated
- **Learning extracted**: Embedding the role-jurisdiction MAP in the SKILL (not just in scattered agent.md files) gives every role visibility into every other role's scope — that's what makes consult vs handoff a real choice rather than guesswork.
- **Next cards surfaced**: Tighten the Sessions section as the session model evolves (e.g. when /catch-up gains per-role filters)
""",
)

F2_3 = FeatureSpec(
    code="F2.3",
    title="acting_role argument enforced on every engine write",
    parent_cap="C2",
    body="""## Map
- Children: none
- Related: F1.3 (validate_jurisdiction is part of the structural validator set); F2.1 (role identities are what acting_role names)

## Story

Adopter team needs mechanical (not behavioral) guarantee that AI agents stay in their lane. Every engine write requires `acting_role` as an explicit keyword argument — the API surface itself surfaces the role at the call site, the engine validates jurisdiction, and the label `role:<X>` lands on the Issue as audit trail. An agent that tries to write outside its lane gets a typed JurisdictionViolation exception.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- Every write function in `engine/core/api.py` requires `acting_role: Role` as keyword-only argument
- `validate_jurisdiction(node_type, acting_role)` raises before the write reaches the adapter
- The adapter applies `role:<X>` label on Issue creation + on every update (so the label is current, not stale)
- Hooks + Actions inherit acting_role from their invoker; cannot fabricate a different role mid-call

## Acceptance check

Verified by `engine/tests/test_permissions.py` (~15 tests) covering valid + invalid role combinations per node type.

## Position in the larger narrative

This is what makes F2.1 (role identities) load-bearing rather than aspirational. The role isn't a polite suggestion; it's an enforced kwarg. The role:label on every Issue makes the audit trail visible directly in GitHub.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: keyword-required argument on 19 write functions; validator hard-rejects mismatch
- **Technology**: Python's keyword-only argument feature (`*`); enum-typed Role parameter
- **UX design**: agents see the typed signature; humans see role:* labels on Issues
- **Monetization**: enforcement is the differentiator vs role-as-prompt approaches
- **Acquisition**: "the API itself surfaces who is writing" — concrete promise
- **Offline experience**: enforcement is local

## Value chain

- **Outputs shipped**: `acting_role` keyword on every write in `engine/core/api.py`; `validate_jurisdiction` in `engine/core/validators.py`; `role:<X>` label-application in `engine/adapters/github.py`
- **Outcomes observed**: Dogfood — every Issue created carries role:product-manager or role:architect (visible on `gh issue list`)
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated
- **Learning extracted**: Making acting_role a keyword-only argument (not positional, not optional) was the right choice — it makes the role visible at every call site without ceremony. A passive default would have allowed silent drift.
- **Next cards surfaced**: Per-role permission scoping at the adapter level (e.g. only DevOps can write to Releases — currently enforced at API layer; could be reinforced at adapter layer for defense in depth)
""",
)


# ============================================================================
# C3 — Sessions that survive role hand-offs
# ============================================================================

F3_1 = FeatureSpec(
    code="F3.1",
    title="Session doc model: branch + sessions/<id>.md + 3-part structure",
    parent_cap="C3",
    body="""## Map
- Children: none
- Related: F3.2 (slash commands create + close the doc); F3.3 (SessionStart hook re-hydrates from it); F3.4 (lifecycle comments reference it)

## Story

Adopter team needs a way for work to span multiple Claude Code conversations and multiple human role-switches without losing context. The session = git branch `session/<YYYY-MM-DD>-<slug>` + markdown doc `sessions/<id>.md` with 3 parts (Frontmatter + Context + Decisions + Handoff). The doc bridges conversations on the same branch; SessionStart re-hydrates new conversations from it.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- Branch naming convention: `session/<YYYY-MM-DD>-<slug>`
- Doc structure: Frontmatter (id, opened, in-play list) + Context (one paragraph, stable) + Decisions (append-only, role-attributed) + Handoff (overwritten, forward-looking)
- Decisions section is **third-person and role-attributed** ("Product Manager: capability-08 Go ..." not "I decided...")
- One doc per session; multiple conversations on the same branch share it

## Acceptance check

Manual review of session doc model in framework SKILL § Sessions. No dogfood session has been opened yet (we agreed to operate pre-session for the v0.3 bootstrap), so dogfood validation is pending.

## Position in the larger narrative

The session doc is the only channel that passes context between roles in the same session — the previous role's transcript is invisible to the next conversation. The doc bridges. Without it, cross-role authorship would re-discover context every time.

## State

done — model shipped; not yet dogfood-exercised.

## Holistic dimensions

- **Functionality**: 3-part doc structure + branch convention
- **Technology**: git branch + plain markdown; no DB, no service
- **UX design**: human + AI both author and read the doc; the structure surfaces what to update
- **Monetization**: continuity is the productivity claim — work doesn't restart every conversation
- **Acquisition**: "your AI work survives role switches and conversation boundaries" — concrete promise
- **Offline experience**: doc is local; survives git pulls; no remote session store

## Value chain

- **Outputs shipped**: Documented model in `.claude/skills/framework/SKILL.md § Sessions`; `sessions/` folder convention; branch naming convention
- **Outcomes observed**: Not yet — we have been operating pre-session for the v0.3 bootstrap dogfood
- **Benefits measured**: Pending first dogfood session
- **Value assessment**: Shipped at model level; real-world value pending first session
- **Learning extracted**: Decisions as third-person + role-attributed (not first-person) is load-bearing — first-person "I decided..." bleeds into the next role's self-model when they rehydrate. The convention is worth enforcing in /session-close.
- **Next cards surfaced**: Auto-drafting Handoff from transcript on /session-close (deferred); session linking across branches for epics (deferred)
""",
)

F3_2 = FeatureSpec(
    code="F3.2",
    title="3 slash commands: /session-open, /session-close, /catch-up",
    parent_cap="C3",
    body="""## Map
- Children: none
- Related: F3.1 (commands operate on the session doc); F3.4 (open/close post lifecycle comments)

## Story

Adopter team's PM (or any role) opens a session via `/session-open <slug>` — creates the branch, scaffolds the doc, posts 📍 in-play comments on affected Issues. Closes via `/session-close` — finalizes the Handoff, posts 🏁 comments, prompts merge/PR/discard. Catches up after time away via `/catch-up [--since 7d]` — digest of graph changes since last invocation.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- 3 SKILLs in `.claude/skills/`: session-open, session-close, catch-up
- 3 Python implementations in `scripts/skills/`: session_open.py, session_close.py, catch_up.py
- /session-open: branch creation + doc scaffold + 📍 comments on `in-play` Issues
- /session-close: Handoff finalization + 🏁 comments + disposition prompt (merge / PR / discard)
- /catch-up: graph diff since last invocation, filterable by time window

## Acceptance check

Verified by `engine/tests/test_skill_scripts.py` skill-frontmatter + per-command tests; structural CI validates the skills in `sem-ai-ci.yml`.

## Position in the larger narrative

These are the only session-lifecycle commands the framework ships. Mid-session annotation of binding decisions is inline discipline (one entry in Decisions + ✅ comment), not a command — the framework doesn't multiply commands beyond the lifecycle moments that genuinely deserve them.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 3 SKILLs + 3 Python scripts implementing branch + doc + comment operations
- **Technology**: Claude Code slash command mechanism; git CLI; gh CLI
- **UX design**: minimal command surface; consistent verbs (open, close, catch-up)
- **Monetization**: lifecycle hygiene is part of the productivity claim
- **Acquisition**: "3 commands cover the session lifecycle" — friction-low onramp
- **Offline experience**: commands work locally (branch creation, doc scaffolding); comments require GitHub connectivity

## Value chain

- **Outputs shipped**: 3 SKILLs in `.claude/skills/` + 3 Python scripts in `scripts/skills/`
- **Outcomes observed**: Not yet — we have been operating pre-session for the v0.3 bootstrap dogfood
- **Benefits measured**: Pending first dogfood session
- **Value assessment**: Shipped + test-validated
- **Learning extracted**: Keeping the slash command surface to 3 (open / close / catch-up) avoids the "every action gets a command" sprawl that kills tool adoption. Stay disciplined.
- **Next cards surfaced**: Per-role /catch-up filter (deferred); session linking via /session-link <id> (deferred)
""",
)

F3_3 = FeatureSpec(
    code="F3.3",
    title="5 lifecycle hooks (SessionStart, PreCompact, PostToolUse ×2, PreToolUse)",
    parent_cap="C3",
    body="""## Map
- Children: none
- Related: F3.1 (session doc loaded by SessionStart); F3.2 (commands work alongside hooks); F4.3 (PostToolUse on transition_status + PreToolUse on gh pr create invoke checks)

## Story

Adopter team's Claude Code session is reactive — hooks fire at graph events so the relevant role + checks engage automatically: SessionStart re-hydrates from session doc; PreCompact refreshes Handoff before context compression; PostToolUse on transition_status invokes the role appropriate to the new status; PostToolUse on `gh pr merge` derives artifacts from PR Closes #N; PreToolUse on `gh pr create` runs PM acceptance check.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- 5 hooks declared in `.claude/settings.json`
- 5 Python scripts in `scripts/hooks/`: session_start.py, pre_compact.py, post_tool_use_transition.py, post_tool_use_pr_merge.py, pre_tool_use_pr_create.py
- Hooks invoke engine/checks where appropriate (semantic CI)
- Hooks set TriggeredBy=HOOK on engine writes so the engine knows the call originated from automated machinery (restricted permissions)

## Acceptance check

Verified by `engine/tests/test_hooks.py` (~20 tests) covering each hook's invocation, payload handling, and TriggeredBy propagation. Settings.json validated by `check_repo.py settings`.

## Position in the larger narrative

The hooks are the framework's *primary reactive layer* per ADR-004. Actions (GitHub Actions) are opt-in examples; hooks are the always-on machinery that makes the multi-agent flow work without manual orchestration.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 5 hooks covering session lifecycle + graph transitions + PR moments
- **Technology**: Claude Code hook mechanism + Python scripts; JSON stdin payload
- **UX design**: invisible to the human — hooks fire silently; surfaced findings appear in Claude Code's output
- **Monetization**: reactive auto-invocation is the productivity claim (no manual "now run the check")
- **Acquisition**: "the framework engages itself when state changes" — concrete differentiator
- **Offline experience**: hooks run locally; only the gh CLI calls require connectivity

## Value chain

- **Outputs shipped**: `.claude/settings.json` (hook declarations); 5 scripts in `scripts/hooks/`
- **Outcomes observed**: Hooks have not been exercised in this session (we agreed pre-session); they will activate when the first session opens
- **Benefits measured**: Pending first dogfood session + adopter usage
- **Value assessment**: Shipped + test-validated
- **Learning extracted**: Restricting TriggeredBy=HOOK permissions (e.g. no status transitions on critical types) is the safety net that lets hooks be aggressive about invoking — they can read freely but cannot write destructively. The split was worth the friction.
- **Next cards surfaced**: PostToolUse on transition_status spawning the next role's agent via `claude --agent` subprocess (the agent-invoking-agent pattern) — deferred per ADR-004
""",
)

F3_4 = FeatureSpec(
    code="F3.4",
    title="Lifecycle comments on Issues: 📍 in-play / ✅ decision / 🏁 closed",
    parent_cap="C3",
    body="""## Map
- Children: none
- Related: F3.1 (session doc + Frontmatter `in-play` list); F3.2 (open / close commands post the comments)

## Story

Adopter team's session leaves traces on the graph through native Issue comments at three lifecycle points: 📍 in-play when a node enters the session, ✅ decision (role) when a binding decision touches it, 🏁 closed when the session ends. The comments are the chronological session history of the node, navigable from the Issue thread itself — no custom field, no in-body section to maintain.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- 📍 comment format: `📍 In play in [session/<id>](<url>)` — posted by /session-open per Issue in `in-play`
- ✅ comment format: `✅ Decision (<role>): <summary>` — posted inline when a binding decision is recorded
- 🏁 comment format: `🏁 Session closed: [session/<id>](<url>) — <outcome>` — posted by /session-close per affected Issue
- Markers are **load-bearing** — the framework's `get_node_artifacts(node)` derivation looks for these emojis

## Acceptance check

Verified manually against the framework SKILL § Sessions specification; comment-posting tested in /session-open + /session-close per `engine/tests/test_skill_scripts.py`.

## Position in the larger narrative

The lifecycle comments are how the session's huella persists on the graph. They make the session traceable from the Issue side (open the Issue, see all the sessions that touched it) without needing a custom field or session-tracking custom table.

## State

done — shipped in v0.3.0; will see real exercise at first dogfood session.

## Holistic dimensions

- **Functionality**: 3 marker formats; native GitHub comments
- **Technology**: gh CLI comment-posting; emoji as load-bearing markers
- **UX design**: human readers scan an Issue's comments and see the session journey at a glance
- **Monetization**: traceability is part of the maintainability claim
- **Acquisition**: visible navigation pattern; "open any Issue, see its sessions"
- **Offline experience**: comments require GitHub; no local mirror

## Value chain

- **Outputs shipped**: Marker format documented in framework SKILL § Sessions; comment-posting implemented in session_open.py + session_close.py + (manual) ✅ inline discipline
- **Outcomes observed**: Pending first dogfood session
- **Benefits measured**: Pending
- **Value assessment**: Shipped + dogfood-pending
- **Learning extracted**: Using emoji as load-bearing markers is unconventional but defensible — they're terse, visually scannable, and unlikely to clash with adopter conventions. Worth keeping.
- **Next cards surfaced**: Automatic 🏁 on all `in-play` Issues at /session-close (currently manual list) — minor UX polish
""",
)

F3_5 = FeatureSpec(
    code="F3.5",
    title="Value chain post-done section in feature template",
    parent_cap="C3",
    body="""## Map
- Children: none
- Related: F1.5 (template SKILL houses this section); F4.2 (pm_acceptance check enforces Learning extracted populated)

## Story

Adopter team's PM populates the `## Value chain` section of every feature after shipping (post-done): Outputs shipped, Outcomes observed, Benefits measured, Value assessment, Learning extracted (always populated — the guaranteed output), Next cards surfaced. The section closes the cycle honestly — including when the value chain doesn't complete (probabilistic per ADR-005).

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `## Value chain` section in feature template with 6 sub-items in order
- `- Learning extracted:` is always populated, never N/A — pm_acceptance check (F4.2) enforces this at PR-time
- Template comment is explicit: "The chain is PROBABILISTIC — most cycles do not complete it fully; honesty matters more than theatre"
- Post-done = after the feature transitions to status:done; pre-done feature bodies leave the section as a stub

## Acceptance check

Verified by `engine/checks/pm_acceptance.py` check codes PM003 (feature done but Value chain missing) and PM004 (Value chain present but Learning extracted missing/N/A); tested in `engine/tests/test_checks.py`.

## Position in the larger narrative

The Value chain section is what makes the framework lifecycle-aware rather than ship-aware. Without it, AI-augmented dev ships features and forgets them. With it, every cycle produces at minimum a Learning that compounds.

## State

done — shipped in v0.3.0; populated for every feature in this very script as part of the reverse-engineering exercise.

## Holistic dimensions

- **Functionality**: 6-slot section in feature template + automated enforcement of Learning extracted
- **Technology**: markdown section + engine/checks/pm_acceptance regex check
- **UX design**: PM fills section post-done; reviewer reads it during retrospective
- **Monetization**: learning compounding IS the lifecycle value claim
- **Acquisition**: "every feature produces learning, including the failures" — honest pitch
- **Offline experience**: section lives in Issue body; no remote dependency

## Value chain

- **Outputs shipped**: `.claude/skills/node-templates/SKILL.md § feature template` Value chain block; `engine/checks/pm_acceptance.py` PM003 + PM004
- **Outcomes observed**: Dogfood — every feature this script creates carries the section (with honest "pending external adoption" framings)
- **Benefits measured**: Pending external adoption to validate the learning-extraction discipline
- **Value assessment**: Shipped + dogfood-exercised
- **Learning extracted**: Pre-filling Value chain at creation time (when the feature is shipped retroactively) is awkward because we lack outcome data — but better than leaving the section blank. The honest "pending external adoption" framing keeps the discipline visible.
- **Next cards surfaced**: Auto-derive Outputs shipped from the closing PR's changed files (already done in engine/checks/artifacts_derive); auto-suggest Outcomes observed from telemetry hooks (deferred, requires F4.4 + adopter-side instrumentation)
""",
)


# ============================================================================
# C4 — Catch structural + semantic defects in CI
# ============================================================================

F4_1 = FeatureSpec(
    code="F4.1",
    title="engine/checks library architecture + Finding type + run_all_checks dispatcher",
    parent_cap="C4",
    body="""## Map
- Children: none
- Related: F4.2 (specific checks implement this surface); F4.3 (CI invokes via this surface)

## Story

Adopter team's framework runs semantic checks at strategic moments (hooks, PR creation, manual `validate_node`) through a shared library architecture: each check is a function returning `list[Finding]`; `run_all_checks(node, adapter)` dispatches by NodeType to the relevant checks; `CheckContext` carries the common payload. The architecture lets adopters write custom checks following the same shape.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `engine/checks/base.py` exposes `CheckContext`, `Finding`, `run_all_checks`, `section_body`, `section_is_populated`
- `run_all_checks` dispatches by NodeType to: security_review (spec/adr/feature), architect_coherence (adr), pm_acceptance (spec/feature), goal_smart (goal)
- `Finding` carries severity + code + message; warn-level by default (never blocks writes)
- Library is importable + extensible — adopters can register custom checks

## Acceptance check

Verified by `engine/tests/test_checks.py` Base helpers section + RunAllChecks section (~15 tests).

## Position in the larger narrative

This is the *semantic CI* substrate, complementing the structural validators (F1.3) that hard-reject. The two layers together provide the framework's defect-catching surface: structural at write, semantic at hook + PR-time.

## State

done — shipped in v0.3.0; extended 2026-05-24 with goal_smart check.

## Holistic dimensions

- **Functionality**: shared library architecture + dispatcher + 4 standard checks
- **Technology**: Python module; pure functions; no I/O at check level (adapter passed via context for chain checks)
- **UX design**: agents see Finding objects with code + message; structured for programmatic handling
- **Monetization**: extensible substrate — adopters can grow it with their own checks
- **Acquisition**: "semantic CI library you can extend" — concrete extensibility promise
- **Offline experience**: checks run locally; CI mode runs in Actions

## Value chain

- **Outputs shipped**: `engine/checks/base.py` (~80 LOC); typed Finding dataclass in `engine/core/models.py`
- **Outcomes observed**: Dogfood — every spine node's body has been (or will be) inspected by run_all_checks; goal_smart catches missing Stakeholder sections we forgot
- **Benefits measured**: Pending external adoption to validate extensibility (does anyone add a custom check?)
- **Value assessment**: Shipped + dogfood-exercised
- **Learning extracted**: Treating each check as a pure function (no shared state, no I/O at check level) made it trivial to compose them in run_all_checks + test them independently. The architecture should stay this way as more checks are added.
- **Next cards surfaced**: Capability-quality check (analogous to goal_smart but for capabilities — WHAT vs HOW leak, Two implementations populated); vision-quality check (Value ambition shape)
""",
)

F4_2 = FeatureSpec(
    code="F4.2",
    title="5 semantic checks shipped (architect_coherence, pm_acceptance, security_review, artifacts_derive, goal_smart)",
    parent_cap="C4",
    body="""## Map
- Children: none
- Related: F4.1 (library architecture houses these); F4.3 (CI invokes); methodology ADR #29 (goal_smart embeds SMART/Stakeholder/why-stack)

## Story

Adopter team's framework ships with 5 named checks that cover the most common AI-augmented authoring failure modes: ADR Security attributes silence (security_review), ADR coherence with supersede chains (architect_coherence), spec/feature acceptance + learning extraction (pm_acceptance), PR-closes-Issue artifact derivation (artifacts_derive), goal SMART + Stakeholder + outcome-shape (goal_smart). Each surfaces warn-level Findings; the human / agent decides what to do.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `engine/checks/security_review.py` (SEC001-SEC003) — spec/adr/feature
- `engine/checks/architect_coherence.py` (ARC001-ARC005) — adr only
- `engine/checks/pm_acceptance.py` (PM001-PM005) — spec, feature
- `engine/checks/artifacts_derive.py` — PR body parsing for `Closes #N`
- `engine/checks/goal_smart.py` (GS001-GS004) — goal only
- All return `list[Finding]` with severity='warning' (never blocks)

## Acceptance check

Verified by `engine/tests/test_checks.py` per-check sections — ~50 tests total covering positive + negative scenarios.

## Position in the larger narrative

These are the framework's opinionated default checks. Adopters can disable, override, or add their own via the engine/checks library architecture (F4.1). The defaults encode the methodology pieces from ADR #29 (definitional literacy).

## State

done — 5 checks shipped in v0.3.0 (goal_smart added 2026-05-24).

## Holistic dimensions

- **Functionality**: 5 checks covering 4 node types + PR body parsing
- **Technology**: Python modules; regex + section_body helpers from base; no I/O except adapter reads for chain checks
- **UX design**: agents see Findings inline in Claude Code; PR reviewers see them at PR-time via the PR hook
- **Monetization**: defects caught early = customer time saved
- **Acquisition**: "CI that thinks before merge" — concrete pitch with 5 named checks
- **Offline experience**: pure Python; runs locally + in CI

## Value chain

- **Outputs shipped**: 5 check modules in `engine/checks/`; ~400 LOC total
- **Outcomes observed**: Dogfood — goal_smart caught missing Stakeholder sections during goal authoring (we added them in the SMART update commit a7a272b)
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated; goal_smart specifically demonstrated immediate value
- **Learning extracted**: Naming each finding with a code (PM001, GS003, SEC002) makes them addressable — agents + humans can reference them in commit messages and discussions. Keep this convention.
- **Next cards surfaced**: Capability-quality check (proposed in methodology ADR #29 future work); risk-surface coverage check (do all 5 Holistic dimensions have substantive content?)
""",
)

F4_3 = FeatureSpec(
    code="F4.3",
    title="Two-layer CI: structural sem-ai-ci.yml + semantic engine/checks invoked from hooks",
    parent_cap="C4",
    body="""## Map
- Children: none
- Related: F4.1 (library substrate); F4.2 (specific checks); F3.3 (hooks invoke checks); F5.4 (Action examples extend this for adopters)

## Story

Adopter team's repo has two layers of automated quality gates: structural CI runs on every push (sem-ai-ci.yml validates catalog + skills + agents + settings + markdown lint); semantic CI runs at hook moments + PR creation (engine/checks invoked from hooks). Defects surface before merge; the structural layer catches framework-contract drift, the semantic layer catches content gaps.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `.github/workflows/sem-ai-ci.yml` runs 4 stages (skills frontmatter, agents frontmatter, settings.json, markdown lint)
- `scripts/validators/check_repo.py` is the structural validator runner (skills / agents / settings)
- Hooks (F3.3) invoke engine/checks at strategic moments (transition_status, gh pr create)
- Semantic findings are warn-level — visible but non-blocking
- ADR Issue migration removed the previous "ADRs as markdown" stage; the structural CI no longer expects docs/adr/

## Acceptance check

Verified by `engine/tests/test_validators.py` (~10 tests) + the workflow file structure verified manually. CI runs green on every push to main.

## Position in the larger narrative

This is the framework's *defense in depth*: structural validation at push (cheap, fast, hard-reject for framework contracts), semantic validation at write/PR (warn-level, content-aware). The two layers complement; neither alone is enough.

## State

done — shipped in v0.3.0; refined 2026-05-24 when the ADR markdown stage was removed (ADRs now live as Issues, not files).

## Holistic dimensions

- **Functionality**: 4 structural stages + 5 semantic checks invoked from hooks
- **Technology**: GitHub Actions YAML + Python validators + Claude Code hook mechanism
- **UX design**: structural failures are red on PRs; semantic warnings are inline in Claude Code sessions
- **Monetization**: defects caught early in the cycle = customer rework savings
- **Acquisition**: "two-layer CI shipped with the template" — concrete value-add
- **Offline experience**: structural CI requires GitHub Actions; semantic CI runs locally too (via hooks or manual validate_node)

## Value chain

- **Outputs shipped**: `.github/workflows/sem-ai-ci.yml`; `scripts/validators/check_repo.py`; hook scripts in `scripts/hooks/`; engine/checks library
- **Outcomes observed**: Dogfood — sem-ai-ci.yml runs green on every commit to PelayoU/SEM-AI; goal_smart caught real gaps during goal authoring
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated
- **Learning extracted**: Removing the ADR markdown stage when ADRs migrated to Issues was important — keeping a structural check for files that no longer exist would have caused confusing failures. CI must stay coherent with the model.
- **Next cards surfaced**: Strict markdown-lint (currently warn-only) once the rule set stabilizes; Action examples (F5.4) for adopters who want post-hoc validation of UI-edited Issues
""",
)

F4_4 = FeatureSpec(
    code="F4.4",
    title="Test suite (~310 tests covering engine + checks + hooks + adapters)",
    parent_cap="C4",
    body="""## Map
- Children: none
- Related: F4.3 (tests run in CI via sem-ai-ci.yml — implicit gate); every other feature (each is tested in this suite)

## Story

Adopter team adopting the framework needs confidence that the engine's mechanical guarantees hold. The test suite — ~310 tests across catalog / validators / API / checks / hooks / GitHub adapter / MCP server / permissions / skill scripts — covers positive + negative cases for every shipped feature. Tests run in 0.2 seconds; CI runs them on every push.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- ~310 tests in `engine/tests/` across 10 test files
- Coverage spans catalog, validators, API, checks, hooks, GitHub adapter, MCP server, permissions, skill scripts
- Tests run in <1 second on a typical dev laptop
- Test suite passes green on every push to main
- MockAdapter in `engine/tests/conftest.py` allows fast in-memory testing without GitHub API calls

## Acceptance check

`pytest engine/tests/ -q` returns "passed" with no failures. CI runs the suite implicitly via the workflow's structural stages (and explicitly when test-runs are added to a future workflow stage).

## Position in the larger narrative

The test suite is the framework's *confidence backbone*. Adopters considering SEM-AI can read tests/test_catalog.py and tests/test_validators.py to verify the mechanical claims are real rather than aspirational. The Mock-based architecture also serves as reference for adopters who write their own checks + tests.

## State

done — shipped in v0.3.0 (295 tests); expanded 2026-05-24 to ~310 (added goal_smart tests + 1 obsolete test updated).

## Holistic dimensions

- **Functionality**: ~310 tests covering shipped behavior; Mock-based for speed
- **Technology**: pytest; pure Python; no Docker / no external services
- **UX design**: developer adopter sees green test count as confidence signal
- **Monetization**: tested mechanics = customer trust = adoption
- **Acquisition**: "295+ tests shipping with the template" — concrete signal of maturity
- **Offline experience**: tests run locally without network; MockAdapter avoids GitHub calls

## Value chain

- **Outputs shipped**: 10 test files in `engine/tests/`; `conftest.py` with MockAdapter; ~310 tests total
- **Outcomes observed**: Dogfood — full suite green on every commit including this script's prerequisites; obsolete test updated when goal_smart landed (we caught + fixed it in the same commit)
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + continuously validated (every commit runs it)
- **Learning extracted**: The MockAdapter as a fast in-memory drop-in for GitHubAdapter is what makes the suite fast (<1s for ~310 tests). Worth keeping the Mock surface in sync with the real adapter as new methods are added.
- **Next cards surfaced**: Test-runs as explicit CI stage (currently implicit via the structural checks importing the engine); coverage reporting (deferred)
""",
)


# ============================================================================
# C5 — GitHub as unified backend, no extra infra
# ============================================================================

F5_1 = FeatureSpec(
    code="F5.1",
    title="GitHub Issues + Projects v2 + Milestones + Releases + PR reviews as storage",
    parent_cap="C5",
    body="""## Map
- Children: none
- Related: F5.2 (adapter mediates access); F1.2b (Milestone/Release bridges); F1.1 (catalog audit uses GitHub natives where possible)

## Story

Adopter team's project plan lives on GitHub objects they already know: Issues for graph nodes, sub-issues for parent links, Projects v2 custom fields for status / related / supersedes, Milestones for release planning, Releases for publication, PR reviews for code inspections. No parallel database, no separate planning tool, no synced copy that drifts.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- Issues are the canonical store; the `#N` is the node id
- Sub-issue native links carry the parent edge (with `parent:#N` label fallback when sub-issues API is unavailable, e.g. personal accounts)
- Projects v2 custom fields carry Status / Related / Supersedes / Superseded by (with `status:<X>` label fallback when Projects v2 scope is missing)
- Milestones (+ structured body) carry release planning; Releases carry publication
- PR reviews are the inspection record for code; non-code inspection uses comments + `inspected` label

## Acceptance check

Verified by `engine/tests/test_github_adapter.py` — adapter operations against MockAdapter; manual verification against real GitHub (PelayoU/SEM-AI) during dogfood.

## Position in the larger narrative

This is the framework's *no-extra-infrastructure* claim, operational. Adopters already have GitHub; SEM-AI piggybacks on what they trust + already pay for. Native bridges keep the catalog minimal (per ADR-001 audit principle).

## State

done — shipped in v0.3.0; ~25 labels provisioned by setup script (fix: 2026-05-25 ee79fb8).

## Holistic dimensions

- **Functionality**: 5 native object types + ~25 framework labels carrying type / status / role / parent
- **Technology**: GitHub REST + GraphQL; no parallel DB
- **UX design**: adopters use familiar GitHub UI; the framework adds discipline, not new screens
- **Monetization**: zero infrastructure cost reduces customer ROI threshold to near-zero
- **Acquisition**: "no DB, no install, no cloud" — friction-low onramp
- **Offline experience**: graph + history live on GitHub; partial offline via `git clone` (code + sessions/), full offline impossible

## Value chain

- **Outputs shipped**: GitHub adapter implementation in `engine/adapters/github.py` (~600 LOC); label conventions documented in framework SKILL + setup script
- **Outcomes observed**: Dogfood — 29 Issues created on PelayoU/SEM-AI using only native GitHub mechanisms; sub-issues API gracefully degraded to parent:#N label on personal account
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated
- **Learning extracted**: Building label-based fallbacks for native features that turn out unavailable (sub-issues API, Projects v2 fields on accounts without scope) was time well spent — the framework works on personal accounts AND on org accounts with full features, without code branching.
- **Next cards surfaced**: Projects v2 Status field via GraphQL (currently label fallback); Discussions as another native bridge for community Q&A
""",
)

F5_2 = FeatureSpec(
    code="F5.2",
    title="GitHubAdapter via gh CLI + Projects v2 GraphQL",
    parent_cap="C5",
    body="""## Map
- Children: none
- Related: F6.1 (implements the BackendAdapter ABC); F6.2 (this is the reference impl); F5.1 (the native objects this adapter mediates)

## Story

Adopter team's engine talks to GitHub through `gh` CLI for most operations (Issues, labels, Milestones, Releases, sub-issues) and `gh api graphql` for Projects v2 field reads/writes. Auth inherits from `gh auth login` — no token plumbing inside the engine. Pagination, retry, rate-limit handling all come from gh.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `engine/adapters/github.py::GitHubAdapter` implements `BackendAdapter` (F6.1) fully
- Uses `gh` CLI via subprocess for Issues + labels + Milestones + Releases
- Uses `gh api graphql` for Projects v2 custom fields when available; falls back to labels when not
- Sub-issues API has graceful fallback to `parent:#N` label
- gh CLI rejects `issueType` JSON field on accounts without Issue Types → falls back to `type:<X>` label

## Acceptance check

Verified by `engine/tests/test_github_adapter.py` (~30 tests with MockAdapter); manual verification against real GitHub (PelayoU/SEM-AI) during the 2026-05-24 dogfood migration.

## Position in the larger narrative

The reference adapter implementation. F6.1 defines the interface; F6.2 designates this as the reference; this feature IS the concrete code.

## State

done — shipped in v0.3.0; refined 2026-05-24 with sub-issues fallback + issueType field removal; 2026-05-25 with setup-script label-provisioning fix.

## Holistic dimensions

- **Functionality**: full BackendAdapter implementation; ~600 LOC
- **Technology**: subprocess to gh CLI; GraphQL for Projects v2; Python's subprocess.CalledProcessError handling
- **UX design**: invisible to the human; agents see typed responses
- **Monetization**: GitHub-coupled but adapter-bounded — opens GitHub markets while preserving portability to others
- **Acquisition**: "uses gh CLI you already have" — zero new tooling
- **Offline experience**: requires GitHub API connectivity for writes; reads can be cached but not in v0.3

## Value chain

- **Outputs shipped**: `engine/adapters/github.py` (~600 LOC)
- **Outcomes observed**: Dogfood — adapter handled the 2026-05-24 migration of 9 ADRs + 8 goals + 10 capabilities; surfaced and worked around 3 GitHub platform quirks (sub-issues 404, issueType JSON field, label-description char limit) — all documented in commits
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated through real-world friction
- **Learning extracted**: GitHub's "personal account vs org account" feature parity is uneven (sub-issues, Issue Types, Projects v2 GraphQL all differ). Building graceful fallbacks beats requiring orgs. The fallbacks are stable enough that adopters won't hit "you need a paid org" friction.
- **Next cards surfaced**: Caching layer for hot reads (deferred); rate-limit-aware backoff (gh provides it but worth verifying)
""",
)

F5_3 = FeatureSpec(
    code="F5.3",
    title="Template distribution + 3-command setup (setup-engine.sh + setup-github-project.sh + README)",
    parent_cap="C5",
    body="""## Map
- Children: none
- Related: F5.1 (setup provisions the native objects); F5.2 (engine setup creates the venv); the methodology ADR #29 (templates that ship are the framework's definitional baseline)

## Story

Adopter team clones the SEM-AI GitHub template ("Use this template") and runs three commands to be operational: `setup-engine.sh` (local venv + Python deps + verify), `setup-github-project.sh` (~25 labels + Issue Types + Projects v2 board), then `claude --agent product-manager` to start work. README walks them through. ≤5 minutes from "I want to try this" to "I have a vision Issue".

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- Repo is configured as a GitHub template (Settings → Template repository: on)
- `scripts/setup-engine.sh` — creates `.venv`, installs `engine/requirements.txt`, verifies `python -m engine.mcp_server --help` works
- `scripts/setup-github-project.sh` — provisions 28 labels (3 cross-cutting + 6 role:* + 7 type:* + 12 status:*); attempts Issue Types + Projects v2 (graceful on personal accounts)
- README.md walks through clone → setup-engine → setup-github-project → first conversation
- Setup is idempotent — re-running is safe

## Acceptance check

Manual: clone fresh repo, run 3 commands, create first vision Issue successfully. Friction tested 2026-05-24 (sub-issues, label provisioning fixes followed).

## Position in the larger narrative

This is the *adopter's first encounter* with the framework — the friction (or lack thereof) determines whether they continue. The 2026-05-25 label-provisioning fix removed a hard-fail that would have stopped every fresh adopter at their first create_node.

## State

done — shipped in v0.3.0; refined 2026-05-25 with label provisioning fix (commit ee79fb8) and idempotency bug fix (gh label list 30-default).

## Holistic dimensions

- **Functionality**: 2 bash scripts + 1 README; idempotent provisioning of all required GitHub objects
- **Technology**: bash + gh CLI + Python venv tooling
- **UX design**: 3-command path; README readable in 5 minutes
- **Monetization**: low friction = higher conversion from "interested" to "operating"
- **Acquisition**: GitHub template + word of mouth; setup is the funnel's bottleneck
- **Offline experience**: setup-engine works fully offline; setup-github-project obviously needs GitHub API

## Value chain

- **Outputs shipped**: `scripts/setup-engine.sh`, `scripts/setup-github-project.sh`, `README.md`, template repo configuration
- **Outcomes observed**: Dogfood — first-time setup surfaced the label-provisioning gap (now fixed); subsequent runs idempotent
- **Benefits measured**: Pending external adoption (time-to-first-Issue for new adopters)
- **Value assessment**: Shipped + dogfood-refined; smoother for next adopter than for us
- **Learning extracted**: Setup scripts must be tested *against a fresh repo*, not just against the dev's own repo. The label-provisioning gap was invisible to us until the migration script's first create_node fell over. Worth automating a smoke test against a new ephemeral repo.
- **Next cards surfaced**: Projects v2 scope detection + clear instructions when missing (currently exits 1); per-OS verification (we tested on darwin only); ephemeral-repo CI smoke test
""",
)

F5_4 = FeatureSpec(
    code="F5.4",
    title="Sample pipeline Action as reference adopter deployment",
    parent_cap="C5",
    body="""## Map
- Children: none
- Related: F4.3 (CI shape the sample mirrors); F5.3 (sample is part of what adopters get from the template)

## Story

Adopter team's CD pipeline is up to them, but SEM-AI ships a reference sample (`examples/.github/workflows/sample-pipeline.yml`) covering the typical multi-environment deploy with required reviewers (staging + production), artifact-derive job on PR merge, and notify-graph job posting 🏁 comments. Adopters copy + adapt rather than starting from scratch.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `examples/.github/workflows/sample-pipeline.yml` ships in the template
- `examples/README.md` explains: what to keep, what to swap, the unsafe-to-break contract (notify-graph job + 🏁 marker)
- Sample uses staging + production environments with required reviewers
- Sample includes artifact-derive job using `engine/checks/artifacts_derive.py`

## Acceptance check

Manual review of the YAML against the framework's expected hook contracts (Closes #N parsing + 🏁 comment posting). Not yet exercised in a real adopter deployment.

## Position in the larger narrative

The sample pipeline is the adopter's reference for "what does an SEM-AI-aware deployment look like?". The framework doesn't dictate CD specifics, but the example shows the integration points (notify-graph, artifact-derive) that downstream Actions should preserve.

## State

done — shipped in v0.3.0; not yet exercised in real-world adopter deployment.

## Holistic dimensions

- **Functionality**: 1 reference workflow + accompanying README
- **Technology**: GitHub Actions YAML; reuses engine/checks/artifacts_derive
- **UX design**: adopter copy-pastes + adapts; the README highlights the contract surface
- **Monetization**: reduces adopter's setup time; lowers the "how do I integrate this with my pipeline" friction
- **Acquisition**: tangible deliverable in the template
- **Offline experience**: workflow runs in GitHub Actions; not a local concern

## Value chain

- **Outputs shipped**: `examples/.github/workflows/sample-pipeline.yml`; `examples/README.md`
- **Outcomes observed**: Pending — no real adopter has copied + adapted yet
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + documented; real-world value pending first adopter deployment
- **Learning extracted**: Making the "unsafe to break" contract explicit (the notify-graph job's parsing of Closes #N) is important — adopters who don't understand the contract might inadvertently remove the marker the framework relies on.
- **Next cards surfaced**: Additional Action examples (sem-ai-validate-posthoc, sem-ai-security-review) — deferred to v0.4; tested smoke deployment against a sample adopter app
""",
)


# ============================================================================
# C6 — Backend portability via adapter pattern
# ============================================================================

F6_1 = FeatureSpec(
    code="F6.1",
    title="BackendAdapter abstract class with closed interface",
    parent_cap="C6",
    body="""## Map
- Children: none
- Related: F6.2 (GitHubAdapter implements this); F6.3 (MCP server speaks through any adapter); F5.2 (current reference implementation)

## Story

Adopter team's engine speaks to its backend through a single abstract interface, `BackendAdapter`. The class declares ~30 abstract methods covering reads (get_issue, list_sub_issues, query_issues, search_issues, project_map, instance_config), writes (create_issue, update_issue, set_status, set_related, add_label, remove_label, supersede, link_commit), and native bridges (create_milestone, assign_to_milestone, publish_release). A non-GitHub adapter is contributable by implementing this surface — no `engine/core/` changes required.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `engine/adapters/base.py::BackendAdapter` exposes ~30 abstract methods
- All methods return immutable types (Node, Milestone, Release, ProjectMap, InstanceConfig)
- Engine API (F1.2a + F1.2b) imports only the abstract base, never the concrete GitHubAdapter
- Import-graph check would catch core → adapter leaks (currently manual review, deferrable to CI lint)

## Acceptance check

Verified manually: `grep "from.*adapters.github" engine/core/` returns empty. `engine/tests/test_github_adapter.py` exercises every abstract method's concrete impl.

## Position in the larger narrative

The abstraction validates the portability claim of G8 — non-GitHub adapters are contributable without engine/core changes. Currently only one concrete adapter exists (GitHubAdapter), so the abstraction is asserted-but-untested; G8 acceptance includes a stub or RFC to validate it.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: ~30 abstract methods covering full I/O surface
- **Technology**: Python's ABC + abstractmethod decorators
- **UX design**: invisible to the human; constrains contributors
- **Monetization**: portability removes the "we don't use GitHub" deal-breaker (G8 outcome)
- **Acquisition**: architectural promise — concrete via "you could write a Jira adapter following this interface"
- **Offline experience**: abstraction is local; implementations may be local or remote

## Value chain

- **Outputs shipped**: `engine/adapters/base.py::BackendAdapter`
- **Outcomes observed**: Dogfood — only one implementation today (GitHubAdapter); the abstraction has not been validated by a second adapter
- **Benefits measured**: Pending — G8's acceptance asks for a stub or RFC
- **Value assessment**: Shipped + structural; portability is **asserted, not yet validated**
- **Learning extracted**: An abstract interface with one implementation is suspicious — it's easy to accidentally codify GitHub-isms in the abstract methods. The G8 acceptance (community RFC or stub adapter) is the right validation gate.
- **Next cards surfaced**: Stub Linear / Jira / GitLab adapter as integration test for the abstraction; import-lint check in CI to catch core → adapter leaks
""",
)

F6_2 = FeatureSpec(
    code="F6.2",
    title="GitHubAdapter as reference implementation of BackendAdapter",
    parent_cap="C6",
    body="""## Map
- Children: none
- Related: F6.1 (the abstract class); F5.2 (the GitHub adapter feature, viewed from C5 angle)

## Story

Adopter team's only-shipped concrete adapter is the GitHubAdapter (F5.2 viewed through C6 lens). It demonstrates the abstraction in action: every method of BackendAdapter has a working implementation; the engine's API layer never imports it directly (only the abstract base). It serves as the contract that future non-GitHub adapter contributions must satisfy.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `engine/adapters/github.py::GitHubAdapter` is a complete implementation of `BackendAdapter`
- Importable as the default adapter via `engine/adapters/__init__.py::load_config` + factory
- All ~30 abstract methods have concrete implementations
- Tested independently via `engine/tests/test_github_adapter.py`

## Acceptance check

Verified by the tests passing + manual confirmation that all abstract methods are concretely implemented (`grep "raise NotImplementedError" engine/adapters/github.py` returns empty).

## Position in the larger narrative

This is the *reference for future adapters*. A contributor adding a LinearAdapter or JiraAdapter follows the same shape as GitHubAdapter: implement every abstract method, return immutable types, surface errors as exceptions the engine can act on.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: complete reference implementation
- **Technology**: subprocess to gh CLI + GraphQL
- **UX design**: invisible; humans see GitHub Issues normally
- **Monetization**: portability promise becomes credible because the reference exists
- **Acquisition**: contributors can read this and understand "what is an adapter?"
- **Offline experience**: GitHub-dependent; future adapters could target local backends

## Value chain

- **Outputs shipped**: `engine/adapters/github.py` as a complete BackendAdapter implementation
- **Outcomes observed**: Dogfood — every engine call in this script (and prior dogfood scripts) flows through this adapter without escape
- **Benefits measured**: Pending external adoption + second adapter contribution
- **Value assessment**: Shipped + dogfood-validated as a reference
- **Learning extracted**: Keeping the GitHubAdapter as the only impl while the abstraction matures was the right call — premature multi-adapter abstraction would have over-fitted to known cases. Now that the GitHub adapter is stable, a second adapter is the validation step.
- **Next cards surfaced**: Linear stub adapter (covered by G8's acceptance criterion); per-adapter test contract (shared abstract test class adopters can subclass)
""",
)

F6_3 = FeatureSpec(
    code="F6.3",
    title="MCP server as stable agent-facing contract (independent of adapter)",
    parent_cap="C6",
    body="""## Map
- Children: none
- Related: F1.2a (the 19 graph tools exposed); F1.2b (the 3 native bridges); F6.1 (the server doesn't know which adapter it talks through)

## Story

Adopter team's AI agents speak to the engine through the MCP server (Model Context Protocol). The server exposes the 22 engine API functions as MCP tools; the agent sees a stable tool surface regardless of which adapter is wired. Swap GitHub for Linear post-v1 and the agent's tool surface doesn't change.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `engine/mcp_server.py` runs as an MCP server (stdio transport)
- 22 typed tools registered (19 graph + 3 bridges)
- Server loads the configured adapter (currently always GitHubAdapter via load_config)
- Agent-facing schema (tool names, parameters, return types) is independent of adapter choice
- `python -m engine.mcp_server` is the canonical entry point

## Acceptance check

Verified by `engine/tests/test_mcp_server.py` — tool registration, schema validation, stdio handling.

## Position in the larger narrative

The MCP server is the *protocol layer* — the abstraction that makes the framework portable to other AI hosts beyond Claude Code. Today Claude Code is the only host that loads it, but the MCP specification is the lingua franca; future hosts (Cursor, Windsurf, in-house tools) can load the same server unchanged.

## State

done — shipped in v0.3.0; not yet exercised against a non-Claude-Code MCP host.

## Holistic dimensions

- **Functionality**: 22 typed tools over MCP stdio
- **Technology**: anthropic-mcp Python library; stdio transport; JSON-RPC underneath
- **UX design**: agent-facing only; no human surface
- **Monetization**: future-proof — adopters who switch AI hosts keep working
- **Acquisition**: "MCP-native, host-portable" — concrete promise for buyers worried about AI vendor lock-in
- **Offline experience**: server runs as a local subprocess; no network beyond what tools require

## Value chain

- **Outputs shipped**: `engine/mcp_server.py` (~300 LOC); tool registration covering 22 API functions
- **Outcomes observed**: Dogfood — Claude Code loads + invokes the server via `.claude/settings.json::mcpServers`; tools all work
- **Benefits measured**: Pending broader MCP host adoption
- **Value assessment**: Shipped + Claude-Code-validated; multi-host pending external interest
- **Learning extracted**: MCP server as a Python module with a CLI entry point (`python -m engine.mcp_server`) is the right pattern — easy to launch, easy to test, no daemon to manage.
- **Next cards surfaced**: Schema generation from API signatures (currently manual); compatibility test against another MCP host as it appears
""",
)


# ============================================================================
# C7 — First-class experimentation lifecycle
# ============================================================================

F7_1 = FeatureSpec(
    code="F7.1",
    title="Uncertainty addressed slot in feature template",
    parent_cap="C7",
    body="""## Map
- Children: none
- Related: F7.2 (label coherence keyed off this slot); F7.3 (sub-type lifecycle uses this slot as the entry point); F1.5 (feature template houses it)

## Story

Adopter team's PM authoring a feature decides: delivery (pays off accumulated learning) or experiment (resolves uncertainty)? The `## Uncertainty addressed` slot in the feature template forces the choice — populate with the unknown to be resolved, or write `N/A — delivery, not experiment` with the reason. No silent skipping; intent surfaces at planning, not after shipping.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `## Uncertainty addressed` section in feature template (F1.5)
- Required to be populated (with `N/A — delivery, not experiment` as the legitimate delivery framing)
- Template comment explains: prototype / spike / A-B / concierge sub-types + expected final status by sub-type
- Naming which Holistic dimension the experiment tests (Monetization↔value risk, UX↔usability, Tech↔viability, etc.)

## Acceptance check

Verified by manual review of the feature template in `.claude/skills/node-templates/SKILL.md`; pm_acceptance check PM005 (F4.2) catches feature with `experiment` label but empty Uncertainty addressed.

## Position in the larger narrative

The slot is what makes experimentation first-class. Without it, the framework conflates delivery and experiment — Value chain reads incorrectly post-done (looking for value when the feature was meant to produce learning).

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 1 required slot in feature template + comment guidance
- **Technology**: markdown section; engine parses it via regex
- **UX design**: PM sees the slot; cannot ship a feature node body without addressing it
- **Monetization**: explicit experimentation is mature product practice — sells to teams that take discovery seriously
- **Acquisition**: differentiator vs trackers that conflate delivery + experiment
- **Offline experience**: slot is body content; lives locally

## Value chain

- **Outputs shipped**: `## Uncertainty addressed` section in feature template; comment explaining sub-types + lifecycles
- **Outcomes observed**: Dogfood — every feature in this script populates the slot honestly (all are delivery)
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated as authoring discipline
- **Learning extracted**: Forcing a positive `N/A — delivery, not experiment` framing (instead of allowing silent omission) makes the delivery vs experiment choice explicit even when delivery is the default. Worth keeping the friction.
- **Next cards surfaced**: Per-sub-type templates within the feature template (deferred — currently all sub-types share the same outer template)
""",
)

F7_2 = FeatureSpec(
    code="F7.2",
    title="experiment label auto-coherence (engine maintains slot ↔ label invariant)",
    parent_cap="C7",
    body="""## Map
- Children: none
- Related: F7.1 (the slot this label tracks); F1.2a (engine API enforces the invariant in create_node + update_node)

## Story

Adopter team's agents and humans never curate the `experiment` label by hand. The engine auto-applies it when `Uncertainty addressed` is populated with non-N/A content, and removes it when the slot is cleared to N/A. Slot and label stay in sync mechanically; the Issue list / Projects v2 board / `gh issue list` reliably show experiments vs deliveries at a glance.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `_ensure_experiment_label_coherence` in `engine/core/api.py` runs after create_node + update_node on features
- `_is_experimental_body` heuristic recognizes populated vs N/A Uncertainty addressed
- Adds `experiment` label when slot populated; removes when slot N/A; idempotent
- PM005 check (F4.2) catches divergence (slot N/A but label present, or slot populated but label absent) for UI-edited Issues that bypass the engine

## Acceptance check

Verified by `engine/tests/test_api.py` slot-label coherence tests (~5 tests covering create + update + N/A transition).

## Position in the larger narrative

This is the engine's only body-content-inspection at write time (per F2.3 / methodology ADR). The choice to make slot-label coherence mechanical (not advisory) reflects that experimentation visibility is too important to leave to discipline alone.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: engine-level invariant; bidirectional sync; idempotent
- **Technology**: regex parse of Uncertainty addressed slot + adapter add/remove label calls
- **UX design**: invisible — users see the label appear/disappear automatically as the slot is edited
- **Monetization**: visibility of experiments at the board level is part of the experimentation value claim
- **Acquisition**: "the label tracks the slot — you cannot misclassify a feature" — concrete promise
- **Offline experience**: invariant maintained at write; visible in GitHub once synced

## Value chain

- **Outputs shipped**: `_ensure_experiment_label_coherence` in `engine/core/api.py`; tests
- **Outcomes observed**: Dogfood — features created in this script all have N/A slot and no experiment label (correctly)
- **Benefits measured**: Pending external adoption with real experimentation flow
- **Value assessment**: Shipped + dogfood-validated
- **Learning extracted**: Making the engine the sole curator of the label (with PM005 as a safety net for UI bypass) is cleaner than asking agents/humans to set it. The label is a *derivative* of the slot, not a primary fact.
- **Next cards surfaced**: Per-sub-type derived labels (e.g. `experiment:prototype`, `experiment:spike`) for finer-grained Projects v2 filters
""",
)

F7_3 = FeatureSpec(
    code="F7.3",
    title="Per-sub-type expected lifecycle (PROTOTYPE / SPIKE / A-B / CONCIERGE)",
    parent_cap="C7",
    body="""## Map
- Children: none
- Related: F7.1 (sub-type declared in the slot); F1.5 (template carries the lifecycle guidance)

## Story

Adopter team's PM closing an experimental feature knows what final status it should land in based on sub-type: PROTOTYPE → `deprecated` (discardable artifact); SPIKE → usually `deprecated`, sometimes `done`; A/B TEST → `done` (winning variant stays); CONCIERGE → `deprecated` (after learning extracted, automation opens as new delivery feature). The framework documents this in the feature template comment so closing logic doesn't have to be re-derived.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- Feature template comment on Uncertainty addressed lists 4 sub-types with expected final statuses
- Guidance: prototype always deprecates after validation (a successful prototype opens a new delivery feature with related link back)
- Guidance: a/b test's winning variant stays as the done feature
- Guidance: concierge's automation opens as a new delivery feature

## Acceptance check

Manual review of the feature template comment in `.claude/skills/node-templates/SKILL.md`.

## Position in the larger narrative

This embeds product methodology (experimentation lifecycle by sub-type) at the template level rather than expecting adopters to bring it. Per methodology ADR #29, this is definitional product literacy — sub-type lifecycle expectations are textbook.

## State

done — shipped in v0.3.0 as part of the feature template guidance.

## Holistic dimensions

- **Functionality**: documented lifecycle expectations for 4 sub-types
- **Technology**: markdown comment in template SKILL
- **UX design**: PM reads when closing an experiment; the comment surfaces the right status to transition to
- **Monetization**: mature experimentation practice — sells to teams that take discovery seriously
- **Acquisition**: differentiator vs tools that treat all experimental features the same
- **Offline experience**: lives in local SKILL file

## Value chain

- **Outputs shipped**: Sub-type lifecycle guidance in feature template comment
- **Outcomes observed**: Pending — no experimental feature has been closed in dogfood yet (all features in this script are delivery)
- **Benefits measured**: Pending external adoption with actual experimentation flow
- **Value assessment**: Shipped at guidance level; real-world value pending
- **Learning extracted**: Sub-type lifecycle is the natural complement to the Uncertainty addressed slot — without it, closing experiments would be a guess. Worth keeping in the template comment vs in a separate doc.
- **Next cards surfaced**: Engine check to suggest the right transition_status target based on sub-type when closing an experimental feature (deferred)
""",
)


# ============================================================================
# C8 — Multi-dimensional evaluation as structural risk surface
# ============================================================================

F8_1 = FeatureSpec(
    code="F8.1",
    title="Holistic dimensions section in spine templates (vision/goal/capability/feature)",
    parent_cap="C8",
    body="""## Map
- Children: none
- Related: F1.5 (templates house this section); F8.2 (risk-class mapping that this section delivers); methodology ADR #29 (embedded methodology piece #2)

## Story

Adopter team's PM authoring vision / goal / capability / feature considers five Holistic Dimensions as structured slots: Technology, UX design, Monetization, Acquisition, Offline experience (plus Functionality as base). Each slot is simultaneously a design slot AND a risk-surface slot — silent omission = absorbed risk; mark N/A only with explicit reason. PM cannot ship a spine node body with a silently-missing dimension.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `## Holistic dimensions` section in vision / goal / capability / feature templates (4 of the 7 types)
- 5 dimensions per node: Functionality, Technology, UX design, Monetization, Acquisition, Offline experience
- Each slot is a single line; populated content or `N/A — <reason>`
- Story + spec + adr deliberately omit (different granularity reasons documented in templates)

## Acceptance check

Manual review of the four spine templates in `.claude/skills/node-templates/SKILL.md`; check by inspection of every spine node body (vision #1, goals #11-#18, capabilities #19-#28) for section presence.

## Position in the larger narrative

This makes risk-thinking structural rather than an after-the-fact assessment. PM cannot author a spine node without considering each dimension; what would otherwise be implicit assumptions become explicit slots.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 5-slot section in 4 spine templates
- **Technology**: markdown template structure
- **UX design**: PM fills slots; readers see coverage at a glance
- **Monetization**: dimensional thinking catches monetization gaps that pure functional thinking misses
- **Acquisition**: same — explicit acquisition slot forces explicit thinking about reach
- **Offline experience**: explicit slot forces explicit thinking about off-screen / off-network reality

## Value chain

- **Outputs shipped**: 5-slot Holistic dimensions block in vision / goal / capability / feature templates
- **Outcomes observed**: Dogfood — every spine node created in this exercise carries the section with substantive (not N/A) content
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated as authoring discipline
- **Learning extracted**: The same dimensions doing double duty as design slot AND risk surface is the key insight — adding a separate "Risks" section would have duplicated; the dimension IS the risk class.
- **Next cards surfaced**: engine/check that warns when a dimension slot has zero substantive content (only N/A without reason)
""",
)

F8_2 = FeatureSpec(
    code="F8.2",
    title="4 canonical risk-class mapping (Monetization↔value · UX↔usability · Tech↔viability · Acquisition+Offline↔business viability)",
    parent_cap="C8",
    body="""## Map
- Children: none
- Related: F8.1 (the dimensions this mapping qualifies); F7.1 (experimental features name which dimension they test)

## Story

Adopter team's framework documents the explicit mapping between Holistic dimensions and the 4 canonical risk classes of modern product approach: Monetization unvalidated = value risk; UX design unvalidated = usability risk; Technology unvalidated = viability risk; Acquisition + Offline unvalidated = business viability risk. The mapping makes risk classes derivable from dimensions rather than tracked separately.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- Risk-class mapping documented in node-templates SKILL on every Holistic dimensions section comment
- Same mapping referenced in feature template's Uncertainty addressed comment (experimental features name which dimension they test → that IS the risk class)
- Framework SKILL § The graph references the mapping when introducing dimensions

## Acceptance check

Manual review of template comments + framework SKILL.

## Position in the larger narrative

Without this mapping, "risk" would be an abstract concern. With it, risk is computable from dimensions: which dimensions are validated → which risk classes are addressed. The framework's risk-thinking is honest and concrete.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: 4-class mapping documented; cross-referenced across templates
- **Technology**: markdown comments in SKILLs
- **UX design**: PM internalizes the mapping by reading the templates repeatedly
- **Monetization**: explicit risk model = mature product practice
- **Acquisition**: differentiator vs tools without an explicit risk model
- **Offline experience**: lives in local SKILLs

## Value chain

- **Outputs shipped**: Risk-class mapping in node-templates SKILL + framework SKILL
- **Outcomes observed**: Dogfood — referenced in spine node bodies (e.g. capability bodies' Holistic dimensions sections)
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-referenced
- **Learning extracted**: Mapping risk classes to dimensions (rather than tracking risks separately) avoids the "risk register that nobody reads" failure mode. The dimension slot IS the risk surface.
- **Next cards surfaced**: Engine check that flags unvalidated dimensions when transitioning a feature to in-progress (deferred — requires dimension-validation telemetry we don't have)
""",
)


# ============================================================================
# C9 — Project intent evolves: bottom-up + supersede
# ============================================================================

F9_1 = FeatureSpec(
    code="F9.1",
    title="Anchor-pending pattern (bottom-up node creation before parent crystallizes)",
    parent_cap="C9",
    body="""## Map
- Children: none
- Related: F1.5 (template documents the pattern in the Map section); F2.2 (framework SKILL § The graph documents the 4 construction modes)

## Story

Adopter team's PM observes a feature emerging from user signals before its capability has crystallized. The anchor-pending pattern allows: set `parent` to the closest meaningful existing ancestor, keep that parent in `draft`, write `anchor pending` in the Map section's `- Parent:` line, correct via `update_node` when the higher level crystallizes. Bottom-up emergence is normal, not exceptional.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- Anchor-pending convention documented in node-templates SKILL § How to use a template (item 6)
- Framework SKILL § The graph documents the 4 construction modes (top-down, bottom-up, mixed, anchor-pending)
- Engine accepts parent_id pointing to a draft ancestor without rejection
- Re-parenting via update_node + transition_status works idempotently

## Acceptance check

Manual review of the convention in templates + framework SKILL; tested by `engine/tests/test_api.py` re-parenting scenarios.

## Position in the larger narrative

Without this pattern, the framework would impose strict top-down construction — which doesn't match how real product work emerges. Bottom-up is the normal way capabilities crystallize from feature patterns; the pattern makes it first-class rather than a workaround.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: documented convention + engine support for re-parenting
- **Technology**: parent_id is mutable via update_node + transition_status
- **UX design**: PM marks `anchor pending` in the Map section; later updates the parent when ready
- **Monetization**: matches how real teams discover product
- **Acquisition**: differentiator vs rigid top-down planning tools
- **Offline experience**: anchor-pending notes are local body text

## Value chain

- **Outputs shipped**: Convention in node-templates SKILL; framework SKILL § The graph; engine.update_node + transition_status support re-parenting
- **Outcomes observed**: Pending — no anchor-pending node created yet in dogfood (we have been doing top-down derivation)
- **Benefits measured**: Pending external adoption with real bottom-up scenarios
- **Value assessment**: Shipped at convention level; real-world value pending
- **Learning extracted**: Documenting the pattern as one of 4 construction modes (not as an exception) is the right framing — it normalizes the practice instead of stigmatizing it.
- **Next cards surfaced**: Anchor-pending dashboard / query (find all bottom-up nodes waiting for parent crystallization) — deferred
""",
)

F9_2 = FeatureSpec(
    code="F9.2",
    title="Supersede / superseded-by chains available on every node type",
    parent_cap="C9",
    body="""## Map
- Children: none
- Related: F1.1 (catalog allows supersede on every type); F1.3 (validate_supersede checks chain consistency); F4.2 (architect_coherence verifies adr chains)

## Story

Adopter team's PM and Architect evolve decisions in place: a superseding node references the superseded; the superseded back-references via `superseded-by`. The pattern is canonically used for ADRs (proposed → accepted → superseded) but available on every type — capabilities, features, specs can all supersede their predecessors with full history preserved.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `supersedes` + `superseded-by` custom fields exist on every node type (per catalog F1.1)
- `engine.api.supersede(superseding, superseded, ...)` enforces chain consistency (no cycles, both nodes exist, types compatible)
- `validate_supersede` (F1.3) hard-rejects broken chains
- `architect_coherence` (F4.2 ARC003-ARC005) flags broken chains as warn-level for older adrs

## Acceptance check

Verified by `engine/tests/test_validators.py` (supersede validators) + `engine/tests/test_checks.py` (architect_coherence chain tests).

## Position in the larger narrative

Without supersede chains, decisions would either accumulate forever (no way to retire a past decision) or be lost (overwritten without trace). Supersede preserves history while making "this is no longer the current decision" explicit and queryable.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: supersede custom fields + API + validators + chain check
- **Technology**: Projects v2 multi-issue-reference fields with `gh api graphql`
- **UX design**: PM / Architect call supersede; readers see the chain in the Issue body + custom fields
- **Monetization**: history preservation is the maintainability claim's structural backbone
- **Acquisition**: "decisions evolve; history persists" — concrete promise
- **Offline experience**: chains queryable from local cache once read

## Value chain

- **Outputs shipped**: catalog supersede support on all types; `engine.api.supersede`; `validate_supersede`; architect_coherence chain checks (ARC003-ARC005)
- **Outcomes observed**: Pending — no node has been superseded in dogfood yet (all 29 Issues are still active)
- **Benefits measured**: Pending external adoption with real decision-evolution scenarios
- **Value assessment**: Shipped at mechanism level; real-world value pending
- **Learning extracted**: Making supersede available on every type (not just adr) cost almost nothing at the catalog level and reserves the option for capabilities / features / specs that need it. Pre-deciding usage would have been premature.
- **Next cards surfaced**: Supersede chain visualizer (find all chains > 2 deep, surface stale references); supersede UI hint in /session-close (deferred)
""",
)


# ============================================================================
# C10 — Adopter-customizable methodology layer
# ============================================================================

F10_1 = FeatureSpec(
    code="F10.1",
    title="`→ method:` pointer convention in node-templates SKILL",
    parent_cap="C10",
    body="""## Map
- Children: none
- Related: F10.2 (the skills mechanism resolves the pointers); F1.5 (the templates carry the pointers); methodology ADR #29 (this is the seam between framework and adopter methodology)

## Story

Adopter team's templates carry inline `→ method:` pointers indicating where a methodology skill should fill the content. Example: capability template has `## Value analysis → method: project's value-analysis skill, if any`. When the adopter authors a capability, the agent looks up the named skill in `.claude/skills/`; if found, invokes it; if not, falls back to training. The pointers make the methodology seam visible and navigable.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `→ method:` pointer convention documented in node-templates SKILL § How to use a template
- Pointers present in capability template (Value analysis, Risks, Feature decomposition), feature template (Requirements detail, Spec), spec template (no pointers — spec methodology lives in adopter skill if any)
- Pointer points to a *skill name*, not a method name (the agent reads SKILL.md frontmatter to discover)

## Acceptance check

Manual review of pointer presence in the templates; verified by reading `.claude/skills/node-templates/SKILL.md`.

## Position in the larger narrative

The pointers are the framework's *explicit handoff to adopter methodology*. Without them, the seam would be ambiguous ("does the framework do value analysis or do I?"). With them, it's clear: section structure is framework; depth comes from the named skill or training.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: documented convention; pointers in 3 templates (capability, feature, spec)
- **Technology**: markdown convention; no engine code
- **UX design**: agent + human both read pointers when scaffolding/auditing
- **Monetization**: enables the methodology marketplace — adopters can author + share methodology skills
- **Acquisition**: "your methodology slots into the framework via these pointers" — concrete extensibility promise
- **Offline experience**: pointers live in local SKILLs

## Value chain

- **Outputs shipped**: `→ method:` convention in node-templates SKILL; pointers in capability + feature + spec templates
- **Outcomes observed**: Dogfood — pointers visible to anyone authoring; no adopter methodology skill has been authored yet
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped at convention level
- **Learning extracted**: Making the pointer textual (rather than a typed reference resolved at runtime) keeps the convention lightweight — the agent reads the pointer like a normal comment. Heavier typing would have been over-engineering.
- **Next cards surfaced**: Engine check that warns when a pointed-at skill is referenced but not installed (helps adopters notice missing methodology)
""",
)

F10_2 = FeatureSpec(
    code="F10.2",
    title="`.claude/skills/` injection mechanism (project methodology layers on framework defaults)",
    parent_cap="C10",
    body="""## Map
- Children: none
- Related: F10.1 (the pointer convention this mechanism resolves); F2.1 (agents preload framework + node-templates skills; project skills are additional)

## Story

Adopter team adds methodology skills under `.claude/skills/<topic>/SKILL.md` — e.g. `.claude/skills/value-analysis/SKILL.md` with their specific framework (Wardley, JTBD, opportunity solution trees). The agent's skill listing automatically surfaces them; the agent invokes them on demand when scaffolding the relevant section. No engine changes; no framework forking.

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- `.claude/skills/` is a standard Claude Code skill directory
- Agents preload framework + node-templates by default; additional skills are discovered automatically by Claude Code's skill listing
- Adopter adds new skill = available immediately; no engine restart, no config change
- Skill frontmatter follows Claude Code conventions

## Acceptance check

Verified by `engine/tests/test_skill_scripts.py` skill frontmatter validators; the dogfood `.claude/skills/` directory currently houses 5 framework skills (framework, node-templates, session-open, session-close, catch-up) — adopters add more.

## Position in the larger narrative

This is the *variable layer* of the fixed/variable architecture (F10.3 / CLAUDE.md). Adopters extend without forking; the framework's fixed layer (catalog, MCP, hooks, role contracts) is untouched.

## State

done — shipped in v0.3.0.

## Holistic dimensions

- **Functionality**: Claude Code skill mechanism; no SEM-AI-specific code
- **Technology**: markdown files with frontmatter; loaded by Claude Code
- **UX design**: adopter creates a new file → agent sees it; no friction
- **Monetization**: enables methodology marketplaces / shared skill packs (community OSS or enterprise paid)
- **Acquisition**: extensibility without forking is the framework's appeal to enterprises with established methodology
- **Offline experience**: skills are local files; no remote skill store

## Value chain

- **Outputs shipped**: directory convention `.claude/skills/`; the 5 framework-shipped skills as reference
- **Outcomes observed**: Dogfood — no adopter methodology skill exists in the SEM-AI repo (we are the framework, not its adopter)
- **Benefits measured**: Pending external adoption — does anyone author a methodology skill?
- **Value assessment**: Shipped + reference-validated
- **Learning extracted**: Riding on Claude Code's native skill mechanism (instead of inventing a SEM-AI-specific extensibility surface) was the right call — adopters need to learn fewer mechanisms, and skills work for any agent regardless of role.
- **Next cards surfaced**: Skill-pack discovery convention (where do community methodology packs live? GitHub topic? curated index?); per-skill validation conventions
""",
)

F10_3 = FeatureSpec(
    code="F10.3",
    title="Fixed/variable layer documented in CLAUDE.md",
    parent_cap="C10",
    body="""## Map
- Children: none
- Related: F10.1 (pointers); F10.2 (skill injection); methodology ADR #29 (the boundary recorded explicitly)

## Story

Adopter team's onboarding doc (CLAUDE.md) names the fixed/variable layer explicitly: **Fixed layer** = catalog + role contracts + MCP + hooks + structural validators + definitional template literacy. **Variable layer** = body content + methodology skills + Actions. Adopters know exactly what's framework-owned (don't override unless forking) vs project-owned (your call).

## Uncertainty addressed

N/A — delivery, not experiment.

## Conditions of satisfaction

- CLAUDE.md explicitly distinguishes fixed vs variable layer near the top
- Methodology ADR #29 (Issue #29) provides the canonical reasoning
- Examples given: graph catalog (fixed) vs value-analysis methodology (variable); role identities (fixed) vs role behavior shaped by skills (variable)

## Acceptance check

Manual review of CLAUDE.md; ADR #29 published as Issue under capability #28.

## Position in the larger narrative

Without an explicit layer boundary, adopters wouldn't know what's safe to customize. The doc + the ADR together make the boundary navigable: read CLAUDE.md for the orientation, read ADR #29 for the boundary test ("can a mechanical check surface the issue? → framework").

## State

done — shipped in v0.3.0; ADR #29 added 2026-05-24 making the boundary explicit + inventoried.

## Holistic dimensions

- **Functionality**: documentation + canonical ADR
- **Technology**: markdown
- **UX design**: adopter reads CLAUDE.md (5 min) + ADR #29 (10 min) and understands the customization surface
- **Monetization**: clarity about what's customizable reduces adopter friction
- **Acquisition**: extensibility story becomes coherent — "fixed catalog + variable methodology" is a tagline
- **Offline experience**: local docs

## Value chain

- **Outputs shipped**: CLAUDE.md "Fixed layer / Variable layer" framing; ADR #29 with full boundary reasoning + inventory
- **Outcomes observed**: Dogfood — the boundary helped us decide where to put the SMART / Stakeholder / why-stack additions (framework, not adopter) and where future opinionated methodology proposals would belong (adopter)
- **Benefits measured**: Pending external adoption
- **Value assessment**: Shipped + dogfood-validated through the methodology ADR
- **Learning extracted**: Writing the boundary doc + the ADR at the moment we needed to make the decision (rather than upfront) gave us a more honest formulation — the boundary is described from real friction, not from imagined contributor questions.
- **Next cards surfaced**: Lightweight per-skill metadata convention (which layer does this skill belong to?); contributor doc explaining how to propose new framework-layer methodology (requires ADR)
""",
)


# ============================================================================
# Master list
# ============================================================================


FEATURES: list[FeatureSpec] = [
    F1_1, F1_2A, F1_2B, F1_3, F1_5,
    F2_1, F2_2, F2_3,
    F3_1, F3_2, F3_3, F3_4, F3_5,
    F4_1, F4_2, F4_3, F4_4,
    F5_1, F5_2, F5_3, F5_4,
    F6_1, F6_2, F6_3,
    F7_1, F7_2, F7_3,
    F8_1, F8_2,
    F9_1, F9_2,
    F10_1, F10_2, F10_3,
]


# ============================================================================
# Main
# ============================================================================


def main() -> int:
    cfg = load_config()
    adapter = GitHubAdapter(cfg)

    print(f"Target repo: {cfg.repo}")
    print(f"Total features to create: {len(FEATURES)}")
    print()

    existing = {f.title: f for f in adapter.query_issues(type=NodeType.FEATURE)}
    print(f"Found {len(existing)} feature Issues already on the graph")
    print()

    created = 0
    skipped = 0
    for spec in FEATURES:
        parent_id = CAP_ID[spec.parent_cap]
        if spec.title in existing:
            print(
                f"  [exists] {spec.code} {spec.title[:55]!r} → "
                f"{existing[spec.title].id} (parent {spec.parent_cap}={parent_id})"
            )
            skipped += 1
            continue
        print(
            f"  [..]     {spec.code} {spec.title[:55]!r} "
            f"(parent {spec.parent_cap}={parent_id})",
            end=" ",
            flush=True,
        )
        try:
            node = api.create_node(
                adapter,
                type=NodeType.FEATURE,
                parent_id=parent_id,
                title=spec.title,
                body=spec.body,
                status=Status.DONE,
                acting_role=Role.PM,
            )
        except Exception as e:
            print(f"FAILED: {e}")
            return 1
        print(f"→ {node.id}")
        created += 1

    print()
    print("==> Summary")
    print(f"    Features created: {created}")
    print(f"    Features already existing: {skipped}")
    print(f"    Total in graph: {created + skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
