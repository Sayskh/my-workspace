---
name: rea-capture-native-ui-scenario
description: Observe or run a scenario in one exact native application window. Run `rea capture-native-ui-scenario --help` for usage details.
requires_bin: rea
command: rea capture-native-ui-scenario
---

# rea capture-native-ui-scenario

Observe or run a scenario in one exact native application window

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Local native executable or app path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--pid` | `number` |  | Existing application PID |
| `--windowId` | `number` |  | Exact selected application window ID |
| `--steps` | `string` |  | JSON array of declarative AX actions or waits |
| `--screenshot` | `boolean` | `true` | Capture only the selected window |
| `--accessibility` | `boolean` | `true` | Read the selected window accessibility tree |
| `--maxNodes` | `number` | `500` | Maximum accessibility nodes per capture |
