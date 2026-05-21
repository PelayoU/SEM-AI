---
name: architect-performance-analysis
description: "Plan and execute performance analysis of a software application using profilers, instrumentation, and the performance↔quality↔security overlap principle from Capers Jones, with specialist consideration above 100,000 function points. Use whenever a system is slow or degrading, when load times grow over time, when 'is this a performance bug or a quality bug?' is the open question, when planning the performance budget for a new architecture, or when designing instrumentation for production monitoring. Triggers include phrases like 'performance', 'slow', 'profiling', 'instrumentation', 'why is this degrading', 'load time', 'response time', 'memory pressure', 'mean time to failure', 'denial of service performance impact', 'do we need a performance specialist'."
---

# architect-performance-analysis

## Purpose

Performance failures are systematically misclassified — many are actually quality failures (a high-severity bug drops performance to zero) or security failures (a denial-of-service attack is a performance issue). Capers Jones inventories the relevant tools (profilers, instrumentation, dynamic analysis), names the diagnostic bug taxonomy (heisenbug, bohrbug, mandelbug, schrodenbug), and prescribes specialists above 100,000 FP. This skill lets the Architect plan and run performance work without reinventing the wheel and without treating performance as a discipline disjoint from quality and security.

## When this skill applies

- An application is slow at release or degrades over time.
- A new architecture is being designed and a performance budget must accompany it.
- Production monitoring needs instrumentation and the design must capture instrumentation hooks early.
- A reported "performance bug" needs classification (heisenbug / bohrbug / mandelbug / schrodenbug).
- A 100,000+ FP application is being staffed and the question is whether a performance specialist is needed (Jones: yes).
- A capacity-planning question hits the team during business-cycle peaks (quarter-end, year-end load).

## Formal criteria

A performance analysis pass is acceptable only if all of the following hold:

1. **Performance, quality, and security treated as overlapping, not disjoint** — "performance best practices overlap best practices in quality control and security control. A general set of best practices includes usage of performance specialists, excellence in quality control, and excellence in security control." A performance plan that does not coordinate with QA and Security is incomplete.
2. **Tools chosen from the empirical set** — profilers, performance measurement devices that collect data on the fly, embedded instrumentation inside the application. Choosing tools by fashion rather than by what the team can actually operate is the common failure mode.
3. **Instrumentation overhead accounted for** — instrumentation and other forms of performance analysis may slow down application speed, so care is needed to ensure the data is correct. Instrumentation impact on the measured system is part of the design, not an afterthought.
4. **Bug taxonomy applied to surfaced issues** — every reported performance bug is classified into one of the four diagnostic categories (or marked as a plain functional bug):
   - **Heisenbug** (after Heisenberg's uncertainty): disappears when an attempt is made to study it.
   - **Bohrbug** (after Niels Bohr): occurs under a well-defined set of conditions, does not disappear.
   - **Mandelbug** (after Benoit Mandelbrot): caused by chaotic factors that make isolation difficult.
   - **Schrodenbug** (after Erwin Schrödinger): does not occur until someone notices the code should not have worked at all, and stops working as soon as the bug is "discovered".
   The taxonomy guides the investigation method.
5. **Mean-time-to-failure tracked, not just average response time** — software performance drops to zero when a high-severity bug stops it from running. MTTF (or equivalent availability metric) is part of the performance picture, especially in the first month or two after release.
6. **Business-cycle effects modelled** — financial / accounting / retail systems show predictable performance degradation at quarter-end, year-end, holidays. The performance plan addresses these explicitly, not as surprises.
7. **Specialist threshold respected** — for applications in the 100,000-FP range, employing specialists is a best practice. Below this tier the Architect can hold the role; above it, a Performance Specialist is the Tier-4 escalation.
8. **Architecture- and design-stage attention** — performance optimization rules and algorithms applied at architecture / design stage are dramatically cheaper than at code stage. Performance is an architectural property, not a coding fix.

## How you proceed

1. **Confirm size tier.** Below ~10,000 FP performance work is mostly local optimization; at 100,000 FP it is an architectural concern and a specialist is appropriate. Pull the FP figure from `product-manager-early-sizing`.
2. **Define the performance budget** during architecture (`architect-architecture-design`, topic 6). Latency, throughput, memory ceiling, startup time, mean-time-to-failure. The budget is part of the architecture decision; ad-hoc tuning later is more expensive.
3. **Pick tools.** Profiler for code-level hotspots. Instrumentation embedded in the application for production telemetry. Synthetic load generators for pre-release verification. Operating-system-level profilers for I/O and memory pressure.
4. **Design the instrumentation** so its overhead is bounded and known. Document the overhead at typical sampling rates. Schedule sampling to avoid distorting steady-state behaviour.
5. **Classify each performance issue using the heisenbug / bohrbug / mandelbug / schrodenbug taxonomy.** Investigation method follows from the class:
   - Bohrbug → reproduce, reduce, fix.
   - Heisenbug → minimize observer effect; binary search via log levels.
   - Mandelbug → statistical reproduction; chaos-aware logging; possibly redesign.
   - Schrodenbug → audit the original assumption that the code worked; fix the real bug surfaced.
6. **Coordinate with QA and Security.** Quality (defect rate, defect removal efficiency) and security (DoS surface, vulnerability backlog) directly determine the performance floor. A performance plan running independently of these will fail.
7. **Plan for business-cycle peaks.** Identify the cycles (quarter, year, market events) and run capacity tests against them. Production capacity is sized for peak, not average.
8. **Escalate to specialist at the size threshold.** Above ~100,000 FP, hand off to a Performance Specialist as Tier-4. The Architect remains responsible for the architectural-level decisions; the specialist handles deep optimization.

## Pitfalls to avoid

- **Performance treated as a separate concern from quality and security.** Jones is explicit. The three overlap; siloed plans solve the wrong problem.
- **Unmeasured instrumentation overhead.** Instrumentation that slows the system distorts the data; if the slowdown is unknown, the data is unreliable.
- **Average-response-time fixation.** A system with great average response time and frequent crashes has zero perceived performance during crashes. Track MTTF or equivalent.
- **No bug-class taxonomy.** Treating every performance defect with the same investigation method wastes time. Heisenbugs do not yield to bohrbug methods.
- **Ignoring business cycles.** Capacity sized to average load collapses at quarter-end — a common failure pattern.
- **Late-stage tuning.** Performance applied at code stage rather than architecture stage is order-of-magnitude more expensive. Set the budget during `architect-architecture-design`.
- **Refusing specialist help above 100,000 FP.** Specialists are recommended at this tier; many software-engineering curricula do not teach performance analysis. Filling the gap with generalists is malpractice.
- **DoS surface not analysed jointly with Security.** Jones is explicit that performance, quality, and security overlap: a DoS attack is a performance issue; error-handling routines are major attack vectors. Dispatch `security-officer-threats-and-defenses` to enumerate DoS vectors and `security-officer-architecture` for architectural mitigations (rate limiting, capability boundaries, isolation). Treating performance, quality, and security as disjoint produces solutions to the wrong problem.
