---
name: po-spec-gherkin
description: "Produce or refine the formal Gherkin specification for a feature — Feature, Background, Scenario / Scenario Outline, Given / When / Then / And / But, with Acceptance Criteria traceable to story IDs (story-007-A → AC-A1). Use whenever a feature has its stories ready and needs its contract, when an existing spec is ambiguous, when QA needs executable acceptance tests, or when 'what does done mean for this feature' is the open question. Triggers include phrases like 'spec', 'Gherkin', 'acceptance criteria', 'AC', 'Given/When/Then', 'BDD', 'Cucumber', 'specification by example', 'how do we test this', 'is this done?'."
---

# po-spec-gherkin

## Purpose

A feature is only as buildable as its acceptance criteria are unambiguous. Gherkin — the syntax behind Cucumber and Specification by Example — turns the conversation from a story (`po-feature-decomposition`'s 5 Cs) into a contract: a small set of *Given / When / Then* scenarios that the team, the user, and the test runner all read the same way. This skill lets the Product Owner author or refine that contract per feature, anchored in the official Cucumber Gherkin reference and the GISF "Specification by Example" treatment, so QA can validate against it and Developer can implement against it without renegotiation.

## When this skill applies

- A feature has stories that pass INVEST and now needs its acceptance contract.
- An existing spec is ambiguous, missing scenarios, or mixes assertions with implementation hints.
- QA cannot derive tests from the current spec.
- A bug is found that "passed acceptance" — usually because the scenario missed an alternative path.
- A spec is being reviewed for compliance or audit.

## Formal criteria

A spec passes review only if all of the following hold:

1. **Story-to-AC traceability** *(cross-reference to `po-feature-decomposition`)* — every scenario maps to a story identifier. Convention: a story labelled `A` produces `AC-A1`, `AC-A2`, … Each AC carries the story letter so the audit trail is one-glance.
2. **One Feature per `.feature` file (or per spec node)** *(`gherkin-reference.pdf` p. 1)* — *"You can only have a single Feature in a `.feature` file."* The Feature is named with the human capability, not the technical module.
3. **Free-form description follows `Feature:`** *(`gherkin-reference.pdf` p. 1)* — the description states why this feature exists and which business rules it embodies. Description lines are ignored by Cucumber at runtime but available to readers and reporters.
4. **Background only when shared by every scenario** *(`gherkin-reference.pdf`, Background section)* — Background is for steps that *every* scenario needs. If only some scenarios share the precondition, do not use Background.
5. **Scenarios use Given / When / Then** *(`gherkin-reference.pdf` p. 1)* — Given establishes context, When is the action under test, Then is the observable outcome. *And* and *But* extend the previous keyword and read naturally.
6. **Observable outcomes only in Then** *(general Cucumber convention, captured in agile-story-essentials.pdf p. 1)* — *Then* names what the team can observe (state, output, side effect), not what the system "does internally". A *Then* that reads as implementation is the most common spec defect.
7. **Three to five steps per scenario** — long scenarios test more than one thing and become fragile. Split into multiple scenarios.
8. **Scenario Outline + Examples when the same scenario applies across multiple data sets** *(`gherkin-reference.pdf`, Scenario Outline section)* — the table-driven form is preferred over copying scenarios.
9. **Acceptance Criteria block at the head of the spec** *(GISF `gisf-life-cycle.pdf` slide 54: examples form the basis for acceptance criteria; `agile-story-essentials.pdf` p. 1: "before you build, agree on what test confirms done")* — the spec node lists numbered AC (AC-A1, AC-A2, …) above the Gherkin block, each AC stated in one human sentence, then realised as one or more Scenarios below.
10. **All discovered scenarios covered: happy path + alternatives + error cases** — Jones BP #18-19 cross-reference: missing alternative paths is a chief source of defects escaping acceptance.

## How you proceed

1. **Confirm the parent feature has INVEST-passing stories.** A spec authored above shaky stories propagates the ambiguity.
2. **Open the spec artifact** with its parent feature explicitly declared and an initial draft status.
3. **Write the AC block first** *(GISF slide 54)* — for each story letter under the parent feature, write one or more numbered AC sentences:
   ```
   ## Acceptance Criteria
   AC-A1: A signed-in customer can transfer funds between their own accounts.
   AC-A2: A transfer fails with a clear error when the source account lacks funds.
   ```
4. **Translate each AC into Gherkin scenarios.** Use the GISF slide-126 example as the canonical shape:
   ```gherkin
   Feature: Transferring money between accounts
     In order to manage my money more efficiently
     As a bank client
     I want to transfer funds between my accounts whenever I need to

     Scenario: Transferring money to a savings account     # AC-A1
       Given my Current account has a balance of 1000.00
       And my Savings account has a balance of 2000.00
       When I transfer 500.00 from my Current account to my Savings account
       Then I should have 500.00 in my Current account
       And I should have 2500.00 in my Savings account

     Scenario: Transferring with insufficient funds     # AC-A2
       Given my Current account has a balance of 1000.00
       And my Savings account has a balance of 2000.00
       When I transfer 1500.00 from my Current account to my Savings account
       Then I should receive an 'insufficient funds' error
       And I should have 1000.00 in my Current account
       And I should have 2000.00 in my Savings account
   ```
5. **Use Background when every Scenario shares a precondition.** Common cases: a signed-in user, an empty cart, a clean DB. If only some scenarios share it, do not use Background — it creates surprising coupling.
6. **Use Scenario Outline + Examples for table-driven cases.** Identical structure with varying data should not be duplicated.
7. **Apply secondary keywords sparingly** *(`gherkin-reference.pdf` p. 1, secondary keywords)*:
   - `"""` for Doc Strings when a step needs multi-line input.
   - `|` for Data Tables when a step takes structured rows.
   - `@` for Tags to group related Scenarios across files.
   - `#` for Comments at the start of a line.
8. **Review each *Then* for observability.** If it reads as "the system processes …" or "we update internally …", rewrite as the user-visible or test-visible outcome.
9. **Inspect the spec with Developer + QA** before promoting it from draft to accepted. This is the Confirmation step of the 5 Cs cycle and is also one of Jones's requirements inspection forms (BP #11).

## Pitfalls to avoid

- **Multiple Features in one file/node.** Cucumber rejects this implicitly; readers reject it instinctively. One feature per spec.
- **Background used as a kitchen sink.** If only half your scenarios need a step, do not put it in Background — you will spend hours later wondering why a scenario fails.
- **Implementation in *Then*.** *"Then the bank processes the transfer"* is unobservable. *"Then I should have 500.00 in my Current account"* is the right form.
- **Scenarios that test multiple things.** A scenario with twelve steps tests three things and breaks for unrelated reasons. Split.
- **Skipping alternative paths.** Most acceptance escapes are missing alternatives — error cases, edge cases, permission cases. Force at least one *unhappy path* scenario per AC.
- **No mapping from AC to story.** Without `# AC-A1` comments (or equivalent in the spec body), the audit chain story → spec → test breaks.
- **Adopting BDD terminology beyond Gherkin.** Some teams import "Then" to mean "next step in the user journey". That is not Cucumber's semantics; do not import it.
- **Citing Adzic's *Specification by Example* as authority without the book in `bibliography/sources/`.** The concept SbE is captured on GISF slide 126; the executable form is in `gherkin-reference.pdf` (Cucumber official). Cite these. If the human wants Adzic's full SbE framework, surface that the source is not in audited bibliography.

## Source

- **Gherkin syntax — primary and secondary keywords, Feature, Rule, Example/Scenario, Given/When/Then/And/But, Background, Scenario Outline/Examples, Doc Strings, Data Tables, Tags, Comments, one Feature per file** — Cucumber official Gherkin Reference, captured in `gherkin-reference.pdf` pp. 1–9.
- **Specification by Example, full worked Feature ("Transferring money between accounts" with two Scenarios)** — GISF UC3M `gisf-delivery-backlog-management.pdf` slide 126.
- **Examples as basis for Acceptance Criteria of a feature** — `gisf-life-cycle.pdf` slide 54.
- **"Before you build, agree on what test confirms done"** — `agile-story-essentials.pdf` p. 1 (Comakers / Patton 2013).
- **Specification by Example as a class of practice** — Gojko Adzic, *Specification by Example* (Manning, 2011). The book itself is not in audited `bibliography/sources/`; the concept is captured via GISF slide 126 and the executable form via the Cucumber reference above.
- Full traceability: `bibliography/skill-references.md` § `po-spec-gherkin`.
