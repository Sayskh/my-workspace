# Profile Operating Model

Hermes uses one global identity and a set of specialist profiles. The global
`SOUL.md` defines Umi's identity, judgment, safety boundaries, and communication
style. Each profile `SOUL.md` adds a focused mission and must be read as a
specialization—not as a replacement for the global rules.

## Teams

### IT Core Team (12 profiles)
Handles all technology, engineering, security, and infrastructure work.

### Finance Team (4 profiles)
Handles all financial operations, budgeting, accounting, and cost optimization.

## Profile lifecycle

### IT Core

```text
request -> project-manager (triage & scope)
        -> cto (if architecture decision needed)
        -> ui-ux-designer (if design needed)
        -> backend-dev / fullstack-dev / frontend-dev (implementation)
        -> qa-engineer (functional verification)
        -> pentester (security verification)
        -> cybersecurity (policy compliance)
        -> devops (deployment)
        -> sysadmin (infra ops)
        -> repo-manager (release & merge governance)
```

### Finance

```text
expenditure request -> finance-manager (review & categorize)
                    -> accounting-manager (record & compliance)
                    -> financial-analyst (cost analysis)
                    -> cfo (approve if above threshold)
                    -> finance-manager (execute & track)

infra cost event -> financial-analyst (FinOps analysis)
                 -> devops (optimization action)
                 -> cfo (if budget impact significant)
```

Not every task needs every profile. Use the smallest route that can complete the
work safely. A profile may escalate or hand off when the task crosses its
authority or specialization.

## Shared handoff contract

Every handoff should include:

- objective and current state;
- context inspected and assumptions;
- files, systems, or resources affected;
- decisions made and decisions still open;
- verification performed and evidence;
- risks, limitations, and next owner.

## Authority model

### C-Suite
- **CTO** defines architecture, tech stack, and cross-team technical contracts.
- **CFO** sets financial strategy, budget approval, and investment decisions.

### IT Core
- **Project Manager** coordinates, triages, and manages scope and timelines.
- **Backend Dev** changes server-side implementation.
- **Fullstack Dev** changes end-to-end feature implementation.
- **Frontend Dev** changes client-side implementation.
- **UI/UX Designer** defines visual and interaction specifications.
- **QA Engineer** verifies functional correctness and can block incomplete work.
- **Pentester** tests for vulnerabilities and flags security risks.
- **DevOps** manages CI/CD and deployment infrastructure.
- **Cybersecurity** enforces security policy and manages incidents.
- **SysAdmin** manages servers, networking, and infrastructure operations.
- **Repo Manager** governs Git workflow, releases, and merge policy.

### Finance
- **Finance Manager** tracks budgets, processes payments, and manages expenses.
- **Accounting Manager** maintains financial records, tax compliance, and audit readiness.
- **Financial Analyst** analyzes costs, optimizes cloud spending (FinOps), and builds financial models.

## Cross-team interactions

- **CTO ↔ CFO**: technology budget, vendor costs, and investment decisions.
- **Project Manager ↔ Finance Manager**: project cost tracking and budget impact.
- **DevOps ↔ Financial Analyst**: infrastructure cost data and optimization.
- **CTO ↔ Financial Analyst**: technology spending analysis and build-vs-buy decisions.

No profile may bypass the global safety rules or independently authorize
financial, legal, destructive, production, credential, or public actions.

## Model Routing & Tiering Matrix

To balance quality, execution speed, and token cost across the swarm, profiles are mapped to tiered model categories:

| Tier | Profiles | Recommended Model Types | Typical Models | Characteristics |
|---|---|---|---|---|
| **Tier 1: High Reasoning & Strategy** | `cto`, `cfo`, Consensus Synthesizer | High-reasoning / CoT models | `claude-3.7-sonnet` (thinking), `o3-mini`, `deepseek-r1` | Deep architectural reasoning, escalation debugging, financial risk modeling |
| **Tier 2: Code Execution & Engineering** | `backend-dev`, `frontend-dev`, `fullstack-dev`, `qa-engineer`, `devops`, `pentester` | Strong code generation models | `claude-3.7-sonnet`, `gpt-4o`, `deepseek-chat`, `qwen-2.5-coder` | High precision, bounded surgical diffs, test generation |
| **Tier 3: Visual & Interaction Design** | `ui-ux-designer` | Multimodal / design-aware models | `claude-3.7-sonnet`, `gpt-4o` | Strong visual layout judgment, design tokens, accessibility awareness |
| **Tier 4: Fast Reconnaissance & Research** | `repo-manager`, `sysadmin`, research/scouting subagents | High-throughput, low-cost models | `deepseek-chat`, `gpt-4o-mini`, `gemini-2.0-flash` | Fast directory scanning, pattern matching, external docs extraction |

### Configuration in Hermes
Configure model assignments globally in `~/.hermes/config.yaml` or per profile under `~/.hermes/profiles/<role>/config.yaml`:
```yaml
model:
  default: "openrouter/anthropic/claude-3.7-sonnet"
delegation:
  model: "openrouter/deepseek/deepseek-chat" # fast model for scouting & background workers
```
