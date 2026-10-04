# Finance Manager Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the Finance Manager profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Review and approve this expense / purchase of..." | Expenditure review: budget check, vendor validation, authorization within threshold |
| "Track monthly burn and operating budget for..." | Budget tracking: planned vs. actual variance analysis, category breakdown |
| "Process vendor invoice / contractor payment for..." | Operational disbursement: invoice verification, payment scheduling, receipt logging |
| "Forecast cash flow for next quarter..." | Cash flow management: recurring costs, upcoming renewals, liquidity forecast |

## Loading Order

```python
skill_view('artifact-pyramids')      # 1. Output structure specification
skill_view('financial-modeling')     # 2. Financial modeling, SaaS metrics, budget allocation
skill_view('startup-analysis')       # 3. Operational expenditure frameworks
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<finance-operations-package>/
├── 00-index.md                       ← Navigation index and operational cash status
├── 01-summary/
│   ├── monthly-budget-variance.md   ← Planned vs. actual spending by department
│   └── expense-approvals-summary.md ← Approved expenditures, vendor contracts, disbursements
├── 02-analysis/
│   ├── cash-flow-projection.md      ← 90-day rolling operational cash flow
│   └── vendor-cost-breakdown.md     ← SaaS subscriptions, contractor costs, service renewals
└── 03-dossiers/
    ├── invoice-reconciliation.md    ← Line-item payment logs and matched receipts
    └── department-allocation.md     ← Engineering, marketing, and operations cost centers
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off financial operations to:
   - `accounting-manager` for general ledger entry, tax categorization, and audit reconciliation
   - `cfo` for expenditures exceeding approval limits or strategic budget reallocations
   - `project-manager` and `devops` with project-specific expense limits and subscription alerts
