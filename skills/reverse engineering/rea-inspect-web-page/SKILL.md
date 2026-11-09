---
name: rea-inspect-web-page
description: Passively inspect one page through CDP, defaulting to its current origin. Run `rea inspect-web-page --help` for usage details.
requires_bin: rea
command: rea inspect-web-page
---

# rea inspect-web-page

Passively inspect one page through CDP, defaulting to its current origin

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
| `--includeAccessibilityText` | `boolean` | `false` | Include accessibility text |
| `--includeConsoleText` | `boolean` | `false` | Include console message text |
| `--includeJsonBodyShapes` | `boolean` | `false` | Include structural shapes of JSON response bodies |
| `--includeWebsocketShapes` | `boolean` | `false` | Include structural shapes of WebSocket payloads |
| `--includeScriptSources` | `boolean` | `false` | Include JavaScript source text |
| `--includeStorageKeys` | `boolean` | `false` | Include storage key names without values |
| `--includeStorageFingerprints` | `boolean` | `false` | Include content-derived storage fingerprints |
