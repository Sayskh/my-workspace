---
name: rea-instructions
description: Read every raw instruction without decompiling. Run `rea instructions --help` for usage details.
requires_bin: rea
command: rea instructions
---

# rea instructions

Read every raw instruction without decompiling

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
