# Topology Selection and Decision/Retry Modeling

## Topology selection (driven by task determinism, not preference)

- **Sequential** — execution graph is known in advance; linear pipeline; minimizes overhead. Use for deterministic, low-risk workflows (e.g., lint -> format -> commit).
- **Hierarchical (conductor + specialists)** — non-linear discovery needing context isolation and unified coordination. Use for most multi-step workforce designs where a conductor delegates to bounded specialists and workers report back only to the lead.
- **Peer-to-peer/blackboard** — open-ended, exploratory, needs resilience against individual failures; higher token and race-condition cost. Use only when the workflow genuinely has no fixed sequence and agents must read/write shared state asynchronously.

Don't default to hierarchical just because it is the most familiar pattern — forcing a deterministic workflow into hierarchical or blackboard adds conductor or shared-memory overhead the task does not need.

## Decision Work Units

A branch point in the workflow (e.g., "research found the topic already well-covered -> pivot to a subtopic") is modeled as its own row type, not folded into an adjacent work unit:

- outcome -> decision point -> input it evaluates -> anticipated branches (each with its own output artifact, owner, risk category, approval requirement, innovation envelope) -> default/fallback if the agent hits a branch not on this list.
- Kanban's parent/child structure is a DAG with all-or-nothing gating and no native if/else — don't pre-build both branches as a static fork. The decision agent creates whichever next task fits, dynamically, gated by its Decision Record.
- An unanticipated branch defaults to escalation unless it is independently low-risk AND within envelope (see the design-ai-workforce SKILL.md "Decision Work Units and novel branches" section) — never let an agent invent a new consequential task type mid-run with no prior risk classification, and never let "agent/system configuration change" branches auto-proceed regardless of apparent risk.

## Retries as bounded branches

Model retries explicitly, not as open loops: define the retry trigger, maximum attempts, what evidence must change between attempts, and the human-escalation condition once attempts are exhausted. This prevents the "repeatedly attempt the same invalid fix until token budget exhausted" failure mode.

## Acceptance-gate scenario checks

Run all of these against a generated design before calling it ready; any failure returns to decomposition/matrix steps, never forward. See `pilot-acceptance-criteria.md` for the extended checks (controlled trial, provenance canary) added for agent-configuration and documentation-style roles.

1. Deterministic, low-risk workflow -> selects sequential topology; no unnecessary conductor/shared-memory layer.
2. Discovery workflow with a predeclared pivot -> emits a Decision Record, exercises the non-default branch in Pilot, preserves branch-specific approval handling.
3. Unanticipated CONSEQUENTIAL branch -> creates only a blocked escalation task; cannot be labeled operationally ready.
4. Parallel work with a shared deliverable -> defines ownership, write-conflict strategy, merge/review point, rejoin acceptance criteria.
5. Unsafe/incomplete approval matrix -> emits no executable roster/scaffold, only a gap report.
6. Bot-proposed governance change -> creates a human-review proposal citing the relevant traceability row and pilot evidence; never silently amends governance.
7. Novel LOW-risk, in-envelope branch discovered -> proceeds without blocking, logged (`NOVEL_AUTO_PROCEEDED`) for after-the-fact review; novel CONSEQUENTIAL branch, out-of-envelope branch, or agent/system configuration change -> blocked proposal (`NOVEL_PROPOSED`) requiring approval.
