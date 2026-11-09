---
name: rea-decompile
description: Read one part of an app as code. Run `rea decompile --help` for usage details.
requires_bin: rea
command: rea decompile
---

# rea decompile

Read one part of an app as code

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | App or program path |
| `address` | `string` | yes | Procedure address |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--snapshot` | `string` |  | Load and update a local analysis snapshot |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
