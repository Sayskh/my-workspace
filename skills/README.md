# Hermes Skills

Skills are task-specific playbooks loaded on demand. The global `SOUL.md` and the
active profile's `SOUL.md` always have priority over a skill.

## Design principles

- Keep one skill focused on one repeatable outcome.
- Load the narrowest matching skill, not an entire domain by default.
- Treat this directory as a library, not a list of always-active instructions.
- Keep runtime metadata (`.hub/`, `.bundled_manifest`, usage files) untouched.
- Add maintained skills with YAML frontmatter containing `name` and an actionable
  `description`.

## Canonical layout

All installed skills used by Hermes belong under this directory. Installer
outputs from other hosts (`.agents/skills` and `.claude/skills`) are copied here
and remain ignored as disposable caches.

```text
skills/
├── software-development/  # engineering, orchestration, review, token control
├── creative/              # UI/UX, design, motion, visual workflows
├── server/                # infrastructure and operations
├── web/                   # web workflows
├── research/              # research and citations
├── productivity/          # documents and task workflows
├── media/                 # media workflows
└── installed-manifest.yaml
```

Use `installed-manifest.yaml` for the authoritative source-to-destination map.
Do not load every skill just because it is installed.

## Domain map

| Domain | Directory | Use for |
|---|---|---|
| Baseline | `antislop/`, `brainstorming/`, `executing-plans/` | Quality, ideation, and controlled execution |
| Software delivery | `software-development/`, `devops/` | Coding, debugging, testing, reviews, and delivery |
| Agent systems | `autonomous-ai-agents/` | Agent orchestration and computer-use workflows |
| Infrastructure | `server/` | Homelab, Linux, Docker, networking, and operations |
| Web | `web/` | Browser research and web workflows |
| Research | `research/`, `note-taking/` | Evidence gathering, citations, and knowledge capture |
| Productivity | `productivity/`, `email/`, `apple/` | Documents, tasks, mail, and personal tools |
| Communication | `social-media/` | Social publishing and platform workflows |
| Creative | `creative/`, `media/` | Visual, audio, video, and media generation |

## Profile routing

Use `skill-catalog.yaml` as the human-maintained routing index. It maps each
profile to preferred domains and the narrow skills that should normally be
considered first.

| Profile | First-choice domains | Typical skill focus |
|---|---|---|
| `default` | baseline, software delivery, research, productivity | Triage, planning, execution, and coordination |
| `planner` | baseline, research, productivity | Discovery, requirements, citations, and action plans |
| `lead` | baseline, software delivery, research | Architecture, contracts, decomposition, and risk |
| `builder` | baseline, software delivery, devops | Implementation, debugging, testing, and integration |
| `reviewer` | baseline, software delivery, security | Verification, static analysis, and quality gates |
| `ops` | baseline, server, devops, web | Incident response, deployment, monitoring, and rollback |

## Loading rules

1. Read the global `SOUL.md` and active profile `SOUL.md` first.
2. Select the smallest skill whose description matches the actual task.
3. Prefer a profile's `core_skills`; use `supporting_skills` only when needed.
4. If skills overlap, choose the more specific one and avoid duplicate instructions.
5. A skill cannot override identity, safety, approval, or confidentiality rules.
6. External actions, destructive operations, production changes, and publication
   require the approval defined by the active profile and workflow.
7. Verify tool results and report evidence instead of claiming success.
8. When no skill matches, follow the profile workflow and document the gap.

## Maintained skill checklist

Every maintained skill should state:

- YAML frontmatter with `name` and an actionable `description`;
- activation criteria and non-goals;
- required inputs and expected outputs;
- tool, network, and permission constraints;
- failure modes and escalation guidance;
- examples or references for non-obvious workflows.
