---
name: server-idrac-9
description: Dell iDRAC 9 out-of-band server management via RACADM and Redfish API.
metadata:
  hermes:
    tags: [server, idrac, dell, ipmi, racadm, hardware]
    category: server
---

# Dell iDRAC 9

Out-of-band hardware management commands for Dell PowerEdge servers.

## Detection & System Info
```bash
racadm getsysinfo
racadm getversion
```

## Server Power Control
```bash
racadm serveraction powerstatus
racadm serveraction powerup
racadm serveraction powerdown
racadm serveraction powercycle
racadm serveraction graceshutdown
```

## Hardware Logs & Sensors
```bash
racadm getsel          # System Event Log
racadm getsensorinfo   # Fan speeds, temperatures, voltages
```

## Redfish REST API
```bash
curl -sk -u "root:password" https://<idrac-ip>/redfish/v1/Systems/System.Embedded.1
curl -sk -u "root:password" https://<idrac-ip>/redfish/v1/Chassis/System.Embedded.1/Power
```
