---
name: rea-compare-web-captures
description: Compare two normalized passive captures or recorded browser scenarios. Run `rea compare-web-captures --help` for usage details.
requires_bin: rea
command: rea compare-web-captures
---

# rea compare-web-captures

Compare two normalized passive captures or recorded browser scenarios

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `beforeJson` | `string` | yes | Earlier normalized web capture JSON |
| `afterJson` | `string` | yes | Later normalized web capture JSON |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--normalizationJson` | `string` | `{"rules":[]}` | Recorded literal normalization policy for browser scenarios |
