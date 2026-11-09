---
name: rea-inspect-plist
description: Parse app plist metadata without launching Hopper. Run `rea inspect-plist --help` for usage details.
requires_bin: rea
command: rea inspect-plist
---

# rea inspect-plist

Parse app plist metadata without launching Hopper

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | App or Mach-O path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--relativePath` | `string` | `Contents/Info.plist` | Plist path relative to the app root |
