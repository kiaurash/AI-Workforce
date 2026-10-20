# M1 — Reusable Artifact Templates

Copy each section into the indicated Markdown file. Replace bracketed placeholders with learner-specific content.

---

# FILE: 01-workforce-blueprint.md

# Provisional AI Workforce Blueprint

Project: [Project name]  
Owner: [Learner]  
Stage: M1 — First working responsibility  
Architecture status: Provisional

## 1. Work Worth Improving

Long-term vision: [Describe the overall opportunity.]

First independently valuable workflow: [Describe one bounded workflow.]

Why it matters: [State the benefit.]

Actual constraint: [What is limiting the work today?]

## 2. First Workflow

Trigger: [...]

Inputs: [...]

Delegated work: [...]

Expected output: [...]

Quality evidence: [...]

Human review: [...]

Out of scope: [...]

## 3. Responsibility Allocation

| Responsibility | Allocation | Reason |
| --- | --- | --- |
| [Responsibility] | Human / Employee / Skill / Tool | [Reason] |

## 4. First Employee

Name: [...]

Mission: [...]

Output: [...]

## 5. Possible Future Employees

| Candidate | Proposed distinct responsibility | Why separation might help | Untested assumption |
| --- | --- | --- | --- |
| [...] | [...] | [...] | [...] |

Additional employee roles are hypotheses, not approved architecture.

## 6. Human Authority

AI may prepare: [...]

Human must approve or decide: [...]

Unauthorized actions: [...]

## 7. Execution Evidence

First output location: [...]

Review location: [...]

Observed limitation: [...]

## 8. M2 Questions

- [...]
- [...]

---

# FILE: employees/first-employee.md

# First Employee Contract

Employee: [Name]  
Contract version: 0.1  
Owner: [Learner]

## Mission

[One bounded outcome.]

## Trigger

[What starts the work?]

## Authorized Inputs

[Files, folders, or explicitly provided information.]

## Permitted Actions

[Specific allowed actions.]

## Prohibited Actions

[Specific forbidden actions.]

## Required Output

File: [outputs/first-run.md]

Format: [Markdown table, report, brief, etc.]

Contents: [Required elements.]

## Evidence Rules

[How claims must be supported.]

## Uncertainty Rules

[What the employee should do when information is missing, disputed, or ambiguous.]

## Human Review and Approval

[What remains provisional until human review.]

## Completion Conditions

[How the participant knows the task has finished.]

## Change History

v0.1: Initial contract.

---

# FILE: inputs/sample-input.md

# Sample Input

Source type: [Transcript / Report / Notes / Research material / Other]

Date or period: [...]

Access authorization: [Fictional / Public / Authorized internal / Anonymized]

## Input Content

[Place a safe representative input here.]

## Learner Notes

[Optional context relevant to evaluating the result.]

---

# FILE: runs/first-run-review.md

# First Run Review

Run ID: M1-001  
Date: [...]  
Builder harness: [...]  
Employee contract version: [...]  
Input path: [...]  
Output path: [...]

## Execution

Was the output file created? Yes / No / Not verified

Evidence source: Direct file inspection / Learner report / Other

Did the agent remain within the stated task? [...]

## Quality Review

Useful or correct elements: [...]

Incorrect or uncertain elements: [...]

Evidence from source: [...]

Failure category: [...]

## Human Intervention

What did I correct or approve? [...]

## Improvement Hypothesis

Proposed change: [...]

Why it might help: [...]

## Retest

Retested? Yes / No

New output path: [...]

Observed result: [...]

Remaining issue: [...]

## Learning Reflection

What did this run teach me about the workflow or its architecture?

[...]

---

# FILE: outputs/first-run.md

This file should be created by the builder agent during M1.

Do not prefill it with a successful-looking response.

The learner should inspect the actual saved result and preserve its evidence for review.