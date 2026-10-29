# Pilot Acceptance Criteria (extended checks)

These supplement the seven acceptance-gate scenarios in `topology-and-decision-modeling.md`. Required whenever the roster includes an agent/system-configuration role (e.g. a Meta-learner) or a narration/logging role (e.g. a Documentarian).

## Controlled-trial requirement for every agent/system configuration change

A recommendation in this category is not "done" when the proposal text exists — it is done only when the Pilot has run an actual controlled trial and recorded its result:

1. **Baseline**: capture the current behavior/output of the target agent on a representative task, before any change.
2. **Candidate**: apply the proposed change to a disposable test profile only (never the live profile directly) — install the candidate skill/Soul.md/toolset change into a fresh test profile, run the same representative task against a copied workspace.
3. **Success metric**: state in advance what "better" means for this change (not post-hoc justification).
4. **Rollback condition**: since the trial ran in a disposable test profile, rollback is simply "do not promote" — the live profile was never touched.
5. **Review date and owner**: a human decides promote / reject / request another trial; the Meta-learner's own run never self-promotes.

A recommendation that skips the test-profile run and goes straight from "I noticed X" to "apply this change" fails this acceptance check regardless of how well-reasoned the proposal text is.

## Provenance / redaction canary for narration-style roles

A Documentarian-type role's notebook entries must be checkable against source artifacts, not merely readable. Before accepting its output as a Pilot pass:

1. Define the entry schema up front: run/task/decision identifier, timestamp, role, event type, source-artifact reference, outcome, experiment/change, evidence citation. No free-text transcript dump.
2. Run a negative-control test: plant something that must NOT appear (a raw prompt fragment, a credential-shaped string, an unrelated agent's private context) in the material the Documentarian has access to, then confirm the resulting notebook entry excludes it.
3. A clean-looking, well-written notebook entry that was never tested with a canary proves nothing — this check is Advisory-only on the runtime side (no tool filters the role's output), so the test is the only evidence that the schema discipline is actually being followed rather than merely instructed.
