# Part A — Claim Audit

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
