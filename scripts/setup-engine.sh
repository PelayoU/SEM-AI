#!/usr/bin/env bash
# ============================================================================
# setup-engine.sh — provision the SEM-AI engine on an adopting project.
#
# Run once after cloning the template. Idempotent: re-run any time to refresh
# the venv or pick up updated dependencies.
#
# What it does:
# 1. Verifies prerequisites (Python 3.11+, gh CLI authenticated)
# 2. Creates a local Python venv at .venv/
# 3. Installs engine/requirements.txt
# 4. Runs `python -m engine.mcp_server --check` to verify the engine
# registers its 22 tools and adapter config loads
#
# After this passes: open Claude Code with `claude --agent <role>` and the
# engine MCP starts automatically (declared in .claude/settings.json).
#
# Required externally (per on dependencies):
# - A CLI with MCP support (Claude Code, OpenCode, etc.) — for using the
# engine; not verified here.
# - `gh` CLI installed + authenticated
# - Python 3.11+
#
# NOT required: mcp__github__* loaded by the CLI client. See .
# ============================================================================

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo "==> SEM-AI engine setup"
echo " Repository: $REPO_ROOT"

# ----- 1. Python ------------------------------------------------------------

if ! command -v python3 >/dev/null 2>&1; then
  echo "FAIL: python3 not on PATH. Install Python 3.11+." >&2
  exit 1
fi

PYTHON_VERSION="$(python3 --version 2>&1 | awk '{print $2}')"
PYTHON_MAJOR="${PYTHON_VERSION%%.*}"
PYTHON_MINOR="$(echo "$PYTHON_VERSION" | cut -d. -f2)"
if [[ "$PYTHON_MAJOR" -lt 3 ]] || { [[ "$PYTHON_MAJOR" -eq 3 ]] && [[ "$PYTHON_MINOR" -lt 11 ]]; }; then
  echo "FAIL: Python 3.11+ required; got $PYTHON_VERSION" >&2
  exit 1
fi
echo " [OK] Python $PYTHON_VERSION"

# ----- 2. gh CLI ------------------------------------------------------------

if ! command -v gh >/dev/null 2>&1; then
  echo "FAIL: gh CLI not on PATH. Install via 'brew install gh' or your package manager." >&2
  echo " See https://cli.github.com/" >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "FAIL: gh CLI not authenticated. Run 'gh auth login' and retry." >&2
  exit 1
fi
echo " [OK] gh CLI authenticated"

# ----- 3. venv --------------------------------------------------------------

if [[ ! -d .venv ]]; then
  echo " [..] Creating .venv/"
  python3 -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

echo " [..] Installing engine/requirements.txt"
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r engine/requirements.txt
echo " [OK] Dependencies installed"

# ----- 4. Verify the engine starts ------------------------------------------

echo " [..] Verifying engine MCP server"
if ! python -m engine.mcp_server --check >/dev/null 2>&1; then
  echo "FAIL: engine.mcp_server --check did not pass. Re-run with verbose:" >&2
  echo " python -m engine.mcp_server --check" >&2
  exit 1
fi
echo " [OK] Engine MCP server: 22 tools registered, imports OK"

# ----- 5. Pytest sanity (optional — only if pytest is installed) ------------

if python -c "import pytest" 2>/dev/null; then
  echo " [..] Running engine tests"
  if ! python -m pytest engine/tests/ -q --no-header 2>&1 | tail -3; then
    echo "WARN: engine tests failed. The engine may still work but something is wrong." >&2
  fi
fi

# ----- Done -----------------------------------------------------------------

cat <<EOF

============================================================
Engine setup complete.

Next steps:
  1. Configure repo target (one of):
       export SEM_AI_REPO=owner/name # current shell
       echo 'export SEM_AI_REPO=owner/name' >> ~/.zshrc # persistent

  2. Provision the GitHub repo (Issue Types + labels + Projects v2):
       ./scripts/setup-github-project.sh

  3. Open Claude Code with a role and start working:
       claude --agent product-manager
       # Or: architect / developer / qa / devops / security-officer

  The engine MCP starts automatically on session start (declared in
  .claude/settings.json). The first session typically opens a 'vision'
  Issue.
============================================================
EOF
