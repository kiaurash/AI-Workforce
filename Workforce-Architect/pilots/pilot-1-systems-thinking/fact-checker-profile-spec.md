# Profile Spec — fact-checker

**Status: spec for human setup. Not activated, not deployed.** A human applies this via the desktop app, `hermes profile` commands, or direct `config.yaml` / profile-directory setup, then verifies it with the activation smoke test below before relying on it.

## Identity
- Profile name: `fact-checker`
- Owns Traceability Matrix rows: `W5 (R2)` (re-read the Traceability Matrix for current details).
- SOUL file: `fact-checker-SOUL.md` (to be placed in profile root or configured system prompt).

## Model / provider
- Recommended family: Precise, instruction-following model with strong critical/adversarial reasoning (e.g. Claude 3.5 Sonnet or GPT-4o).
- Reason: Requires zero tolerance for unsupported claims, strict citation cross-checking, and adversarial evaluation of draft assertions.

## Skills
- `research:grounded-citations` (Grounding answers and draft assertions in verifiable sources).
- `web:blocked-page-recovery` (Accessing primary sources behind soft walls or complex formatting).

## Toolset
- Required: `web_search`, `web_extract`, `read_file`, `write_file`.
- Explicitly NOT granted:
  * CMS publishing tools (Enforced: absent).
  * Outbound communication / email broadcast tools (Enforced: absent).
  * `kanban_unblock` or orchestrator tools (Enforced: absent).
  * `skill_manage` or configuration mutation tools (Enforced: absent).

## Memory / data boundary
- May retain: Fact-check rubrics, database of verified citations, publication verification records.
- Must stay excluded: Unverified assertions, draft scratchpads, unrelated user history.

## Governance / approval references
- Touches Traceability row W5 (R2).
- Serves as the primary internal audit gate before editorial packaging (W6) and human publication approval (G1).
- Disputed claims that survive 2 retry rounds must be logged as `FLAGGED_FOR_HUMAN_ADJUDICATION`.

## Activation smoke test (required before calling this role ready)
1. Feed a test draft containing:
   - 2 verifiable factual claims with real citations.
   - 1 intentionally fabricated or misattributed claim.
2. Verify agent produces:
   - `fact-check-report.md` marking the 2 real claims as PASS and the fabricated claim as FAIL.
   - Annotates the draft with clear revision feedback.
3. Verify agent halts at the boundary and does NOT attempt to rewrite the article narrative or publish.

## Explicitly NOT granted, standing policy
- External publishing or communication tools.
- Profile-creation or profile-activation tooling.
