# SysAdmin — Hermes Profile

Systems administrator and infrastructure operations guardian for Hermes Agent. Manages server operating systems, networking, storage, homelab nodes, reverse proxies, and host observability.

## What This Profile Provides

- Linux, NixOS, and Windows server configuration and maintenance
- Reverse proxy (Nginx, Traefik, Caddy) setup and automated SSL/TLS management
- Systems diagnostics: memory leaks, disk fill-ups, CPU spikes, network latency
- Storage management: ZFS/btrfs snapshots, volume resizing, automated backup routines
- Disaster recovery runbooks and bare-metal server provisioning

## Quick Start

```bash
hermes --profile sysadmin
```

## Skill Dependencies

- `artifact-pyramids` (Required)
- `site-reliability-engineering` (Required)
- `docker-management` (Recommended)
- `systematic-debugging` (Recommended)
