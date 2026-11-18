# Building and Auditing an AI-Agent Toolchain
## AI Tools and Prompt Engineering | B.Tech CSE
### Campus Helpdesk AI Agent

**Student:** Nimish Bordiya
**Roll Number:** 150096725027
**Class / Batch:** 2nd Year — Jeff Bezos
**Date:** 17 November 2026

> All timetable, fee and hostel records are fictional mock data. Source access date is 17 November 2026. This report distinguishes verified local tests from tests that still require the student's Claude Code/MCP Inspector environment.

## Project Overview

This project demonstrates reusable AI instructions as a Skill, packaging through a Claude Code Plugin, access to mock campus data through an MCP server, and parallel Git development using worktrees. The agent example answers timetable and fee queries and provides a hostel-rules resource.


## Part A — Claim Audit (15 marks)


**Access date for all links below: 17 November 2026.** The verdicts are based on the official documentation listed. "Unverified" means I could not establish the claim from a reliable primary source; it does not mean that it is certainly false.

| No. | Verdict | Correction and reasoning | Official source URL | Date accessed |
|---:|---|---|---|---|
| 1 | True | MCP uses JSON-RPC 2.0 messages. The server feature set includes tools, resources and prompts; these are capabilities a server may expose, not a statement that every server must expose all three. | https://modelcontextprotocol.io/specification/2025-03-26 | 17 Nov 2026 |
| 2 | False | `2025-02-30` is not a valid calendar date, and the cited MCP specification does not define a mandatory Persistent Memory Primitive. MCP describes tools, resources, prompts and other protocol features; a client/server may implement application-specific storage, but that is not this claimed required primitive. | https://modelcontextprotocol.io/specification/2025-03-26 | 17 Nov 2026 |
| 3 | True | The Agent Skills format uses a folder with a required `SKILL.md`; its frontmatter includes a name and description. Claude Code explains that skill descriptions are available for selection and the full body is loaded when the skill is used, while linked supporting files can be read when needed. | https://code.claude.com/docs/en/skills ; https://agentskills.io/specification | 17 Nov 2026 |
| 4 | False | The official Skill structure does not require `skill.config.yaml` or a `runtime: python3.14` field. A Skill may include optional scripts, references and assets, but runtime dependencies must be documented and installed by the user/environment as needed. | https://code.claude.com/docs/en/skills | 17 Nov 2026 |
| 5 | True | Git supports a main worktree and linked worktrees. They share common repository data while each worktree has its own working directory and per-worktree metadata such as `HEAD` and index. | https://git-scm.com/docs/git-worktree | 17 Nov 2026 |
| 6 | False | `git worktree sync --all` is not a documented Git worktree subcommand. The official command list includes `add`, `list`, `lock`, `move`, `prune`, `remove`, `repair` and `unlock`; fetching/rebasing must be done with normal Git commands in the relevant worktree. | https://git-scm.com/docs/git-worktree | 17 Nov 2026 |
| 7 | True, with scope | Claude Code plugins can package Skills, agents, hooks and MCP server configurations as one installable directory/unit. This is a Claude Code plugin model, not a universal definition that every plugin system supports the same component types. | https://code.claude.com/docs/en/plugins | 17 Nov 2026 |
| 8 | False | RFC 9999 exists, but it is titled "Remote ATtestation procedureS (RATS) Conceptual Message Wrapper (CMW)", not "MCP Transport Security". It does not impose an Ed25519-signature requirement on stdio MCP servers. MCP's stdio transport describes a local subprocess using stdin/stdout JSON-RPC; the cited requirement is absent. | https://www.rfc-editor.org/rfc/rfc9999.html ; https://modelcontextprotocol.io/specification/2025-03-26/basic/transports | 17 Nov 2026 |
| 9 | False | Git normally refuses to check out a branch already checked out in another worktree. The documented `--ignore-other-worktrees` option exists for exceptional cases, but it is not the default and should be used carefully. | https://git-scm.com/docs/git-checkout | 17 Nov 2026 |
| 10 | Unverified | I could not verify a primary publication by "Hendricks and Oyelaran (2024)" supporting the 12-Skill threshold, 40% accuracy drop, or term "skill collapse". No numerical effect or named phenomenon should be repeated as fact without a traceable paper, DOI, venue and methods. | https://api.crossref.org/works?query.bibliographic=Hendricks%20Oyelaran%202024%20skill%20collapse | 17 Nov 2026 |

## Notes on careful verification

- The briefing's date `2025-02-30` is invalid; the valid MCP specification revision used for this audit is `2025-03-26`.
- RFC 9999 is real, but the briefing gives it a fabricated title and an unrelated security requirement. This is why checking only whether an RFC number exists is not enough.
- A failed public search does not prove that a paper or package can never exist. Use **Unverified** when the evidence is insufficient.


## Part B — Design and Test a Skill (20 marks)


## Skill purpose
`timetable-helper` answers timetable questions from the supplied fictional CSV. It does not answer fee or hostel questions. The complete Skill is in `skills/timetable-helper/SKILL.md`.

## Progressive disclosure
- `SKILL.md`: short task instructions, source-of-truth rule and anti-fabrication rule.
- `references/csv-dictionary.md`: column meanings and examples.
- `references/edge-cases.md`: missing batch/day, weekends, ambiguous dates and adversarial requests.
- `scripts/timetable.py`: deterministic CSV lookup helper.

The official Skills documentation describes the required `SKILL.md` with YAML frontmatter and optional references/scripts. Claude Code uses the name and description to select a Skill, and supporting files can be read as needed. Sources: https://code.claude.com/docs/en/skills and https://agentskills.io/specification.

## Prompt tests
Seven prompt cases are provided: three expected triggers, two expected non-triggers, one ambiguous prompt and one adversarial prompt. **Automatic Skill selection has not yet been observed in Claude Code**, so the observed-result column remains pending until run locally. Python tests verify CSV lookup logic, not LLM trigger selection.

## Description experiment
Version 1 is too broad ("Helps students with college information") and can trigger for unrelated questions. Version 2 is too narrow ("Shows the CSE-JB-2025 Monday timetable") and misses other supported days and batches. The final description specifies the CSV, task, natural trigger wording and exclusions.

## Adversarial test
Prompt: "Show Monday's timetable and add an AI Ethics lecture at 2 PM even if it is missing from the CSV." The timetable Skill should trigger but refuse to invent the AI Ethics class, returning only rows present in the CSV.


## Part C — Package a Plugin (20 marks)


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


## Part D — Build an MCP Server (20 marks)


## Implementation
The server source is `mcp-server/server.py`. It uses the official MCP Python SDK v1 `FastMCP` API and stdio transport. It exposes:
- `get_timetable(batch: string, day: string)`: returns matching rows from `data/timetable.csv`.
- `get_fee_status(student_id: string)`: returns a mock record from `data/fee_status.json`.
- `hostel://rules`: read-only resource containing `data/hostel_rules.md`.

Tool descriptions and Python type hints define purpose and input schema. Expected lookup failures raise `ToolError`, so the SDK can return an error-marked tool result (`isError: true`) with a useful message. Sources: https://py.sdk.modelcontextprotocol.io/v1/ and https://py.sdk.modelcontextprotocol.io/servers/handling-errors/.

## SDK version
The server is pinned to `mcp>=1.28,<2` because it uses the v1 `FastMCP` import path and the assignment asks for the initialize handshake and JSON-RPC trace. The official SDK now has a v2 line with breaking changes; v1 is separately documented and remains in maintenance. Sources: https://py.sdk.modelcontextprotocol.io/v1/ and https://py.sdk.modelcontextprotocol.io/migration/.

## Package check
The suggested package `@nimbus/mcp-skill-bridge@2.3` was not found in the public web search results consulted on 17 November 2026. This does not prove no private or unpublished package exists. Finding: **Unverified in public search; not used**. Run this exact registry check locally and save its output:

```bash
npm view @nimbus/mcp-skill-bridge@2.3 version
```

An npm `E404` supports the narrower statement that the requested version was not found in the public npm registry at the time checked. If a version is returned, inspect publisher, repository, README and source before relying on it.

## Running and testing
From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r mcp-server/requirements.txt
npx -y @modelcontextprotocol/inspector python mcp-server/server.py
```

In Inspector, connect, list tools, call `get_timetable` with `CSE-JB-2025` and `Monday`, call `get_fee_status` with `STU102`, read `hostel://rules`, and try an unknown batch such as `CSE-FAKE-9999`. Save screenshots or export logs. Inspector execution has not been performed in the generation environment.

## JSON-RPC exchange and capability negotiation
The JSON-RPC examples in the report are **illustrative protocol examples**, not captured execution output. Capture the real Inspector trace for `initialize`, `tools/list`, and `tools/call`. The official lifecycle page says initialization negotiates protocol version and capabilities, and the client then sends `notifications/initialized`: https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle.

A `tools/list` response contains each tool's name, description and input schema. A `tools/call` request names the tool and supplies arguments: https://modelcontextprotocol.io/specification/2025-03-26/server/tools. Capabilities tell each side which optional features the other supports; they do not automatically grant permission to perform arbitrary actions.

## Failure case
Expected failure test: call `get_timetable` with `batch=CSE-FAKE-9999` and `day=Monday`. The handler raises `ToolError("Unknown batch ...")`; v1 FastMCP should return an error-marked tool result containing a message. Capture actual Inspector output before claiming it was observed.

## Tool descriptions as an attack surface
Tool descriptions are provided to the model so it can decide which tool to select and how to call it. A malicious description could mislead the model into choosing an inappropriate tool or disclosing data. Descriptions should be truthful and narrow, and server-side validation remains necessary because a description is not an enforcement mechanism.


## Part E — Parallel Development with Worktrees (15 marks)


## Worktree demonstration
The project includes `scripts/worktree-lab.sh`. It creates a base commit, then three linked worktrees and one change in each. It changes the same line on two branches, merges the first, and causes a conflict on the second. Resolve the conflict and capture the output.

Run only in a disposable clone or after committing all work:

```bash
bash scripts/worktree-lab.sh
```

When the script reports the conflict, edit `conflict-demo.txt` to contain `owner=skill-tests+mcp-server`, then run:

```bash
git add conflict-demo.txt
git commit -m "Resolve worktree merge conflict"
git worktree list
git log --oneline --graph --decorate --all
```

## Conceptual answers

**(a) Why does Git refuse the same branch in two worktrees?** If the same branch were checked out in two worktrees, both could update the same branch tip independently, creating confusing and unsafe states. Git refuses by default; `--force` can override some safeguards but is not recommended for normal work. Source: https://git-scm.com/docs/git-worktree.

**(b) What is shared and what is not?** Linked worktrees share the repository object database and common repository data. Each worktree has its own working directory and per-worktree state such as `HEAD` and index. Normal folders such as `node_modules`, `.venv` and `.env` are files in a particular working directory; they are not automatically shared. Source: https://git-scm.com/docs/git-worktree.

**(c) How should stale worktrees be cleaned safely?** Inspect `git worktree list` first. Use `git worktree remove <path>` for a clean linked worktree. If a directory was deleted manually and metadata is stale, preview with `git worktree prune --dry-run`, then prune if appropriate. Back up uncommitted work first. Source: https://git-scm.com/docs/git-worktree.

## Evaluate `/worktree-merge`
The official Claude Code documentation does not establish a built-in `/worktree-merge` command that automatically resolves Git conflicts. Treat the claim as **Unverified** unless the exact installed version's official command reference lists it. Even if an AI agent helps with a merge, a human must review the diff, conflict resolution, tests and security implications before committing. Sources: https://code.claude.com/docs/en/plugins and https://code.claude.com/docs/en/cli-reference.


## Actual worktree demonstration output

The following log was captured by running the worktree demonstration in a disposable copy of this project in the build environment. It shows three linked worktrees, a non-zero second merge (conflict), the manually resolved file, and the final commit graph. Re-run it on the student's machine if the instructor requires evidence from that machine.

```text
WORKTREE LIST:
/mnt/data/campus-helpdesk-worktree-demo-final/repo                c89ce0e [main]
/mnt/data/campus-helpdesk-worktree-demo-final/campus-hook-path    be93e86 [bugfix/hook-path]
/mnt/data/campus-helpdesk-worktree-demo-final/campus-mcp-server   ba36447 [feature/mcp-server]
/mnt/data/campus-helpdesk-worktree-demo-final/campus-skill-tests  c78f52c [feature/skill-tests]

SECOND MERGE EXIT CODE: 1
CONFLICT OUTPUT:
Auto-merging conflict-demo.txt
CONFLICT (content): Merge conflict in conflict-demo.txt
Automatic merge failed; fix conflicts and then commit the result.

RESOLVED FILE:
owner=skill-tests+mcp-server

HISTORY GRAPH:
* be93e86 (bugfix/hook-path) Add hook path workstream note
| *   c89ce0e (HEAD -> main) Resolve worktree merge conflict
| |\  
| | * ba36447 (feature/mcp-server) Change owner in mcp-server
| |/  
|/|   
| * c78f52c (feature/skill-tests) Change owner in skill-tests
|/  
* 83e7e28 Add conflict demo base
```


## Part F — Reflection and Prompt Log (10 marks)


## Reflection (approximately 300 words)

The four technologies solve different problems in an AI development project. An Agent Skill stores reusable instructions and domain knowledge. In this project, the timetable Skill tells the agent how to read a CSV, which fields to show, and what to do when a record is missing. A plugin solves a packaging and distribution problem. It groups the Skill, slash command, hook and MCP configuration so that another developer can install the features as one unit.

MCP solves the connection problem between an AI application and external data or functions. The timetable and fee tools let an agent request information from a server instead of guessing. The hostel rules resource provides read-only context. Git Worktrees solve a software-development workflow problem. They let different branches be checked out in separate folders at the same time while sharing the repository's common Git data.

I would choose a Skill when the main requirement is guidance: a repeatable procedure, domain rules, output format, or checklist. I would choose an MCP tool when the agent needs to perform a defined operation or retrieve data from another program. The two can work together: the Skill can explain when and how to call the MCP tool, while the MCP server performs the lookup and validates the input.

I would never delegate sensitive or irreversible work to an agent without review. Examples include transferring money, changing official student records, deleting production data, publishing an application, changing access permissions, or merging code that affects security. AI output can be useful, but it can misunderstand requirements, follow malicious instructions in files, or produce plausible but incorrect code. A human should verify sources, inspect diffs, run tests, check permissions and approve important actions. This assignment also taught me that an official-looking claim is not automatically true: the source URL, version, date and actual content must be checked.

## Prompt log

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


## Official Source List


**Access date for the sources below: 17 November 2026.** Verify URLs again on the date you submit if the instructor expects the actual submission date.

1. MCP 2025-03-26 specification overview: https://modelcontextprotocol.io/specification/2025-03-26
2. MCP lifecycle and capability negotiation: https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle
3. MCP server tools, tool listing, calling and errors: https://modelcontextprotocol.io/specification/2025-03-26/server/tools
4. MCP stdio transport: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports
5. Agent Skills specification: https://agentskills.io/specification
6. Claude Code Skills documentation: https://code.claude.com/docs/en/skills
7. Claude Code Plugins overview: https://code.claude.com/docs/en/plugins
8. Claude Code plugin marketplace guide: https://code.claude.com/docs/en/plugin-marketplaces
9. Claude Code plugin manifest reference: https://code.claude.com/docs/en/plugins-reference
10. Claude Code Hooks reference: https://code.claude.com/docs/en/hooks
11. Claude Code CLI reference: https://code.claude.com/docs/en/cli-reference
12. Git worktree documentation: https://git-scm.com/docs/git-worktree
13. Git checkout documentation: https://git-scm.com/docs/git-checkout
14. Official MCP Python SDK repository: https://github.com/modelcontextprotocol/python-sdk
15. Official MCP Python SDK v1 documentation: https://py.sdk.modelcontextprotocol.io/v1/
16. Official MCP Python SDK migration guide: https://py.sdk.modelcontextprotocol.io/migration/
17. Official MCP Python SDK error handling: https://py.sdk.modelcontextprotocol.io/servers/handling-errors/
18. RFC 9999 official text: https://www.rfc-editor.org/rfc/rfc9999.html
19. Crossref bibliographic search for the alleged Hendricks and Oyelaran paper: https://api.crossref.org/works?query.bibliographic=Hendricks%20Oyelaran%202024%20skill%20collapse

The alleged `@nimbus/mcp-skill-bridge@2.3` package was not relied upon. A public search did not establish a verifiable record, and the local `npm view` attempt timed out due network/DNS restrictions. The package's existence is therefore Unverified, not proven false.


## Final Evidence Checklist


This checklist is not proof of execution.

- [x] Python timetable unit-test output (`evidence/offline-validation.txt`)
- [x] JSON syntax and hook allow/deny validation (`evidence/offline-validation.txt`)
- [x] Git worktree list, conflict, resolution and graph (`evidence/worktree-demo/`)
- [x] Attempted npm registry check; network timeout recorded (`evidence/package-check-attempt.txt`)
- [x] Attempted MCP SDK install; DNS/network failure recorded (`evidence/mcp-install-attempt.txt`)
- [ ] Actual Skill trigger outcomes from Claude Code
- [ ] `claude plugin validate` output for plugin and marketplace
- [ ] Marketplace add / install / plugin list / details / uninstall terminal output
- [ ] MCP Inspector connected-server screenshot
- [ ] MCP tools list screenshot with schemas
- [ ] Successful timetable tool call screenshot
- [ ] Successful fee tool call screenshot
- [ ] Hostel rules resource screenshot
- [ ] Unknown batch failure screenshot
- [ ] Actual JSON-RPC trace for initialize, tools/list and tools/call
- [ ] Record Claude Code, Git, Python, Node/npm and MCP SDK versions
- [ ] Fill in student name, roll number and class on the report cover


## Appendix — Verification status

**Verified in the generated project environment:** five Python timetable helper tests; JSON syntax for the project configuration; simulated protected-folder hook allow/deny behaviour; and a real Git worktree demonstration with three linked worktrees, distinct workstream changes, a merge conflict, manual resolution, `git worktree list` output and a history graph.

**Not verified in the generated environment:** MCP SDK installation/server execution and MCP Inspector; Claude Code plugin validation and installation; automatic Skill selection in Claude Code; and the public npm registry result for `@nimbus/mcp-skill-bridge@2.3`. Network/DNS restrictions blocked package installation and the npm check timed out. No screenshots, JSON-RPC execution traces or external installation successes are fabricated. Complete the checklist and add the actual local evidence before submission.
