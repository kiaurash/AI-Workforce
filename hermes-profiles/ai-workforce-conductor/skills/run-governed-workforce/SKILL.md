---
name: run-governed-workforce
description: Coordinate a repository-first Builder-Reviewer run.
version: 0.1.0
---

# Run a Governed Workforce

Use this skill from the Conductor's canonical Bot Chat when an activated Builder and Reviewer are available. It coordinates a bounded Builder → Reviewer workflow using repository artifacts as the authoritative record.

## Preconditions

Confirm all of the following before starting:

- The learner has selected one bounded workflow and named its human approval boundary.
- The capstone repository is the active project workspace.
- Builder and Reviewer are activated in `profiles/role-activation-log.md`.
- Input is authorized and paths are known.
- The requested work is classified as `workshop` or `practice` in the run manifest.
- The requested work does not include a live external or consequential action. In cohort one, the workflow may prepare a real draft, proposed update, review packet, or approval record, but a human performs every actual send, publication, purchase, authoritative-record update, or production action outside the course workflow.

If a prerequisite is missing, create no run. State what is blocked and what evidence is needed.

## Procedure

1. Create `runs/<run-id>/run-manifest.md` from the supplied template. Set `Run type` to `workshop` or `practice`, then record the contract, input, output, handoff, review, and approval paths. Completion: every required path is explicit.
2. For a `practice` run, reuse the applicable workshop contract and record the required practice outcome: `complete`, `blocked`, or `needs catch-up`. A blocked or catch-up run must include blocker evidence and one attempted recovery step. Completion: the practice checklist in the manifest is complete before the next workshop.
3. Create or verify a Builder contract that specifies authorized input, permitted actions, prohibited actions, output path, evidence rules, uncertainty rules, and completion conditions. Completion: contract is inspectable in the repository.
4. Send the activated Builder an asynchronous Bot message using `message_agent` containing only the run ID, contract path, input path, output path, receipt path, and completion request. Do not include private learner discussion, unrelated history, or a desired conclusion. Completion: record the coordination notice or delivery ID in the manifest.
5. Require the Builder to save its proposal and run receipt before signaling completion. Inspect that both files exist. If either is absent, set the manifest to `blocked` and stop; do not infer success from a message.
6. Create a minimal review packet containing only the contract, approved source evidence, Builder proposal, and structured Builder handoff. Record its contents in the manifest. Completion: the packet excludes conversation summaries, unrelated repository artifacts, and recommended review disposition.
7. Send the activated Reviewer an asynchronous Bot message containing only the review task, review-packet paths, permitted output path, and disposition vocabulary: `accept`, `return for correction`, or `escalate to human`. Completion: record the coordination notice or delivery ID.
8. Require `reviews/review-decision.md` and inspect its cited evidence, findings, uncertainty, and disposition. If it is absent or unsupported, set the manifest to `blocked` and stop.
9. If the Reviewer returns `return for correction`, preserve the original proposal, record the required correction, and initiate a new Builder attempt with a new receipt. If it returns `escalate to human`, stop for human decision. If it returns `accept`, still stop at the designated human approval boundary whenever the next action is consequential.
10. Record the human decision in the approval log and update the manifest. Completion: the final manifest status and artifact paths are inspectable.

## Important limits

- Bot messages are asynchronous triggers, not transactional proof of delivery or work completion.
- `message_agent` is available only in a canonical Bot Chat. Do not run this skill from an ordinary chat, CLI session, or cron job and expect Bot-to-Bot messaging.
- A Reviewer receives a fresh conversation when delegated, but shared workspace/tool access is not hard access control. The minimal packet teaches context discipline; sensitive workflows need separately staged workspaces, scoped credentials, and access controls.
- The Conductor coordinates. It must not approve its own work, overwrite a review decision, or take the downstream consequential action.

## Run receipt

At close, report the run ID, manifest path, verified artifacts, Reviewer disposition, approval status, blockers, and any unresolved uncertainty. Never report a successful workforce run without direct evidence that the required artifacts exist.
