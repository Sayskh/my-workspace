---
name: rea-inspect-asset-catalog
description: Inspect compiled Apple asset catalog metadata. Run `rea inspect-asset-catalog --help` for usage details.
requires_bin: rea
command: rea inspect-asset-catalog
---

# rea inspect-asset-catalog

Inspect compiled Apple asset catalog metadata

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Apple .app bundle path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--offset` | `number` | `0` | First metadata record |
| `--limit` | `number` | `1000` | Maximum records to return |
