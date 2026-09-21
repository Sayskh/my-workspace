---
name: server-arduino-bare
description: Arduino CLI development, compilation, flashing, and serial monitoring.
metadata:
  hermes:
    tags: [server, arduino, embedded, microcontroller, iot]
    category: server
---

# Arduino Bare-Metal & CLI

CLI tools and sketch workflows for Arduino and ESP microcontroller boards.

## Arduino CLI Usage
```bash
# Install core
arduino-cli core install arduino:avr
arduino-cli core install esp32:esp32

# Compile sketch
arduino-cli compile --fqbn arduino:avr:uno sketch/

# Upload to board
arduino-cli upload -p /dev/ttyUSB0 --fqbn arduino:avr:uno sketch/

# Serial monitor
arduino-cli monitor -p /dev/ttyUSB0 --config baudrate=115200
```

## Common Board FQBNs
- Arduino Uno: `arduino:avr:uno`
- Arduino Nano: `arduino:avr:nano`
- Arduino Mega: `arduino:avr:mega`
- ESP32: `esp32:esp32:esp32`
- NodeMCU ESP8266: `esp8266:esp8266:nodemcuv2`
