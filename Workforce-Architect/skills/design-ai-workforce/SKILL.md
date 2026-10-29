---
name: design-ai-workforce
description: Use when designing a multi-agent AI workforce.
version: 0.2.0
---

# Design an AI Workforce

Use this skill when a user arrives with a workflow concept (rough sketch or detailed process map) and wants agents, profiles, and skills designed for it. This skill governs the DESIGN, SCAFFOLD, and PILOT phases. It does not itself activate a production role contract — if the target environment already has an activation/run-manifest discipline for roles (e.g. a Conductor/Builder/Reviewer/Observer contract), hand off to that discipline for ongoing production runs rather than duplicating its mechanics here.

## Procedure (each step gates the next — do not skip ahead)

1. **Decompose the workflow into work units first**, including **Decision Work Units** (branch points) and **Retry Units** (bounded loops: trigger, max attempts, what evidence changes per attempt, escalation condition once exhausted). Never accept a request to name roles before decomposition — roles brainstormed ahead of decomposition reproduce generic names ("researcher," "reviewer") instead of roles justified by the actual work.
2. **Build the Traceability Matrix** (`templates/traceability-matrix.md`): one row per work unit — outcome → work unit → input/source → output artifact → owner agent → allowed tools → verifier/evidence → risk category → approval record → escalation path. The roster is DERIVED from this matrix, never brainstormed independently of it. Each proposed agent must own at least one row with a defined artifact and acceptance evidence.
3. **Risk/Approval Matrix is a hard gate** (`templates/risk-approval-matrix.md`). Before any agent roster or scaffold is emitted, every consequential action category — external writes, money, production/infra changes, outbound communication, personnel, legal/contractual, **and agent/system configuration change** (see Pitfalls) — must have a declared approval owner. If any such category is undefined, emit a gap report ONLY — no executable roster, no scaffold — regardless of how finished the rest of the design looks.
4. **Label every proposed control with its enforcement evidence** — Enforced / Governed / Advisory. See `references/evidence-labels-and-runtime-enforcement.md` for the definitions and the known Hermes-runtime enforcement boundaries. Never let a generated design imply a safety property the runtime can't actually back.
5. **Choose topology from task determinism, not default preference.** See `references/topology-and-decision-modeling.md`. A deterministic workflow forced into a hierarchical/blackboard pattern just because that pattern is familiar adds coordination overhead the task doesn't need.
6. **Emit output in three honestly-labeled tiers**:
   - *Auto-deployed*: kanban tasks (one per matrix row) + SKILL.md files — created and verified by read-back.
   - *Human-apply spec*: new Bot/profile definitions (model, toolset, skills) — labeled "requires human setup," never "deployed" (no tool in this runtime creates a profile from inside a skill).
   - *Governance doc*: the Traceability Matrix and Risk/Approval Matrix — live as a dedicated governance kanban task thread for per-engagement audit history, plus durable templates under this skill for cross-engagement reuse. Never render these as if they were self-enforcing.
7. **Progress through modes, never straight to production**: Design (matrices/specs only) → Scaffold (kanban tasks/SKILL.md actually created, only after a user confirms the risk gate and the exact artifact manifest — see Scaffold mutation boundaries below) → Pilot (one bounded, non-consequential test run that must exercise at least one non-default Decision branch, not only the happy path).
8. **Run the acceptance-gate scenario checks before calling anything "ready"** (full list in `references/topology-and-decision-modeling.md`, plus the extended checks in `references/pilot-acceptance-criteria.md`). Any failure sends the design back to steps 1-3, never forward to Scaffold/Pilot. Distinguish artifact validity (files/tasks exist and parse) from operational validity (a run proved the unit does what its row claims, including a deliberate escalation trigger) — existence alone never earns a "deployable" label.

## Scaffold mutation boundaries

- **May always create/update without per-run confirmation**: the design package (Traceability Matrix, Risk/Approval Matrix, Decision Records), the per-engagement governance task thread, and draft profile specifications (documents, never represented as configured or running bots).
- **Requires a user-confirmed artifact manifest first**: any SKILL.md creation/change, any kanban task graph creation beyond the governance thread, any cron schedule creation. State the exact list of files/tasks/schedules and wait for explicit confirmation before creating any of it.
- **Must never do in this version**: configure/activate a profile, unblock/approve consequential or out-of-envelope work, dispatch Pilot work for a work unit whose risk row is undefined or unapproved, or modify governance rules without human approval.

## Decision Work Units and novel branches

- Every Decision Work Unit produces a durable Decision Record (`templates/decision-record.md`) before any branch task is created: evidence evaluated, explicit criteria/thresholds (never "use judgment"), selected branch + rationale, confidence/dissent, applicable risk/approval reference, authorized next-task template(s) or `ESCALATE_UNPLANNED_BRANCH`, human override field.
- A consequential decision agent is read-only/non-executing: it recommends a branch; a separate dispatch step creates the downstream task only once the applicable gate is satisfied.
- When the agent discovers a beneficial path outside the anticipated branches, apply the SAME risk-category test used everywhere else rather than a blanket dead-stop, AND require `envelope_check = pass` (the branch must stay within that Decision Work Unit's pre-authorized innovation envelope: allowed artifact/destination types, tool/data scope, max extra tasks/iterations, cost/time budget, prohibited objective changes, review owner/deadline — defined at design time on the Traceability Matrix row, consumption logged at runtime on the Decision Record):
  - risk = low/no **and** envelope_check = pass → create the task normally, flag the record `NOVEL_AUTO_PROCEEDED` for after-the-fact human review. This is where creative flexibility belongs — don't gate what isn't consequential and stays in-scope.
  - risk = consequential, OR envelope_check = fail, OR category = agent/system configuration change (see Pitfalls — this category never auto-proceeds) → `NOVEL_PROPOSED`, create the task with `initial_status='blocked'`; a human `kanban_unblock` both reviews and approves it.
  - genuinely stuck with no proposal → `ANOMALOUS_BLOCKED` (different review framing: "what do I do," not "is this good").

## Pitfalls

- A workforce design that claims a safety property backed only by a prompt instruction (Advisory) is unsafe by construction — always cite the actual mechanism (tool absent from the Bot's toolset, a genuine dispatch-time block, a human review step) before labeling anything Enforced or Governed.
- In this Hermes runtime, `kanban_create` has no native allowlist on assignee, tools, or task shape — approved-template/assignee enforcement can only ever be Governed (a human checks at `kanban_unblock` time), never Enforced. Don't design a control that assumes the dispatcher validates content.
- Bots must never silently edit a durable governance skill or matrix. A bot proposes a change via a comment or human-review task citing the specific Traceability Matrix row or pilot evidence that motivated it; a human (or a designated admin bot, post-approval) applies it. Keep "propose" and "commit" as separate, human-gated steps.
- Don't pre-wire both sides of a decision as a static kanban DAG fork — kanban parent/child gating is all-or-nothing AND with no native if/else. The decision agent creates whichever next task actually fits, dynamically, gated by its Decision Record.
- **"Agent/system configuration change" (e.g. a Meta-learner/Observer-style proposal to adjust another agent's skill, Soul.md, or toolset) is its own consequential category, not covered by the other six.** Its blast radius is another agent's standing behavior across every future run, not one task's output — a single Decision Record's risk/envelope fields don't capture that well. No proposal in this category auto-proceeds regardless of apparent risk level; it always creates a blocked proposal requiring a controlled trial (baseline, candidate, success metric, rollback condition, review date — see `references/pilot-acceptance-criteria.md`) before a human applies it.
- A role whose job is narration/logging (e.g. a Documentarian) still needs a provenance/redaction discipline in its Traceability row — "verifier/evidence" for such a role should be "entries are traceable to a specific kanban task/decision record/run manifest ID," not "narrative is readable." This constraint is Advisory only (no tool filters its output), so the Pilot must include a negative-control canary check, not just a passing read.
