#!/usr/bin/env python3
import json, os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
json_files=list(ROOT.rglob("*.json"))
for p in json_files: json.loads(p.read_text(encoding="utf-8"))
print(f"JSON syntax: {len(json_files)} files passed")
test=subprocess.run([sys.executable,"-m","unittest","discover","-s",str(ROOT/"skills/timetable-helper/tests"),"-v"],cwd=ROOT,text=True,capture_output=True)
print(test.stdout,end="")
print(test.stderr,end="",file=sys.stderr)
if test.returncode: raise SystemExit(test.returncode)
hook=ROOT/"plugin/campus-helpdesk/hooks/scripts/protect_data.py"
plugin_root=ROOT/"plugin/campus-helpdesk"
env=os.environ.copy(); env["CLAUDE_PLUGIN_ROOT"]=str(plugin_root)
def run_hook(path):
    payload={"cwd":str(ROOT),"tool_input":{"file_path":str(path)}}
    return subprocess.run([sys.executable,str(hook)],input=json.dumps(payload),text=True,capture_output=True,env=env)
denied=run_hook(plugin_root/"data/official/records.txt")
allowed=run_hook(ROOT/"data/timetable.csv")
assert json.loads(denied.stdout)["hookSpecificOutput"]["permissionDecision"]=="deny"
assert allowed.returncode==0 and not allowed.stdout.strip()
print("Hook protected path: DENY passed")
print("Hook ordinary path: no decision passed")
print("Offline project validation: PASSED")
