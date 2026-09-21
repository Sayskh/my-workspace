# Hermes Tools and Installation Status

This file records the tools requested for the Hermes workspace. It separates
installed tools from failed or deferred installs and keeps setup reproducible.
Skill sources are copied into the canonical `skills/` tree; `.agents/` and
`.claude/` are disposable installer outputs and are ignored.

> [!NOTE]
> **Token Saving & Compression Delegated to 9Router Proxy**
> Token optimization (RTK tool output compression, Headroom context compression,
> Caveman LLM output compression, and Ponytail prompt bias) is handled
> centrally by **9Router Proxy** (`http://localhost:20128/dashboard/token-saver`).
> Standalone workspace-level installations for these tools are no longer required.

## Installed

| Tool | Status | Verification | Notes |
|---|---|---|---|
| `markitdown[all]` | Installed | `python -m pip show markitdown` | Installed in global Python 3.14 environment |
| `ui-ux-pro-max` | Installed | `.claude/skills/ui-ux-pro-max` exists | Claude-specific installer output |

## Offloaded to 9Router Token Saver

| Tool | Status | Managed By | Purpose in 9Router |
|---|---|---|---|
| `rtk` | Active in 9Router | 9Router Proxy | Compress tool output (`git`/`grep`/`ls`/`tree`/`logs`) |
| `headroom-ai` | Managed via 9Router | 9Router Proxy | Compress prompts via `/v1/compress` |
| `caveman` | Active in 9Router | 9Router Proxy | Compress LLM output (terse-style system prompt) |
| `ponytail` | Active in 9Router | 9Router Proxy | Lazy senior dev prompt bias (minimal code, YAGNI) |

## Environment warnings

`markitdown[all]` was installed globally and pip reported an existing
`spotdl` dependency conflict involving `fastapi` and `uvicorn`. Prefer a
separate environment for future Python tools:

```bash
python -m venv .tools/markitdown
.tools/markitdown/Scripts/python.exe -m pip install "markitdown[all]"
```

Do not add `.tools/` environments to Git.

## Recommended setup

1. Keep Hermes skills in `skills/` only.
2. Load profile `core` skills first; load at most two support skills.
3. Use `skills/installed-manifest.yaml` as the routing index.
4. Keep `.agents/` and `.claude/` ignored installer outputs.
5. All token/cost reduction is routed through 9Router Proxy Token Saver.
6. Keep heavy Python tools in `.tools/<name>` instead of the global interpreter.
