# Financial Analyst Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the Financial Analyst (FinOps) profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Analyze cloud infrastructure spending / FinOps for..." | FinOps analysis: cost per query, compute right-sizing, reserved instances, egress costs |
| "Calculate SaaS metrics (ARR, MRR, NRR, CAC, LTV)..." | SaaS metrics: cohort retention, payback curve, magic number, rule of 40 |
| "Build a financial forecast / sensitivity model for..." | Quantitative modeling: Monte Carlo simulation, multi-variable sensitivity, hiring plan |
| "Evaluate market comps / valuation benchmarks for..." | Valuation & benchmarks: public SaaS multiples, ARR multiples, gross margin benchmarks |

## Loading Order

```python
skill_view('artifact-pyramids')              # 1. Output structure specification
skill_view('financial-modeling')             # 2. SaaS metrics, unit economics, financial models
skill_view('saas-valuation-compression')     # 3. Market valuation multiples and compression trends
skill_view('yfinance-data')                  # 4. Market and public comp data
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<financial-intelligence-package>/
├── 00-index.md                       ← Navigation index and executive insight summary
├── 01-summary/
│   ├── saas-kpi-dashboard.md        ← ARR, MRR, NRR, Gross Margin, CAC Payback, Rule of 40
│   └── finops-cost-recommendation.md ← Identified cloud savings, right-sizing opportunities
├── 02-analysis/
│   ├── unit-cost-breakdown.md       ← Cost per tenant, cost per API request, compute vs. storage
│   └── cohort-and-churn-analysis.md ← Net retention curves, expansion revenue, churn trends
└── 03-dossiers/
    ├── financial-model-worksheets.md ← Formulas, cohort tables, forecast scenarios
    └── benchmark-comparisons.md     ← Public SaaS multiples, peer group comparisons
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off analytical findings to:
   - `cfo` for strategic pricing, fundraising narratives, and capital planning
   - `devops` with concrete FinOps right-sizing actions and cloud savings targets
   - `finance-manager` with variance drivers and adjusted forecast models
