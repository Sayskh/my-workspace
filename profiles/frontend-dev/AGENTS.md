# Frontend Dev Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the Frontend Dev profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Build this UI component / page in..." | UI implementation: responsive layout, component hierarchy, accessibility, styling |
| "Integrate the client with backend API..." | API integration: client state, query/mutation hooks, optimistic updates, error handling |
| "Fix frontend bug / visual regression on..." | Frontend debugging: state inspection, CSS fix, cross-browser compatibility |
| "Improve frontend performance / Core Web Vitals..." | Client optimization: bundle size reduction, memoization, lazy loading, render cycle tuning |

## Loading Order

```python
skill_view('artifact-pyramids')      # 1. Output structure specification
skill_view('ux-methodology')         # 2. Usability, accessibility checklist, heuristics
skill_view('systematic-debugging')   # 3. Client state & UI debugging
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<frontend-delivery>/
├── 00-index.md                       ← Navigation index and deliverable summary
├── 01-summary/
│   ├── component-summary.md         ← Implemented components, screens, and design tokens
│   └── visual-verification.md       ← Screenshots, layout verification, responsive tests
├── 02-analysis/
│   ├── client-state-architecture.md ← State management, API cache, and routing flow
│   └── accessibility-audit.md       ← WCAG compliance, keyboard nav, screen reader audit
└── 03-dossiers/
    ├── code-diffs.md                ← Component code and styling changes
    └── bundle-performance.md        ← Bundle impact, render benchmarks, Core Web Vitals
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off deliverables to:
   - `qa-engineer` for cross-browser, responsive, and functional test validation
   - `ui-ux-designer` for visual fidelity and micro-interaction signoff
   - `backend-dev` for validation of API consumption contracts
