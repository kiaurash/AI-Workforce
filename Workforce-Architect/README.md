# Workforce-Architect

A standalone deliverable: a Hermes skill (plus the profile spec and Soul.md needed to
run it) that lets a user with a workflow concept in mind design a multi-agent AI
workforce — decomposed work units, a derived agent roster, a hard risk/approval gate,
and an honest Enforced/Governed/Advisory labeling of every proposed control.

**This is a separate project from the AI-Workforce course capstone materials** that
live elsewhere in this repository (`Course.md`, `AI-Workforce-Tutorials/`,
`hermes-profiles/`). It happens to live in the same repo at the user's direction; it
does not depend on, extend, or get taught by those course materials, and should not be
merged into their narrative. If you are here for the course, see `Course.md` instead.

## Install the skill

Full step-by-step guide: `GETTING-STARTED.md`. Quick version, two options — pick whichever is easier for you:

### Option A — install directly from the repo (simplest, no git clone needed)

In a Hermes chat on your own machine, run:

```
hermes skills install --yes "https://raw.githubusercontent.com/kiaurash/AI-Workforce/main/Workforce-Architect/skills/design-ai-workforce/SKILL.md"
```

Hermes fetches the `SKILL.md` and automatically pulls its linked `templates/` and
`references/` files from the same place — you don't need to download anything
separately. (The `--yes` skips the interactive confirmation prompt; drop it if you'd
rather review the install prompt first.) Then start a **new** Hermes session (skills
load once per session start).

### Option B — create a local directory (clone the whole repo)

If you want your own editable copy, or Option A doesn't work on your setup:

```
git clone https://github.com/kiaurash/AI-Workforce.git
cp -r AI-Workforce/Workforce-Architect/skills/design-ai-workforce "$HERMES_HOME/skills/design-ai-workforce"
```

`$HERMES_HOME` resolves to the right location automatically — the default install
(`~/.hermes` on Linux/macOS, `%LOCALAPPDATA%/hermes` on Windows) or your active
profile's own directory if you're using a Hermes **profile** rather than the default
install. Run the `cp` command from inside that session/profile's own shell so the
variable resolves correctly.

Then start a **new** Hermes session.

## Contents

- `skills/design-ai-workforce/` — the skill itself (SKILL.md + templates + references).
  Install as a personal skill (`skill_manage(action='create')`, copying this content) or
  by pointing a profile's skills directory at a checkout of this folder.
- `profile/SOUL.md` — the identity and operating procedure for a `workforce-architect`
  Bot profile that runs this skill with full Design -> Scaffold -> Pilot authority.
- `profile/PROFILE_SPEC.md` — the profile configuration (model, toolset, skills) a human
  applies to actually create the Bot. No tool in this Hermes runtime creates a profile
  from inside a skill, so this is a spec for human setup, not a deployed artifact.

## Status

Design, Scaffold, and the agent/system-configuration-change gate have been
cold-start Pilot-tested (two independent Pilot runs, see
`pilots/pilot-1-systems-thinking/` for full evidence). Task execution — an agent
actually doing the designed work — has deliberately not been exercised yet; see
`GETTING-STARTED.md`'s "Current maturity" note before treating any generated
workforce as operational.
