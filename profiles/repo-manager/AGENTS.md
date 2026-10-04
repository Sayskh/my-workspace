# Repo Manager Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the Repo Manager profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Prepare release / tag version..." | Release governance: bump version (SemVer), generate CHANGELOG, tag release, draft notes |
| "Audit pull request / merge readiness..." | Merge criteria check: passing CI, reviews approved, clean rebase, linear history |
| "Organize repository structure / clean branches..." | Git hygiene: prune stale branches, enforce .gitignore, configure branch protection |
| "Resolve Git merge conflict / rebase issue..." | Conflict management: clean three-way merge resolution, history preservation |

## Loading Order

```python
skill_view('artifact-pyramids')          # 1. Output structure specification
skill_view('technical-documentation')    # 2. Release notes, changelog generation, repository standards
skill_view('implementation-planning')    # 3. Release scheduling and version alignment
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<repo-release-package>/
├── 00-index.md                       ← Navigation index and release summary
├── 01-summary/
│   ├── release-notes.md             ← Executive release notes, features, fixes, breaking changes
│   └── changelog-diff.md            ← Semantic commits categorized since previous tag
├── 02-analysis/
│   ├── merge-audit-report.md        ← PR review approvals, CI verification proofs, sign-offs
│   └── dependency-diff.md           ← Lockfile changes, upgraded dependencies, security status
└── 03-dossiers/
    ├── branch-protection-rules.md   ← Configured branch policies, required status checks
    └── git-rebase-instructions.md   ← Exact git commands for clean branch integration
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off tagged release packages to:
   - `devops` to trigger automated production deployment
   - `project-manager` for milestone closure and stakeholder notification
   - `qa-engineer` for final release candidate smoke test signoff
