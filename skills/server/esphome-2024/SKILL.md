---
name: server-esphome-2024
description: ESPHome YAML configuration, validation, compilation, and OTA flashing for IoT devices.
metadata:
  hermes:
    tags: [server, esphome, iot, esp32, esp8266, home-assistant]
    category: server
---

# ESPHome

CLI commands and workflows for ESPHome smart home nodes.

## CLI Commands
```bash
# Validate YAML config
esphome config node.yaml

# Compile firmware
esphome compile node.yaml

# Flash over serial
esphome run node.yaml --device /dev/ttyUSB0

# Flash over Wi-Fi (OTA)
esphome run node.yaml --device 192.168.1.50

# Live serial / wireless logs
esphome logs node.yaml --device 192.168.1.50
```
