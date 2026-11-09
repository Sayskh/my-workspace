---
name: rea-evidence-export
description: Validate and atomically export canonical Evidence JSON. Run `rea evidence-export --help` for usage details.
requires_bin: rea
command: rea evidence-export
---

# rea evidence-export

Validate and atomically export canonical Evidence JSON

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source` | `string` | yes | Existing evidence bundle JSON path |
| `output` | `string` | yes | Canonical output JSON path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--overwrite` | `boolean` | `false` | Replace output file |
