---
name: server-vmware-esxi-8
description: VMware ESXi 8.x hypervisor CLI management via esxcli and vim-cmd.
metadata:
  hermes:
    tags: [server, vmware, esxi, hypervisor, vsphere]
    category: server
---

# VMware ESXi 8

Command line operations for VMware ESXi bare-metal hypervisor.

## Detection & System Info
```bash
vmware -v
esxcli system version get
uname -a
```

## Virtual Machine Operations (`vim-cmd`)
```bash
# List all registered VMs
vim-cmd vmsvc/getallvms

# VM power management
vim-cmd vmsvc/power.getstate <vmid>
vim-cmd vmsvc/power.on <vmid>
vim-cmd vmsvc/power.off <vmid>
vim-cmd vmsvc/power.reboot <vmid>

# Snapshot management
vim-cmd vmsvc/snapshot.get <vmid>
vim-cmd vmsvc/snapshot.create <vmid> <snapshot_name> <description>
```

## Storage & Network (`esxcli`)
```bash
# Datastores
esxcli storage filesystem list
esxcli storage vmfs extent list

# Virtual switches & NICs
esxcli network vswitch standard list
esxcli network nic list
```
