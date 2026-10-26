# AI Workforce Conductor Profile Distribution

This distribution installs one **Conductor** Hermes profile for the AI Workforce course. It intentionally does **not** install a complete multi-profile workforce. The learner creates and activates Builder, Reviewer, and Observer Bots progressively in Hermes Desktop.

## Install

From a local clone of this repository:

```text
hermes profile install <path-to>/hermes-profiles/ai-workforce-conductor
```

From a published distribution repository, use its Git URL with `hermes profile install`.

The installer previews the manifest. Credentials, sessions, memories, and runtime logs are not distributed; each learner authenticates locally.

## Desktop-first setup

1. Open Hermes Desktop and select the installed **AI Workforce Conductor** Bot/profile.
2. Open its canonical Bot Chat.
3. Invoke `/setup-ai-workforce-roles` to create and activate only the roles needed for the learner's current module.
4. Keep the learner's capstone repository open as the project workspace.

## Included skills

- `setup-ai-workforce-roles`: guides Desktop creation and role-activation tests for Builder, Reviewer, and Observer.
- `run-governed-workforce`: coordinates one repository-first Builder → Reviewer run from the Conductor's canonical Bot Chat.

## Evidence rule

Bot messages coordinate asynchronously. Repository artifacts are authoritative. A role is not operational merely because it appears in the Bots tab: it must pass its role-specific activation test and have a recorded human activation decision.
