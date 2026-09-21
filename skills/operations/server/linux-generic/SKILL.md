---
name: server-linux-generic
description: Generic Linux system administration, diagnostics, and triage runbook.
metadata:
  hermes:
    tags: [server, linux, sysadmin, triage, bash]
    category: server
---

# Linux Generic

Standard Linux diagnostic tools, service management, and troubleshooting procedures.

## System Identification & OS
```bash
uname -a
cat /etc/os-release
hostnamectl
uptime
```

## Service Management (systemd)
```bash
systemctl status <service>
systemctl restart <service>
systemctl enable --now <service>
journalctl -u <service> -n 50 --no-pager
journalctl -xe --no-pager
```

## Resource & Performance Diagnostics
```bash
# CPU & Load
top -b -n 1 | head -20
htop

# Memory & Swap
free -h
vmstat 1 5

# Storage & Inodes
df -h
df -i
du -sh /var/log/* | sort -rh | head -10

# Network & Listening Ports
ss -tulpn
ip a
ip route
```

## Process Management
```bash
ps aux | grep <process_name>
kill -15 <PID>   # Graceful termination
kill -9 <PID>    # Force kill
```
