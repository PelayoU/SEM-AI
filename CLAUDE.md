# This repository carries a Software-Engineering-Management framework.

The framework contract — what you do, the one rule, the graph (what a node is, how you read/change it), sessions, and the role-jurisdiction map — is the **`framework` skill** (`.claude/skills/framework/SKILL.md`). That skill is the single source of truth.

Every agent (`.claude/agents/<role>.md`) preloads `framework` via its `skills:` frontmatter, so the contract is present for both `claude --agent <role>` (primary) and Task subagents — neither depends on this file.

You work as **one role at a time**. Pick a role with `claude --agent <role>`. With no role active, read the `framework` skill first, then ask the human which role to take.
