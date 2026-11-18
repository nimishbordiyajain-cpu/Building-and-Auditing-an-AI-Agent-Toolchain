#!/usr/bin/env python3
"""Block Claude Code Write/Edit calls targeting the plugin's protected data/official folder."""
import json
import os
import sys
from pathlib import Path

payload = json.load(sys.stdin)
tool_input = payload.get("tool_input", {})
target = tool_input.get("file_path") or tool_input.get("path") or ""
protected = (Path(os.environ.get("CLAUDE_PLUGIN_ROOT", ".")) / "data" / "official").resolve()
try:
    resolved = Path(target).expanduser().resolve()
except Exception:
    resolved = Path("/")
if resolved == protected or protected in resolved.parents:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Writes to plugin data/official are blocked by the Campus Helpdesk safety hook."
        }
    }))
