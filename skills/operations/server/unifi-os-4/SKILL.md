---
name: server-unifi-os-4
description: UniFi OS 4 (UniFi Dream Machine Pro/SE) controller management and REST API.
metadata:
  hermes:
    tags: [server, unifi, udm, networking, ubiquiti]
    category: server
---

# UniFi OS 4

Diagnostics and API integration for UniFi Dream Machines and Gateway devices.

## Detection & System
```bash
ubnt-device-info
cat /etc/version
systemctl status unifi-core
```

## Local REST API Endpoints
Base path: `https://<unifi-ip>/proxy/network/api/s/default/`
Header required: `X-API-KEY: <api_key>`

```bash
# Connected clients
curl -sk -H "X-API-KEY: <key>" https://<ip>/proxy/network/api/s/default/stat/sta

# Device inventory
curl -sk -H "X-API-KEY: <key>" https://<ip>/proxy/network/api/s/default/stat/device

# System events
curl -sk -H "X-API-KEY: <key>" https://<ip>/proxy/network/api/s/default/stat/event
```
