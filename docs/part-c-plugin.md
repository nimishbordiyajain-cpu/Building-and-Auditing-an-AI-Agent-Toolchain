# Part C — Package a Plugin

## Package contents
The installable plugin is `marketplace/plugins/campus-helpdesk/`. It contains the manifest, timetable Skill, `/show-timetable` command, PreToolUse hook, MCP configuration, server and mock data. Plugin `hooks.json` uses the plugin-specific `{"hooks": {...}}` wrapper. The hook command is one command string. It denies Write/Edit calls targeting `data/official/` inside the plugin. It is a demonstration guard, not a replacement for OS permissions.

## Exact local validation and installation steps
Run from the extracted project root in a shell with Claude Code CLI installed:

```bash
claude plugin validate ./marketplace/plugins/campus-helpdesk
claude plugin validate ./marketplace
claude plugin marketplace add ./marketplace
claude plugin install campus-helpdesk@nimbus-campus-marketplace
claude plugin list
claude plugin details campus-helpdesk
```

Uninstall:

```bash
claude plugin uninstall campus-helpdesk@nimbus-campus-marketplace
```

Optionally remove the marketplace:

```bash
claude plugin marketplace remove nimbus-campus-marketplace
```

The install identifier is the marketplace entry name, followed by `@`, followed by the marketplace name. Marketplace plugin paths are relative to the marketplace root. Official instructions: https://code.claude.com/docs/en/plugin-marketplaces and https://code.claude.com/docs/en/plugins-reference.

**Evidence requirement:** Save actual terminal output for validation, marketplace add, installation, `plugin list`, `plugin details`, and uninstall. These commands have not been run in the generation environment, so no successful installation is claimed.

## Threat model

| Threat | Example | Concrete mitigation |
|---|---|---|
| Prompt injection through Skill text | A malicious Skill tells the model to ignore the user or reveal secrets. | Review Skill text before installation; keep credentials out of model context; restrict Skill purpose; test adversarial inputs. |
| Malicious hooks running shell commands | A hook executes a destructive command or uploads local files with the user's permissions. | Inspect every hook and referenced script; avoid opaque remote scripts; use least privilege and a disposable test project; require human approval for destructive/network actions. |
| MCP tool poisoning through descriptions | A tool description misrepresents its purpose or instructs the model to disclose private data. | Review tool names/descriptions and source code; expose only necessary tools; validate arguments server-side; require confirmation for sensitive actions; log calls. |

A plugin is executable software, not just documentation. Installing one grants its hooks and server processes access according to the host user's permissions.
