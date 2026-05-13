---
name: architect-architecture-design
description: "Draft, refine, or audit the architecture and design of a software application against Capers Jones's seven fundamental architectural topics (overall structure, data, interfaces, decomposition, linkage, performance, security), the Zachman 6×6 schema, and size-driven importance scaling (architecture useful at 1k FP, important at 10k, critical at 100k). Use whenever the human wants to choose an architectural style (monolithic, client-server, 3-tier, N-tier, event-driven, peer-to-peer, model-driven, pattern-based, SOA, cloud), pick a design notation (UML, use-cases, data-flow, state-transition, …), structure the data layer, or run a design inspection. Triggers include phrases like 'architecture', 'design', 'how do we structure this', 'SOA vs monolith', 'event-driven', 'three-tier', 'Zachman', 'design notation', 'do we need an architect for this'."
---

# architect-architecture-design

## Purpose

Architecture grows in importance non-linearly with application size: invisible below 100 function points, critical above 100,000 (Jones Table 7-7). This skill lets the Architect produce or audit architectural decisions that cover the seven fundamental topics Jones inventoried, slot the work onto the Zachman 6×6 schema where useful, choose an architectural style with the trade-offs made explicit, and pick a design notation from the 40+ alternatives in current use without pretending any single one is uniquely correct.

## When this skill applies

- A new application is starting and the architectural style is unset.
- A monolith is being decomposed and the team is choosing between SOA, event-driven, 3-tier, etc.
- Data structures are being designed (hierarchical / relational / row-oriented / column-oriented / OO).
- A design notation must be picked for the project (UML, use-cases, data-flow, etc.).
- An existing application's architecture is being audited (performance bottleneck, security concern, decomposition feels wrong).
- The team disputes whether a 10,000-FP application really needs formal architecture (Jones: yes, it does).

## Formal criteria

An architectural decision is acceptable only if all of the following hold:

1. **All seven fundamental topics addressed** *(Jones Ch 7, p. 470)* — every architecture explicitly covers:
   1. Overall structure of the application.
   2. Structure of the data used by the application.
   3. Interfaces between the application and the outside world.
   4. Decomposition into functional components.
   5. Linkage / transmission of information among the functional components.
   6. Performance attributes associated with the structure.
   7. Security attributes associated with the structure.
   Silence on any topic is the most common architectural defect.
2. **Size-tier respected** *(Jones Table 7-7, p. 472)* —
   - **≤ 100 FP**: no formal architecture needed.
   - **1,000 FP**: architecture useful.
   - **10,000 FP**: architecture important — at least one architect assigned.
   - **100,000 FP**: architecture critical — multiple architects, formal artifacts, inspections mandatory.
   - **>1,000,000 FP** (enterprise scale): Enterprise Architect role (Ch 9 Table 9-23 #2).
3. **Zachman 6×6 schema applied for 10,000+ FP applications** *(Jones BP #14, Table 2-2, p. 76)* — columns *What / How / Where / Who / When / Why* × rows *Planner / Owner / Designer / Builder / Contractor / Enterprise*. The cells need not all be filled; the matrix forces awareness of which decisions are missing.
4. **Architectural style chosen explicitly, with trade-offs documented** *(Jones Ch 7, pp. 473–475)* — the candidate styles include monolithic, client-server, 3-tier, N-tier, event-driven, peer-to-peer, model-driven, pattern-based, service-oriented architecture (SOA), and cloud computing. The chosen style is named, alternatives listed, and the trade-offs against the seven fundamental topics made explicit. Jones (p. 474) is explicit that no architectural style is universally a good or bad choice; the criteria are too hazy to declare a winner without empirical evidence.
5. **Data architecture chosen with awareness** *(Jones Ch 7, p. 473)* — hierarchical, relational, row-oriented, column-oriented, object-oriented data, or hybrid. Data volume and growth rate stated (records, expected growth, retention horizon).
6. **Design notation selected from the 40+ alternatives** *(Jones BP #14, p. 76)* — UML and use-cases dominate as of 2009; older but still valid options include flowcharts, HIPO, Warnier-Orr, Jackson, Nassi-Schneiderman, entity-relationship, state-transition, action diagrams, decision tables, and data-flow diagrams. Hybrid combinations are normal. The choice is recorded; mixing five notations without a primary is the failure mode.
7. **Architectural patterns considered for reuse** *(Jones BP #14, p. 77, links to BP #26)* — when the application belongs to an industry with strong existing patterns (Jones reports ~80% portfolio similarity within industries: banks, insurance, manufacturing, pharma), the architecture starts from those patterns rather than greenfield.
8. **Design inspection scheduled before code** *(Jones BP #14, p. 77, cross-reference to BP #36)* — architecture inspections are the highest-yield defect removal activity for design-stage defects.

## How you proceed

1. **Confirm size tier.** Pull the FP figure from `po-early-sizing`. Without a size, you cannot apply Table 7-7's escalation rule. If FP is missing, surface that as a precondition.
2. **Walk the seven fundamental topics.** For each, write one paragraph that captures the current decision or open question. Topics with "TBD" become explicit work items, not silent gaps.
3. **Choose an architectural style.** List the candidates (monolithic, client-server, 3-tier, N-tier, event-driven, peer-to-peer, model-driven, pattern-based, SOA, cloud). For each plausible candidate, evaluate against the seven topics. The winner is documented with its trade-offs; the rejected candidates are recorded too, so future re-evaluation has a baseline.
4. **Apply the Zachman schema** for 10,000+ FP work. Build the 6×6 matrix and fill the cells the application actually constrains; mark the rest as "not applicable for this application" with a one-line reason.
5. **Choose the data architecture.** Pick the data model (hierarchical / relational / row-oriented / column-oriented / OO / hybrid). State volumes, growth rate (Jones reports software grows ~8%/year; data faster). Note the join points to the application architecture.
6. **Select the design notation.** Pick a primary (UML + use-cases is the modal choice as of 2009). Allow secondary notations for specialized concerns (state-transition for protocol layers, data-flow for ETL pipelines).
7. **Mine the industry pattern set.** If the application is in an industry with strong portfolio similarity (banks/insurance/pharma/manufacturing), start the architecture from the known patterns and document where this application diverges. Greenfield architecture is rarely justified.
8. **Schedule design inspection.** Coordinate with QA (`qa-inspections-program` when that role exists) — inspections of the architecture documents at this stage detect defects an order of magnitude cheaper than catching them in test.

## Pitfalls to avoid

- **Silence on a fundamental topic.** An architecture document that does not address performance, or does not address security, is missing material Jones lists as required. Default for "not applicable" is to write the words "not applicable, because …", not to omit.
- **Universal style winners.** Jones is explicit: no architectural style is universally good or bad. Documenting "we chose SOA" without trade-offs is a religious decision, not an engineering one.
- **Over-engineering small applications.** Below 1,000 FP, formal architecture costs more than it saves (Table 7-7). Apply discipline proportional to size.
- **Greenfield architecture in pattern-rich industries.** Banking, insurance, pharma, and manufacturing have ~80% portfolio similarity (Jones BP #14, p. 77). Starting from scratch ignores empirical patterns.
- **Notation salad.** Mixing UML, data-flow, state-transition, and decision tables without a primary notation makes the design document unreadable. Pick one primary; use others surgically.
- **Single-architect decisions on 100,000+ FP work.** Above this tier Jones recommends a team of architects with formal coordination. One architect making all decisions becomes the bottleneck and the single point of failure.
- **No design inspection.** Skipping architecture inspection moves the defects forward to test or production, where they cost orders of magnitude more.
- **Adopting Bass / Ford / Ousterhout / Martin / Nygard as authority.** These are not in audited `bibliography/sources/`. The concepts (quality attributes, fitness functions, deep modules, dependency rule, ADRs) are widely useful but cannot be cited as anchored authority here. ADRs in particular are common industry practice — adopt the format if useful, but cite as convention, not as Jones-anchored requirement.

## Source

- **Best Practice #14 — *Software Architecture and Design* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 75–77).** Size-driven importance, Zachman 6×6 schema (Table 2-2), 40+ design notation alternatives, reusable design patterns, industry portfolio similarity ~80%.
- **Chapter 7 § *Software Architecture* (Jones 2010, pp. 470–475).** Seven fundamental topics, Table 7-7 size-importance scaling, architectural style evolution (Dijkstra/Parnas 1968 → Mary Shaw / David Garlan), modern styles (monolithic, client-server, 3-tier, N-tier, event-driven, peer-to-peer, model-driven, pattern-based, SOA, cloud), architect assignment scope 5,000–100,000 FP, Jones's explicit warning that style-evaluation criteria are "too hazy" for universal verdicts.
- **Chapter 9 Table 9-23 (Jones 2010, p. 621).** Architect impact: 100,000 FP assignment scope, defect prevention 17%, defect removal 12%. Enterprise Architect: 250,000 FP, 25%, 20%.
- Full traceability: `bibliography/skill-references.md` § `architect-architecture-design`.
