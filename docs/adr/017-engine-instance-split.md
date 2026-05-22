---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-22
updated: 2026-05-22
maintained_by_role: architect
---

# ADR 017 — Engine / instance split (mechanism vs opinion)

## Context & forces

v0.1 mixed two layers: (a) the generic role discipline that defines *what a Product Manager / Architect / Developer / QA / DevOps / Security Officer does* in **any** methodology and (b) the *specific* methodology citations this project's instance adopts (Cagan, Jones, Cohn / Patton, Fagan, Humble & Farley, Nygard, ANSI / IEEE 1471, ISBSG, IFPUG / COSMIC, SRD). Mixing them locked the engine to one school. A different product running the framework would either inherit citations that do not match its bibliography, or fork the engine.

## Decision

Separate the **engine** (mechanism — methodology-blind) from the **instance** (opinion — YAML + markdown).

- `engine/` (Python package): generic mechanism — read / write / validate / estimate / walk / render — over the YAML config. Methodology-blind: it knows about *node types*, *parents*, *sections*, *thresholds*, *role permissions*, but not about Jones, Cagan, Fagan, etc.
- `instance/` (this project's instance): YAML configs + markdown methodology playbooks declaring this project's opinions. `node_types.yaml` / `thresholds.yaml` / `forbidden.yaml` / `required_fields.yaml` / `lifecycle.yaml` / `jurisdiction.yaml` / `sizing.yaml` + `methodology/*.md` (reference playbooks).

A different product running SEM-AI would replace `instance/` with its own; the engine stays the same.

## Overall structure

Two-layer composition (engine + instance) with the agent.md set sitting on top — the role contract reads from both: discipline criteria are in agent.md (sourced from instance/methodology/), tool calls flow through the engine.

## Data structure

`Instance` dataclass (frozen) loaded once at MCP startup. Subfields: `node_types` · `role_permissions` · `thresholds` · `required_fields` · `forbidden_patterns` · `security_*` · `transitions` · `sizing_coefficients` · `paths`.

## Interfaces to the outside world

Instance is read via `engine.config_loader.load_instance(root)`. No write path: the YAML files are version-controlled and changed via PR like any other file. Hot-reload in the MCP is out of scope.

## Decomposition into functional components

`engine/config_loader.py` is the single import point. Every other engine module accepts an `Instance` as its first arg, no global state.

## Linkage / information transmission

Engine modules pass `Instance` by reference; modules are pure functions over it. Validators / jurisdiction / lifecycle do no IO beyond reading frontmatter via `graph_walker`.

## Performance attributes

Instance load: one-shot at MCP startup, ~10 ms for 7 small YAML files. Validators are pure regex + list scans, O(rules × body-length); on a 100-node project, full revalidation completes in < 500 ms.

## Security attributes

Dispatched to Security Officer.

- Instance YAML is plain data; no code execution path through it.
- Regex patterns are compiled at load time; malformed patterns surface as `re.error` and prevent startup (fail-loud).
- The instance dir is part of the repo and goes through PR review like any other change; an attacker who can edit `instance/` can already commit code.

## Style: chosen + rejected

- **Chosen**: engine in Python + instance in YAML/markdown. Pragmatic, hot-swappable, no DSL to learn.
- **Rejected**: hard-code thresholds in engine. Locks the framework to one methodology — exactly the problem we are solving.
- **Rejected**: JSON instance. YAML's comments + multi-line strings make it more human-readable for methodology config.
- **Rejected**: TypeScript instance (e.g. exporting typed constants). Couples instance to the engine's runtime; a Java engine reading TS configs is awkward; YAML is language-neutral.

## Consequences

- Two products can run SEM-AI side by side with different methodology instances (one Jones, one SAFe, one Modern Agile) and share the engine via package import.
- Methodology drift is mechanical to detect: `instance/thresholds.yaml` changes are visible in PRs; opinions are not buried in code.
- Engine maintenance simplifies (no opinion to update when the bibliography evolves).
- Loss: a methodology change that affects engine semantics (e.g. a new node type with new validators) still requires both an engine change and an instance change. Mitigation: `engine/validators.py` is generic over the rules in `instance/required_fields.yaml` — only structural changes need engine code.

## Design inspection

PR triggers sem-ai-validate; the validator is itself instance-driven, so changes to either layer are equally visible at review time.
