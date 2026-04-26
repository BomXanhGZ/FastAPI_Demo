# AGENTS.md

## Goal

Help with coding tasks safely inside this project.

Priorities:

1. Protect user work
2. Never modify remote Git state
3. Make minimal, focused changes
4. Always explain changes briefly
5. Always show what changed after editing

---

## Git Safety

Never run commands that modify remote Git state:

- git push
- git push --force
- git push --tags
- git remote add/remove/set-url
- gh repo
- gh pr create/merge
- deployment commands that publish code

Never run destructive local Git commands unless explicitly approved:

- git commit
- git reset / git reset --hard
- git checkout .
- git restore .
- git clean / git clean -fd
- git rebase
- git merge
- git branch -D
- git stash clear

Allowed Git commands:

- git status
- git diff
- git diff --stat
- git log --oneline
- git branch
- git remote -v

If any other Git action is needed, stop and ask first.

---

## Coding Rules

Edit files inside the current project only.

Make the smallest correct change that fully solves the task.

Keep existing coding style, naming style, folder structure, and architecture.

Do not:

- rewrite whole files unless necessary
- refactor unrelated code
- rename files, folders, functions, classes, variables, APIs, or database fields unless required
- change public behavior unless required
- change formatting across the entire project
- add dependencies or install/upgrade packages unless approved
- change project structure unless approved

If the project pattern is unclear, inspect nearby files and follow the closest existing pattern.

---

## Code Quality

Code should be:

- simple and readable
- easy to debug
- minimally changed
- consistent with the existing project
- safe around edge cases
- clear in error handling

When modifying logic, consider:

- input validation
- null/empty values
- error cases
- backward compatibility
- existing tests
- existing API contracts
- existing data formats

---

## Architecture

Respect the current architecture.

Do not move logic between layers or introduce new layers, patterns, services, managers, helpers, or utilities unless clearly needed.

If the project already has separation such as controller/service/repository, UI/service/store, or handler/usecase/gateway, follow it.

If no clear architecture exists, keep the change local and simple.

---

## Sensitive Files

Ask before modifying:

- .env / .env.*
- files containing secret, token, credential
- Dockerfile
- docker-compose.yml
- package.json / lock files
- requirements.txt
- pyproject.toml
- migration files
- CI/CD files
- deployment configs
- infrastructure files
- nginx/*
- terraform/*
- .github/workflows/*

Never expose secrets or tokens.

---

## Workflow

Before editing:

1. Inspect relevant files
2. Understand the current pattern
3. Identify the root cause or required change
4. Explain the planned change briefly

After editing:

1. Show changed files
2. Show `git diff --stat`
3. Summarize the exact changes
4. Explain why the changes were made
5. Mention verification and remaining manual checks

Use this finish format:

- Root cause:
- Files changed:
- What changed:
- Why:
- Verification:
- Remaining checks:

---

## Default Behavior

If the task is unclear, ask before editing.

If multiple solutions exist, choose the safest minimal fix.

Never push, commit, deploy, reset, discard, or publish changes without explicit user approval.