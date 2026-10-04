# Fullstack Dev Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the Fullstack Dev profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Build this feature end-to-end..." | Full vertical slice: UI component + API endpoint + DB migration + client-server wiring |
| "Prototype a working fullstack app for..." | Rapid prototyping: end-to-end interactive proof of concept |
| "Refactor the data flow from frontend to database for..." | Fullstack optimization: cohesive contract, schema update, state refactor |
| "Fix bug spanning client and server..." | Cross-layer debugging: trace from browser click to backend service and DB |

## Loading Order

```python
skill_view('artifact-pyramids')      # 1. Output structure specification
skill_view('systematic-debugging')   # 2. Cross-layer diagnostic workflows
skill_view('architecture')           # 3. System contracts and data flow
skill_view('ux-methodology')         # 4. Interface usability and accessibility
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<fullstack-delivery>/
├── 00-index.md                       ← Navigation index and deliverable summary
├── 01-summary/
│   ├── feature-overview.md          ← What was implemented across frontend and backend
│   └── integration-test-results.md  ← Fullstack test suite runs and verification proof
├── 02-analysis/
│   ├── end-to-end-data-flow.md      ← Sequence diagram and data contract
│   └── schema-and-api-changes.md    ← Migration details and endpoint signatures
└── 03-dossiers/
    ├── frontend-code-diffs.md       ← UI components, styles, and client state
    └── backend-code-diffs.md        ← Server logic, queries, and migrations
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off deliverables to:
   - `qa-engineer` for end-to-end user acceptance and integration test runs
   - `pentester` for fullstack attack surface review (auth, input validation, CSRF)
   - `devops` for deployment and database migration execution
