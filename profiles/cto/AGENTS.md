# CTO Profile — Agent Guidance

This document is for AI agents that interact with or consume outputs from the CTO Hermes profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Define the technology strategy for..." | Full engagement: requirements analysis → architecture design → technology selection → pyramid |
| "Evaluate this architecture decision..." | ADR-focused: context analysis → option evaluation → architecture decision record |
| "Should we build or buy X?" | Build-vs-buy-focused: capability analysis → TCO modeling → recommendation |
| "Review the technology stack for..." | Technology radar engagement: stack evaluation → radar classification → gap analysis |
| "Set engineering standards for..." | Standards-focused: current-state assessment → standard definition → adoption strategy |
| "Design the architecture for..." | Architecture engagement: requirements → constraints → system design → ADR documentation |
| "Escalate persistent bug / architecture dead-end..." | Escalation mode: deep root cause analysis across system boundaries, high-order reasoning |
| "Run consensus on these options..." | Multi-model consensus: parallel multi-LLM debate and synthesized verdict |

## Loading Order

When starting a CTO engagement, load skills in this sequence:

```python
skill_view('artifact-pyramids')      # 1. Output format specification
skill_view('executive-methodology')  # 2. Executive frameworks (decision frameworks, stakeholder communication)
skill_view('technology-radar')       # 3. Technology governance (build-vs-buy, architecture governance, engineering metrics)
```

## Output Contract

The profile produces technology artifacts as an artifact pyramid. The response to the caller is always the **absolute path to `00-index.md`** at the pyramid root. Not a summary. Not a natural-language handoff.

### Expected Structure

```
<engagement>/
├── 00-index.md                       ← Navigation index with SOURCES
├── 01-summary/
│   ├── technology-recommendation.md ← Primary recommendation with architectural rationale
│   └── architecture-decision.md     ← Key ADR for the central architectural choice
├── 02-analysis/
│   ├── build-vs-buy-evaluation.md  ← Per-capability build-vs-buy analysis with TCO
│   ├── technology-radar-update.md  ← Radar classification changes and rationale
│   └── architecture-tradeoffs.md   ← Architectural option evaluation
└── 03-dossiers/
    ├── reference-architectures.md  ← Reference architecture documents
    ├── standards-definitions.md    ← Engineering standards and conventions
    └── technology-survey.md        ← Evaluated technologies with data sources
```

### Cross-Reference Rules

1. **Every ADR in L2 is referenced in L1** — summary decisions link to full analysis
2. **Build-vs-buy recommendations include total cost of ownership data** with sources in L3
3. **Technology radar classifications are justified** with evidence from engineering metrics
4. **SOURCES sections at every layer** — absolute paths with descriptions

## Handoff Protocol

1. **The pyramid IS the handoff.** Close with the path. Do not summarize.
2. **Architecture Decision Records (ADRs)** follow the standard format: Context → Decision → Consequences.
3. **Technology radar entries** are classified into Adopt, Trial, Assess, or Hold with clear migration guidance.
4. **Output feeds into devops, backend-dev, fullstack-dev, and frontend-dev** profiles for implementation.

## Related Profiles

- **CFO** — coordinates on technology investment sizing and TCO assessment.
- **project-manager** — translates technical strategy and constraints into project roadmap and milestones.
- **devops** — receives infrastructure architectural blueprints and CI/CD standards.
- **cybersecurity** — aligns on security governance, zero-trust architecture, and compliance boundaries.
- **repo-manager** — enforces repository structure and branch protection rules aligned with technical standards.
