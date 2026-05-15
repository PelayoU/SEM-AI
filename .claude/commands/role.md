---
description: Declare the active SEM-IA role (writes .claude/.active-role). Required before any substrate work — the node-before-artifact gate denies all substrate writes until a valid role is declared.
argument-hint: <product-owner|architect|qa|developer|devops>
allowed-tools: Bash, Write, Read
---

Declare the active SEM-IA role.

**Requested role:** `$ARGUMENTS`

Follow these steps in order:

1. **Validate.** The role must be exactly one of: `product-owner`, `architect`, `qa`, `developer`, `devops`. If `$ARGUMENTS` is empty or not in that set, stop and tell the human the five valid roles. Do not write the marker.

2. **Write the marker.** Write `$ARGUMENTS` (just the role name + newline) to `.claude/.active-role`, overwriting any previous value. This path is gate-ignored (runtime state), so the write always succeeds even with the gate live — it is the ceremony that *moves authorship*, distinct from subagent consultation (ADR-005).

3. **Confirm.** Report: the active role is now `<role>`; its substrate jurisdiction (summarise from `.claude/role-scope.json` for that role); and the reminder that substrate writes outside that jurisdiction, or with no governing node, are hard-blocked by `.claude/hooks/enforce-node-before-artifact.sh` (no override).

This command is the only sanctioned way to set the active role. Switching role is an explicit ceremony, by design (CLAUDE.md § Role jurisdiction; ADR-012).
