# M1 — Package README

## Package title

M1 — Find the Work, Build the First Employee

Version 1.0

## Entry Ramp v1 status

This package is governed by the [M1 Entry Ramp v1 Retrofit](ENTRY-RAMP-V1-RETROFIT.md), which establishes the Hermes Desktop/Conductor reference path, exact evidence-map paths, cohort-one draft/proposal boundary, and required manual practice run. Use that addendum before distributing any older M1 worksheet, guide, skill, demo, or template.

## Intended folder structure

```text
M1-First-AI-Employee/
├── README.md
├── facilitator/
│   └── M1-Facilitator-Guide.md
├── skills/
│   └── m1-first-ai-employee-socratic-tutor/
│       └── SKILL.md
├── demo/
│   └── M1-Practitioner-Demo.md
├── learner/
│   └── M1-Workbook.md
├── templates/
│   └── M1-Artifact-Templates.md
└── assessment/
    └── M1-Mastery-Rubric.md
```

## Required companion materials

- M0 AI Workforce Opportunity Map, when available.
- M0.5 Workspace Readiness Report.
- M0.5 sample meeting transcript.
- A supported and tested AI agent environment.

## How to use the materials

### Facilitator

Read the Facilitator Guide.

Prepare the live demonstration, including the actual first-run failure and corrected run.

Confirm that a functional fallback workspace is available.

Distribute the learner workbook and templates.

Lead the group through the timed phases.

### Individual learner

Open a separate AI conversation or activate the M1 Socratic Tutor skill.

Share the relevant M0 Opportunity Map or describe the selected workflow.

Follow one question at a time.

Use the builder harness for actual file operations.

Record results in the workbook and run review.

### Builder harness

Open the learner's working project.

Read the learner's First Employee Contract.

Execute only its authorized task.

Write the required output file.

Stop for human review.

## Important operating distinction

The Socratic Tutor and the builder agent must not be treated as the same logical role.

The tutor helps the learner understand, reason, and evaluate.

The builder agent performs the work.

A learner may use the same underlying AI platform for both, but preferably in separate conversations or sessions.

## Installation and invocation

The tutor skill uses standard YAML frontmatter and a SKILL.md structure.

For a platform with native Agent Skills support, install the skill in its documented skill location and confirm discovery/activation.

Otherwise the facilitator may provide the full tutor instructions in a dedicated AI conversation.

Platform-specific installation and feature support must be verified before class.

## M1 classroom readiness

Before the workshop, confirm:

- The starter input exists.
- The default demonstration harness can open the input.
- The output folder is writable.
- The failed example is clearly identified as illustrative or genuinely observed.
- The corrected example has been tested.
- The peer review format is practical for the group size.
- The facilitator can assist learners who encounter setup problems.

## Session success

Prepared participants should leave with:

1. One bounded workflow.
2. One first employee contract.
3. One actual saved output.
4. One execution review.
5. One provisional architecture.
6. One learner reflection.

Learners who need setup support may complete personal execution after class and before M2.

## Important limitations

The tutor cannot assume the learner's local files are accessible.

The facilitator should not report a demo as tested until it has been run.

An instruction file is not a deterministic security mechanism.

A successful first run does not prove production reliability.

The M1 objective is a bounded learning milestone, not deployment of an autonomous production system.

## M2 handoff

Bring:

- First Employee Contract.
- First-run output.
- Run Review.
- Workforce Blueprint.
- Observed failure or uncertainty.
- Question about specialization or reusable skills.

M2 should build on the actual M1 evidence rather than restarting architectural discovery.