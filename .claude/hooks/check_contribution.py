"""PostToolUse hook (Edit/Write): run the checks CONTRIBUTING.md requires.

After Claude edits a .py file, run `ruff check`, `ruff format --check`, and the
file's doctests. If any fail, exit code 2 sends the output back to Claude to fix.
"""
import json
import subprocess
import sys

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "")
if not path.endswith(".py") or ".claude" in path.replace("\\", "/"):
    sys.exit(0)

checks = [
    ["ruff", "check", path],
    ["ruff", "format", "--check", path],
    [sys.executable, "-m", "doctest", path],
]
failures = []
for check in checks:
    try:
        result = subprocess.run(check, capture_output=True, text=True)
    except FileNotFoundError:
        failures.append(f"{check[0]} is not installed (pip install ruff)")
        continue
    if result.returncode != 0:
        output = (result.stdout + result.stderr).strip().splitlines()[-15:]
        failures.append(" ".join(check[:3]) + " failed:\n" + "\n".join(output))

if failures:
    print("CONTRIBUTING.md checks failed for " + path + ":\n" + "\n\n".join(failures), file=sys.stderr)
    sys.exit(2)
sys.exit(0)
