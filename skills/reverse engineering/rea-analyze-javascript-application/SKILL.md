---
name: rea-analyze-javascript-application
description: Statically reconstruct a local JavaScript/Electron application. Run `rea analyze-javascript-application --help` for usage details.
requires_bin: rea
command: rea analyze-javascript-application
---

# rea analyze-javascript-application

Statically reconstruct a local JavaScript/Electron application

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `string` | yes | ASAR or extracted application path |

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--artifactFormat` | `string` | `auto` | Application artifact format |
