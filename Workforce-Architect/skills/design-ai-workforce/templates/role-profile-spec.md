# Role Profile Spec Template

Generate exactly one of these per rostered Bot, alongside its Role SOUL.md
(`templates/role-soul.md`). Derived from `workforce-architect`'s own
`profile/PROFILE_SPEC.md` — same pattern, generalized to any designed role. Like the
Role SOUL.md, this is always a **human-apply spec**: no tool in this Hermes runtime
creates or activates a profile from inside a skill. Rendering this document is never
"deploying" the Bot.

```markdown
# Profile Spec — <role-name>

**Status: spec for human setup. Not activated, not deployed.** A human applies this via
the desktop app, `hermes profile` commands, or direct `config.yaml`/profile-directory
setup, then verifies it with the activation smoke test below before relying on it.

## Identity
- Profile name: <role-name>
- Owns Traceability Matrix rows: <Row ID 1>, <Row ID 2>, ... (cite by ID, don't restate
  — re-read the matrix for current details)
- SOUL file: `role-souls/<role-name>-SOUL.md` (or wherever the rendered Role SOUL.md for
  this Bot was placed) — copy to the new profile's SOUL/system-prompt location per the
  setup method used.

## Model / provider
- Recommended family: <state one, with a one-line reason tied to what this role's rows
  actually require — e.g. "structured-output consistency and conservative instruction-
  following" if it owns Advisory-boundary-heavy rows, or "fast/cheap" if its rows are
  pure mechanical lookups with no judgment calls>.
- Swappable via `hermes model` against this profile at any time; revisit after this
  role's rows have been exercised in a Pilot, not before.

## Skills
- `<generated-skill-name>` — from the Scaffold tier: auto-deployed if this profile is
  the same one running `design-ai-workforce`, otherwise human-apply (file content +
  target path provided separately; a human or this profile's owner installs it).
- List any other skill this role genuinely needs (do not grant speculatively — see
  SKILL.md's "Complementary skills" section: check availability on the target profile
  before referencing a name, and don't grant repository-write/automated-review tools by
  default).

## Toolset
- Required (from this role's owned rows' "Allowed Tools" column): <list>.
- Explicitly NOT granted: <any tool that would let this role perform a consequential
  action its rows don't authorize — name it, don't just imply it>. For each item here,
  state the evidence basis: Enforced (the absence itself, verified against the actual
  toolset grant — not the accompanying prose), Governed (relies on a human/reviewer
  catching misuse before consequence), or Advisory (instruction only, no backstop). Do
  not round up — if you can't point to the specific mechanism, it's Advisory.

## Memory / data boundary
- What this role's standing memory/notes may retain: <structured fields relevant to its
  owned work units' audit trail>.
- What must stay excluded: <raw prompts, credentials, other agents' private context,
  personal data not required for its work units>. If this is Advisory-only (no tool
  filters it), say so and point to the relevant canary-test requirement in
  `references/pilot-acceptance-criteria.md`.

## Governance / approval references
- Risk/Approval Matrix categories this role's rows touch, and their approval owners
  (cite the matrix, don't restate it in full).
- If this role owns an "agent/system configuration change" row: it never auto-proceeds
  regardless of risk level — see SKILL.md Pitfalls and `templates/decision-record.md`.

## Activation smoke test (required before calling this role ready)
State the specific test that will be run once the profile is configured — not "it
responds to messages," but a test tied to this role's actual owned rows: give it one
representative input, verify it produces the expected output artifact/schema, verify it
stops at every boundary stated above (does not use an absent tool, does not unblock a
task it shouldn't, does not exceed its innovation envelope if it owns a Decision Work
Unit). Record the result as artifact evidence, not a chat transcript claim — same
"don't treat chat as proof of completion" discipline used everywhere else in this
design.

## Explicitly NOT granted, standing policy
- Any tool that performs a consequential external action this role's own rows don't
  specifically call for (publish, send email/payment, modify production infra,
  hire/terminate personnel, sign a contract).
- Profile-creation or profile-activation tooling (none exists in this runtime to grant
  to any profile).
```
