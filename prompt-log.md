# Prompt Log — Campus Helpdesk AI Agent

This log records concrete issues identified during preparation. Add your own actual local Claude Code/MCP Inspector interactions and timestamps before submission. It does not claim that local plugin installation or Inspector testing has already happened.

| # | Tool | Prompt / request | Initial AI output or issue | How I detected it and what I changed |
|---:|---|---|---|---|
| 1 | ChatGPT + assignment brief | Create the required Skill tests. | Initial draft had 3 triggers, 2 non-triggers and an adversarial prompt, but no separate ambiguous prompt. | Compared it with Part B and added an ambiguous prompt as a sixth case; retained adversarial as a seventh. |
| 2 | ChatGPT + official Claude Code plugin docs | Check the hook configuration. | An earlier explanation incorrectly said the outer `hooks` wrapper was invalid for plugin `hooks.json`. | Checked the plugin-specific hook format. It requires the wrapper; kept it and corrected the command field to one command string. |
| 3 | ChatGPT + official hook reference | Validate the PreToolUse block response. | An initial draft used an unverified response shape. | Checked the Hooks reference and used `hookSpecificOutput.hookEventName`, `permissionDecision: "deny"` and `permissionDecisionReason`. |
| 4 | ChatGPT + MCP Python SDK docs | Explain the MCP failure case. | A plain `ValueError` did not document the intended user-readable tool failure. | Checked SDK error handling and changed anticipated lookup failures to `ToolError`. |
| 5 | ChatGPT + official MCP SDK docs | Choose an SDK version for initialize/tools/list/call. | An unpinned dependency could install v2, which has breaking changes from v1. | Checked SDK migration and v1 docs; retained `mcp>=1.28,<2` because this code uses the v1 `FastMCP` import path. |
| 6 | ChatGPT + official Git docs | Create three worktrees and a conflict. | The first script attempted worktree creation before committing a shared base and did not make a distinct change in the third worktree. | Checked Git worktree usage, committed the base first, and added a separate hook-path change. |
| 7 | ChatGPT + official marketplace docs | Write exact plugin installation steps. | The first draft did not clearly document the complete marketplace lifecycle. | Checked the official marketplace walkthrough and documented validation, marketplace add, install, list, details, uninstall and marketplace removal. |
| 8 | npm CLI attempt in restricted build environment | Check `@nimbus/mcp-skill-bridge@2.3`. | `npm view @nimbus/mcp-skill-bridge@2.3 version` timed out; DNS/network access was unavailable. | Did not claim the package is nonexistent. Kept the result Unverified and provided the exact command for a network-enabled local check. |

**Honesty note:** This log is a record of issues found while preparing the project. It must be supplemented with the student's own local test prompts, outputs and screenshots. Do not state that a Claude Code plugin or MCP Inspector test passed until it has been run.
