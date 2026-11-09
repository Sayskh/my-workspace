---
name: rea-inspect-electron-page
description: Passively inspect one Electron file page. Run `rea inspect-electron-page --help` for usage details.
requires_bin: rea
command: rea inspect-electron-page
---

# rea inspect-electron-page

Passively inspect one Electron file page

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `endpoint` | `string` | yes | Literal-loopback Electron CDP endpoint |
| `targetId` | `string` | yes | Target ID from list-electron-targets |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--observationMs` | `number` | `100` | Observation duration in milliseconds |
| `--includeScriptSources` | `boolean` | `false` | Include JavaScript source text |
