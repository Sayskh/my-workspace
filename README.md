# Hermes Agent Workspace

Personal [Hermes Agent](https://github.com/NousResearch/hermes-agent) configuration tuned for multi-agent workflows, homelab infrastructure management, and developer tooling.

---

## Profiles & Architecture

Instead of running a single generalist agent, tasks are split across role-specific profiles with isolated personas (`SOUL.md`), memories, and configurations.

```text
                  [ User / Telegram ]
                           │
                           ▼
                  default (Umi / Lead)
                           │
        ┌──────────┬───────┴──────┬──────────┬──────────┐
        ▼          ▼              ▼          ▼          ▼
     planner      lead         builder    reviewer     ops
      (PRD)    (Arch/API)       (Code)    (Security)  (Infra)
```

| Profile | Focus |
|---|---|
| `default` | Orchestration, triage, and Telegram gateway entry point |
| `planner` | Specs, user stories, requirements, and edge-case discovery |
| `lead` | System design, database schemas, and API contracts |
| `builder` | Implementation, refactoring, and integration code |
| `reviewer` | Static analysis, test coverage verification, and code audits |
| `ops` | Linux/Docker management, service health checks, and homelab triage |

---

## Model Recommendations

### Cloud Models

| Profile | Primary Pick | Alternative | Notes |
|---|---|---|---|
| `default` | `claude-fable-5.1` | `gpt-5.6-terra` | Long-context router, cost-efficient cached turns |
| `planner` | `claude-opus-5` | `qwen-3.8-max` | High reasoning depth for long specifications |
| `lead` | `claude-fable-5.1 (thinking)` | `deepseek-v4-pro (think-max)` | Strict design decisions and contract validation |
| `builder` | `claude-fable-5.1` | `gpt-5.6-sol` | Long-horizon coding and self-verification |
| `reviewer` | `deepseek-v4-pro (think-max)` | `claude-opus-5` | Thorough security auditing and edge-case scanning |
| `ops` | `qwen-3.8-max` | `deepseek-v4-flash` | Fast log inspection, command execution |

### Local Models (Ollama)

| Hardware Tier | General & Routing | Coding | Reasoning |
|---|---|---|---|
| 8–12 GB VRAM | `qwen3.5:9b` | `gemma4:8b` | `qwen3.5:9b` |
| 16–24 GB VRAM | `qwen3.8:27b` | `devstral-small-2:24b` | `gemma4:27b` |
| 32+ GB VRAM | `qwen3-coder-next` | `qwen3-coder-next` | `deepseek-v4-pro` (quantized) |

---

## Configured MCP Servers

Active integrations configured in `config.yaml` (`hermes mcp list`):

| Server | Category | Purpose |
|---|---|---|
| `n8n` | Automation | Run local and remote automation webhooks |
| `cloudflare` | Infra | DNS records and Cloudflare tunnel ingress |
| `grafana` | Monitoring | Query Prometheus metrics and container stats |
| `supabase` | Database | Postgres queries, migrations, and auth policies |
| `context7` | Dev | Library docs lookup and current API specs |
| `deepwiki` | Dev | GitHub repository semantic search |
| `semgrep` | Security | SAST scanning and rule checking |
| `sentry` | Diagnostics | Inspect live exceptions and error stack traces |
| `postman` | API | Run API collections and schema tests |
| `hugging_face` | ML | Model search, dataset discovery, and inference APIs |
| `linear` | Tracking | Issue board updates and tracking |
| `notion` | Notes | Search and sync documentation |
| `todoist` | Tasks | Task creation and priority sync |
| `wolfram` | Math | Analytical computing and scientific calculations |

---

## Server & Homelab Skills (`skills/server/`)

Operational guides and playbooks loaded into the agent:

- **Incident response**: 5-step runbook execution (*Pre-flight → Plan → Execute → Verify → Rollback*)
- **Containers**: Docker Swarm, private registries, GPU pass-through, compose stacks
- **Hypervisors & OS**: Proxmox VE 8, LXC containers, Debian 12, NixOS
- **Networking & Storage**: RouterOS, UniFi, TrueNAS SCALE, Synology DSM

---

## How to Run

### Switching Profiles
```bash
# Default profile (orchestration)
hermes

# Specialist profile
hermes -p builder
hermes -p reviewer
hermes -p ops
```

### Telegram Gateway
```bash
hermes gateway start
hermes gateway status
```

### Docker Deployment (Server / VPS)
```bash
cp .env.example .env
docker compose -f docker-compose.server.yml up -d
```

### Workspace Sync (Local Windows Setup)
If editing profiles or skills in this repository while Hermes runs from `%LOCALAPPDATA%\hermes`:
```bash
python sync.py push   # Repo -> AppData
python sync.py pull   # AppData -> Repo
python sync.py all    # Bidirectional sync
```
*(Note: `sync.py` is ignored in Git to prevent local environment leaks).*

---

## Repository Structure

```text
hermes-agent/
├── config.yaml               # Active Hermes config & MCP definitions
├── SOUL.md                   # Default persona (Umi)
├── profiles/                 # Squad profiles (SOUL.md, configs)
│   ├── planner/
│   ├── lead/
│   ├── builder/
│   ├── reviewer/
│   └── ops/
├── skills/                   # Loaded skill definitions
│   ├── server/               # Homelab & infra administration
│   ├── devops/               # Verification & CI/CD workflows
│   └── software-development/ # Deep work, planning, code review
├── docker-compose.server.yml # Containerized stack
└── .env.example              # Environment variables template
```
