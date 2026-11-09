---
name: rea-trace
description: Trace a literal feature through analyzed references. Run `rea trace --help` for usage details.
requires_bin: rea
command: rea trace
---

# rea trace

Trace a literal feature through analyzed references

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | App or program path |
| `query` | `string` | yes | Literal feature query |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--caseSensitive` | `boolean` | `false` | Match the query with exact letter case |
| `--snapshot` | `string` |  | Load and update a local analysis snapshot |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
