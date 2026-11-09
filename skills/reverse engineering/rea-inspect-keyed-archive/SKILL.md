---
name: rea-inspect-keyed-archive
description: Inspect a Foundation keyed archive as an object-reference graph. Run `rea inspect-keyed-archive --help` for usage details.
requires_bin: rea
command: rea inspect-keyed-archive
---

# rea inspect-keyed-archive

Inspect a Foundation keyed archive as an object-reference graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Foundation plist archive or Apple app bundle |
| `archive` | `string` | yes | Relative archive path when the target is a bundle |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--root` | `string` |  | Named $top archive root |
| `--offset` | `number` | `0` | First original object-table index |
| `--limit` | `number` | `20000` | Maximum object-table entries to return |
