---
name: server-idrac-dell
description: Dell PowerEdge hardware lifecycle, BIOS configuration, and RAID management.
metadata:
  hermes:
    tags: [server, dell, poweredge, bios, raid, racadm]
    category: server
---

# Dell PowerEdge & RACADM Configuration

Lifecycle controller and BIOS configuration for Dell enterprise servers.

## BIOS & Firmware Inventory
```bash
racadm hwinventory
racadm get BIOS.SysInformation
```

## PERC / RAID Controller
```bash
racadm raid get controllers
racadm raid get pdisks
racadm raid get vdisks
```

## Job Queue Management
```bash
# View pending lifecycle jobs
racadm jobqueue view

# Clear stuck jobs
racadm jobqueue delete -i JID_CLEARALL
```
