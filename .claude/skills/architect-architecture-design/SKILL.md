---
name: architect-architecture-design
description: "Draft, refine, or audit the architecture and design of a software application against Capers Jones's seven fundamental architectural topics (overall structure, data, interfaces, decomposition, linkage, performance, security), the Zachman 6×6 schema, and size-driven importance scaling (architecture useful at 1k FP, important at 10k, critical at 100k). Use whenever the human wants to choose an architectural style (monolithic, client-server, 3-tier, N-tier, event-driven, peer-to-peer, model-driven, pattern-based, SOA, cloud), pick a design notation (UML, use-cases, data-flow, state-transition, …), structure the data layer, or run a design inspection. Triggers include phrases like 'architecture', 'design', 'how do we structure this', 'SOA vs monolith', 'event-driven', 'three-tier', 'Zachman', 'design notation', 'do we need an architect for this'."
---

# architect-architecture-design

## Purpose

Architecture grows in importance non-linearly with application size: invisible below 100 function points, critical above 100,000. This skill lets the Architect produce or audit architectural decisions that cover the seven fundamental topics Capers Jones inventoried, slot the work onto the Zachman 6×6 schema where useful, choose an architectural style with the trade-offs made explicit, and pick a design notation from the 40+ alternatives in current use without pretending any single one is uniquely correct.

## When this skill applies

- A new application is starting and the architectural style is unset.
- A monolith is being decomposed and the team is choosing between SOA, event-driven, 3-tier, etc.
- Data structures are being designed (hierarchical / relational / row-oriented / column-oriented / OO).
- A design notation must be picked for the project (UML, use-cases, data-flow, etc.).
- An existing application's architecture is being audited (performance bottleneck, security concern, decomposition feels wrong).
- The team disputes whether a 10,000-FP application really needs formal architecture (Jones: yes, it does).

## Formal criteria

An architectural decision is acceptable only if all of the following hold:

1. **All seven fundamental topics addressed** — every architecture explicitly covers:
   1. Overall structure of the application.
   2. Structure of the data used by the application.
   3. Interfaces between the application and the outside world.
   4. Decomposition into functional components.
   5. Linkage / transmission of information among the functional components.
   6. Performance attributes associated with the structure.
   7. Security attributes associated with the structure.
   Silence on any topic is the most common architectural defect.
2. **Size-tier respected** —
   - **≤ 100 FP**: no formal architecture needed.
   - **1,000 FP**: architecture useful.
   - **10,000 FP**: architecture important — at least one architect assigned.
   - **100,000 FP**: architecture critical — multiple architects, formal artifacts, inspections mandatory.
   - **>1,000,000 FP** (enterprise scale): the Enterprise Architect role.
3. **Zachman 6×6 schema applied for 10,000+ FP applications** — columns *What / How / Where / Who / When / Why* × rows *Planner / Owner / Designer / Builder / Contractor / Enterprise*. The cells need not all be filled; the matrix forces awareness of which decisions are missing.
4. **Architectural style chosen explicitly, with trade-offs documented** — the candidate styles include monolithic, client-server, 3-tier, N-tier, event-driven, peer-to-peer, model-driven, pattern-based, service-oriented architecture (SOA), and cloud computing. The chosen style is named, alternatives listed, and the trade-offs against the seven fundamental topics made explicit. Jones is explicit that no architectural style is universally a good or bad choice; the criteria are too hazy to declare a winner without empirical evidence.
5. **Data architecture chosen with awareness** — hierarchical, relational, row-oriented, column-oriented, object-oriented data, or hybrid. Data volume and growth rate stated (records, expected growth, retention horizon).
6. **Design notation selected from the 40+ alternatives** — UML and use-cases dominate as of 2009; older but still valid options include flowcharts, HIPO, Warnier-Orr, Jackson, Nassi-Schneiderman, entity-relationship, state-transition, action diagrams, decision tables, and data-flow diagrams. Hybrid combinations are normal. The choice is recorded; mixing five notations without a primary is the failure mode.
7. **Architectural patterns considered for reuse** — when the application belongs to an industry with strong existing patterns (Jones reports ~80% portfolio similarity within industries: banks, insurance, manufacturing, pharma), the architecture starts from those patterns rather than greenfield.
8. **Design inspection scheduled before code** — architecture inspections are the highest-yield defect removal activity for design-stage defects.

## How you proceed

1. **Confirm size tier.** Pull the FP figure from `product-manager-early-sizing`. Without a size, you cannot apply the escalation rule. If FP is missing, surface that as a precondition.
2. **Walk the seven fundamental topics.** For each, write one paragraph that captures the current decision or open question. Topics with "TBD" become explicit work items, not silent gaps.
3. **Choose an architectural style.** List the candidates (monolithic, client-server, 3-tier, N-tier, event-driven, peer-to-peer, model-driven, pattern-based, SOA, cloud). For each plausible candidate, evaluate against the seven topics. The winner is documented with its trade-offs; the rejected candidates are recorded too, so future re-evaluation has a baseline.
4. **Apply the Zachman schema** for 10,000+ FP work. Build the 6×6 matrix and fill the cells the application actually constrains; mark the rest as "not applicable for this application" with a one-line reason.
5. **Choose the data architecture.** Pick the data model (hierarchical / relational / row-oriented / column-oriented / OO / hybrid). State volumes and growth rate (Jones reports software grows ~8%/year; data faster). Note the join points to the application architecture.
6. **Select the design notation.** Pick a primary (UML + use-cases is the modal choice as of 2009). Allow secondary notations for specialized concerns (state-transition for protocol layers, data-flow for ETL pipelines).
7. **Mine the industry pattern set.** If the application is in an industry with strong portfolio similarity (banks/insurance/pharma/manufacturing), start the architecture from the known patterns and document where this application diverges. Greenfield architecture is rarely justified.
8. **Schedule design inspection.** Coordinate with QA (`qa-inspections-program` when that role exists) — inspections of the architecture documents at this stage detect defects an order of magnitude cheaper than catching them in test.

## Pitfalls to avoid

- **Silence on a fundamental topic.** An architecture document that does not address performance, or does not address security, is missing material Jones lists as required. Default for "not applicable" is to write the words "not applicable, because …", not to omit.
- **Universal style winners.** Jones is explicit: no architectural style is universally good or bad. Documenting "we chose SOA" without trade-offs is a religious decision, not an engineering one.
- **Over-engineering small applications.** Below 1,000 FP, formal architecture costs more than it saves. Apply discipline proportional to size.
- **Greenfield architecture in pattern-rich industries.** Banking, insurance, pharma, and manufacturing have ~80% portfolio similarity (Jones). Starting from scratch ignores empirical patterns.
- **Notation salad.** Mixing UML, data-flow, state-transition, and decision tables without a primary notation makes the design document unreadable. Pick one primary; use others surgically.
- **Single-architect decisions on 100,000+ FP work.** Above this tier Jones recommends a team of architects with formal coordination. One architect making all decisions becomes the bottleneck and the single point of failure.
- **No design inspection.** Skipping architecture inspection moves the defects forward to test or production, where they cost orders of magnitude more.