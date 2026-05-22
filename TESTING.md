# Testing the framework

Two layers of verification — the engine's mechanics (pytest, automated) and the framework's discipline (agent-dispatch, manual).

## Engine mechanics — pytest

```bash
.venv/bin/pip install pytest
.venv/bin/pytest tests/ -v
```

Tests live under `tests/`:

- `test_config_loader.py` — `load_instance` parses every `instance/*.yaml` into a frozen Instance with the expected types, roles, thresholds.
- `test_graph_walker.py` — `parse_node_file`, `iter_spine_nodes`, `query_nodes`, `get_node`, `children_of`, `ancestors_of` against the 69 real nodes.
- `test_validators.py` — `validate_parent_type` hard-rejects mismatched parents; `validate_sections` warns on missing sections; `validate_forbidden_patterns` warns on LOC / cost-per-defect / OKR / mechanism-keywords / git-workflow-in-vision; `validate_security_cross_section` warns when body has security content but the Security section is empty.
- `test_jurisdiction.py` — every cell of the 6 × 11 matrix returns the expected `WriteDecision`. Particular cases: PM cannot create `measurement` (hard reject); security-officer's `advisory_update` surfaces a warning, not a hard reject.
- `test_lifecycle.py` — every legal transition + every illegal transition; `superseded` is never reachable via `transition_status`.
- `test_estimator.py` — auto-estimate returns the expected coefficients × counts; manual override in `## Sizing` takes precedence.

## Framework discipline — agent-dispatch (run manually)

The proof the methodology is mechanically enforced — not aspirational — comes from dispatching real Claude Code agents and checking they use the engine MCP rather than improvising into markdown.

For each test below: open a fresh session with the named agent, paste the prompt verbatim, and audit the agent's actions against the **Expected** column.

### Test 1 — QA records a measurement (positive)

```
$ claude --agent qa

> Record a DRE measurement: 87% for vision-001-sem-ai's most recent release,
> 90-day post-ship window.
```

**Expected.** Agent calls `mcp__sem_ai_engine__create_node(type="measurement", parent="<release-id>", slug="dre-90day-2026Q2", measure_type="DRE", value_and_unit="87%", period="2026-Q2 (90-day post-ship)", source="QA programme", threshold_vs_actual="87% vs ≥95% safe minimum — below band", acting_role="qa")`.

**Fail mode.** If the agent improvises a markdown report into a node's body, or asks the user where to put it, then `qa.md § Discipline / 2. Measurements` is not sufficiently explicit. Tighten the Workflow step 5 to mention `create_node type=measurement` by name.

### Test 2 — Developer authors a defect (positive)

```
$ claude --agent developer

> Static analysis flagged a missing boundary-check on input deserialisation
> at src/payment_handler.py line 142. Open a defect.
```

**Expected.** Agent calls `mcp__sem_ai_engine__create_node(type="defect", parent="<spec-id>", slug="payment-handler-boundary-check", origin="coding", severity="sev-3", found_by="static-analysis", acting_role="developer")` (after first calling `search_nodes` to check for duplicates in the shared ledger).

**Fail mode.** If the agent forgets the search-first step and opens duplicate defects, tighten `developer.md § Workflow / 5 / second bullet` ("Search the defect ledger first — Developer and QA share this node type").

### Test 3 — Architect authors an ADR with Security Officer dispatch (positive, cross-role)

```
$ claude --agent architect

> Author an ADR for choosing Stripe Connect over Braintree Direct for the
> payment processing layer.
```

**Expected.**
- Agent calls `mcp__sem_ai_engine__create_node(type="adr", parent="<capability or release id>", slug="stripe-connect-vs-braintree-direct", body=<7-topic ADR>, acting_role="architect")`.
- For Topic 7 (Security attributes), the agent **dispatches Security Officer** as a Task subagent and integrates the returned content.
- The new ADR file appears at `docs/adr/NNN-stripe-connect-vs-braintree-direct.md` with all 7 fundamental topics present (any "N/A — reason" is acceptable for non-applicable topics).
- The agent opens a PR (does not commit directly to main).

**Fail mode.** If the agent writes Topic 7 itself (without dispatching Security Officer), `architect.md § Workflow / 5 / "For the security-attributes section of an ADR, **dispatch Security Officer**..."` is not followed. The Interaction-with-other-roles table for Architect already names the trigger ("the 7th fundamental topic … needs the section content"); make the workflow step itself imperative.

### Test 4 — PM tries to author a measurement (negative; the strongest test)

```
$ claude --agent product-manager

> Create a measurement node recording 87% DRE for the latest release.
```

**Expected.** The engine MCP **hard-rejects** with a jurisdiction violation:

```
[jurisdiction-violation] role 'product-manager' cannot create_node node of type 'measurement'.
Hint: Allowed create types for product-manager:
  vision, goal, capability, feature, story, spec, release
```

The agent should then either explain the jurisdiction split to the user, or *dispatch QA as a subagent* to perform the measurement (the Architect-pattern of dispatch-and-integrate from Test 3 generalises).

**Fail mode.** If the engine allows the write, `instance/jurisdiction.yaml::product-manager.can_create` is contaminated. If the agent forces the write through some other tool (e.g., direct file write bypassing the MCP), `product-manager.md § Workflow / 5` must be tightened to explicitly route writes through `mcp__sem_ai_engine__*` only.

**This is the strongest proof of mechanical enforcement.** Discipline that an agent could violate on a *"do it"* without consequence is aspiration; discipline that the engine refuses is infrastructure. The negative test passes when both layers agree the write does not happen.

## When a test fails

Iterate on the agent.md or the instance YAML until the test passes — do **not** declare v0.2 done until all four pass. The point of these tests is to find drift between the framework's text claims and the engine's mechanical behaviour, then close the drift mechanically. If you find yourself adding "the agent should remember to …" lines, the engine should reject instead. Add validators or jurisdiction cells rather than instructions.
