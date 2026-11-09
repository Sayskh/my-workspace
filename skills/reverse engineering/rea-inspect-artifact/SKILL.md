---
name: rea-inspect-artifact
description: Inspect one artifact and return all available observations and next probes. Run `rea inspect-artifact --help` for usage details.
requires_bin: rea
command: rea inspect-artifact
---

# rea inspect-artifact

Inspect one artifact and return all available observations and next probes

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Application or package path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--integrityPolicy` | `string` | `fail` | Behavior when declared artifact integrity does not match |
