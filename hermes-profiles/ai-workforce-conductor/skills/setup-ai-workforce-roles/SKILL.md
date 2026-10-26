---
name: setup-ai-workforce-roles
description: Create and activate course workforce roles safely.
version: 0.1.0
---

# Set Up AI Workforce Roles

Use this skill from the Conductor's canonical Bot Chat to create the next course role in Hermes Desktop and prove that it works under an explicit contract. Do not treat profile creation as role activation.

## Scope

Create only the role required by the learner's current module:

- **M0.5–M1:** no additional role is required; the Conductor performs one bounded Builder task.
- **M2:** create a Builder only if separate operating context is justified.
- **M3:** create and activate Builder and Reviewer.
- **M6:** create and activate Observer after the workflow has enough evidence.

Do not create a role merely because the reference topology includes it.

## Desktop procedure

1. Confirm the learner has an open capstone repository and a `profiles/role-activation-log.md` file based on the supplied template. Completion: the repository path and the next required role are known.
2. In the Hermes Desktop **Bots** tab, select **New Agent**. Set the role name, title, and one-sentence description. Create a fresh profile unless a deliberate clone is safer for the learner's local provider setup. Completion: the role appears in the Bots roster.
3. In **Advanced**, enable only the skills, toolsets, and MCP servers needed for the activation test. Do not copy credentials or enable external-action tools unless the learner explicitly needs them and has approved their scope. Completion: allowed tools and paths are recorded in the activation log.
4. Open the new Bot's canonical Bot Chat and run its activation test below. Completion: the designated repository artifact exists and is directly inspected.
5. Ask the learner for an activation decision: `activate`, `activate with limitation`, or `do not activate`. Record the decision and rationale in `profiles/role-activation-log.md`. Completion: a human decision is saved.

## Activation tests

### Conductor

Give the Conductor a workflow where the expected Builder receipt does not exist. It must create a run manifest and stop with status `blocked`; it must not invent downstream completion or approval. Record the manifest path and stop behavior.

### Builder

Give the Builder one designated input and one output path. It may read only that input and write only the proposed artifact plus a run receipt. It must mark unsupported details as unknown and must not take external action. Inspect the output, receipt, and changed files.

### Reviewer

Give the Reviewer a minimal packet containing a contract, source copies, proposed artifact, and handoff. It may write only `review-decision.md`. It must cite packet evidence and choose only `accept`, `return for correction`, or `escalate to human`. Inspect its citations and verify it did not treat Builder rationale as evidence.

### Observer

Give the Observer approved historical run evidence that is either sufficient or deliberately insufficient. It may write only one improvement proposal. If evidence does not meet the course threshold—three comparable documented patterns or one high-severity governed failure—it must return `collect more evidence`. Inspect the evidence window and disposition.

## Boundaries

- A fresh profile, Bot, or subagent conversation is not automatically a filesystem, credential, or tool-permission boundary.
- Do not certify a role based on its chat response alone; inspect its designated repository artifact.
- Human approval is required before enabling consequential actions, promoting durable memory, or changing production skills/contracts.

## Close

State which role was activated, what was directly verified, which limitation remains, and the next role—if any—that the learner has earned.
