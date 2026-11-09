---
name: rea-trace-native-values
description: Trace bounded native def-use and call dependencies. Run `rea trace-native-values --help` for usage details.
requires_bin: rea
command: rea trace-native-values
---

# rea trace-native-values

Trace bounded native def-use and call dependencies

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Local native executable or app path |
| `procedure` | `string` | yes | Explicit native procedure symbol or address |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--maxDepth` | `number` | `3` | Maximum call traversal depth |
| `--maxFunctions` | `number` | `16` | Maximum function decompilations |
| `--maxCallSites` | `number` | `256` | Maximum static call-site resolutions |
| `--maxNodes` | `number` | `5000` | Maximum retained graph nodes |
| `--maxEdges` | `number` | `10000` | Maximum retained graph edges |
| `--offset` | `number` | `0` | First graph node index |
| `--limit` | `number` | `1000` | Maximum nodes on this page |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
