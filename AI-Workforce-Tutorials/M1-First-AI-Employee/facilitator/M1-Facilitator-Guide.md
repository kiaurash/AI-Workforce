# M1 — Facilitator Guide

Course: Build Your AI Employee Workforce  
Session: M1 — Find the Work, Build the First Employee  
Duration: 60 minutes  
Delivery: Hybrid instructor-led workshop with individual Socratic AI tutors and learner-selected builder harnesses  
Version: 1.0

## Purpose

Participants move from an M0 opportunity hypothesis to a working, bounded AI employee session that produces one reviewable artifact.

The participant should discover the limitations of their initial workflow design through execution, not simply receive an architecture proposed by the tutor.

## Learning outcomes

- **LO-1:** Identify a bounded workflow and justify initial responsibilities.
- **LO-2:** Run a bounded AI employee with an explicit contract.
- **LO-4:** Identify a human approval boundary and restrict permitted actions.
- **LO-8:** Produce, review, and explain a real capstone artifact.

## Anchor question

What is the smallest useful piece of work I can responsibly delegate to an AI employee today?

## Three operating roles

### Facilitator

- Leads demonstrations and group discussions.
- Maintains session time and checkpoints.
- Addresses technical blockers.
- Asks participants to explain what they learned.
- Challenges architecture claims during peer review.

### Socratic AI Tutor

- Uses the participant's M0 Opportunity Map.
- Asks one question at a time.
- Helps identify meaningful value, boundaries, and appropriate delegation.
- Challenges unjustified claims or excessive scope.
- Guides the participant through the workbook.
- Provides progressively stronger help after genuine difficulty.
- Assesses explanation and transfer separately from artifact completion.

### Builder Harness

Codex, Claude Code, or Gemini CLI:

- Opens the learner's actual project workspace.
- Reads the authorized input.
- Carries out the bounded assignment.
- Writes the proposed output.
- Makes any proposed file changes inspectable.

Do not assume the tutor is the builder or that a generated answer in chat is a saved file.

## Preparation

### Learner brings

- M0 Opportunity Map or a bounded workflow idea.
- M0.5 Readiness Report, if completed.
- A functioning supported harness when available.
- One representative input, fictional or appropriately authorized.
- An idea of the desired output.

### Facilitator prepares

- A tested starter workspace.
- A real demonstration of an agent run.
- A deliberately flawed run.
- A corrected run.
- The learner workbook.
- A first employee contract template.
- An execution-review template.
- A facilitator-provided fallback for learners without a working harness.
- A peer-review pairing or round-robin plan.

Do not use real confidential meeting transcripts in the demonstration.

## Before learners begin

Explain the distinction:

The tutor helps you decide what to build. Your chosen agent harness does the actual building. You judge whether its work is acceptable.

If using the same AI product for tutoring and execution, prefer separate conversations or sessions with clearly different instructions and purposes.

## Minute-by-minute session plan

### 0–5 — Opening: What outcome matters?

Facilitator prompt:

"What is the one useful artifact you hope your AI employee will produce today?"

Participants use their M0 maps or a specific workflow idea.

The tutor helps narrow the answer to one observable deliverable.

Examples:

- A meeting commitment register.
- A concise competitor research brief with citations.
- A draft project-status report.
- A collection of research evidence.
- A proposal-preparation outline.

Do not accept an entire AI department as a first-session deliverable.

Checkpoint: One output described in a sentence.

### 5–11 — Practitioner demonstration and failure

Demonstrate the Meeting Commitment Extractor supplied in the demo materials.

Show:

1. A real input transcript.
2. An intentionally insufficient employee instruction.
3. A plausible but incorrect output.
4. The source evidence contradicting that output.
5. A revised instruction that requires evidence and uncertainty handling.
6. A corrected output.

Ask:

"What evidence makes something a confirmed commitment rather than an attractive suggestion?"

Checkpoint: Participants can identify why the initial result was wrong.

### 11–17 — Autonomy ladder and responsibility

Teach the five modes:

1. Prompt — a guided task.
2. Skill — a reusable procedure.
3. Bounded employee — delegated responsibility with context and limits.
4. Workforce — collaboration among justified specialists.
5. Recurring governed operation — trigger-based execution with oversight.

Clarify that these are not mandatory sequential levels and that specialization is separate from autonomy.

Ask:

"What would another AI employee accomplish that a good skill within one employee could not?"

Checkpoint: Participants can give at least one valid reason for specialization or explain why it is premature.

### 17–25 — Bound the learner's workflow

Learners complete the Workflow Card with their tutor.

Required:

- Trigger.
- Input.
- One responsibility to delegate.
- Output.
- Evidence or acceptance criteria.
- Human review point.
- Out-of-scope activities.

Socratic challenge:

"Would this output be independently valuable if we never built the rest of your proposed workforce?"

If no, narrow the workflow.

Facilitator intervention:

Help learners whose input access is blocked, whose project includes sensitive people judgments, or whose first slice is still too large.

Checkpoint: The workflow can be executed and reviewed within the remaining session.

### 25–39 — Build and run

Participants customize the First Employee Contract.

The AI tutor guides contract reasoning; the builder harness executes the task.

Minimum contract:

- Mission.
- Authorized inputs.
- Allowed actions.
- Disallowed actions.
- Required output and file path.
- Evidence requirements.
- Handling of unknowns.
- Human approval boundary.
- Completion criteria.

Learners run their agent session on one actual or representative input.

The output must be saved to the project.

Facilitator circulates and deals with actual blockers.

Checkpoint: A saved output exists, or a specific execution blocker is recorded.

### 39–47 — Inspect and correct

Learners open the saved artifact and compare it with source material.

Ask:

"What did the agent get wrong, miss, or state without sufficient evidence?"

Select one substantial defect or uncertainty.

If the first run appears correct, use an edge case or ambiguous input. Do not invent a failure.

Revise one element of the contract and rerun when feasible.

Record the actual outcome.

Checkpoint: A Run Review showing observed evidence and at least one improvement hypothesis.

### 47–54 — Provisional architecture

Use the first run to create a Responsibility Map.

The learner distinguishes:

- Human decisions.
- Employee responsibilities.
- Repeatable skills.
- Tools.
- Potential additional employees.

A second employee must be justified by a specific separation benefit such as distinct context, permission, expertise, parallelism, or independent verification.

Do not encourage agent proliferation.

Checkpoint: A provisional Workforce Blueprint with explicit unresolved questions.

### 54–60 — Peer clinic and reflection

In pairs or a short round-robin, each participant reports:

- What artifact was created?
- What was done well?
- What went wrong or remains uncertain?
- What is the next smallest improvement?

Peer challenge:

"What's your strongest evidence that this AI employee is useful?"

Final tutor prompt:

"What did running this employee reveal about the workflow that you hadn't understood before?"

Ask each learner to write a summary before completing M1.

Checkpoint: Reflection and M2 priorities recorded.

## Adaptive timing rules

The facilitator should prioritize:

1. Bounded workflow.
2. Working output.
3. Human inspection.
4. Recorded uncertainty or correction.
5. Architecture reflection.

If time is short, simplify the org-chart discussion.

Do not skip output review merely to finish the blueprint.

Participants still completing setup may use the facilitator's tested example, but should independently complete M0.5 and a first run before starting the M2 build.

## Socratic facilitation rules

Challenge only when warranted:

- Unclear value.
- Overly broad scope.
- Premature multi-agent design.
- Undefined output.
- Unsupported assumption.
- Missing human authority.
- Risky or sensitive data use.
- Unobservable correctness.

Do not oppose ideas simply to make the session seem Socratic.

Acknowledge sound reasoning, ask for evidence when necessary, and move forward.

## Troubleshooting

### Learner has no working harness

Use facilitator's demo environment for the exercise. Record that personal execution remains incomplete.

### Learner's project is too large

Ask for the smallest independently useful output.

### Learner has no sample input

Use a fictional course input or construct a safe representative case.

### Agent outputs text but not a file

Return to the builder environment and request the designated output file. Verify its existence.

### Agent produces a plausible but incorrect answer

Ask the learner to identify the unsupported claim before revising instructions.

### Learner cannot explain the architecture

Use one counterexample: "What happens if we combine these two responsibilities in one agent?"

### Learner is stuck after two questions

Reframe, narrow the problem, give a partial example, then a worked example if needed. Follow with a new analogous unaided task.

## End-of-session evaluation

Collect:

- Workflow Card.
- Saved output or blocker.
- First Employee Contract.
- Run Review.
- Provisional Workforce Blueprint.
- Learner reflection.

Mark completion and mastery separately.

Artifact creation alone does not establish independent understanding.

## M2 handoff

The learner should enter M2 knowing:

- Which responsibility the existing employee performs.
- What was difficult or unreliable.
- Which procedures might become skills.
- What additional specialization, if any, has a credible justification.
- What context and tool access the employee needs.

M2 begins by improving an existing working capability, not by inventing an org chart from scratch.