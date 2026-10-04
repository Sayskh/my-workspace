# Hermes Agent Workspace

Curated [Hermes Agent](https://github.com/NousResearch/hermes-agent) profiles and shared skills for specialist multi-agent swarms — opinionated, Hermes-native, and artifact-pyramid structured.

---

## Architecture & Specialist Swarm

Instead of a single monolithic agent, tasks are routed to 16 specialized roles organized into two coordinated teams: **IT Core** and **Finance**. Global safety rules, ethics, and base identity are defined in `SOUL.md` (Umi, Chief of Staff & Gateway), while each profile adds a focused mission, authority boundary, and skill dependencies.

```text
                                [ User / Client ]
                                        │
                                        ▼
                                 SOUL.md (Umi)
                            Chief of Staff & Gateway
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

Detailed lifecycle pipelines, authority matrices, and cross-team interactions are documented in **[PROFILES.md](file:///d:/aqil/code/hermes-agent/PROFILES.md)**.

---

## Profiles Roster

### IT Core Team (12 Profiles)

| Profile | Focus & Mission | Core Skills |
|---|---|---|
| [`cto`](file:///d:/aqil/code/hermes-agent/profiles/cto/) | Technology strategy, architecture governance, build-vs-buy TCO | `artifact-pyramids`, `executive-methodology`, `technology-radar` |
| [`project-manager`](file:///d:/aqil/code/hermes-agent/profiles/project-manager/) | Work breakdown (WBS), sprint planning, critical path analysis | `artifact-pyramids`, `implementation-planning` |
| [`backend-dev`](file:///d:/aqil/code/hermes-agent/profiles/backend-dev/) | Server-side services, database persistence, API contracts | `artifact-pyramids`, `systematic-debugging`, `architecture` |
| [`fullstack-dev`](file:///d:/aqil/code/hermes-agent/profiles/fullstack-dev/) | Vertical feature slices end-to-end (UI + API + DB) | `artifact-pyramids`, `systematic-debugging`, `ux-methodology` |
| [`frontend-dev`](file:///d:/aqil/code/hermes-agent/profiles/frontend-dev/) | Client interfaces, responsive design, WCAG accessibility, state | `artifact-pyramids`, `ux-methodology` |
| [`ui-ux-designer`](file:///d:/aqil/code/hermes-agent/profiles/ui-ux-designer/) | User journeys, design systems, visual tokens, wireframes | `artifact-pyramids`, `ux-methodology`, `mermaid-diagrams` |
| [`qa-engineer`](file:///d:/aqil/code/hermes-agent/profiles/qa-engineer/) | Automated test suites, edge case fuzzing, quality gatekeeping | `artifact-pyramids`, `qa-methodology` |
| [`pentester`](file:///d:/aqil/code/hermes-agent/profiles/pentester/) | Offensive security assessments, CVSS exploit verification | `artifact-pyramids`, `security-audit-methodology` |
| [`devops`](file:///d:/aqil/code/hermes-agent/profiles/devops/) | CI/CD pipelines, container orchestration, Docker, zero-downtime | `artifact-pyramids`, `docker-management`, `site-reliability-engineering` |
| [`cybersecurity`](file:///d:/aqil/code/hermes-agent/profiles/cybersecurity/) | Defensive zero-trust architecture, IAM, secret hygiene, incident response | `artifact-pyramids`, `security-audit-methodology` |
| [`sysadmin`](file:///d:/aqil/code/hermes-agent/profiles/sysadmin/) | Server operating systems, networking, storage arrays, observability | `artifact-pyramids`, `site-reliability-engineering` |
| [`repo-manager`](file:///d:/aqil/code/hermes-agent/profiles/repo-manager/) | Git hygiene, branch protection, SemVer, automated changelogs | `artifact-pyramids`, `technical-documentation` |

### Finance Team (4 Profiles)

| Profile | Focus & Mission | Core Skills |
|---|---|---|
| [`cfo`](file:///d:/aqil/code/hermes-agent/profiles/cfo/) | Financial strategy, capital allocation, cash runway, economic modeling | `artifact-pyramids`, `financial-modeling`, `executive-methodology` |
| [`finance-manager`](file:///d:/aqil/code/hermes-agent/profiles/finance-manager/) | Budget tracking, operational disbursements, vendor contracts, cash flow | `artifact-pyramids`, `financial-modeling`, `startup-analysis` |
| [`accounting-manager`](file:///d:/aqil/code/hermes-agent/profiles/accounting-manager/) | General ledger, double-entry bookkeeping, GAAP, tax compliance | `artifact-pyramids`, `financial-modeling`, `technical-documentation` |
| [`financial-analyst`](file:///d:/aqil/code/hermes-agent/profiles/financial-analyst/) | FinOps cloud cost optimization, SaaS metrics, cohort retention | `artifact-pyramids`, `financial-modeling`, `saas-valuation-compression`, `yfinance-data` |

---

## Standard Profile Specification

Every profile adheres to the strict 4-document specification:

```text
profiles/<role>/
├── SOUL.md       # Identity, First Principles, Decision Heuristics, Artifact Pyramid Output Contract
├── profile.yaml  # Machine-readable description, required skills, and recommended skills
├── AGENTS.md     # Agent Guidance: Trigger Patterns ("User says X -> Means Y"), loading order, handoff
└── README.md     # Human-facing profile documentation and quickstart
```

---

## Skills Architecture

Skills are organized into modular domain directories under `skills/`:

```text
skills/
├── baseline/       # antislop, ideation, artifact-pyramids
├── engineering/    # architecture (ADRs, C4, Arc42), technology-radar, systematic-debugging,
│                   # qa-methodology, security-audit-methodology, implementation-planning,
│                   # technical-documentation, executive-methodology
├── finance/        # financial-modeling, startup-analysis, saas-valuation-compression,
│                   # yfinance-data, stock-liquidity
├── operations/     # docker-management, site-reliability-engineering, server, web
├── creative/       # ux-methodology, mermaid-diagrams, design
├── knowledge/      # research, citations, note-taking
├── productivity/   # task management, documents
├── communications/ # email, social media
└── media/          # audio, video processing
```

### The Output Contract: Artifact Pyramids

Profiles avoid flooding the chat context with thousands of unstructured lines. Instead, complex deliverables follow the **Artifact Pyramid** convention:

```text
<engagement-output>/
├── 00-index.md          ← Navigation index, metadata, SOURCES
├── 01-summary/          ← L1: Executive summary, primary recommendations, ADRs
├── 02-analysis/         ← L2: In-depth trade-off evaluations, models, matrices
└── 03-dossiers/         ← L3: Raw logs, workbooks, test scripts, diffs
```
The caller receives the absolute path to `00-index.md` as the handoff pointer.

---

## How to Run

### Default Gateway (Umi)
```bash
hermes
```

### Specialist Profiles
```bash
# IT Core
hermes --profile cto
hermes --profile project-manager
hermes --profile backend-dev
hermes --profile fullstack-dev
hermes --profile frontend-dev
hermes --profile ui-ux-designer
hermes --profile qa-engineer
hermes --profile pentester
hermes --profile devops
hermes --profile cybersecurity
hermes --profile sysadmin
hermes --profile repo-manager

# Finance
hermes --profile cfo
hermes --profile finance-manager
hermes --profile accounting-manager
hermes --profile financial-analyst
```

---

## Validation

Verify that all profiles, YAML metadata, and skill references comply with standards:

```bash
python scripts/validate_profiles.py
```

Expected output:
```text
Profile validation passed: 16 profiles, 247 shared skills.
```

---

## License

MIT
