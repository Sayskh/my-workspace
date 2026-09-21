---
name: server-truenas
description: TrueNAS SCALE / CORE storage, ZFS pools, dataset management, and middleware CLI.
metadata:
  hermes:
    tags: [server, truenas, zfs, storage, nas]
    category: server
---

# TrueNAS

Storage, ZFS management, and middleware operations for TrueNAS.

## Detection
```bash
cat /etc/version
cli -c "system info"
midclt call system.info
```

## ZFS Pools & Datasets
```bash
# Pool status
zpool status
zpool list

# Dataset status
zfs list
zfs get all <dataset_name>

# ZFS Snapshots
zfs list -t snapshot
zfs snapshot <pool/dataset>@snap-$(date +%Y%m%d%H%M)
zfs rollback <pool/dataset>@<snapshot_name>
```

## TrueNAS Middleware CLI (`midclt`)
```bash
# Get system alerts
midclt call alert.list

# List network interfaces
midclt call interface.query

# List SMB shares
midclt call sharing.smb.query
```
