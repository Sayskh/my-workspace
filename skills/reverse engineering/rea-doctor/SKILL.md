---
name: rea-doctor
description: Check whether REA is ready. Run `rea doctor --help` for usage details.
requires_bin: rea
command: rea doctor
---

# rea doctor

Check whether REA is ready

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--target` | `string` |  | Optional app path to check |
| `--client` | `array` |  | Agent registration whose readiness is required; repeatable |
| `--provider` | `array` |  | Deep-analysis provider whose readiness is required |
| `--skill` | `boolean` |  | Require the installed REA skill identity to be aligned |
