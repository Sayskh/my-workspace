---
name: rea-inspect-native-data-type
description: Inspect one recovered database type or typed data object. Run `rea inspect-native-data-type --help` for usage details.
requires_bin: rea
command: rea inspect-native-data-type
---

# rea inspect-native-data-type

Inspect one recovered database type or typed data object

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Local native executable or app path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--type` | `string` |  | Exact database type category path |
| `--address` | `string` |  |  |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
