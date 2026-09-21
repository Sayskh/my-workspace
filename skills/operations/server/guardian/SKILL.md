---
name: server-guardian
description: Rules, pre-flight checks, and recovery procedures for Docker, Linux, and homelab services.
version: 1.1.0
metadata:
  hermes:
    tags: [homelab, docker, devops, linux, recovery]
    category: server
---

# Server Guardian

Operational rules, safe execution patterns, and recovery procedures for homelab infrastructure.

## Operational Rules

1. **Pre-flight Check First**: Check target service status and port bindings before running modifications (`docker ps`, `ss -tulpn`, `systemctl status`).
2. **Never Run Destructive Commands Blindly**: Do not run `rm -rf`, `docker system prune -a --volumes`, or drop database tables without explicit backup and user confirmation.
3. **Isolate Database Ports**: Keep PostgreSQL/MySQL/Redis on internal bridge networks or localhost (`127.0.0.1`), never bind `0.0.0.0` unless routed through a VPN (Tailscale/WireGuard).
4. **Immediate Verification**: After restarting or deploying a container, check logs (`docker logs --tail 30 <name>`) and verify HTTP status or socket response before marking task complete.
5. **Fast Rollback**: If a service enters a crash loop (`CrashLoopBackOff`, Exit Code 137, Exit Code 1), revert configuration or restart the prior stable container immediately.

---

## Quick Reference & Commands

### Docker Operations
```bash
# Health & Status
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
docker logs <container> --tail 50
docker inspect <container> | grep -i health

# Safe Stack Update
docker compose pull <service>
docker compose up -d --no-deps <service>

# Resource Usage
docker stats --no-stream
```

### Port Conflict & Network Triage
```bash
# Identify process listening on port
ss -tulpn | grep :<PORT>
lsof -i :<PORT>

# Bridge network inspection
docker network inspect bridge
```

### System Health
```bash
# Memory, Disk, GPU
free -h
df -h /
nvidia-smi  # (if GPU host)
```

---

## Crash Triage Playbook

| Exit Code / Error | Root Cause | Immediate Action |
|---|---|---|
| `137` | OOM (Out of Memory) | Check `docker stats`, increase container memory limit, or free host RAM. |
| `1` | Application / Config Error | Check `docker logs --tail 50 <name>`, verify `.env` and volume file permissions. |
| `127` | Binary or Command Not Found | Check entrypoint, `PATH`, or Dockerfile base image. |
| `Bind: address already in use` | Port collision | Run `ss -tulpn \| grep <PORT>`, kill old process or change host port mapping. |

---

## Response Output Guidelines

Keep reports terse, informative, and actionable:
```
Status: [SUCCESS / FAILED]
Target: <service_name>
Action: <what was executed>
Verification: <health check / log status>
```
