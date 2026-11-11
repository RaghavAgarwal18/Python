"""PreToolUse hook (Bash): never contribute to the upstream project.

Blocks:
  - any `git push` that names `upstream` or TheAlgorithms/Python
  - any `gh pr create` that doesn't say `--repo <our fork>`
    (gh targets the upstream parent of a fork by default)
Exit code 2 = block the command and tell Claude why.
"""
import json
import re
import sys

UPSTREAM = "thealgorithms/python"

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")
lowered = command.lower()

problem = None
if "git push" in lowered and ("upstream" in lowered or UPSTREAM in lowered):
    problem = "git push to upstream"
elif "gh pr create" in lowered:
    repo = re.search(r"--repo[ =]+(\S+)", lowered) or re.search(r"-R +(\S+)", command)
    if repo is None:
        problem = "gh pr create without --repo (it would target upstream by default)"
    elif UPSTREAM in repo.group(1).lower():
        problem = "gh pr create against TheAlgorithms/Python"

if problem:
    print(
        f"Blocked: {problem}. This lab must not contribute to the upstream project. "
        "Push to origin (the fork) and open the PR with --repo <your-username>/Python.",
        file=sys.stderr,
    )
    sys.exit(2)
sys.exit(0)
