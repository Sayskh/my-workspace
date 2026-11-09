---
name: rea-xrefs
description: List bounded references to an analyzed address. Run `rea xrefs --help` for usage details.
requires_bin: rea
command: rea xrefs
---

# rea xrefs

List bounded references to an analyzed address

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | App or program path |
| `address` | `string` | yes | Hexadecimal address |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--snapshot` | `string` |  | Load and update a local analysis snapshot |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
