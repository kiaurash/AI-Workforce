# Workforce Traceability Matrix

One row per work unit. The roster is derived from this matrix, not brainstormed.

| Workflow Outcome | Work Unit | Input / Source of Truth | Output Artifact / Schema | Owner Agent | Allowed Tools | Verifier / Evidence | Risk Category | Approval Record | Escalation Path |
|---|---|---|---|---|---|---|---|---|---|
| Published blog post | Fact-check draft | Draft + source list | Annotated draft (pass/fail notes) | Fact-Checker | web search, read-only doc access | Human skim or second-agent spot-check | Low (internal doc) | None required | Flag back to Writer if sources unverifiable |

For a Decision Work Unit, replace "Output Artifact" with "Decision Record" (see templates/decision-record.md) and list anticipated branches as sub-rows, each with its own risk category, approval record, and innovation envelope (authorized artifact/destination types, tool/data scope, max extra tasks/iterations, cost/time budget, prohibited objective changes, review owner/deadline) governing whether a novel discovery within that branch's family may auto-proceed.

For a Retry Unit, add columns: retry trigger, max attempts, evidence change per attempt, human-escalation condition once exhausted.

For an "agent/system configuration change" row (e.g. a Meta-learner proposing a skill/Soul.md/tool adjustment to another agent), do not fill in a standard risk/envelope pair — this category has no auto-proceed path. Instead record: target agent, proposed change, baseline behavior, candidate behavior, success metric, rollback condition, review date, and reviewing human/owner.
