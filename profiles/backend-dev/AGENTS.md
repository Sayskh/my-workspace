# Backend Dev Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the Backend Dev profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Build an API endpoint for..." | API implementation: controller, validation, business logic, response serialization |
| "Design the database schema / migration for..." | Data modeling: relational schema, indexes, constraints, migration scripts |
| "Optimize backend query / service performance..." | Performance profiling: slow query optimization, caching layer, indexing |
| "Debug backend error / 500 status on..." | Systematic debugging: stack trace analysis, repro, root cause fix, regression test |

## Loading Order

```python
skill_view('artifact-pyramids')      # 1. Output structure specification
skill_view('systematic-debugging')   # 2. Root cause diagnosis and verification
skill_view('architecture')           # 3. System contracts, ADRs, database patterns
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<backend-delivery>/
├── 00-index.md                       ← Navigation index and deliverable summary
├── 01-summary/
│   ├── implementation-summary.md    ← Changes made, endpoints exposed, schema changes
│   └── test-results.md              ← Unit, integration test results and coverage
├── 02-analysis/
│   ├── api-contracts.md             ← OpenAPI / JSON schema definitions
│   └── database-migration-notes.md  ← Schema diffs, indexes, rollback steps
└── 03-dossiers/
    ├── code-diffs.md                ← Key code changes and architecture rationale
    └── benchmark-results.md         ← Latency, throughput, query execution plans
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off deliverables to:
   - `qa-engineer` for end-to-end and integration verification
   - `pentester` for security audit of exposed endpoints and input validation
   - `frontend-dev` for API contract integration
   - `devops` for database migration and deployment pipelines
