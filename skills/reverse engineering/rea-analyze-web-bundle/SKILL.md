---
name: rea-analyze-web-bundle
description: Capture and statically analyze a page bundle, defaulting to the selected target origin. Run `rea analyze-web-bundle --help` for usage details.
requires_bin: rea
command: rea analyze-web-bundle
---

# rea analyze-web-bundle

Capture and statically analyze a page bundle, defaulting to the selected target origin

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `endpoint` | `string` | yes | Configured loopback CDP HTTP endpoint |
| `targetId` | `string` | yes | Target ID from list-browser-targets |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--allowedOrigins` | `array` |  | Optional exact-origin filter |
| `--observationMs` | `number` | `500` | Observation duration in milliseconds |
| `--fetchSourceMaps` | `boolean` | `false` | Fetch source maps referenced by captured scripts |
