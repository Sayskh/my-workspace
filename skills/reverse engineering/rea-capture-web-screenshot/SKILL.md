---
name: rea-capture-web-screenshot
description: Capture one visible page viewport within the supplied origin scope. Run `rea capture-web-screenshot --help` for usage details.
requires_bin: rea
command: rea capture-web-screenshot
---

# rea capture-web-screenshot

Capture one visible page viewport within the supplied origin scope

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `endpoint` | `string` | yes | Configured loopback CDP HTTP endpoint |
| `targetId` | `string` | yes | Target ID from list-browser-targets |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--allowedOrigins` | `array` |  | Optional exact-origin filter |
