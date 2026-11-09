---
name: rea-decode-interface-builder
description: Decode compiled storyboard and nib archives from an app bundle. Run `rea decode-interface-builder --help` for usage details.
requires_bin: rea
command: rea decode-interface-builder
---

# rea decode-interface-builder

Decode compiled storyboard and nib archives from an app bundle

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Apple .app bundle path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--maxDocuments` | `number` | `64` | Maximum archives to decode |
| `--maxObjects` | `number` | `20000` | Maximum graph objects |
| `--maxConnections` | `number` | `40000` | Maximum decoded connections |
