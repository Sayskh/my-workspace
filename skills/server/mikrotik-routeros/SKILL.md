---
name: server-mikrotik-routeros
description: MikroTik RouterOS v6/v7 CLI navigation, firewall, routing, and interface status.
metadata:
  hermes:
    tags: [server, mikrotik, routeros, networking, firewall]
    category: server
---

# MikroTik RouterOS

CLI commands and network diagnostics for MikroTik routers and switches.

## Detection & System Info
```routeros
/system resource print
/system identity print
/system routerboard print
/system package print
```

## Interfaces & IP Configuration
```routeros
/interface print
/interface ethernet print
/ip address print
/ip route print
/ip dhcp-server lease print
```

## Firewall & NAT Rules
```routeros
/ip firewall filter print
/ip firewall nat print
/ip firewall connection print
```

## Ping, Trace & Bandwidth Tools
```routeros
/ping 1.1.1.1 count=4
/tool traceroute 1.1.1.1
/tool torch interface=ether1
```
