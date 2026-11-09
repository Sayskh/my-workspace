# Workspace Personalization & Rebranding Guide

This workspace is configured with default identifiers:
- **Owner Name:** `Hio`
- **Orchestrator Name:** `Umi`

If you fork or clone this repository for your own digital ecosystem, use the interactive grill-me prompt below. Feed it directly to your coding assistant (OpenCode, Claude Code, Antigravity, or Cursor) to run a guided, interactive setup that updates all files surgically.

---

## Interactive Grill-Me Prompt

Copy and paste the text block below into your AI session:

```markdown
Act as a strict, surgical operations architect using the grill-me protocol.

I want to personalize this workspace by replacing the default identity references:
- Current Owner Name: "Hio" -> [My Name]
- Current Orchestrator Name: "Umi" -> [My Orchestrator Name]

Before editing any files, interview me with targeted questions to lock in my exact preferences:
1. What is your preferred name or handle (to replace "Hio")?
2. What is your chosen AI Orchestrator name (to replace "Umi")?
3. What is the orchestrator's primary title or role (for example: "Chief of Staff", "Operations Overseer", "Systems Copilot")?
4. Which platforms do you actively run this on (OpenCode, Hermes Agent, Claude Code, Antigravity, Cursor, Generic API)?
5. Are there any custom domains or infrastructure stacks you want reflected (homelab OS, preferred languages, databases)?

Once I confirm my answers:
1. Present a concrete execution plan showing the exact files to be updated:
   - SOUL.md (Gateway identity and core authority)
   - AGENTS.md and CLAUDE.md (Universal operating rules)
   - SYSTEM_PROMPT.md (Standalone API system prompt)
   - PROFILES.md and README.md
   - profiles/*/SOUL.md and profiles/*/AGENTS.md (16 specialist subagents)
   - OpenCode agents (rename umi.md to <your-orchestrator>.md)
2. Perform surgical, case-sensitive replacements across the codebase without breaking YAML keys, git history, or skill references.
3. Run verification:
   - Search for any remaining untransformed occurrences of "Hio" or "Umi".
   - Run `python scripts/validate_profiles.py` to confirm all 16 profiles and 373 skills remain fully valid.
```

---

## Manual Rebranding Reference

If you prefer updating the files manually, the primary identity anchors are:

| File Path | Description | Key Replacements |
|---|---|---|
| `SOUL.md` | Primary gateway identity & swarm matrix | Replace "Hio" and "Umi" in identity headers |
| `AGENTS.md` | Universal operating rules & delegation model | Replace "Umi" in section 1 |
| `CLAUDE.md` | Claude Code project instructions | Replace "Umi" in section 1 |
| `SYSTEM_PROMPT.md` | Standalone LLM API system prompt | Replace "Hio" and "Umi" in identity section |
| `PROFILES.md` | Swarm lifecycle pipelines and roster | Replace "Umi" in orchestration topology |
| `README.md` | Repository overview | Replace "Hio" and "Umi" in title and architecture |
| `profiles/*/SOUL.md` | Subagent persona definitions | Update communication handoffs mentioning Umi/Hio |
| `profiles/*/AGENTS.md` | Subagent trigger patterns | Update handoff targets mentioning Umi |
