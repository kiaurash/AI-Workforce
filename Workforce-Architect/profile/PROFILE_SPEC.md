# Profile Spec — workforce-architect

**Status: spec for human setup. No tool in this Hermes runtime creates a Bot profile
from inside a skill — a human applies this via the desktop app, `hermes profile`
commands, or direct `config.yaml`/profile-directory setup.** Do not treat this
document as a deployed or activated profile.

## Identity
- Profile name: `workforce-architect`
- SOUL file: `profile/SOUL.md` (this folder) — copy to the new profile's SOUL/system
  prompt location per the setup method used.

## Model / provider
- No fixed requirement. Per user direction, start with whatever model/provider this
  Hermes install currently defaults to, and swap later with `hermes model` against the
  `workforce-architect` profile. Nothing in the skill or Soul.md depends on a specific
  model.

## Skills
- `design-ai-workforce` (this repo, `skills/design-ai-workforce/`). Install as a
  personal skill under the profile's `skills/` directory, or point the profile's skill
  search path at a checkout of this repo folder.

## Toolset (MVP: Design + Scaffold + Pilot, per user direction to include pilot
execution tools now rather than defer)

Orchestration group (always needed):
- `kanban_create`, `kanban_link`, `kanban_comment`, `kanban_show`, `kanban_list`
- `kanban_block`, `kanban_unblock` — included so the profile can block its own output;
  by convention (Advisory, not Enforced — the tool does not check who calls it)
  unblocking a consequential/out-of-envelope item is reserved for the human reviewer,
  per SOUL.md's operating procedure. Document this honestly in any readiness report
  rather than claiming the tool itself enforces the separation.
- `skill_manage`
- `cronjob_manage`
- `message_agent` (or the active platform's equivalent bot-to-bot messaging tool)

Generic pilot-execution group (a piloted work unit could be almost any kind of task):
- `web_search`, `web_extract`
- `read_file`, `write_file`, `patch`, `search_files`
- `execute_code` or `terminal` (whichever this deployment's profile convention uses)

## Explicitly NOT granted in v1
- Any tool that performs a consequential external action directly (publish, send
  email/payment, modify production infra, hire/terminate personnel, sign a contract).
  The roster design should mark such tools as absent for this profile and, where a
  piloted workflow genuinely needs one, that specific tool belongs to a *designed*
  agent in the roster this profile produces — never to the architect profile itself.
- Profile-creation or profile-activation tooling (none exists in this runtime to grant).
