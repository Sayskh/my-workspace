---
name: rea-compare-process-captures
description: Compare two process capture Evidence JSON files. Run `rea compare-process-captures --help` for usage details.
requires_bin: rea
command: rea compare-process-captures
---

# rea compare-process-captures

Compare two process capture Evidence JSON files

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `left` | `string` | yes | Left capture Evidence JSON path |
| `right` | `string` | yes | Right capture Evidence JSON path |
| `traceSpec` | `string` | no | Optional partial-order or finite-trace specification path |
