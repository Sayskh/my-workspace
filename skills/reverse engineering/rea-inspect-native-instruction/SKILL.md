---
name: rea-inspect-native-instruction
description: Inspect one native instruction with decoded operand facts. Run `rea inspect-native-instruction --help` for usage details.
requires_bin: rea
command: rea inspect-native-instruction
---

# rea inspect-native-instruction

Inspect one native instruction with decoded operand facts

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Local native executable or app path |
| `address` | `string` | yes | Exact native address |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
