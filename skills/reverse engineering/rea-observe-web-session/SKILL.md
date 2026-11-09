---
name: rea-observe-web-session
description: Observe user-driven page navigation during a chosen window. Run `rea observe-web-session --help` for usage details.
requires_bin: rea
command: rea observe-web-session
---

# rea observe-web-session

Observe user-driven page navigation during a chosen window

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `endpoint` | `string` | yes | Configured loopback CDP HTTP endpoint |
| `targetId` | `string` | yes | Target ID from list-browser-targets |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--allowedOrigins` | `array` |  | Optional exact-origin filter |
| `--observationMs` | `number` | `10000` | Observation duration in milliseconds |
