---
name: rea-observe-javascript-runtime
description: Passively observe one exact Node/Electron Inspector target. Run `rea observe-javascript-runtime --help` for usage details.
requires_bin: rea
command: rea observe-javascript-runtime
---

# rea observe-javascript-runtime

Passively observe one exact Node/Electron Inspector target

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `endpoint` | `string` | yes | Literal-loopback Inspector endpoint |
| `targetId` | `string` | yes | Target from list-javascript-runtime-targets |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--runtimeKind` | `string` |  | Declared target role; Inspector cannot authenticate the Electron role |
| `--observationMs` | `number` | `100` | Observation window in milliseconds |
