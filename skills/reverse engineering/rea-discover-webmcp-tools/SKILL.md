---
name: rea-discover-webmcp-tools
description: Passively discover page-declared WebMCP tools. Run `rea discover-webmcp-tools --help` for usage details.
requires_bin: rea
command: rea discover-webmcp-tools
---

# rea discover-webmcp-tools

Passively discover page-declared WebMCP tools

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `endpoint` | `string` | yes | Configured loopback CDP HTTP endpoint |
| `targetId` | `string` | yes | Target ID from list-browser-targets |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--allowedOrigins` | `array` |  | Optional exact-origin filter |
| `--observationMs` | `number` | `100` | Observation duration in milliseconds |
