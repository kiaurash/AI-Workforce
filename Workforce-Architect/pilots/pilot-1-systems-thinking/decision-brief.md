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

## Operationally validated (the mechanism actually fired, not just documented)

1. **Decomposition-before-roster-naming held.** The cold-start agent asked five
   categories of clarifying questions and refused to name agents until the workflow
   was decomposed into work units — exactly the SKILL.md step 1 requirement, observed
   on a blind run, not asserted by us.
2. **Decision Work Unit mechanics fired correctly.** D1's Decision Record populated
   every required field (evidence/provenance, explicit numeric saturation threshold,
   confidence 90%, innovation envelope check = `pass`, correct `NOVEL_AUTO_PROCEEDED`
   flag for an in-envelope low-risk pivot) — this is the single most-debated mechanism
   in the whole design (Codex findings, the envelope-check addition, the three-way
   novel-branch flag), and it worked on a cold run.
3. **Risk/Approval Matrix hard gate held against the hardened template.** All 7
   categories were explicitly analyzed (no blank/copied "not applicable" — the
   REQUIRED-prompt template change from PR #3's review actually changed behavior:
   each "not applicable" line cites a specific reason, e.g. "no agent profile possesses
   CMS publishing tools").
4. **First-run Scaffold blocking rule fired correctly — the most important single
   result of this Pilot.** Every one of the 8 tasks was created `blocked`, including
   the low-risk rows (W1, W3, W4, W6) that the pre-Codex-review version of this skill
   would NOT have blocked. This is the exact gap Codex's source-level review found in
   PR #3, and the fix verifiably works on a blind run.
5. **Board-wide `kanban_unblock` caveat self-surfaced.** The cold-start agent
   proactively added a "Runtime Safety & Board Assumptions" section citing the
   board-configuration dependency — it had read `references/evidence-labels-and-
   runtime-enforcement.md`, not just the main procedure, unprompted.
6. **Unrelated concurrent board activity did not contaminate the run.** One
   pre-existing task from a different profile/project (`wf-instructor`'s separate
   "docu-dramedy" initiative) coexisted on the same board with zero cross-task
   interference — checked directly via `kanban_show`.

## Failed / unknown / real findings (not failures of the skill, findings from using it)

1. **Minor step-ordering deviation**: the cold-start agent narrated the Risk/Approval
   Matrix before the full Traceability Matrix table in chat, though the Traceability
   Matrix was the correctly-structured saved artifact. SKILL.md's step order (matrix
   before risk matrix) wasn't followed to the letter in the narration, even though the
   final artifacts are both correct and complete.
2. **Roster-completeness gate wording gap**: the gate requires "its required skill(s)"
   per Bot; the cold-start agent referenced existing catalog skills (`research:arxiv`)
   rather than generating new bespoke SKILL.md files. Reasonable adaptation, but the
   gate's current wording implies generation is mandatory — needs a wording fix:
   "reference an existing skill OR generate a new one," per @ai-workforce-conductor.
3. **Not yet tested**: actual task execution (unblocking W1 and letting an agent run
   it for real) — Pilot #1 stops at Scaffold. Operational validity for the *execution*
   layer (do agents actually produce correct outputs when run, does the Retry Unit
   logic actually trigger on a real inconclusive-research case) remains unproven.
4. **Not yet tested**: the "Agent/system configuration change" controlled-trial gate
   — no work unit in this workflow touches that category. That's Pilot #2's job
   (`wf-meta-learner`), still pending and still blocked on the SWARM-Wisdom naming
   question from earlier in this thread.

## Readiness label (per `references/evidence-labels-and-runtime-enforcement.md`)

**Deployable with governance only** for the Design+Scaffold layer specifically: the
artifacts are correct and the first-run safety mechanism is confirmed operational, but
the design has not yet been through real task execution, so it is not yet "deployable
now" for the full workflow. **Requires additional infrastructure/evidence** before any
claim beyond Design+Scaffold validity.

## Revisions required before calling this skill fully validated

1. Fix roster-completeness wording (#2 above) — low effort, no architecture change.
2. Run Pilot #1 part 2 (actual execution) OR accept this as sufficient evidence for
   Design+Scaffold and move directly to Pilot #2 — human decision, not ours to make.
3. Resolve the SWARM-Wisdom naming question before starting Pilot #2.
