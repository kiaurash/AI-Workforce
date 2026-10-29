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

Design + Scaffold + Pilot toolset included (MVP, per user direction: ship pilot
execution tools now rather than deferring). Not yet piloted end-to-end. First planned
pilot: use this skill to design two additional roles for the course workforce — a
Meta-learner (Observer pattern) and a Documentarian (evidence-linked lab notebook) —
as a dogfooding exercise, not hand-specified roles.
