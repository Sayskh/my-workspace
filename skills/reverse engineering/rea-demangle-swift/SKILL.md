---
name: rea-demangle-swift
description: Demangle Swift symbols without Hopper. Run `rea demangle-swift --help` for usage details.
requires_bin: rea
command: rea demangle-swift
---

# rea demangle-swift

Demangle Swift symbols without Hopper

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Artifact path used for evidence identity |
| `symbols` | `array` | yes | Swift mangled symbols to demangle |
