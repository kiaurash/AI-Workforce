# Role Decision Record

Use this template at the end of the Builder (M2), Reviewer (M3), or Observer (M6) experiment. Save one record per role at `profiles/role-decision-<role>.md` and link it from `profiles/role-activation-log.md`. See Course.md section 3.5.

Adopting and declining receive equal credit. The assessment looks at the evidence and the reasoning, not at the outcome.

```markdown
# Role Decision Record: [Builder / Reviewer / Observer]

Module: [M2 / M3 / M6]
Date: [...]
Human owner: [...]

## State reached
[ ] Concept demonstrated (facilitator demonstration or labeled supplied case)
[ ] Experiment completed (the role's evidence task was run by me under an explicit contract)
[ ] Decision recorded (this record, citing experiment evidence)

## Experiment evidence
Required evidence for this role: [Builder: skill-vs-baseline repeat-run comparison | Reviewer: activation test + one real disposition | Observer: activation test + one proposal or `collect more evidence`]
Paths: [run ids, receipts, review packet, activation log entry]
Supplied (not my own) material used: [none / what, and where it was labeled]

## Decision
Status: [adopt | adopt conditionally | do not adopt | deferred pending experiment]
Condition (only if conditional): [for example, high-risk runs only]

If no experiment evidence exists, the only valid status is `deferred pending experiment`.

## What the role did (observed)
Caught or improved: [...]
Missed or got wrong: [...]
Produced but not needed: [...]

## Cost (label each figure `estimate` or `measured`)
Extra human time per run: [...]
Setup time: [...]
Extra files or records to maintain: [...]

## Simpler alternative considered
[a skill | a checklist | human review | none] and what it would and would not cover: [...]

## Reasoning
[Why this status follows from the evidence above. Name the risk the role covers or does not cover.]

## What would change this decision
[...]

## Activation log updated
[ ] profiles/role-activation-log.md shows `adopted`, `not adopted`, or `deferred`, with a link to this record
```

## Illustrative example: a justified decision not to adopt (fictional)

```markdown
# Role Decision Record: Reviewer

Module: M3
Human owner: Sam (operations analyst)

## State reached
[x] Concept demonstrated  [x] Experiment completed  [x] Decision recorded

## Experiment evidence
Required evidence: activation test + one real disposition
Paths: profiles/role-activation-log.md (Reviewer entry), runs/review-packet-weekly-status.md, runs/review-decision-001.md
Supplied material used: none

## Decision
Status: do not adopt (for the weekly internal status summary only)

## What the role did (observed)
Caught or improved: the activation test passed; the Reviewer correctly refused an empty packet.
Missed or got wrong: on the real packet it returned `approve` with no findings. I found one date I could not trace to the source; the Reviewer did not flag it.
Produced but not needed: a four-section disposition for a half-page summary.

## Cost
Extra human time per run: about 8 minutes (measured, one run)
Setup time: about 25 minutes (estimate)
Extra files or records to maintain: 2 per run

## Simpler alternative considered
A five-line source checklist that I apply myself before relying on the summary. It would have caught the untraceable date. It does not give an independent view, which matters for external reports but not for this internal summary.

## Reasoning
For a low-risk internal summary read by my own team, the checklist covers the failure I observed at a fraction of the cost. One run is not enough to conclude the Reviewer is useless.

## What would change this decision
If the summary is sent to a client or senior management, or if the checklist misses an error in three consecutive runs, I would re-run the experiment.
```

## Illustrative example: not a decision (fictional)

> "I did not adopt the Reviewer because I ran out of time."

This has no experiment evidence, so the status is `deferred pending experiment`, not `do not adopt`.
