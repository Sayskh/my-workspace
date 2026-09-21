---
name: server-cisco-ios
description: Cisco IOS / IOS-XE switch and router CLI commands and configuration.
metadata:
  hermes:
    tags: [server, cisco, ios, switch, router, networking]
    category: server
---

# Cisco IOS

Standard operational and configuration commands for Cisco network devices.

## Device Identification
```ios
show version
show inventory
show running-config
```

## Interfaces & VLANs
```ios
show ip interface brief
show interfaces status
show vlan brief
show mac address-table
```

## Routing & Neighbors
```ios
show ip route
show cdp neighbors detail
show lldp neighbors detail
```

## Saving Configuration
```ios
copy running-config startup-config
# or
write memory
```
