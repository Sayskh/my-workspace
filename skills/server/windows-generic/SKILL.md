---
name: server-windows-generic
description: Windows Server and client administration via PowerShell and WinRM.
metadata:
  hermes:
    tags: [server, windows, powershell, sysadmin, winrm]
    category: server
---

# Windows Administration

PowerShell and remote command execution for Windows hosts.

## System Info & Diagnostics
```powershell
Get-ComputerInfo
Get-Service | Where-Object {$_.Status -eq 'Running'}
Get-EventLog -LogName System -Newest 20 -EntryType Error,Warning
```

## Disk & Performance
```powershell
Get-PSDrive -PSProvider FileSystem
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
```

## Remote Access via WinRM (from Linux)
```bash
evil-winrm -i <target_ip> -u <username> -p <password>
```
