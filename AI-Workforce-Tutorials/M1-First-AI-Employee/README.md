# M1 — Package README

## Package title

M1 — Find the Work, Build the First Employee, and Draft the Workforce Blueprint

Version 2.0 (Hermes Desktop reference path; harness-neutral concepts)

## What M1 teaches

M1 teaches a learner to delegate one bounded piece of real work to an AI employee, verify what actually happened, and then use that evidence to decide what should become an employee, a skill, a tool, or a human responsibility.

The module has two anchor questions.

- **Primary anchor:** What is the smallest useful piece of work I can responsibly delegate to an AI employee today?
- **Blueprint anchor:** What should become an AI employee, what should remain a skill or tool, and what should stay under human control?

The learner answers the primary question by running a Builder task. The learner answers the Blueprint anchor afterward, for the same workflow, using the evidence from that run.

## Sequencing decision: build first, then architect

An earlier proposal for this module (the "Architect Your AI Workforce" design) taught architecture before any run. The course design (`Course.md` v4.0) says the opposite: learners build early, start with one bounded capability, and earn specialization from evidence. This package follows the course design and folds the architecture tools into the part of the session that comes after the first run.

| Architecture tool | Where it now lives |
| --- | --- |
| Opening challenge ("five free employees") | Prediction recorded in minutes 7–12; revisited at the explain-back in minutes 55–60 |
| First Workforce Test | Workflow-bounding step, minutes 12–18 |
| Outcome-based decomposition (trigger → inputs → responsibilities → decisions → deliverable) | Workflow Card, minutes 12–18; Blueprint Studio Part A |
| Four-Bucket Test (employee / skill / tool / human) | Blueprint Lite, minutes 38–45, on the learner's own run |
| Topology choice | Blueprint Lite default (single bounded employee); Blueprint Studio Part B |
| Candidate roles and the "disappearing employee" test | Blueprint Studio Part C |
| Authority map (A / R / P / X) | Blueprint Lite, minutes 38–45 |
| Architecture stress test | Blueprint Studio Part D |
| Explain-back and transfer | Minutes 55–60 and the mastery check |

## Folder structure

```text
M1-First-AI-Employee/
├── README.md
├── ENTRY-RAMP-V1-RETROFIT.md
├── facilitator/
│   └── M1-Facilitator-Guide.md
├── learner/
│   └── M1-Workbook.md
├── templates/
│   └── M1-Artifact-Templates.md
├── demo/
│   ├── M1-Practitioner-Demo.md
│   ├── M1-Worked-Example-Workforce.md
│   └── fixtures/
│       └── m1-demo-meeting.md
├── assessment/
│   └── M1-Mastery-Rubric.md
└── skills/
    └── m1-first-ai-employee-socratic-tutor/
        ├── SKILL.md
        └── references/
            ├── m1-contract-field-guide.md
            ├── m1-misconception-map.md
            └── m1-diagnostic.md
```

The Conductor profile carries the runtime copy of the tutor at `hermes-profiles/ai-workforce-conductor/skills/m1-first-ai-employee-tutor/`. The three `references/` files in the package are canonical. When either changes, update the Conductor copy in the same commit.

## The 60-minute shape

The session follows the course-wide pattern: 7 minutes of demonstration, 5 minutes of retrieval, 33 minutes of guided work, 10 minutes of peer clinic, and 5 minutes of reflection.

| Minutes | Segment | Output |
| --- | --- | --- |
| 0–7 | Practitioner demonstration with a planted failure | Learners can say why the first result was wrong |
| 7–12 | Retrieval and prediction | Pre-registered headcount prediction; one-sentence target output |
| 12–18 | Bound the workflow | First Workforce Test; Workflow Card |
| 18–25 | First Employee Contract | `employees/first-employee.md` |
| 25–32 | Build and run | `outputs/first-proposal.md`, `runs/m1-first-run-receipt.md`, `runs/m1-workshop-manifest.md` |
| 32–38 | Inspect and correct | `runs/m1-first-run-review.md` |
| 38–45 | Blueprint Lite | `01-workforce-blueprint.md` |
| 45–55 | Peer clinic | One challenge received and one decision reconsidered |
| 55–60 | Explain-back, reflection, practice-run handoff | Revised headcount answer; next action |

## Evidence map

All paths follow the Entry Ramp v1 evidence map. Repository artifacts are authoritative; chat claims are not proof.

```text
ai-workforce/
├── 01-workforce-blueprint.md
├── employees/first-employee.md
├── inputs/representative-input.md
├── outputs/first-proposal.md
├── runs/
│   ├── m1-workshop-manifest.md      (run_type: workshop)
│   ├── m1-first-run-receipt.md
│   ├── m1-first-run-review.md
│   ├── value-checkpoint.md
│   └── m1-practice-manifest.md      (run_type: practice)
├── learning/learning-record.md      (written by the Tutor only)
└── governance/cohort-one-action-boundary.md
```

## Required companion materials

- M0 `discovery/opportunity-map.md` and `discovery/workflow-safety-triage.md`.
- M0.5 readiness evidence (Gate A and Gate B) and the imported Conductor profile.
- One safe, authorized representative input saved at `inputs/representative-input.md`.
- The Entry Ramp starter workspace or a tested fallback.

## How to use the materials

### Facilitator

1. Read the Facilitator Guide, then the Demonstration and Worked Example.
2. Run the demonstration yourself before class and record the real first-run output, the real corrected output, and what did not improve. The failed output printed in the demo file is illustrative until you replace it with your own record.
3. Confirm a working Conductor workspace or a tested fallback for each learner.
4. Distribute the Workbook and Templates.

### Individual learner

Open the AI Workforce Conductor's canonical Bot Chat. The M1 tutor skill starts with a short diagnostic, then guides the workbook one question at a time. The Builder action starts only after you approve the contract and file paths.

### Builder

The Builder reads only its own contract (`employees/first-employee.md`, read-only) and `inputs/representative-input.md`, writes only `outputs/first-proposal.md` and `runs/m1-first-run-receipt.md`, updates the workshop manifest, and stops for human review.

## Important operating distinction

The Socratic tutor and the Builder are different logical roles even when they run on the same platform. The tutor helps the learner reason and evaluate. The Builder performs the bounded work. Use separate conversations or clearly separated sessions, and label every Builder instruction as such.

## Before the session

Each learner completes the 3–4 minute intake diagnostic with the M1 tutor before the workshop (`skills/.../references/m1-diagnostic.md`). It records which design beliefs the learner already holds so the tutor can ask the right prediction questions later. It is not graded.

## Between-session work

1. **Manual practice run (required, 15–30 minutes).** Complete `runs/m1-practice-manifest.md` with `run_type: practice`. Status is `complete`, `blocked`, or `needs catch-up`. A blocked learner submits the manifest, direct blocker evidence, and one attempted recovery step.
2. **Blueprint Studio (recommended, about 25 minutes).** Expand the Blueprint Lite into a fuller architecture decision: topology comparison, candidate-role tests, stress test, and a revised headcount answer. It is described in the Workbook and Templates. A missing Studio does not block M2; the gap is recorded and M2 opens with a five-minute review.

Do not build any new employee or specialist Bot between sessions. Specialization is earned in M2 and M3.

## Session success

A prepared learner leaves with:

1. one bounded workflow;
2. one first employee contract;
3. one saved output and receipt, verified by direct inspection;
4. one run review with an observed limitation;
5. one Blueprint Lite with an authority map and a topology decision; and
6. one revised answer to the opening headcount prediction, with reasons.

## Important limitations

- The tutor cannot assume the learner's local files are accessible.
- A demo is not "tested" until the facilitator has run it and recorded the result.
- An instruction file is not a deterministic security mechanism. Technical enforcement of the authority map belongs to M4.
- A successful first run is one observation, not evidence of production reliability.
- Evidence behind the architecture guidance is practitioner synthesis drawn mostly from software-engineering contexts. See the "Evidence and limits" section of the Facilitator Guide.
- M1 is a bounded learning milestone, not deployment of an autonomous production system.

## M2 handoff

The learner brings the contract, output, receipt, run review, Blueprint Lite (and Studio, if done), the observed limitation, and one question about reusable skills or specialization. M2 builds on this evidence instead of restarting architectural discovery.
