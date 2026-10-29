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
- `kanban_block` only — **`kanban_unblock` is deliberately NOT granted.** The architect
  has no legitimate use for releasing its own blocked work (it creates blocked tasks,
  it never needs to lift the block); removing the tool converts this boundary from
  Advisory ("please don't") to Enforced (the capability genuinely does not exist in
  this profile's toolset). Per Codex review of PR #3, granting it alongside an
  "only a human calls this, by convention" note made the convention meaningless —
  removing the tool is the actual fix, not a stronger instruction.
- `skill_manage`
- `cronjob_manage`
- `message_agent` (or the active platform's equivalent bot-to-bot messaging tool)

Generic pilot-execution group (a piloted work unit could be almost any kind of task).
**Merged v1 policy (Codex review + room consensus), per user approval:**
1. Keep `execute_code`/`terminal` in the toolset per the MVP requirement, but scope
   their working directory to a dedicated, disposable pilot-workspace path, separate
   from this skill's own files and any governance/kanban-task content.
2. Explicitly prohibited from use on any work unit that is blocked, consequential, or
   in the "Agent/system configuration change" category. These tools run the bounded,
   already-approved representative Pilot task only — never anything still awaiting
   human review.
3. **Evidence label: Advisory-bounded, accepted residual risk for v1** — see
   `references/evidence-labels-and-runtime-enforcement.md`. No filesystem/network
   sandbox exists in this runtime; the dedicated-directory scoping improves procedure
   and auditability, it is not a security boundary. Do not represent it as one.
4. Logged as a "requires additional infrastructure for Enforced status" item — a
   future revision with real sandboxing (OS-level permissions, container, scoped
   credentials) is a tracked upgrade, not a forgotten gap.

- `web_search`, `web_extract`
- `read_file`, `write_file`, `patch`, `search_files`
- `execute_code` or `terminal` (whichever this deployment's profile convention uses) —
  working directory scoped to the disposable pilot workspace per policy above

## Explicitly NOT granted in v1
- Any tool that performs a consequential external action directly (publish, send
  email/payment, modify production infra, hire/terminate personnel, sign a contract).
  The roster design should mark such tools as absent for this profile and, where a
  piloted workflow genuinely needs one, that specific tool belongs to a *designed*
  agent in the roster this profile produces — never to the architect profile itself.
- Profile-creation or profile-activation tooling (none exists in this runtime to grant).
