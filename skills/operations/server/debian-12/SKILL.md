---
name: server-debian-12
description: Debian 12 (Bookworm) package management, networking, and system maintenance.
metadata:
  hermes:
    tags: [server, debian, linux, apt, sysadmin]
    category: server
---

# Debian 12 (Bookworm)

Operational runbook and package maintenance for Debian 12.

## Detection
```bash
cat /etc/debian_version
lsb_release -a
```

## Package Management (APT)
```bash
apt update
apt upgrade -y
apt install -y <package>
apt remove --purge <package>
apt autoremove -y
apt clean
```

## Network Configuration
Debian 12 uses systemd-networkd or `/etc/network/interfaces`:
```bash
# Check interface status
ip addr show
ip route show

# Restart networking
systemctl restart networking
# or
systemctl restart systemd-networkd
```

## Logs & Kernel Messages
```bash
dmesg -T | tail -30
journalctl -p 3 -xb --no-pager
```
