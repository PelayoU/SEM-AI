---
name: product-manager-user-involvement
description: "Design and manage user participation across the project lifecycle using Capers Jones's 12-form involvement inventory, with scale-aware techniques (embedded full-time user for small Agile teams; surveys, focus groups, usability labs for mass-user applications). Use whenever the human asks how users should be involved, plans a user research activity, wonders why users feel unheard, decides whether to embed a user representative, or designs the cadence of user touchpoints. Triggers include phrases like 'user feedback', 'how do we involve users', 'usability lab', 'focus group', 'survey', 'embedded user', 'user representative', 'user satisfaction', 'are users actually involved?'."
---

# product-manager-user-involvement

## Purpose

Software projects fail user-satisfaction tests in two ways: by skipping user participation altogether, or by adopting a single form (e.g., "we have a Product Manager who talks to users") and assuming that covers all twelve forms Capers Jones inventories. This skill lets the Product Manager design a portfolio of user-involvement activities sized to the application — embedded users for small Agile work, surveys and usability labs for mass-user products — with explicit ratios so the team can detect when user involvement is too thin to underwrite satisfaction.

## When this skill applies

- A new project starts and the user-involvement plan is empty.
- The team complains "the users keep changing their mind" — usually a symptom of insufficient or wrong-form involvement, not user volatility.
- A release shipped and users are unhappy despite "we built what they asked".
- The user base is too large or distributed for one embedded user representative.
- A specialized review needs user participation (requirements, design, acceptance test) and the right form is unclear.

## Formal criteria

A user-involvement plan passes review only if all of the following hold:

1. **Twelve forms considered, not assumed** — the plan addresses each of the twelve forms below explicitly, either scheduling it or marking it not applicable with a one-line reason. Implicit coverage is the failure mode.
2. **Effort ratio between 10% and 50% of dev effort** — total user effort sits in the empirical band; the typical average is ~20%. Less than 10% is a satisfaction risk; more than 50% is usually committee overhead.
3. **Scale-appropriate technique** — an embedded full-time user works for small Agile projects and small user populations; mass-user applications (above ~10,000 users) require surveys, focus groups, and usability labs because no single user can know all use cases.
4. **Stakeholder map exists** — "users" is decomposed into Future Users, Indirectly Affected parties, and Decision Makers / Blockers. A plan that does not distinguish them defaults to whichever group has the loudest representative.
5. **Persona or persona-sketch per user type** — each user type is represented by a lightweight persona sketch so the team can reason about whose needs are being served. Anonymous "users" produce anonymous decisions.
6. **Defect-reporting and acceptance-testing loops include users** (forms 11–12) — these two forms are systematically forgotten when user involvement is conceived as upstream-only. Without them, the satisfaction feedback loop never closes.

## How you proceed

1. **Map the user population first.** How many users? How heterogeneous? Are there decision-makers separate from end-users? Use the three categories — Future Users, Indirectly Affected, Decision Makers / Blockers — to make this visible.
2. **Pick scale-appropriate techniques.** Below ~50 users with daily interaction: an embedded full-time user representative (Agile pattern) is viable. Above several thousand: surveys + focus groups + usability labs are the realistic instruments.
3. **Walk the twelve forms.** For each, decide *included* (with planned cadence) or *not applicable* (with reason):
   1. Joint application design (JAD) sessions.
   2. Quality function deployment (QFD).
   3. Reviewing business rules and algorithms mined from legacy applications.
   4. Agile projects on a full-time basis (embedded user representative).
   5. Requirements reviews.
   6. Change control boards.
   7. Reviewing documents produced by contractors.
   8. Design reviews.
   9. Using prototypes and sample screens.
   10. Training classes to learn the new application.
   11. Defect reporting from design through testing.
   12. Acceptance testing.
4. **Estimate user effort and check the ratio.** Sum the planned user hours and divide by the dev team's planned hours. Below 10%, expect satisfaction risk and surface that explicitly. Above 50%, surface that the schedule is committee-bound.
5. **Build persona sketches per user type** — short, lightweight, named. Persona-by-persona, walk every active form: who from this persona class attends, how often, with what authority.
6. **Schedule the satisfaction feedback loop** — forms 11 (defect reporting) and 12 (acceptance testing) close the loop. Without them, the team learns about user dissatisfaction only at retrospective or in the wild.
7. **Re-evaluate at every release boundary.** User involvement decays — embedded users leave, focus groups age out. Refresh the plan event-driven, not calendar-driven.

## Pitfalls to avoid

- **"The Product Manager talks to users" as the entire plan.** Product Manager conversation is one channel of one form. The other eleven forms are independent.
- **One embedded user for a mass-user product.** No single user can know all use cases for an application with thousands of users. Surveys and usability labs are the only scalable instruments.
- **Forgetting indirectly affected parties.** Compliance officers, downstream teams, integration partners — they are users too. They appear at acceptance testing and break the release.
- **No personas.** Forms 1–12 applied to anonymous "users" produce inconsistent decisions because everyone fills in a different mental user when needed.
- **Skipping defect reporting and acceptance testing.** Forms 11 and 12 are the satisfaction feedback loop. They are the most commonly skipped — and the skipping shows up at release as "users are unhappy".
