# Pilot #1 Decision Brief — Systems Thinking Blog/Newsletter Workflow

**Topic piloted:** "How to leverage Systems Thinking in the Age of AI" → weekly blog
post + newsletter piece for AI practitioners/engineering leaders, applying Meadows'
Leverage Points.

**Execution method:** Genuinely cold-start test. A fresh Hermes profile (`pilot-test-1`)
received only the installed `design-ai-workforce` skill bundle (full directory copy, not
raw-URL install) and a model — no accumulated context from the design discussion that
produced the skill. Prompted per the exact script in this repo's intake process: asked
to decompose the workflow and withhold roster naming until decomposition was done.

## Scope actually run

- **Design mode**: full run, cold-start, through roster derivation.
- **Scaffold mode**: full run, cold-start, kanban toolset added mid-session.
- **Pilot execution** (actually unblocking and running a task): explicitly **not** run
  in this pass — stopped here by deliberate choice to review Design+Scaffold evidence
  before spending further effort. See "Not yet tested" below.

## Validated by construction (file/task existence, read back directly — not chat claims)

- `traceability-matrix.md`, `risk-approval-matrix.md`, `decision-record-d1.md`, and one
  `*-SOUL.md` + `*-profile-spec.md` pair per rostered Bot (`systems-researcher`,
  `systems-writer`, `fact-checker`) all exist as real files — verified via `read_file`
  against the actual saved paths, not inferred from the session transcript.
- 8 kanban tasks exist on the live board — verified via `kanban_show`/`kanban_list`,
  not the chat transcript — correctly parent-chained (W1→W2→D1→W3→W4→W5→W6→G1).

## Observed behavior and validated controls

1. **Decomposition-before-roster-naming held.** The cold-start agent asked five
   categories of clarifying questions and refused to name agents until the workflow
   was decomposed into work units — exactly the SKILL.md step 1 requirement, observed
   on a blind run, not asserted by us.
2. **Decision Record structure was populated, but its evidence gate failed.** D1
   included all expected fields and emitted `NOVEL_AUTO_PROCEEDED`; independent review
   found that the claimed framing brief, research dossier, 42-article count, and 90%
   confidence were unsupported because the source artifacts were never created or
   committed. The corrected record is `ANOMALOUS_BLOCKED`, `envelope_check =
   not_evaluated`, with W3 held blocked. This validates template population, **not**
   decision correctness or authorization.
3. **Risk/Approval Matrix category coverage held, but runtime labels failed review.**
   All 7 categories were explicitly addressed with no blank/copied placeholders.
   However, it mislabeled proposed human-apply tool omissions as Enforced runtime
   facts. The corrected matrix labels them proposed constraints, Governed/unverified
   pending profile activation and smoke tests.
4. **First-run Scaffold blocking rule fired correctly — the strongest result of this
   Pilot.** Every one of the 8 tasks was created `blocked`, including the low-risk rows
   (W1, W3, W4, W6) that the pre-Codex-review version would not have blocked. This is
   verified against live kanban state.
5. **Board-control labeling failed independent review.** The generated matrix falsely
   asserted that no agent possesses `kanban_unblock`. Multiple non-human profiles on
   this shared board can possess it. The corrected package states that blocked-task
   dispatch is Enforced, while human-exclusive release is not Enforced here and remains
   Governed by procedure and board composition.
6. **Unrelated concurrent board activity did not contaminate the run.** One
   pre-existing task from a different profile/project (`wf-instructor`'s separate
   "docu-dramedy" initiative) coexisted on the same board with zero observed cross-task
   interference — checked directly via `kanban_show`.

## Failed / unknown / real findings (not failures of the skill, findings from using it)

1. **Minor step-ordering deviation**: the cold-start agent narrated the Risk/Approval
   Matrix before the full Traceability Matrix table in chat, though the Traceability
   Matrix was the correctly-structured saved artifact. SKILL.md's step order (matrix
   before risk matrix) wasn't followed to the letter in the narration, even though the
   final artifacts are both correct and complete.
2. **Roster-completeness and catalog-name findings**: the cold-start agent referenced
   existing skills rather than generating bespoke role skills, which is a reasonable
   interpretation if the gate explicitly allows "reference an existing skill OR
   generate a new one." It also emitted invalid qualified names (`research:arxiv`,
   `web:blocked-page-recovery`, `research:grounded-citations`); these are corrected in
   the profile specs to `arxiv`, `blocked-page-recovery`, and `grounded-citations`.
   Human-only owner `human-editor` is now explicitly excluded from Bot artifact
   completeness and governed by a separate approval contract.
3. **D1 evidence provenance failed**: the cold-start agent claimed 42 inspected
   articles and 90% confidence without preserving the declared framing brief or
   research dossier. The record is downgraded to illustrative and blocked; this is a
   substantive Pilot finding, not missing documentation to be reconstructed after the
   fact.
4. **Proposed tool boundaries are not runtime facts**: no role profile was activated,
   so all omissions remain proposed constraints pending activation smoke tests.
5. **Not yet tested**: actual task execution (unblocking W1 and letting an agent run
   it for real). Operational validity for outputs and Retry Unit behavior remains
   unproven.
6. **Not yet tested**: the "Agent/system configuration change" controlled-trial gate.
   That's Pilot #2's scope, but Pilot #2 remains blocked until this corrected evidence
   package passes independent re-review.

## Readiness label (per `references/evidence-labels-and-runtime-enforcement.md`)

**Requires additional infrastructure/evidence.** The Scaffold first-run blocking
control is operationally validated, and decomposition/structure generation worked.
The package is **not deployable** as a workforce design yet: D1's evidence gate failed,
profile tool boundaries remain proposed until activation smoke tests, and task
execution was not tested. Pilot #2 must not consume this package until independent
re-review accepts these corrections.

## Revisions required before calling this skill fully validated

1. Independently re-review this corrected evidence package.
2. Update the reusable roster-completeness wording to allow a verified existing skill
   or a generated skill, and explicitly exclude human-only approval owners from Bot
   artifact requirements.
3. In a future execution Pilot, require Decision Records to fail closed when any
   declared authoritative input artifact is absent; preserve source inventory/query
   evidence before permitting `envelope_check = pass`.
4. Activate candidate role profiles only in a disposable test setup, smoke-test their
   actual tool/skill boundaries, and keep all eight tasks blocked until that evidence
   is reviewed.
5. Only then consider Pilot #2; the user has selected a fresh `wf-meta-learner` scope
   that leaves the unrelated SWARM-Wisdom profiles untouched.
