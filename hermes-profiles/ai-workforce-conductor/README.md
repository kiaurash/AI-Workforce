# AI Workforce Conductor Profile Distribution

This distribution installs one **Conductor** Hermes profile for the AI Workforce course. It intentionally does **not** install a complete multi-profile workforce. The learner creates and activates Builder, Reviewer, and Observer Bots progressively in Hermes Desktop.

## Get the distribution onto your machine

`hermes profile install` only works from a local directory containing
`distribution.yaml` at its root, or a git repository whose **root** has one. This
repository hosts several distributions in subfolders, so there is no single-command
"install straight from the repo" option — clone it first, then install from the local
path:

```text
git clone https://github.com/kiaurash/AI-Workforce.git
hermes profile install AI-Workforce/hermes-profiles/ai-workforce-conductor
```

(Replace the path with wherever you cloned the repo.) The installer previews the
manifest before creating anything.

## Install

From a local clone of this repository:

```text
git clone https://github.com/kiaurash/AI-Workforce.git
hermes profile install AI-Workforce/hermes-profiles/ai-workforce-conductor
```

From a published distribution repository, use its Git URL with `hermes profile
install` — but only if `distribution.yaml` sits at that repository's root; there is
no subdirectory syntax, so a git URL pointed at this repo (which hosts multiple
distributions in subfolders) will not work. Clone first for this one.

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
