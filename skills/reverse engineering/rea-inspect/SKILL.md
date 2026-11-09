---
name: rea-inspect
description: Inspect an app overview with evidence. Run `rea inspect --help` for usage details.
requires_bin: rea
command: rea inspect
---

# rea inspect

Inspect an app overview with evidence

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | App, program, or analysis database path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--snapshot` | `string` |  | Load and update a local analysis snapshot |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
