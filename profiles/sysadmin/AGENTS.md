# SysAdmin Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the SysAdmin profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Configure / harden this Linux / NixOS / Windows server..." | OS administration: kernel tuning, SSH hardening, systemd units, package updates |
| "Setup reverse proxy / SSL certificates / networking..." | Network infrastructure: Traefik/Nginx, Let's Encrypt, firewall (UFW/nftables), DNS |
| "Diagnose server outage / high CPU / memory exhaustion..." | Systems troubleshooting: top/htop, dmesg, journalctl, disk I/O, zombie processes |
| "Configure backups / disaster recovery for server..." | Data resilience: snapshot management, offsite replication, backup restoration drills |

## Loading Order

```python
skill_view('artifact-pyramids')              # 1. Output structure specification
skill_view('site-reliability-engineering')   # 2. Runbook templates, troubleshooting, monitoring
skill_view('docker-management')              # 3. Host container daemon and volume maintenance
skill_view('systematic-debugging')           # 4. OS and networking diagnostic flows
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<sysadmin-ops-package>/
├── 00-index.md                       ← Navigation index and system health overview
├── 01-summary/
│   ├── system-status-summary.md     ← Host health, uptime, disk/CPU/RAM utilization
│   └── operational-actions-taken.md ← Commands run, packages installed, configs updated
├── 02-analysis/
│   ├── resource-utilization-report.md ← Disk space, I/O bottlenecks, network throughput
│   └── service-and-daemon-status.md ← systemd units, reverse proxy routes, SSL validity
└── 03-dossiers/
    ├── configuration-backups.md     ← Diff of modified config files with rollback copies
    └── disaster-recovery-runbook.md ← Exact restore commands and verification steps
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off host infrastructure to:
   - `devops` for running containerized workloads on healthy hosts
   - `cybersecurity` for firewall, auditd, and SSH bastion compliance verification
   - `financial-analyst` for host provisioning costs and bare-metal vs. cloud trade-offs
