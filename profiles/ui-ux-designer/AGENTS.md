# UI/UX Designer Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the UI/UX Designer profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Design the user flow / wireframe for..." | UX architecture: user journey, information architecture, wireframe structure |
| "Create a design system / tokens for..." | Design tokens: typography scale, color palette, spacing, elevations, components |
| "Audit the usability / UX of..." | UX audit: Nielsen Norman heuristics, accessibility audit, friction points |
| "Define interaction patterns and micro-animations for..." | Interaction design: transitions, hover/focus states, modal & toast behaviors |

## Loading Order

```python
skill_view('artifact-pyramids')      # 1. Output structure specification
skill_view('ux-methodology')         # 2. Usability heuristics, accessibility checklist, research methods
skill_view('mermaid-diagrams')       # 3. User flows, journey maps, state charts
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<ux-design-package>/
├── 00-index.md                       ← Navigation index and design brief
├── 01-summary/
│   ├── design-specification.md      ← Visual identity, core screens, and layouts
│   └── user-journey-map.md          ← Happy path, error states, and flow diagrams
├── 02-analysis/
│   ├── design-system-tokens.md      ← Color palette, typography, spacing, radius
│   └── accessibility-heuristics.md  ← Contrast ratios, target sizes, WCAG compliance
└── 03-dossiers/
    ├── component-specifications.md  ← States (idle, hover, active, disabled) per component
    └── edge-cases-and-empty-states.md ← Error screens, empty states, zero-data views
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off deliverables to:
   - `frontend-dev` and `fullstack-dev` for pixel-accurate implementation
   - `project-manager` for validation against user stories and sprint milestones
   - `qa-engineer` for visual regression verification criteria
