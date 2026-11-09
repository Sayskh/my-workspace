---
name: rea-setup
description: Configure agent integrations and optional analysis providers. Run `rea setup --help` for usage details.
requires_bin: rea
command: rea setup
---

# rea setup

Configure agent integrations and optional analysis providers

## Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--yes` | `boolean` | `false` | Approve user-owned setup actions without prompting |
| `--installHopper` | `boolean` | `false` | Also approve Hopper installation with --yes |
| `--client` | `array` |  | Agent integration to configure; repeat for multiple agents |
| `--allDetected` | `boolean` | `false` | Configure every detected supported agent |
| `--skill` | `boolean` |  | Override the bundled skill included with agent integrations |
| `--dryRun` | `boolean` | `false` | Print the resolved plan without applying it |
| `--accessible` | `boolean` | `false` | Use sequential accessible setup prompts |
