# M1 — Reusable Artifact Templates

Copy each section into the indicated Markdown file in the learner's `ai-workforce/` repository. Replace bracketed placeholders. Write `unknown` where information is missing; do not guess.

Repository artifacts are the evidence of completion. A chat message is not.

---

# FILE: governance/cohort-one-action-boundary.md

(The Entry Ramp starter workspace supplies this file. Complete it before the Builder runs.)

```markdown
# Cohort-One Action Boundary

Workflow: [name]

The Builder may read: [employees/first-employee.md (read-only) and the representative input path]

The Builder may write: [exact paths: proposal and receipt only]

The Builder must not: [send, publish, purchase, update authoritative records, use external systems, edit sources]

Human-only actions: [list]

Approval required before any later execution: [list]
```

---

# FILE: employees/first-employee.md

```markdown
# First Employee Contract

Employee: [Name]
Contract version: 0.1
Owner: [Learner]

## Mission
[One bounded outcome.]

## Trigger
[What starts the work?]

## Authorized input
[Exact paths: employees/first-employee.md (this contract, read-only) and inputs/representative-input.md]

## Permitted actions
[Read this contract and the authorized input. Write the proposal and the receipt.]

## Prohibited actions
[Edit sources or this contract. Contact anyone. Use external systems. Update authoritative records. Invent facts.]

## Required output
File: outputs/first-proposal.md
Format: [table / brief / outline]
Contents: [required elements]

## Evidence rules
[How each claim must be supported: quotation, location.]

## Uncertainty rules
[Missing or ambiguous information is marked `unknown`; conditional or unassigned items are kept separate.]

## Human review and approval
[What stays provisional until a human reviews it. Cohort one: no live external execution.]

## Completion conditions
[How the learner knows the task has finished.]

## Change history
v0.1: Initial contract.
```

---

# FILE: runs/m1-workshop-manifest.md

Use the Conductor's run manifest template and set `Run type: workshop`.

```markdown
# Governed Workforce Run Manifest

Run ID: [YYYYMMDD-m1-workshop-001]
Run type: workshop
Requested by: [human]
Workflow: [name]
Status: [draft / builder-active / awaiting-human-approval / complete / blocked / needs catch-up]

## Paths
Contract: employees/first-employee.md
Input: inputs/representative-input.md
Builder proposal: outputs/first-proposal.md
Builder receipt: runs/m1-first-run-receipt.md

## Completion gates (workshop)
- [ ] Contract and designated input are recorded.
- [ ] Proposal and receipt are saved.
- [ ] Learner opened the output and recorded evidence or a limitation.

## Coordination log
[Message delivery IDs or notices. These are not completion evidence.]
```

---

# FILE: runs/m1-first-run-receipt.md

The **Builder** writes this file. The learner does not prefill it. Everything in it is the Builder's own account until the learner verifies it.

```markdown
# M1 First Run Receipt

Run ID: [matches the manifest]
Contract version: [...]
Input read: [exact path]
Files written: [exact paths]
Actions taken: [list]
Information marked unknown: [list]
Anything skipped or not attempted: [list]
Stopped for human review: Yes / No

Builder's stated limitations (unverified): [...]
```

---

# FILE: runs/m1-first-run-review.md

```markdown
# M1 First Run Review

Run ID: [...]
Date: [...]
Contract version: [...]
Input path: [...]
Output path: [...]

## Execution
Output file exists: Yes / No / Not verified
Evidence source: Direct file inspection / Learner report / Other
Builder stayed within contract: [...]

## Quality review
Correct or useful elements: [...]
Incorrect, unsupported, or uncertain elements: [...]
Source evidence (quote or location): [...]
Failure category: Factual / Unsupported inference / Omission / Format / Tool failure / Scope / Approval / Other

## Human intervention
What I corrected or approved: [...]

## Improvement hypothesis
Proposed change: [...]
Why it might help: [...]

## Retest
Retested: Yes / No
New output path: [...]
Observed result: [...]
Remaining issue: [...]

## Learning record
Diagnostic results (tier-3d, from this learner's own answers): [item → what the learner chose → misconception id, if any]
Mastery evidence: [independent / assisted / not demonstrated / untested, per competency]
Explain-back: [learner's own words]
Transfer case and response: [...]
Remaining gaps: [...]
```

---

# FILE: 01-workforce-blueprint.md

Start with the Lite sections. Add the Studio sections between sessions.

```markdown
# AI Workforce Blueprint

Workflow: [...]
Trigger: [...]
Desired outcome: [...]
Primary deliverable: [...]
Human owner: [...]
Stage: M1 [Lite / Studio]
Architecture status: Provisional

## 1. Responsibility sort (Lite)
| Responsibility | Employee | Skill | Tool | Human | Why |
| --- | --- | --- | --- | --- | --- |
| [...] | | | | | |

Disappearing-employee test for any extra employee I considered: [...]

## 2. Authority map (Lite)
Architectural map only. Technical enforcement begins in M4.

| Responsibility | A / R / P / X | Reason |
| --- | --- | --- |
| [...] | | |

A = autonomous inside designated paths. R = reviewed before reliance. P = explicit approval each time (not enabled in cohort one). X = prohibited; the human acts outside the workflow.

Most consequential action and who holds authority: [...]

## 3. Topology (Lite)
Starting topology: Single bounded employee / Manager–Worker / Sequential / Peer-blackboard / Hybrid
Why, in one sentence: [...]
Evidence that would make me change it: [...]

## 4. Skills needed
1. [...]
2. [...]

## 5. Tools needed
1. [...]
2. [...]

## 6. Human-held decisions
1. [...]
2. [...]

## 7. Initial success measures
1. [...]
2. [...]

## 8. Unresolved questions for M2
- [...]

---
## Studio additions (between sessions)

## 9. Whole-workflow decomposition
Trigger → Inputs → Responsibilities → Decisions → Deliverable: [...]
Candidate boundaries (different context, judgment, tools, or authority): [...]

## 10. Topology comparison
Workflow character: predictable and linear / adaptive but centrally coordinated / exploratory and collaborative
Chosen topology and reason: [...]

## 11. Candidate roles (hypotheses; zero to four)
| Candidate | Owns | Separation benefit | Disappearing-employee test | Earned in |
| --- | --- | --- | --- | --- |
| [...] | | | | M2 / M3 / M6 / not in course |

One sentence per kept employee: "This employee owns the outcome of ___."

## 12. Stress test (revise once)
1. Redundancy: [...]
2. Missing ownership: [...]
3. Context overlap: [...]
4. Tool boundary: [...]
5. Human boundary: [...]
Revisions made: [...]

## 13. Headcount answer
Original prediction: [number and reason]
Revised answer: [number and reason for each role]
```

---

# FILE: runs/m1-practice-manifest.md

```markdown
# Governed Workforce Run Manifest

Run ID: [YYYYMMDD-m1-practice-001]
Run type: practice
Requested by: [human]
Workflow: [name]
Status: [complete / blocked / needs catch-up]

## Paths
Contract: employees/first-employee.md
Input: [inputs/... a second representative input, if available]
Builder proposal: [outputs/... path]
Builder receipt: [runs/... path]

## Practice checklist
- [ ] Reused the contract, manifest, receipt, and review artifacts.
- [ ] Opened the output and recorded what I saw.
- [ ] Status is complete, blocked, or needs catch-up.

## If blocked or needs catch-up (minimum viable submission)
Direct blocker evidence: [file path, error text, or what I observed]
One attempted recovery step and its result: [...]

## Coordination log
[Notices only; not completion evidence.]
```

---

# OPTIONAL: Workflow Candidate Scorecard (use only if unsure which M0 workflow to start with)

Score each 1–5.

| Criterion | Workflow A | Workflow B | Workflow C |
| --- | --- | --- | --- |
| Repeats frequently |  |  |  |
| Business value |  |  |  |
| Can define a good output |  |  |  |
| Contains separable responsibilities |  |  |  |
| Data and tools are accessible |  |  |  |
| Errors are recoverable |  |  |  |
| Human approval points are identifiable |  |  |  |
| **Total** |  |  |  |

Choose one. Then check it against `discovery/workflow-safety-triage.md` before the Builder runs. If a workflow scores high on value but its errors are not recoverable, narrow it to a draft-only slice.

---

# FILE: inputs/representative-input.md

The Entry Ramp starter workspace supplies this file. Replace the placeholder with one safe, authorized representative input. Do not paste secrets, credentials, or unauthorized personal data.

---

# FILE: outputs/first-proposal.md

The Builder creates this file during M1. Do not prefill it with a successful-looking response. The learner inspects the actual saved result and preserves its evidence in the run review.
