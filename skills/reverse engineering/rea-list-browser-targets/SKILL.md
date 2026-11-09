---
name: rea-list-browser-targets
description: List page targets from a selected loopback CDP browser, optionally filtered by origin. Run `rea list-browser-targets --help` for usage details.
requires_bin: rea
command: rea list-browser-targets
---

# rea list-browser-targets

List page targets from a selected loopback CDP browser, optionally filtered by origin

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `endpoint` | `string` | yes | Configured loopback CDP HTTP endpoint |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--allowedOrigins` | `array` |  | Optional exact-origin filter |
