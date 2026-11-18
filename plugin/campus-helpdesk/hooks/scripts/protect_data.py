#!/usr/bin/env python3
import json, os, sys
from pathlib import Path
try:
    event=json.load(sys.stdin)
except (json.JSONDecodeError, UnicodeDecodeError):
    print("Invalid hook input; write was not approved.", file=sys.stderr)
    raise SystemExit(2)
tool_input=event.get("tool_input") or {}
target_text=tool_input.get("file_path") or tool_input.get("path") or ""
plugin_root=Path(os.environ.get("CLAUDE_PLUGIN_ROOT", Path(__file__).resolve().parents[2]))
protected=(plugin_root/"data"/"official").resolve()
if not target_text:
    raise SystemExit(0)
target=Path(target_text).expanduser()
if not target.is_absolute():
    target=Path(event.get("cwd") or os.getcwd())/target
target=target.resolve()
if target==protected or protected in target.parents:
    print(json.dumps({"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Writes to the protected data/official folder are blocked."}}))
