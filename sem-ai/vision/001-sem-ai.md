---
type: vision
status: draft
created: 2026-05-20
updated: 2026-05-22
maintained_by_role: product-manager
---

# Vision — SEM-AI

> **Pre-migration note**: this file is the canonical vision of the SEM-AI project. It was authored in the SQLite-backed reference implementation (`.sem/graph.db`) on 2026-05-20 and saved here on 2026-05-22 as the first node migrated to the GitHub-backed file convention (per `PIVOT-TO-GITHUB.md`). Once the full migration runs (Día 3 of the pivot plan), this file will be the authoritative vision; the SQLite record becomes historical reference.

## Why (start with why)

Working with AI is now the default mode of software development. The industry has settled this over the last two years: engineer and model operate collaboratively, with no fixed division of labour — sometimes the human writes and the AI reviews, sometimes the AI produces and the human validates, sometimes both dialogue over a decision. This is the position from which everything else is reasoned, not an assumption to be reproved.

That mode introduces an operational problem the classical Software Engineering Management (SEM) discipline does not absorb. AI, by *structural* deficiencies — no memory across sessions, no perspective of its own, no scope sense, confirmation bias — continually does what it should not: it leaves the agreed architecture, introduces redundant code, touches modules outside scope, forgets conventions, contradicts decisions already taken. It transgresses, precisely, the same dimensions classical SEM separates into roles (scope, architecture, implementation, quality, security, deployment). And the human reviewing AI output must verify all of them, in parallel, while producing — a job classical SEM's review layer (Product Manager, Architect, QA, Security) was never designed for: those roles were built to review a *human* who writes code (and therefore already internalizes architecture, scope, conventions), not a human who in turn reviews *AI* output. The cost does not get absorbed by the upper roles; it multiplies in layers — once on the developer reviewing in parallel, again on each upper role re-doing the check from scratch.

The empirical fingerprint of that multiplied cost is already in the literature. METR (2025) measured a 19% effective slowdown when working with AI on mature repositories. Uplevel (2024) recorded a 41% increase in bug rate per commit among Copilot users. Stack Overflow's 2025 Developer Survey reports 66% of developers frustrated by "almost-correct" outputs that demand costly debugging. Faced with that cost, two opposite reactions emerge in the field: relegate AI to accessory work (lose productivity, fall out of the ecosystem) — or stop reviewing and slide into vibe coding (ship time bombs of subtle bugs, vulnerabilities, wrong architecture, unmaintainable code). Both are rational responses to a cost the practitioner is being asked to absorb alone. Neither is the right answer.

The right answer is that working with AI requires its own management infrastructure.

## The future as a socio-technical system

Three years from now, the engineer working with AI is no longer the sole bearer of the review cost AI generates. Around that engineer lives an infrastructure of role-homologous AI agents — one for each dimension classical SEM separates into a role (scope, architecture, implementation, quality, security, deployment). Each agent operates within its jurisdiction on a shared substrate of project intent: the same artifacts the human roles read, write, and validate. The agent and the human do not work from divergent representations — the decision the human Architect signs off on is the decision the Architect-agent recorded; the scope the human Product Manager validates is the scope the PM-agent worked. Human review on the AI's output collapses from *discovery* — searching for what drifted — to *validation* — confirming what was already recorded as compliant.

Two consequences follow.

First, the two failure reactions of today lose their motivator. Vibe coding loses its: the infrastructure does not permit unrecorded work — every piece of intent has its place and every decision a persistence point, so delegation without reading leaves a trail that exposes itself. Skepticism loses its: the review cost is absorbed by the infrastructure as a structural property of the system, not paid by the practitioner as discretionary labour. Neither reaction remains rational once the cost that motivated them is absorbed structurally.

Second, because each SEM role has a homologous AI agent that holds it in its dimension, what classical SEM needed several humans to sustain rigorously, a single human can now sustain without collapse — alternating between agents as the role being exercised changes. The infrastructure works for a team (each human paired with their role-agent) and for one engineer (the same human, multi-role, alternating). The human composition flexes around an unchanged infrastructure. The AI does not take the human's place; it takes the place organizational infrastructure used to occupy *around* human work, reformulated now to also absorb the specific cost of working with AI.

## The future product story

SEM-AI is the materialization of that infrastructure. It is a Software Engineering Management discipline *for working with AI* — six role-homologous AI agents (Product Manager, Architect, Developer, QA, DevOps, Security), each scoped to its jurisdiction, operating over a shared typed project-intent graph that is the substrate. The methodology each agent applies is not improvised: it is encoded in audited bodies (Cagan for product, Jones for measurement and discipline, Fagan for inspection, Humble & Farley for deployment), so the agent performs its dimensional labour faithfully — the same labour a senior practitioner in that discipline would perform, only consistently, at the pace AI work generates it, and persisted in the substrate rather than lost in conversation.

The engineer does not invoke the system — the engineer *inhabits* it. Intent, decisions, scope, quality posture, security posture, and the code that satisfies them all live in one connected substrate that the human is the author of and the agents maintain. Authorship and judgment remain with the human throughout; the agents do not take the deciding mind, they take the dimensional labour that, in classical SEM, several specialists were needed to perform.

## One-breath narrative

SEM-AI is a Software Engineering Management discipline for working with AI: a layer of role-homologous AI agents around the engineer, each scoped to one classical SEM dimension and operating over a shared typed project-intent graph, so the review cost AI generates is absorbed by infrastructure instead of by the human — and the same infrastructure works for a team or for a single engineer.

## Positioning statement

> For **engineers working with AI** — in teams or alone — who **find that AI's structural deficiencies (no memory, no perspective, no scope sense, confirmation bias) generate a review cost that classical SEM does not absorb and that multiplies in layers**, **SEM-AI** is **a Software Engineering Management infrastructure for AI-collaborative work** that **stands up the SEM roles as homologous AI agents operating over a shared typed intent graph, on the same artifacts the human roles validate against later**. Unlike **chat-based AI coding assistants** (which produce output but do not absorb its review cost) and **classical SEM tooling** (which was built to review humans writing code, not humans reviewing AI output), **SEM-AI absorbs the review cost structurally — turning human review from discovery into validation — and therefore dissolves the conditions that make skepticism and vibe coding rational reactions to AI today**.

## Horizon

**Three years (2026 → 2029).** Long enough that the infrastructure thesis compounds across multiple releases, that the role-agent contract matures against real engineers (team and solo) and real projects, and that the empirical claim — review cost absorbed structurally — can be measured against the same literature that today documents the cost (METR, Uplevel, Stack Overflow). Short enough that the trends adopted below — the industry-settled mode of working with AI, the persistence of classical SEM's audited bodies, current LLM reliability inside a role contract — are still credibly believable rather than speculation. The multi-human collaboration layer at server scale (shared DB, RBAC, cross-user sync) is acknowledged as an additional layer reached *within* this horizon, not its premise.

## Adopted trends

- **Working with AI is the settled default mode of software development.** Over the last two years the industry has converged on AI-collaborative engineering as the standard practice; this is the position the vision reasons from, not an assumption to be re-proven.
- **AI's structural deficiencies are not transient.** No memory across sessions, no perspective of its own, no scope discipline, confirmation bias — these are properties of how the tools are built and used at scale, not artefacts that dissolve with model size. Infrastructure is the lever that absorbs them; raw model capability is not.
- **Classical SEM disciplines are settled and durable.** Product management, measurement and discipline, formal inspection, the function-point family — decades-stable, audited bodies of work. A product built on them as the *shape* of the AI-agent layer will not be invalidated by methodology fashion within the horizon.
- **LLM agents are now reliable enough to operate inside a role contract.** They can consult each other, dispatch within jurisdiction, and refuse out-of-scope work — the unlock that makes a "company of role-agents around the engineer" plausible rather than rhetorical.
- **Project intent must be machine-readable to be useful to agents.** Markdown documents alone are not enough. Typed, queryable graphs of intent — the substrate SEM-AI operates on — become the standard for any serious AI-agent work.
- **The same infrastructure scales from one engineer to a team without rebuild.** Because each SEM role has a homologous agent, the human composition (one engineer alternating across roles, or several engineers each paired with a role-agent) flexes around an unchanged infrastructure — so a single product addresses both segments, with the multi-human collaboration layer added inside the horizon rather than forking the product.
