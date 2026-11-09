# Umi Harness

Cross-platform multi-agent orchestration harness, 16 specialist profiles, and 373 capability skills.

Umi serves as the primary gateway and Chief of Staff. Umi analyzes requests, decomposes workflows, and delegates domain-specific execution to specialized subagents across IT Core and Finance teams.

Compatible out-of-the-box with **Hermes Agent**, **OpenCode**, **Claude Code**, **Antigravity**, **Cursor IDE**, and standard **LLM APIs** (OpenAI / Anthropic / xAI).

---

## Architecture & Swarm Topology

Umi delegates domain implementation directly to specialist subagents. Gateway rules prevent direct domain execution when a specialized profile exists.

```text
                                [ User Request ]
                                        │
                                        ▼
                                  Umi (Gateway)
                      Chief of Staff & Primary Orchestrator
                     (SOUL.md / AGENTS.md / SYSTEM_PROMPT.md)
                                        │
                    ┌───────────────────┴───────────────────┐
                    ▼                                       ▼
             IT Core Team (12)                       Finance Team (4)
      ┌─────────────────────────────┐         ┌─────────────────────────────┐
      │ cto                         │         │ cfo                         │
      │ project-manager             │         │ finance-manager             │
      │ backend-dev / fullstack-dev │         │ accounting-manager          │
      │ frontend-dev                │         │ financial-analyst (FinOps)  │
      │ ui-ux-designer              │         └─────────────────────────────┘
      │ qa-engineer                 │
      │ pentester                   │
      │ devops                      │
      │ cybersecurity               │
      │ sysadmin                    │
      │ repo-manager                │
      └─────────────────────────────┘
```

Detailed lifecycle pipelines, authority matrices, and cross-team interactions are documented in **[PROFILES.md](PROFILES.md)**.

---

## Profiles Roster

### IT Core Team (12 Profiles)

| Profile | Focus & Domain | Core Skills |
|---|---|---|
| [`cto`](profiles/cto/) | Architecture governance, technology strategy, RFCs, build-vs-buy TCO | `artifact-pyramids`, `executive-methodology`, `technology-radar` |
| [`project-manager`](profiles/project-manager/) | Work breakdown structures (WBS), sprint planning, milestone tracking | `artifact-pyramids`, `implementation-planning` |
| [`backend-dev`](profiles/backend-dev/) | Server APIs, database persistence, schema migrations, query plans | `artifact-pyramids`, `systematic-debugging`, `nodejs-backend-patterns` |
| [`fullstack-dev`](profiles/fullstack-dev/) | End-to-end vertical feature slices (UI + API + DB integration) | `artifact-pyramids`, `systematic-debugging`, `ux-methodology` |
| [`frontend-dev`](profiles/frontend-dev/) | Client interfaces, responsive design, WCAG accessibility, state | `artifact-pyramids`, `ux-methodology`, `react-best-practices` |
| [`ui-ux-designer`](profiles/ui-ux-designer/) | UX journeys, design systems, visual tokens, wireframes, UI styling | `artifact-pyramids`, `ux-methodology`, `mermaid-diagrams` |
| [`qa-engineer`](profiles/qa-engineer/) | Automated test suites, edge case verification, quality gatekeeping | `artifact-pyramids`, `qa-methodology`, `javascript-testing-patterns` |
| [`pentester`](profiles/pentester/) | Offensive security assessments, CVSS exploit verification | `artifact-pyramids`, `security-audit-methodology` |
| [`devops`](profiles/devops/) | CI/CD pipelines, container orchestration, Docker, zero-downtime | `artifact-pyramids`, `docker-management`, `site-reliability-engineering` |
| [`cybersecurity`](profiles/cybersecurity/) | Defensive zero-trust architecture, IAM, secrets hygiene, incident triage | `artifact-pyramids`, `security-audit-methodology` |
| [`sysadmin`](profiles/sysadmin/) | Linux OS, homelab infrastructure, networking, storage arrays, observability | `artifact-pyramids`, `site-reliability-engineering` |
| [`repo-manager`](profiles/repo-manager/) | Git hygiene, branch protection, SemVer, changelogs, release tagging | `artifact-pyramids`, `technical-documentation` |

### Finance Team (4 Profiles)

| Profile | Focus & Domain | Core Skills |
|---|---|---|
| [`cfo`](profiles/cfo/) | Financial strategy, capital runway, economic modeling, executive decisions | `artifact-pyramids`, `financial-modeling`, `executive-methodology` |
| [`finance-manager`](profiles/finance-manager/) | Operational budget tracking, cash flow, disbursements, vendor contracts | `artifact-pyramids`, `financial-modeling`, `startup-analysis` |
| [`accounting-manager`](profiles/accounting-manager/) | General ledger, double-entry bookkeeping, GAAP, tax compliance | `artifact-pyramids`, `financial-modeling`, `technical-documentation` |
| [`financial-analyst`](profiles/financial-analyst/) | FinOps cloud cost optimization, SaaS metrics, cohort retention | `artifact-pyramids`, `financial-modeling`, `saas-valuation-compression`, `yfinance-data` |

Every profile is strictly defined across 4 documents:
- `SOUL.md`: Identity, first principles, decision heuristics, output contract
- `profile.yaml`: Machine-readable description, required and recommended skills
- `AGENTS.md`: Trigger patterns ("User says X -> Means Y"), loading order, handoff protocol
- `README.md`: Profile documentation and quickstart

---

## Skills Architecture

The repository contains **373 shared skills** organized into domain categories:

```text
skills/
├── agent-systems/          # Multi-agent coordination, session guard, token optimization
├── antislop/               # Hardened design and copy rules for AI agents
├── baseline/               # Core execution, ideation, artifact pyramids
├── communications/         # Email, social media integrations
├── creative/               # UI/UX design, visual design, animations, diagrams
├── engineering/            # Architecture, testing, devops, database, backend/frontend
├── finance/                # Financial modeling, FinOps, startup valuation, stock analysis
├── knowledge/              # Research, citations, note-taking
├── media/                  # Audio, video processing
├── operations/             # Linux, homelab, virtualization, networking, cloud
├── productivity/           # Office documents (xlsx, docx, pdf), workspace pipelines
└── reverse engineering/    # Reverse engineering suite (REA)
```

100% of skills are mapped in the auto-dispatch routing matrix in `SOUL.md`, `SYSTEM_PROMPT.md`, and OpenCode `umi.md`. No manual skill invocation is required.

---

## Output Contract: Artifact Pyramids

Complex deliverables must avoid polluting context with raw logs and unstructured dumps. Outputs follow the Artifact Pyramid convention:

```text
<engagement-output>/
├── 00-index.md          <- Navigation index, metadata, source citations
├── 01-summary/          <- L1: Executive summary, primary recommendations, ADRs
├── 02-analysis/         <- L2: In-depth trade-off evaluations, models, matrices
└── 03-dossiers/         <- L3: Raw logs, workbooks, test scripts, diffs
```

Handoff between subagents returns the path to `00-index.md` as the authoritative pointer.

---

## Multi-Platform Setup & Execution

### 1. Hermes Agent
Run the root orchestrator directly, or launch into a specific specialist profile:
```bash
# Default gateway (Umi)
hermes

# Specialist profile
hermes --profile cto
hermes --profile backend-dev
hermes --profile devops
```

### 2. OpenCode
Point `~/.config/opencode/opencode.json` to the workspace skills directory. OpenCode auto-loads `AGENTS.md` and discovers agent definitions in `~/.config/opencode/agents/`:
```bash
opencode
```

### 3. Claude Code
Claude Code natively reads `CLAUDE.md` from the repository root:
```bash
claude
```

### 4. Antigravity
Antigravity automatically consumes root `AGENTS.md` and exposes workspace tools and skills.

### 5. Cursor IDE
Cursor auto-applies rules from `.cursor/rules/karpathy-guidelines.mdc` across workspace files.

### 6. Generic LLM APIs / Custom Bots (Grok, Open bot, LiteLLM)
Load `SYSTEM_PROMPT.md` directly into the system prompt parameter of any completions request.

---

## Core Engineering Rules

All profiles and implementations adhere to four fundamental execution principles:

1. **Think Before Coding:** State assumptions explicitly. Surface trade-offs before implementing. Push back when simpler solutions exist. Stop and ask if requirements are ambiguous.
2. **Simplicity First:** Strict YAGNI. Minimum code that solves the problem. No speculative abstractions, single-use interfaces, or premature configurability. Delete before adding.
3. **Surgical Changes:** Touch only what must be touched. Match existing conventions. Do not touch adjacent working code. Clean up orphaned imports and variables.
4. **Goal-Driven Execution:** Define deterministic success criteria before editing files. Verify every change with automated tests or deterministic checks.

---

## Customization & Forking

To adapt this workspace with your own name and preferred AI orchestrator identity, follow the interactive setup guide in **[docs/CUSTOMIZE.md](docs/CUSTOMIZE.md)**. It includes a ready-to-run `grill-me` prompt that will walk through your preferences and update all configuration anchors automatically.

---

## Validation

Run the profile validator to verify YAML structure, frontmatter schemas, and skill references:

```bash
python scripts/validate_profiles.py
```

Expected output:
```text
Profile validation passed: 16 profiles, 373 shared skills.
```

---

## License

MIT
