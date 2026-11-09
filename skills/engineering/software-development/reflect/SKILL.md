---
name: reflect
description: Review recent sessions and work history, detect recurring friction, and synthesize reusable skills, agent rules, commands, or playbooks.
---

# Reflect Workflow

Reflect is a retrospective workflow for identifying recurring friction and
codifying lessons into permanent, reusable assets.

## When to Use

- When user invokes `/reflect` or asks to review past sessions.
- When the same manual task, command sequence, or debugging loop occurs repeatedly.
- When turning session friction into new skills or updated profile guidance.

Do not use for one-off tasks, routine implementation, or speculative rule creation without evidence.

## Core Contract

Reflect is strictly evidence-driven:
1. **Analyze:** Inspect recent conversation turns, memory entries, session logs, and git commits.
2. **Identify Friction:** Find patterns occurring 2+ times with predictable inputs and outcomes.
3. **Select Smallest Form:** Prefer the smallest effective intervention:
   - System prompt rule / AGENTS.md update $\rightarrow$ for small behavior changes.
   - Reusable skill (`SKILL.md`) $\rightarrow$ for multi-step task workflows.
   - Declarative script / template $\rightarrow$ for deterministic automation.
4. **Propose Before Applying:** Present a concise summary of findings, proposed changes, and rationale before modifying workspace configurations.

## Output Format

```text
Findings
- <pattern>: frequency, evidence, root cause.

Recommended Changes
- <target>: proposed addition/update and justification.

Skipped
- <candidate>: why insufficient evidence exists.
```
