# M1 Entry Ramp v1 Retrofit

This addendum governs the existing M1 package. Where it conflicts with an older harness-neutral/Codex/Claude/Gemini assumption, this addendum controls.

## Reference path

Use Hermes Desktop and the imported **Conductor** profile. The learner invokes the run from the Conductor’s canonical Bot Chat or Desktop workspace. The Conductor coordinates and verifies artifacts; it must not invent completion.

## Required M1 files

Use the [Entry Ramp v1 evidence map](../Entry-Ramp-v1/README.md). M1 must create or update:

- `employees/first-employee.md`
- `inputs/representative-input.md`
- `outputs/first-proposal.md`
- `runs/m1-workshop-manifest.md` with `run_type: workshop`
- `runs/m1-first-run-receipt.md`
- `runs/m1-first-run-review.md`
- `governance/cohort-one-action-boundary.md`

The Builder may read only the designated representative input and write only the proposed artifact plus receipt. It may not send, publish, purchase, update authoritative records, or use external systems.

## In-session minimum gate

Within 60 minutes, the learner must produce one bounded draft/proposal, inspect the saved file against its source, and record one observed limitation. A rerun and expanded Workforce Blueprint may move to practice work when time is short.

## Required practice run

After M1, the learner completes a manual `practice-run` using `runs/m1-practice-manifest.md` with `run_type: practice`. The manifest records `complete`, `blocked`, or `needs catch-up`.

For `blocked` or `needs catch-up`, the minimum viable submission is: the manifest, direct blocker evidence, and one attempted recovery step. This is not a failure grade; it is operational evidence for the catch-up clinic.

## Facilitator update

Before class, prepare either an activated Conductor workspace or a tested fallback. Do not spend the M1 workshop creating specialist Bots. Builder/Reviewer roles are introduced only when later modules justify them.
