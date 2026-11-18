#!/usr/bin/env bash
set -euo pipefail
# Run in a disposable clone or a clean project root after saving all work.
printf 'owner=main\\n' > conflict-demo.txt
git add conflict-demo.txt
git commit -m "Add conflict demo base"

git worktree add ../campus-skill-tests -b feature/skill-tests
git worktree add ../campus-mcp-server -b feature/mcp-server
git worktree add ../campus-hook-path -b bugfix/hook-path

printf 'owner=skill-tests\\n' > ../campus-skill-tests/conflict-demo.txt
git -C ../campus-skill-tests add conflict-demo.txt
git -C ../campus-skill-tests commit -m "Change owner in skill-tests"

printf 'owner=mcp-server\\n' > ../campus-mcp-server/conflict-demo.txt
git -C ../campus-mcp-server add conflict-demo.txt
git -C ../campus-mcp-server commit -m "Change owner in mcp-server"

mkdir -p ../campus-hook-path/worktree-notes
echo "Hook path workstream completed." > ../campus-hook-path/worktree-notes/hook-path.txt
git -C ../campus-hook-path add worktree-notes/hook-path.txt
git -C ../campus-hook-path commit -m "Add hook path workstream note"

git merge feature/skill-tests
if git merge feature/mcp-server; then
  echo "Unexpected: no conflict occurred."
else
  echo "Conflict created. Resolve conflict-demo.txt, then run:"
  echo "git add conflict-demo.txt && git commit -m 'Resolve worktree merge conflict'"
fi
git worktree list
