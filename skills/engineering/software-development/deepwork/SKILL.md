---
name: deepwork
description: Structured orchestrator workflow for large, high-risk, multi-phase coding efforts with explicit dependency graphs and review gates. Do not activate for routine single-file changes.
---

# Deepwork Workflow

Deepwork is an orchestrator workflow for heavy development sessions: multiple
dependent phases, cross-cutting architectural changes, high-risk migrations,
or sustained coordination across specialist lanes. Skip it for trivial edits,
quick docs changes, simple bug fixes, or routine bounded features.

## Core Contract

When deepwork is active, the orchestrator/project manager acts as a scheduler,
not as the default implementation worker.

## Workspace State

`.slim/deepwork/` holds session and task state:
- `.slim/deepwork/<session-id>.md`: Pinned router head tracking current session phase.
- `.slim/deepwork/<task-slug>/`: Task directory containing progress and topic files.
  - `progress.md`: Compact log and open checklist (status, phase, next step, frozen constraints).
  - `<topic>.md`: Detailed analysis, design artifacts, or verification reports.

Ensure `.gitignore` contains `.slim/deepwork/` and `.ignore` contains `!.slim/deepwork/`.

## Planning Phase

1. **Decomposition:** Draft a phased execution plan based on natural delivery boundaries.
2. **Review Gates:** Make an architectural review (`cto` / senior advisor) mandatory after each major phase.
3. **Execution Path:** Identify independent parallel lanes versus sequential blocking dependencies before dispatching work.

## Execution Discipline

- Dispatch independent implementation tasks to developer subagents (`backend-dev`, `frontend-dev`, `fullstack-dev`) via background execution (`delegate_task(background=True)`).
- Keep the parent orchestrator unblocked; reconcile terminal results before advancing.
- Do not advance to the next phase while background jobs are running or terminal results remain unreconciled.

## Design Protection Guardrail

When a deepwork phase includes UI/UX work:
- Deliver visual specifications through `ui-ux-designer`.
- Developers must preserve layout, hierarchy, spacing, motion, affordances, and responsive styling without flattening them under the guise of refactoring.
- Follow-up visual or interaction changes route back to `ui-ux-designer`.

## Completion

Upon concluding the initiative:
- Run final end-to-end verification.
- Update `progress.md` to `status: completed` with key deliverable references.
- Deliver a concise executive summary with the path to deliverables.
