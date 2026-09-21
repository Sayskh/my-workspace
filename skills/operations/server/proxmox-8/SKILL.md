---
name: server-proxmox-8
description: Proxmox VE 8 virtualization management (VMs, LXC containers, storage, snapshots).
metadata:
  hermes:
    tags: [server, proxmox, pve, virtualization, lxc, qemu]
    category: server
---

# Proxmox VE 8

Virtual machine, LXC container, and cluster operations for Proxmox VE 8.

## Detection
```bash
pveversion
pvesh get /nodes
qm list
pct list
```

## Virtual Machine (QM) Management
```bash
# List & Status
qm list
qm status <vmid>
qm config <vmid>

# Lifecycle
qm start <vmid>
qm shutdown <vmid>
qm stop <vmid>           # Force stop
qm destroy <vmid>        # DESTRUCTIVE: Delete VM and disks

# Create VM
qm create <vmid> --name <name> --memory 2048 --cores 2 --net0 virtio,bridge=vmbr0
qm importdisk <vmid> <disk.img> local-lvm
qm set <vmid> --scsi0 local-lvm:vm-<vmid>-disk-0
qm set <vmid> --boot order=scsi0
```

## LXC Container (PCT) Management
```bash
pct list
pct start <ctid>
pct stop <ctid>
pct enter <ctid>
pct destroy <ctid>       # DESTRUCTIVE: Delete container
```

## Storage & Backup Snapshots
```bash
# Storage status
pvesm status
pvesm list local-lvm

# Create VM snapshot
qm snapshot <vmid> <snapname> --description "Pre-upgrade snapshot"

# Backup VM with vzdump
vzdump <vmid> --storage local --mode snapshot --compress zstd
```
