---
name: rea-compare-managed-members
description: Compare managed PE/CLI member inventories by exact declared type, name, and signature; names alone never form a match. Run `rea compare-managed-members --help` for usage details.
requires_bin: rea
command: rea compare-managed-members
---

# rea compare-managed-members

Compare managed PE/CLI member inventories by exact declared type, name, and signature; names alone never form a match

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `leftPath` | `string` | yes | Baseline managed PE executable or assembly |
| `rightPath` | `string` | yes | Candidate managed PE executable or assembly |
