# Entry Ramp v1 — M0 → M0.5 → M1

Entry Ramp v1 is the first tested learner journey for **Build Your AI Workforce with Hermes**. Learners use one repository and progress from selecting a safe, valuable workflow to creating a first inspectable draft/proposal.

## Acceptance test

A fresh learner must be able to:

1. complete M0 and save `discovery/opportunity-map.md` and `discovery/workflow-safety-triage.md`;
2. complete M0.5 Gate A and Gate B;
3. complete M1 with one bounded Builder task that saves only a permitted draft/proposal and receipt;
4. inspect repository evidence and record one limitation; and
5. complete a manual practice run, or submit a documented `blocked`/`needs catch-up` path.

## Fixed evidence map

```text
ai-workforce/
├── workspace-rules.md
├── discovery/
│   ├── opportunity-map.md
│   └── workflow-safety-triage.md
├── inputs/
│   └── representative-input.md
├── outputs/
│   ├── commitments.md
│   └── first-proposal.md
├── employees/
│   └── first-employee.md
├── runs/
│   ├── m0.5-smoke-test-receipt.md
│   ├── m1-workshop-manifest.md
│   ├── m1-first-run-receipt.md
│   ├── m1-first-run-review.md
│   └── m1-practice-manifest.md
├── governance/
│   └── cohort-one-action-boundary.md
└── profiles/
    └── role-activation-log.md
```

Repository artifacts are authoritative. Bot messages and chat claims are coordination signals, not completion evidence.

## Cohort-one policy

Both knowledge-work and operational workflows are supported. All live external or consequential execution is prohibited inside cohort one; learners prepare drafts, proposed updates, evidence packets, and approval records only.

## Materials

- [M0 Opportunity Discovery](../M0-Opportunity-Discovery/README.md)
- [M0.5 Hermes Desktop onboarding](../M0.5-Hermes-Desktop-Onboarding/README.md)
- [M1 Entry Ramp retrofit](../M1-First-AI-Employee/ENTRY-RAMP-V1-RETROFIT.md)
- [Conductor distribution](../../hermes-profiles/ai-workforce-conductor/README.md)
