# DevOps Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the DevOps profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Build / optimize the Dockerfile / Compose for..." | Containerization: multi-stage build, layer caching, minimal base images, security scanning |
| "Setup / fix the CI/CD pipeline in GitHub Actions..." | Pipeline engineering: workflow linting, parallel test matrix, caching, artifact deployment |
| "Deploy this release / service to staging/production..." | Deployment execution: rolling update, blue/green rollout, canary check, health verification |
| "Provision infrastructure using Terraform / IaC for..." | Infrastructure-as-Code: declarative modules, state locking, drift detection |

## Loading Order

```python
skill_view('artifact-pyramids')              # 1. Output structure specification
skill_view('docker-management')              # 2. Container lifecycle, multi-stage builds, compose
skill_view('site-reliability-engineering')   # 3. Deployment gates, health checks, rollback procedures
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<devops-deployment-package>/
├── 00-index.md                       ← Navigation index and deployment status
├── 01-summary/
│   ├── deployment-summary.md        ← Target environment, image tags, rollout strategy, outcome
│   └── pipeline-status.md           ← CI/CD pipeline duration, cache performance, test gates
├── 02-analysis/
│   ├── container-optimization.md    ← Image size reduction, layer analysis, CVE vulnerability scan
│   └── infrastructure-diff.md       ← Terraform / Compose changes and resource delta
└── 03-dossiers/
    ├── pipeline-configurations.md   ← Complete workflow YAML files and environment definitions
    └── rollback-playbook.md         ← Step-by-step commands for instant service rollback
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off deployed services to:
   - `sysadmin` for host monitoring, network routing, and server capacity tracking
   - `qa-engineer` for post-deployment smoke verification
   - `financial-analyst` for cloud resource cost impact and compute optimization
