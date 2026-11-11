---
name: contribute-to-issue
description: Contribute a fix for an open TheAlgorithms/Python issue inside this fork, following CONTRIBUTING.md, and open the pull request against the fork (never upstream). Use when asked to work on an issue, fix a bug, or open a PR.
---

# Contribute to an issue (inside the fork only)

## 1. Prepare
1. Read `CONTRIBUTING.md` fully.
2. Check the remotes with `git remote -v`. `origin` must be the user's fork.
   If `upstream` is missing: `git remote add upstream https://github.com/TheAlgorithms/Python.git`
3. Sync and branch:
   ```bash
   git checkout master
   git pull upstream master        # read-only: pulling from upstream is fine
   git checkout -b fix-<issue-number>-<short-name>
   ```

## 2. Understand and reproduce the issue
1. Read the issue text the user gives you (number, file, expected vs actual behavior).
2. Reproduce the bug with a tiny example BEFORE changing anything, and note the wrong output.
3. Find the correct expected value from an independent source (the spec, or a
   standard-library reference), not from the buggy function.

## 3. Make the change
- Fix only what the issue describes, in the file it names. Keep the change small.
- Add doctests that would have caught the bug (the failing case from step 2), and keep
  the existing doctests passing.
- Keep or add type hints, a clear docstring, and descriptive names.
- Do not edit `README.md` or `DIRECTORY.md`.

## 4. Check (CONTRIBUTING.md requirements)
```bash
ruff check <file>
ruff format <file>
python -m doctest -v <file>
```
All three must pass. (A hook also runs these after every edit.)
Then ask the `contribution-reviewer` sub-agent to review the diff.

## 5. Commit and push to the FORK
```bash
git add <file>
git commit -m "Fix <short description> (#<issue-number>)"
git push origin fix-<issue-number>-<short-name>
```

## 6. Open the pull request in the FORK
`gh pr create` targets the upstream project by default, so always pass `--repo`:
```bash
gh pr create --repo <your-username>/Python --base master --head fix-<issue-number>-<short-name> \
  --title "Fix <short description>" \
  --body "Fixes #<issue-number> (TheAlgorithms/Python). Practice PR inside my fork for CS440 Lab 6."
```
CONTRIBUTING.md asks for `Fixes #<issue-number>` in the description.
Report the PR link back. Never push to `upstream` or open a PR on TheAlgorithms/Python.
