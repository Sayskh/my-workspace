---
name: server-truenas-scale
description: TrueNAS SCALE Debian-based operations, Apps, and ZFS storage management.
metadata:
  hermes:
    tags: [server, truenas-scale, zfs, debian, storage]
    category: server
---

# TrueNAS SCALE

Runbook for Debian-based TrueNAS SCALE deployments.

## Detection & System Status
```bash
cat /etc/version
cli system info
midclt call system.info | jq .
```

## Disk & ZFS Health
```bash
zpool status -v
smartctl -H /dev/sdX
midclt call disk.query
```

## TrueNAS Apps & Docker Stack
```bash
# List active apps
midclt call app.query

# App lifecycle
midclt call app.start "<app_name>"
midclt call app.stop "<app_name>"
```
