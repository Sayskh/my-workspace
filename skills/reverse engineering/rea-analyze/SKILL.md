---
name: rea-analyze
description: Get an overview of an app. Run `rea analyze --help` for usage details.
requires_bin: rea
command: rea analyze
---

# rea analyze

Get an overview of an app

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | App, program, or analysis database path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--snapshot` | `string` |  | Load and update a local analysis snapshot |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
