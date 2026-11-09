---
name: rea-search
description: Search every analyzed string or procedure name. Run `rea search --help` for usage details.
requires_bin: rea
command: rea search
---

# rea search

Search every analyzed string or procedure name

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | App or program path |
| `pattern` | `string` | yes | Literal text or regex pattern |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--kind` | `string` | `strings` | Analyzed item kind to search |
| `--mode` | `string` | `literal` | Interpret the pattern as literal text or a regex |
| `--caseSensitive` | `boolean` | `false` | Match the pattern with exact letter case |
| `--snapshot` | `string` |  | Load and update a local analysis snapshot |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
