---
name: rea-compare-web-screenshots
description: Compare two self-verifying PNG artifact JSON values. Run `rea compare-web-screenshots --help` for usage details.
requires_bin: rea
command: rea compare-web-screenshots
---

# rea compare-web-screenshots

Compare two self-verifying PNG artifact JSON values

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `beforeJson` | `string` | yes | Earlier screenshot artifact JSON |
| `afterJson` | `string` | yes | Later screenshot artifact JSON |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--channelThreshold` | `number` | `0` | Per-channel difference threshold for changed pixels |
