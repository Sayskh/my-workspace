---
name: rea-function
description: Analyze one complete function with evidence. Run `rea function --help` for usage details.
requires_bin: rea
command: rea function
---

# rea function

Analyze one complete function with evidence

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
