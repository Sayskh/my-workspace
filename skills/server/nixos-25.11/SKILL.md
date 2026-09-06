---
name: server-nixos-25.11
description: NixOS declarative system configuration, rebuilds, and garbage collection.
metadata:
  hermes:
    tags: [server, nixos, declarative, linux, sysadmin]
    category: server
---

# NixOS 25.11

Declarative configuration and package operations for NixOS systems.

## Detection
```bash
nixos-version
nix --version
cat /etc/nixos/configuration.nix | head -30
```

## Rebuild & Switch Flow
```bash
# Dry run / build test
nixos-rebuild dry-build

# Test configuration (temporary, not boot default)
nixos-rebuild test

# Permanent switch and boot entry update
nixos-rebuild switch

# Rollback to previous generation
nixos-rebuild switch --rollback
```

## Generations & Garbage Collection
```bash
# List system generations
nix-env --list-generations --profile /nix/var/nix/profiles/system

# Clean older generations and collect garbage
nix-collect-garbage -d
nixos-rebuild boot
```
