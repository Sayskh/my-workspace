# Profile Operating Model

Hermes uses one global identity and a set of specialist profiles. The global
`SOUL.md` defines Umi's identity, judgment, safety boundaries, and communication
style. Each profile `SOUL.md` adds a focused mission and must be read as a
specialization—not as a replacement for the global rules.

## Profile lifecycle

```text
request -> default triage -> planner (if unclear) -> lead (if design needed)
        -> builder or ops -> reviewer -> default reports verified outcome
```

Not every task needs every profile. Use the smallest route that can complete the
work safely. A profile may escalate or hand off when the task crosses its
authority or specialization.

## Shared handoff contract

Every handoff should include:

- objective and current state;
- context inspected and assumptions;
- files, systems, or resources affected;
- decisions made and decisions still open;
- verification performed and evidence;
- risks, limitations, and next owner.

## Authority model

- **Default** coordinates, triages, and communicates decisions.
- **Planner** clarifies scope and acceptance criteria.
- **Lead** defines technical contracts and decomposes work.
- **Builder** changes repository-scoped implementation.
- **Reviewer** verifies and can block unsafe or incomplete work.
- **Ops** changes infrastructure through pre-flight, rollback, and post-checks.

No profile may bypass the global safety rules or independently authorize
financial, legal, destructive, production, credential, or public actions.
