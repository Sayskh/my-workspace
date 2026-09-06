---
name: server-vmware-esxi
description: General VMware ESXi hypervisor maintenance, host diagnostics, and hardware health.
metadata:
  hermes:
    tags: [server, vmware, esxi, hardware, sysadmin]
    category: server
---

# VMware ESXi Host Operations

Host diagnostics, hardware sensor monitoring, and maintenance mode operations.

## Host Hardware & Sensors
```bash
esxcli hardware platform get
esxcli hardware cpu global get
esxcli hardware memory get
```

## Maintenance Mode
```bash
# Enter maintenance mode
esxcli system maintenanceMode set --enable true

# Exit maintenance mode
esxcli system maintenanceMode set --enable false
```

## Firewall & Services
```bash
esxcli network firewall get
esxcli network firewall set --enabled false
chkconfig --list
```
