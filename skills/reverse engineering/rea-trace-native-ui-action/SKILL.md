---
name: rea-trace-native-ui-action
description: Trace a compiled UI action selector to its native handler and direct callees. Run `rea trace-native-ui-action --help` for usage details.
requires_bin: rea
command: rea trace-native-ui-action
---

# rea trace-native-ui-action

Trace a compiled UI action selector to its native handler and direct callees

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Target path used to bind the result evidence |
| `action` | `string` | yes | A unique compiled UI action selector or interface object ID |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--maxDepth` | `number` | `8` | Maximum relationship depth |
| `--maxNodes` | `number` | `250` | Maximum returned graph nodes |
| `--maxEdges` | `number` | `500` | Maximum returned graph edges |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
