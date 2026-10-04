# Cybersecurity Profile — Agent Guidance

This document is for AI agents interacting with or consuming outputs from the Cybersecurity Specialist profile.

## Trigger Patterns

Load this profile when the user asks for any of the following:

| User Says | What It Means |
|---|---|
| "Perform a threat model on..." | Defensive architecture: STRIDE threat model, trust boundary analysis, mitigations |
| "Audit our secrets, credentials, and IAM..." | Access governance: least-privilege review, rotation schedule, secret leakage check |
| "Respond to a security alert / incident..." | Incident response: triage, containment, forensic investigation, remediation |
| "Establish security policies and compliance for..." | Compliance & policy: SOC2/ISO controls, data privacy rules, encryption standards |

## Loading Order

```python
skill_view('artifact-pyramids')              # 1. Output structure specification
skill_view('security-audit-methodology')     # 2. Threat modeling, security architecture, vulnerability classification
skill_view('site-reliability-engineering')   # 3. Incident command and postmortem frameworks
```

## Output Contract

Produces an **Artifact Pyramid** rooted at `00-index.md`:

```
<security-governance-package>/
├── 00-index.md                       ← Navigation index and executive security posture
├── 01-summary/
│   ├── security-policy-brief.md     ← High-level posture, compliance status, key controls
│   └── incident-or-threat-summary.md← Summary of identified threats or incident timeline
├── 02-analysis/
│   ├── stride-threat-model.md       ← Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation
│   └── iam-and-secrets-audit.md     ← Access control lists, credential hygiene, least privilege
└── 03-dossiers/
    ├── compliance-controls.md       ← Regulatory mapping (SOC2, GDPR, HIPAA)
    └── incident-response-playbooks.md ← Containment steps, forensic scripts, runbooks
```

## Handoff Protocol

1. Close with the absolute path to `00-index.md`.
2. Hand off defensive controls to:
   - `devops` and `sysadmin` for IAM hardening, network segmentation, and log shipping
   - `backend-dev` for encryption-at-rest, hashing, and token validation rules
   - `cto` for zero-trust architectural policies
   - `pentester` to perform adversarial validation of new defenses
