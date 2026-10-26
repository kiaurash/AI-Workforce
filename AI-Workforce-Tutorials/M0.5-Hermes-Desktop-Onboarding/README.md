# M0.5 — Hermes Desktop Onboarding

## Purpose

M0.5 verifies two separate capabilities before M1:

- **Gate A — Desktop and repository readiness:** Hermes Desktop can read a designated local file, write a constrained output, and leave source material unchanged.
- **Gate B — Conductor distribution readiness:** the imported Conductor profile creates a run manifest and stops safely when an expected downstream artifact is absent.

Passing one gate does not pass the other. A working chat is not proof of a working workspace, and an installed profile is not proof of an operational role.

## Learner materials

- [M0.5 Learner Workbook](learner/M0.5-Workbook.md)
- [Starter workspace](starter-workspace/README.md)
- [AI Workforce Conductor distribution](../../hermes-profiles/ai-workforce-conductor/README.md)

## Facilitation rule

Use the Windows-first Hermes Desktop path as the reference implementation. Claude/Codex adaptations may be offered later, but they must meet the same two gates and leave the same inspectable repository evidence.

## Completion evidence

Each learner leaves M0.5 with:

1. `starter-workspace/outputs/commitments.md`, directly inspected against the source transcript;
2. a completed readiness table in the workbook;
3. a Conductor activation entry in `profiles/role-activation-log.md`; and
4. a blocked run manifest that proves the Conductor did not invent a missing downstream artifact.

The learner does not create Builder, Reviewer, or Observer Bots during M0.5. Those roles are earned and activated progressively in later modules.
