# M1 — Mastery and Completion Rubric

## Purpose

Evaluate the learner's demonstrated ability to define, run, inspect, and explain a bounded AI employee, and to decide from run evidence what should be an employee, a skill, a tool, or a human responsibility.

Artifact completion and conceptual mastery are evaluated separately.

## Competencies

### C1 — Workflow value and scope

The learner can identify an independently useful workflow, its input, trigger, output, and intended human benefit.

### C2 — Employee versus skill versus tool

The learner can explain when a responsibility deserves a bounded employee and when a simpler skill or tool is sufficient.

### C3 — Bounded employee design

The learner can specify authorized inputs, allowed actions, output requirements, uncertainty behavior, and human review.

### C4 — Evidence-based execution review

The learner can inspect a saved artifact, compare it with its source, recognize a material error or ambiguity, and propose a targeted correction.

### C5 — Provisional architecture and authority

The learner can defend an initial human/employee/skill/tool allocation, an A/R/P/X authority map, and a starting topology, and can identify what is still untested. Each kept role is justified by a specific separation benefit (responsibility, context, expertise, permissions, verification, or parallelism), not by "it is another step".

## Four mastery levels

| Level | Meaning | Evidence |
| --- | --- | --- |
| 0 | Not demonstrated | Unable to perform or explain |
| 1 | Emerging | Recognizes concepts but needs substantial guidance |
| 2 | Assisted application | Can handle familiar case with hints or examples |
| 3 | Independent transfer | Explains unaided and applies the concept to a new case |

Do not award Level 3 merely for producing the correct document.

## Minimum artifact requirements

For a prepared learner:

- A bounded Workflow Card.
- `employees/first-employee.md`.
- `outputs/first-proposal.md` and `runs/m1-first-run-receipt.md`.
- `runs/m1-first-run-review.md`.
- `01-workforce-blueprint.md` (Lite: responsibility sort, authority map, topology).
- The opening headcount prediction and the learner's revised answer.
- A short reflection.

If a learner is blocked by environment setup, record what was actually accomplished and what remains incomplete.

## Diagnostic prompts

Use one at a time as appropriate, preferably after the relevant concept.

### Diagnostic A — Scope

A manager wants an AI workforce to monitor customer complaints, evaluate employee performance, send customer replies, update policies, and coordinate the department.

Question:

"What is one useful first workflow you could test without automating all these responsibilities?"

Evidence of understanding:

The learner chooses one bounded trigger-to-output workflow with explicit human oversight.

### Diagnostic B — Employee versus skill

A workflow extracts three fields from the same kind of report every week.

Question:

"Why might this be better represented as a reusable skill than a separate AI employee?"

Evidence of understanding:

The learner identifies repeatable procedure versus distinct delegated responsibility.

### Diagnostic C — Human authority

An agent drafts a sensitive customer response and proposes issuing a refund.

Question:

"What can it prepare, and what should require human authorization?"

Evidence of understanding:

The learner separates drafting/recommendation from consequential execution.

### Diagnostic D — Evidence review

An agent includes a plausible recommendation that does not appear in its source.

Question:

"How would you determine whether the recommendation is supported?"

Evidence of understanding:

The learner traces the claim back to source evidence and acknowledges uncertainty.

## Transfer tasks

Select one new scenario different from the learner's first exercise.

### Transfer Case 1 — Research brief

A research agent finds three articles but one is outdated and another contradicts the others.

Ask:

"How should the employee contract require the agent to represent that uncertainty, and what remains for the human to decide?"

### Transfer Case 2 — Action register

A transcript says a task "could be done next week" but no owner volunteers.

Ask:

"How would you require the employee to represent this statement?"

### Transfer Case 3 — Multiple agents

A learner proposes a Researcher, Summarizer, Rewriter, Formatter, Reviewer, and Manager for a one-page weekly brief.

Ask:

"Which responsibilities could be combined or treated as skills, and what evidence would justify separating any of them?"

### Transfer Case 4 — Tool permission

An employee can read local documents and draft updates, but requests permission to email an external client.

Ask:

"What should happen, and how would you express the boundary in the contract?"

### Transfer Case 5 — Four-Bucket sort on a new workflow

A learner who ran a meeting-commitment extractor now plans a weekly customer-feedback digest: read the export, group comments by theme, score each theme's severity with a standard rubric, write the digest in the house format, and decide which themes go to the product team.

Ask:

"Which of these responsibilities are employee, skill, tool, or human, and what is your reason for each?"

Defensible: reading is a tool; grouping with judgment may be the employee's owned responsibility; the severity rubric and house format are skills; deciding what goes to the product team is human. The scoring question is the reasoning, not a match to this answer.

### Transfer Case 6 — Authority and topology

The digest workflow adds a request: "Post the digest to the team channel each Monday and open tickets for the top three themes."

Ask:

"What A/R/P/X label does each action get in cohort one, what does the map not do, and what topology would you start with and why?"

Defensible: posting and ticket creation are X in cohort one (the human does them outside the workflow) or P in a later, separately controlled setting; the map is architectural, not enforcement; start with a single bounded employee and name the evidence that would justify a Reviewer.

## Assessment method

1. Ask the learner for an unaided explanation.
2. Inspect the answer for reasoning, not just correct terminology.
3. Present one new case.
4. Ask the learner to apply the relevant principle.
5. Record exact or concise quoted evidence of their reasoning.
6. Note unresolved gaps.

If a learner needs a worked example, return to a new transfer case after the example.

## Learning Record

Learner:  
Date:  
Workflow:  
Builder path (Conductor workspace / other):  
Headcount prediction → revised answer:  

| Competency | Level 0–3 | Evidence | Remaining gap |
| --- | --- | --- | --- |
| C1 Scope/value |   |   |   |
| C2 Employee/skill/tool |   |   |   |
| C3 Employee contract |   |   |   |
| C4 Evidence review |   |   |   |
| C5 Architecture and authority |   |   |   |

Execution status: Completed / Partial / Blocked / Unverified

Artifact location: [...]

Intake diagnostic (learner's own record, `tier-3d`): [distractors chosen and confidence, from `runs/m1-first-run-review.md`]

Summary given by learner: [...]

M2 preparation: [...]

## Recommended follow-up

Before M2, ask the learner to explain the hardest distinction they encountered without reopening their worked example.

At the beginning of M2, revisit one unresolved misconception or design uncertainty before introducing additional employee roles.

## Mastery standard

Level 3 requires:

- An unaided explanation.
- Successful application to a new case.
- Reasoning consistent with the evidence.

A runnable employee is an implementation achievement. Independent explanation plus transfer is a learning achievement.

Both matter.