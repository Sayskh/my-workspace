# Accounting Manager Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the Accounting Manager profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Reconcile accounts / balance sheet for..." | General ledger reconciliation: bank vs. book balance, journal adjustments, suspense clearing |
| "Audit tax obligations and compliance for..." | Compliance check: sales tax, VAT, corporate tax accruals, withholding requirements |
| "Prepare period-close / GAAP financial statements..." | Period close: revenue recognition (ASC 606), depreciation, amortization, trial balance |
| "Audit receipt documentation / internal controls..." | Audit readiness: internal control review, voucher trails, supporting documentation |

## Loading Order

```python
skill_view('artifact-pyramids')          # 1. Output structure specification
skill_view('financial-modeling')         # 2. Financial accounting models, ratios, GAAP standards
skill_view('technical-documentation')    # 3. Compliance documentation and audit trails
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<accounting-audit-package>/
├── 00-index.md                       ← Navigation index and audit readiness score
├── 01-summary/
│   ├── financial-statements.md      ← Balance Sheet, Income Statement, Cash Flow Statement
│   └── compliance-and-tax-status.md ← Tax liabilities, statutory filing deadlines, risk status
├── 02-analysis/
│   ├── account-reconciliation.md    ← Bank, AR, AP reconciliations and variance explanations
│   └── journal-entries-and-accruals.md ← Adjusting journal entries, accruals, depreciation
└── 03-dossiers/
    ├── audit-trail-and-evidence.md  ← Vouchers, invoices, bank statements, tax IDs
    └── accounting-policy-notes.md   ← Revenue recognition policy, capitalization criteria
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off accounting packages to:
   - `cfo` for formal signing of financial statements and board reporting
   - `finance-manager` for operational adjustments and vendor payment scheduling
   - External auditors or tax accountants with full audit documentation
