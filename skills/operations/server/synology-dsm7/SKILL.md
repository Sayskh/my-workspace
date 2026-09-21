---
name: server-synology-dsm7
description: Synology DiskStation Manager (DSM 7) CLI, package management, and RAID status.
metadata:
  hermes:
    tags: [server, synology, dsm, nas, storage]
    category: server
---

# Synology DSM 7

Command-line utilities and diagnostics for Synology NAS running DSM 7.

## Detection
```bash
cat /etc.defaults/VERSION
uname -a
synopkg list | head -10
```

## Storage & Volume Status
```bash
# Disk & Volume details
synostgvolume --get-all
cat /proc/mdstat

# Smart test status
smartctl -a /dev/sata1
```

## Package Center (`synopkg`)
```bash
# List installed packages
synopkg list

# Start / Stop package
synopkg start <package_name>
synopkg stop <package_name>
synopkg status <package_name>
```

## Service Control
```bash
synosystemctl get-status <service>
synosystemctl restart <service>
```
