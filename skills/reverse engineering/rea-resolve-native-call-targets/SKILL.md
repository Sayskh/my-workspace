---
name: rea-resolve-native-call-targets
description: Resolve one static native call site. Run `rea resolve-native-call-targets --help` for usage details.
requires_bin: rea
command: rea resolve-native-call-targets
---

# rea resolve-native-call-targets

Resolve one static native call site

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | Local native executable or app path |
| `address` | `string` | yes | Exact native address |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--provider` | `unknown` |  | Bind deep analysis to a provider ID or use deterministic auto selection |
