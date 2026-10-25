# Hermes Desktop Course Redesign — Confirmed Direction

## Status

Confirmed by the course sponsor on 2026-10-25. This decision record guides the revision of the AI Workforce course and its tutorial materials.

## Platform model

Hermes Desktop is the strongly preferred learner environment and the primary environment for demonstrations, templates, and readiness checks.

Learners may instead use Codex or Claude when their circumstances require it. Those environments are supported adapters, not the reference implementation. An adapter must preserve the same learning evidence, bounded authority model, durable handoffs, and human approvals.

## Learner setup

Each learner installs and uses Hermes Desktop on their own machine. M0.5 must therefore validate an individual learner's actual local environment rather than treating a facilitator demonstration as evidence of readiness.

## Capstone model

Each learner builds a workforce for the workflow selected in M0, the AI Workforce Opportunity Map discovery process. The course will not require a common capstone workflow.

Shared examples may be used for demonstrations and troubleshooting, but learners must transfer the method to their own selected workflow from M1 onward.

## Three-role Hermes backbone

The core learning environment uses bounded roles with durable, reviewable artifacts:

| Role | Primary authority | Required artifact |
|---|---|---|
| Default / orchestrator-reviewer | Coordinate work, inspect handoffs, request and record human decisions | Review and approval record |
| Research analyst | Gather evidence and draft a cited research brief using its assigned NotebookLM workflow | Cited evidence brief |
| Course designer | Transform approved evidence and learner requirements into instructional artifacts | Course or learning-workflow artifact |

Profiles are isolated workspaces. Learners must verify the active profile before each run. They must not assume that sessions, skills, memory, connections, permissions, or access available to one role exist in another.

## M0.5 operational readiness gate

A learner is ready for M1 only when they can provide evidence of all of the following:

1. Each role's named active profile has been verified.
2. Each role can access its designated workspace.
3. The research role has demonstrated its assigned source-access path, including NotebookLM where that role is part of the learner's workflow.
4. The research role saved a cited evidence brief to the designated handoff location.
5. The orchestrator reviewed the brief and recorded an explicit human approval decision.
6. The designer produced an artifact using only the approved evidence brief and named learner requirements.
7. The learner inspected the resulting files and confirmed no unauthorized external action occurred.

A learner who cannot demonstrate their own research-source access may observe the facilitator path and use a supplied approved brief, but is provisionally ready rather than fully ready for a research-enabled workforce.

## Role and authority boundaries

- Default may coordinate and review, but does not silently authorize consequential external actions.
- Research gathers evidence and writes drafts; it does not publish, message external parties, alter authoritative records, or approve its own work.
- Design produces learning artifacts from approved inputs; it does not treat unapproved drafts as evidence.
- External publishing, messaging, and authoritative-record changes remain outside the core path unless the learner implements and demonstrates an explicit human approval gate.

## Durable project artifacts

The project workspace must contain and preserve:

- role contracts;
- defined output locations;
- a handoff template with source references, status, uncertainties, and approval state;
- approval criteria and decision records; and
- learner-visible execution and review evidence.

Conversational context alone is not an acceptable handoff or approval mechanism.

## Open research dependency

The NotebookLM-backed research brief will be incorporated before the revised module sequence is finalized. It must identify source-grounded constraints on role separation, handoff/provenance, citation practices, and learner-facing risks.
