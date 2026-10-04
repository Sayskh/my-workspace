# CFO Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the CFO profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Evaluate the financial viability of..." | Full financial appraisal: unit economics, sensitivity modeling, capital allocation |
| "What is our runway and burn rate..." | Cash analysis: monthly burn, runway projection, stress test |
| "Build a financial model for..." | Financial modeling: 3-statement or revenue model, scenario projections |
| "Assess this pricing or revenue model..." | Monetization strategy: unit economics, gross margins, CAC payback |
| "Should we invest in or approve this budget for..." | Capital allocation: ROI analysis, opportunity cost, risk-adjusted returns |

## Loading Order

```python
skill_view('artifact-pyramids')      # 1. Output format specification
skill_view('executive-methodology')  # 2. Executive decision frameworks
skill_view('financial-modeling')     # 3. Financial modeling, SaaS metrics, unit economics
skill_view('startup-analysis')       # 4. Startup viability frameworks (VC/CEO perspectives)
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<financial-engagement>/
├── 00-index.md                       ← Navigation index and executive summary
├── 01-summary/
│   ├── financial-recommendation.md  ← Core recommendation, budget decision, and rationale
│   └── runway-burn-overview.md      ← High-level runway, burn, and cash position
├── 02-analysis/
│   ├── scenario-modeling.md         ← Base, downside, and upside scenarios
│   ├── unit-economics.md            ← CAC, LTV, payback period, and margins
│   └── cost-structure-analysis.md   ← Fixed vs. variable breakdown and cloud costs
└── 03-dossiers/
    ├── model-workbooks.md           ← Complete assumptions, data sources, formulas
    └── sensitivity-tables.md        ← Multi-variable sensitivity analysis
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off budget allocations and operational targets to:
   - `finance-manager` for day-to-day execution and expense tracking
   - `accounting-manager` for compliance, ledger auditing, and tax readiness
   - `financial-analyst` for FinOps cloud tracking and ongoing variance analysis
   - `cto` for infrastructure budget boundaries and build-vs-buy modeling
