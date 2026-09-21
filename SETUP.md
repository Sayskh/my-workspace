# Hermes Agent Setup

This is the canonical setup guide for the repository. It is intentionally
incremental: install the core first, verify it, then add optional tools only
when a workflow needs them.

## 1. Core Hermes configuration

From the repository root:

```bash
hermes
```

Keep the existing `config.yaml` and MCP configuration. Profiles are selected
with:

```bash
hermes -p planner
hermes -p lead
hermes -p builder
hermes -p reviewer
hermes -p ops
```

Read `SOUL.md`, the active `profiles/<profile>/SOUL.md`, and then select skills
from `skills/installed-manifest.yaml`.

## 2. Install skills

The `skills` CLI installs skills for multiple agent hosts, so its default output
may create `.agents/` and `.claude/`. Those directories are installer outputs
and are ignored by this repo; Hermes' canonical skill library is `skills/`.

Install the requested sources:

```bash
npx skills add educlopez/ui-craft -y
npx skills add dickwu/apple-design-skill --skill apple-design -y
npx ui-ux-pro-max-cli init --ai claude
npx skills add https://github.com/Leonxlnx/taste-skill -y
npx skills@latest add emilkowalski/skills -y
npx skills add JuliusBrussee/caveman -y
npx skills add https://github.com/multica-ai/andrej-karpathy-skills -y
```

Review external skills before use. Do not load every installed skill for every
request; use the profile routing in `skills/installed-manifest.yaml`.

## 3. Token Saver & Cost Tools (9Router Proxy)

Token optimization and prompt/context compression are handled at the proxy
gateway layer using **9Router Proxy** (`http://localhost:20128/dashboard/token-saver`):
- **RTK**: Compresses tool output (`git`/`grep`/`ls`/`tree`/`logs`) for 60–90% input token savings.
- **Headroom**: Context compression before routing to upstream models.
- **Caveman**: Output compression with terse-style system prompting.
- **Ponytail**: Lazy senior dev prompt bias (minimal code, YAGNI).

No standalone installations of RTK, Graft, Headroom, or Ponytail are needed in this workspace.

### Optional Document Parser (MarkItDown)

Install in an isolated environment if document parsing (PDF, Office, etc.) is needed:

```bash
python -m venv .tools/markitdown
.tools/markitdown/Scripts/python.exe -m pip install "markitdown[all]"
```

## 4. Verification checklist

```bash
python -c "import yaml; yaml.safe_load(open('config.yaml')); yaml.safe_load(open('skills/skill-catalog.yaml')); yaml.safe_load(open('skills/installed-manifest.yaml')); print('YAML OK')"
git status --short
```

For a low-token workflow:

1. Read global and active profile `SOUL.md`.
2. Select one core skill.
3. Add at most one support skill.
4. Route requests through 9Router Proxy Token Saver for automatic compression.
5. Stop loading instructions once the task procedure is clear.
6. Verify the result and report only relevant evidence.
