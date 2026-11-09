---
name: rea-inspect-native-dispatch-metadata
description: Inspect typed Objective-C and Swift dispatch metadata. Run `rea inspect-native-dispatch-metadata --help` for usage details.
requires_bin: rea
command: rea inspect-native-dispatch-metadata
---

# rea inspect-native-dispatch-metadata

Inspect typed Objective-C and Swift dispatch metadata

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Target path used to bind the result evidence |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--maxRecords` | `number` | `5000` | Maximum symbol records to inspect |
| `--snapshot` | `string` |  | Load or update the local analysis snapshot |
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
