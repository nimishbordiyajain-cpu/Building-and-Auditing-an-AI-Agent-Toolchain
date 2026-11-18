# Part E — Parallel Development with Git Worktrees

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
