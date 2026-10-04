# Project Manager Profile — Agent Guidance

This document guides AI agents interacting with or consuming outputs from the Project Manager profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Plan the project / feature for..." | Full initiative decomposition: milestones, task breakdown, critical path |
| "Break down this feature into sprint tasks..." | Work decomposition: actionable dev stories, acceptance criteria, story points |
| "Map the dependencies for this release..." | Dependency mapping: blocker identification, critical path analysis |
| "Track progress and identify blockers on..." | Delivery status: velocity assessment, risk mitigation, blocker resolution |

## Loading Order

```python
skill_view('artifact-pyramids')          # 1. Progressive disclosure structure
skill_view('implementation-planning')    # 2. Work breakdown and critical path frameworks
skill_view('mermaid-diagrams')           # 3. Gantt charts, dependency diagrams, workflows
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<project-plan>/
├── 00-index.md                       ← Navigation index and executive summary
├── 01-summary/
│   ├── delivery-roadmap.md          ← High-level milestones and release timeline
│   └── critical-path-summary.md     ← Key dependencies and immediate priorities
├── 02-analysis/
│   ├── work-breakdown-structure.md  ← Epics, stories, and task specifications
│   ├── risk-blocker-matrix.md       ← Identified risks, mitigations, and owners
│   └── dependency-graph.md          ← Mermaid diagram of task relationships
└── 03-dossiers/
    ├── task-specifications.md       ← Acceptance criteria and verification checklists
    └── stakeholder-briefing.md      ← Comms plan and status update cadences
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off task specifications to:
   - `cto` for architecture validation
   - `ui-ux-designer` for design assets and flows
   - `backend-dev` / `frontend-dev` / `fullstack-dev` for code execution
   - `qa-engineer` for acceptance test criteria
