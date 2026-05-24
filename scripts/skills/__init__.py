"""Python implementations of the framework's three slash-command skills.

Each script is invoked from the corresponding SKILL.md
(`.claude/skills/<name>/SKILL.md`) via `.venv/bin/python scripts/skills/<name>.py`.
The skill markdown gives the agent the instructions; the script does the
Python work (git operations, gh CLI calls, doc scaffolding, delta digest).

Three skills:

  session_open.py creates a session branch + doc + posts 📍 comments
  session_close.py finalizes the Handoff + posts 🏁 + merge/PR/discard
  catch_up.py delta digest of graph changes since last invocation
"""
