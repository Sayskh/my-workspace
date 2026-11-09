---
name: rea-inspect-native-api
description: Reconstruct one native function API boundary with evidence. Run `rea inspect-native-api --help` for usage details.
requires_bin: rea
command: rea inspect-native-api
---

# rea inspect-native-api

Reconstruct one native function API boundary with evidence

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | App or program path |
| `address` | `string` | yes | Procedure name or address |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--snapshot` | `string` |  | Load and update a local analysis snapshot |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
