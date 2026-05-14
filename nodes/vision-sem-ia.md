---
category: vision
id: vision-sem-ia
status: draft
created: 2026-05-14
updated: 2026-05-14
---

# Vision — AI as infrastructure for Software Engineering Management

> Authored via `po-vision`. Canonical criteria: Cagan's Ten Principles of Product Vision (GISF `gisf-discovery.pdf` slide 89) + 5-step construction method (slide 86) + 2-to-10-year horizon (slide 82).

## Statement

In 2031, working with AI in software engineering is no longer a productivity gamble: it has its own management infrastructure. Anyone running a software engineering effort — from a solo builder to a large enterprise — operates with the discipline of a full SE organization, because the organizational layer that used to depend on human bandwidth has been reformulated as a substrate of homologous AI agents that read, write and verify on the project's vault and coordinate handoffs. The agents absorb the cost specific to working with AI (review burden, hallucination, scope drift, context loss); the human keeps authorship, judgement and the right to sign.

## Time horizon

**5 years (target: 2031).** Above 2 years and below 10, per Cagan / GISF `gisf-discovery.pdf` slide 82.

## Positioning statement (slide 84)

For **anyone running a software engineering effort, from solo builder to large enterprise**,
who **cannot afford the review cost, technical debt and scope drift that working with AI introduces, yet cannot afford to skip AI either**,
**SEM-IA**
is **an AI-as-infrastructure framework — a reformulation of Software Engineering Management for the AI era**
that **provides one homologous AI agent per classical SE role (Product Owner, Architect, QA, Developer, DevOps; Security and Designer planned), each reading, writing and verifying a traceable vault and coordinating handoffs under human direction**.
Unlike **AI-as-tool (undifferentiated chat copilots) or AI-as-employee (autonomous agents that appropriate execution)**,
SEM-IA **places AI in the position previously occupied by organizational infrastructure — reformulated to also absorb the cost specific to working with AI — so authorship, judgement and signature remain human at every scale**.

## 5-step construction trace (slide 86)

1. **Time horizon set** — 5 years (target 2031).
2. **Future described as a socio-technical system** (ignoring the product) — A software engineering effort of any size operates with the same level of organizational rigor. The infrastructure that used to require headcount — a PO guarding scope, an Architect guarding decisions, a QA guarding quality, a DevOps guarding release, a Developer writing code, plus Security and Designer where the work demands it — exists as a substrate of role-specific agents. Each agent has its own scope, custody, bibliography and skills; each reads and writes the part of the project's vault that concerns its role; agents coordinate handoffs through the vault rather than through meetings. The human directs; the agent maintains. AI's specific costs (hallucinations, scope drift, context loss, review burden) are absorbed by the substrate by design, not retrofit.
3. **Future product story told** — SEM-IA is that substrate: a framework that makes the seven classical SE roles available as agents grounded in audited bibliography (Capers Jones, Marty Cagan, GISF UC3M, Patton, Cohn, Cucumber) and a curated catalog of skills, all backed by a navigable graph of markdown nodes that traces vision through code.
4. **Story communicated** (one-breath statement, principle 10) — *"SEM-IA is AI-as-infrastructure: one homologous agent per classical SE role, vault-mediated, human-directed, making software engineering rigor available at any scale."*
5. **Positioning statement written** — above.

## Ten Principles of Product Vision — self-check (slide 89, verbatim)

1. **Start with why.** ✅ — Why = the AI-specific cost (review, hallucination, scope, context) that today blocks AI adoption in enterprises and prevents freelancers from scaling. Without absorbing this cost, AI adoption is not viable.
2. **Fall in love with the problem, not the solution.** ✅ — Problem named structurally: working with AI lacks its own management infrastructure. The agent-per-role implementation is one materialisation; the problem is the anchor.
3. **Don't be afraid to think big, with vision.** ✅ — Paradigm-level claim: "AI as infrastructure" vs. AI-as-tool / AI-as-employee. Targets all of SE work, not a niche.
4. **Don't be afraid to disrupt yourself.** ✅ — Reformulates classical SEM and explicitly rejects the "AI as autonomous worker" framing currently in fashion.
5. **Product vision needs to inspire.** ✅ — Reading this, a competent engineer sees why this layer is missing and would want to build it.
6. **Determine and adopt relevant and significant trends.** ✅ — Anchored on: LLM capability curve, AI-tool proliferation outpacing AI-process maturity, demand for AI traceability and audit (EU AI Act, ISO/IEC 42001), knowledge-work bandwidth crisis.
7. **Skate where the puck is going, not where it was.** ✅ — In 2025 the question is "should we use AI?". In 2031 it will be "what's our SEM-IA?". The vision targets the latter.
8. **Be stubborn in vision, but flexible in details.** ✅ — Vision is durable (paradigm + red line). Role count, bibliography, template format, skill mechanics are all flexible.
9. **Keep in mind that any product vision is an act of faith.** ✅ — The act of faith: "AI as infrastructure" beats "AI as employee" durably, even as autonomous agents improve. Authorship stays human, mandatorily.
10. **Evangelize continuously and relentlessly.** ✅ — One-breath statement ready (step 4 above).

## Origin

Formulated by **pelayo** (human PO of SEM-IA) during session [[2026-05-14-sem-ia-self-bootstrap]], drafted with the PO-agent applying skill `po-vision`. The vision absorbs an earlier TFM thesis paragraph by the same author — reformulated as infrastructure (not as persona-product), with the role list pruned to the current catalog (5 implemented + Security + Designer planned; Coach and Quant removed as legacy).

## Source

- Skill: `po-vision`.
- Cagan, *Inspired* — Ten Principles + 5-step method, captured in GISF UC3M `gisf-discovery.pdf` slides 82, 84, 86, 89.
- Origin of "start with why": Sinek, *Start with Why* (Portfolio, 2009).
- Out-of-bibliography reference flagged for traceability: the **"AI as infrastructure"** paradigm framing is the human author's formulation, not anchored in `bibliography/sources/`. It is a conventional thesis statement, not an audited citation.
