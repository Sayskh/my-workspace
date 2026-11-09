---
name: multi-model-consensus
description: Multi-model consensus workflow for high-stakes decisions. Queries multiple LLM models in parallel and synthesizes diverse perspectives into a unified consensus report.
---

# Multi-Model Consensus Workflow

Multi-model consensus dispatches a question to multiple distinct LLMs concurrently,
collects their independent evaluations, and synthesizes an objective consensus report.

## When to Use

- High-stakes architectural choices (e.g., framework migration, database paradigm shift).
- Ambiguous security, compliance, or capital allocation trade-offs.
- Persistent debugging roadblocks where single-model analysis has dead-ended.
- Explicit user requests: "run consensus on X", "evaluate these options with multiple models".

Do not use for routine implementation, simple bug fixes, or minor styling decisions.

## Workflow

1. **Formulate the Decision Problem:**
   Define the decision objective, evaluated options, constraints, and evaluation criteria (scalability, cost, complexity, risk).
2. **Parallel Dispatch:**
   Query 2 to 4 diverse model families simultaneously (e.g., Anthropic Claude, OpenAI GPT, DeepSeek, Google Gemini) via `scripts/consensus.py` or subagent tasks.
3. **Synthesis & Verdict:**
   Compare the responses, identify points of unanimity, highlight key trade-off dissents, and produce a structured consensus report.

## Output Structure

The consensus report follows this format:

```markdown
# Consensus Report: <Decision Title>

## Executive Verdict
- Recommended Path: <Chosen Option>
- Confidence Level: <High | Medium | Low>
- Primary Rationale: <1-2 sentences summarizing consensus rationale>

## Comparative Analysis
| Criterion | Option A | Option B | Consensus View |
|---|---|---|---|
| Maintainability | ... | ... | ... |
| Performance / Scalability | ... | ... | ... |
| Cost / Complexity | ... | ... | ... |

## Key Points of Divergence
- <Note any meaningful disagreements between evaluated models>

## Actionable Next Steps
1. <Immediate tactical implementation step>
```
