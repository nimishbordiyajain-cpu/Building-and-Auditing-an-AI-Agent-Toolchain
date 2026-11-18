# Campus Helpdesk AI Agent

A coursework demonstration for AI Tools and Prompt Engineering. It packages timetable instructions as an Agent Skill, bundles components as a Claude Code plugin, exposes mock campus data through an MCP server, and documents Git worktree collaboration.

## Safety and data
All timetable, fee and hostel data are fictional. Do not add real student data, passwords, tokens or API keys.

## Project layout
```text
data/                         mock CSV/JSON/Markdown data
skills/timetable-helper/      Agent Skill, references, helper and tests
mcp-server/                   Python MCP server
plugin/campus-helpdesk/       installable Claude Code plugin source
marketplace/                  local Claude Code marketplace
docs/                         report sections A-F
screenshots/                  add your own verified screenshots here
```

## Quick start
1. Python 3.11+ recommended.
2. Create a virtual environment and install `mcp-server/requirements.txt`.
3. Run helper tests: `python -m unittest discover -s skills/timetable-helper/tests -v`.
4. Run a sample lookup: `python skills/timetable-helper/scripts/timetable.py --batch CSE-JB-2025 --day Monday`.
5. Test the MCP server: `npx -y @modelcontextprotocol/inspector python mcp-server/server.py`.
6. Validate and install the plugin using commands in `docs/part-c-plugin.md`.

## Important verification status
- Python CSV helper tests can be run locally.
- MCP Inspector screenshots, Claude Code plugin installation, prompt-trigger tests and Git worktree conflict evidence must be generated on the student's machine.
- The JSON-RPC trace in the report is labelled illustrative, not a captured network transcript.
- The suggested `@nimbus/mcp-skill-bridge@2.3` package is not used. Recheck the npm registry before making a definitive absence claim.

## Official sources
See `docs/part-a-claim-audit.md` and `docs/source-list.md`.


## Honest test status
Verified locally in the build environment: 5 Python timetable tests, JSON syntax, simulated protected-folder hook allow/deny behaviour, and a real Git worktree merge-conflict demonstration. See `evidence/`.

Not yet verified: MCP SDK installation/server execution and MCP Inspector; Claude Code plugin validation/installation; automatic Skill triggering; public npm package lookup. Network/DNS restrictions prevented the MCP and npm package checks here. These are clearly marked as pending and must be run on the student's Mac before submission. No screenshots or tool logs have been fabricated.
