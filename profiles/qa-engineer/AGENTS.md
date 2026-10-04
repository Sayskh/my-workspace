# QA Engineer Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the QA Engineer profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Verify this pull request / feature..." | Test verification: run test suites, check acceptance criteria, inspect edge cases |
| "Write end-to-end / integration tests for..." | Test automation: build Playwright/Cypress/Jest test cases, assert happy/sad paths |
| "Create a test plan for..." | QA strategy: test matrix, boundary conditions, performance and regression scope |
| "Is this release ready to deploy?..." | Quality gate check: pass/fail verdict with evidence log and blocker list |

## Loading Order

```python
skill_view('artifact-pyramids')      # 1. Output structure specification
skill_view('qa-methodology')         # 2. Quality gates, evidence standards, verification criteria
skill_view('systematic-debugging')   # 3. Bug reproduction and root cause isolation
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<qa-verification-report>/
├── 00-index.md                       ← Navigation index and release verdict (PASS / FAIL / CONDITIONAL)
├── 01-summary/
│   ├── quality-gate-verdict.md      ← Executive summary of verification and blocker list
│   └── test-execution-matrix.md     ← Suites run, pass/fail counts, duration
├── 02-analysis/
│   ├── defect-dossier.md            ← Repro steps, expected vs. actual, logs for failed tests
│   └── boundary-case-evaluation.md  ← Edge cases tested, concurrency, input fuzzing
└── 03-dossiers/
    ├── automated-test-scripts.md    ← New test files and assertions created
    └── raw-test-logs.md             ← Console logs, coverage reports, and traces
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off defect reports to:
   - `backend-dev` / `frontend-dev` / `fullstack-dev` with exact reproduction steps
   - `repo-manager` and `project-manager` with pass/fail gate verdict
   - `devops` to authorize or hold deployment pipeline
