# After Installing: What To Do Next

You've installed both `ai-workforce-tutor` and `ai-workforce-conductor`. This sheet
is the short version of what happens next — see `Course.md` for the full design.

## 1. Sign in to both profiles separately

Credentials are per-profile, not shared. For each profile, either set a static API
key in that profile's own `.env`, or sign in with OAuth:

```text
hermes -p ai-workforce-tutor auth add <provider>
hermes -p ai-workforce-conductor auth add <provider>
```

## 2. Set the Tutor's write sandbox (one-time, per learner)

The Tutor can only write one file, and only inside a folder you point it at. In
`ai-workforce-tutor`'s `.env`, set:

```text
HERMES_WRITE_SAFE_ROOT=<path-to-your-capstone-repo>\learning
```

Use your own capstone repository's `learning/` folder, not the course repo.

## 3. Run the Tutor's activation test before trusting it

Don't skip this — it's how you confirm the write limit actually holds, not just that
the Soul says so. Follow `ai-workforce-tutor/activation-test/README.md`: copy its
`fixture/` folder, point `HERMES_WRITE_SAFE_ROOT` at the copy, send `prompt-1.txt`
then `prompt-2.txt` in the Tutor's Bot Chat, and check all 6 pass conditions. Record
the result (pass/fail per condition) in your capstone's `profiles/role-activation-log.md`.

## 4. Start with the Tutor, not the Conductor

Open the Tutor's Bot Chat and describe the real workflow you want to build (a real
responsibility you own — not a hypothetical). It will diagnose what you already
know and ask Socratic questions before giving you anything. This is deliberate:
Course.md's design principle #2 is "build early," but principle #4 is "evidence
before confidence" — the Tutor makes sure you understand a step before you skip to
building it.

## 5. Hand off to the Conductor through yourself, not Bot-to-Bot

When the Tutor gives you a draft instruction, you carry it to the Conductor's Bot
Chat yourself and decide whether to run it. If the Tutor and Conductor ever exchange
direct messages, treat those as notifications only — never as an assignment, and
never as evidence that something happened.

## 6. In the Conductor's Bot Chat, scope roles to your current module

Run `/setup-ai-workforce-roles` to create and activate only the roles your current
module needs — don't stand up the full Builder/Reviewer/Observer topology on day one.
The course's staged shape is:

| Module | Default shape |
| --- | --- |
| M0.5–M1 | Conductor acting as a bounded Builder |
| M2 | Builder plus a reusable skill |
| M3 | Conductor → Builder → Reviewer, run as an experiment |
| M4–M5 | governed operation using whichever roles you kept |
| M6 | Observer, run as an experiment |

## 7. Every role gets an experiment before a decision, not just a demo

Per Course.md §3.5: watching a demo is not evidence. For Builder/Reviewer/Observer,
run that role's actual activation test and one real task, then record **adopt**,
**do not adopt**, or **deferred pending experiment** in a Role Decision Record —
citing what the role caught, missed, or cost. Declining a role for good evidence-based
reasons scores the same as keeping it.

## 8. Treat your capstone repository as the source of truth, not the chat

Both Bots will say things in chat. None of it counts until there's a saved,
inspectable artifact in your capstone repo: contracts, outputs, receipts, review
decisions, approval records. If a Bot claims a run passed or a file exists, open the
file yourself before believing it.

## Quick reference: who does what

| | Tutor | Conductor |
| --- | --- | --- |
| Purpose | diagnoses, teaches, drafts instructions | runs the actual workflow, verifies gates |
| Counts as a workforce role? | No — learning support only | Yes |
| May write | `learning/learning-record.md` only | designated operational paths |
| Never | certifies a run, creates missing outputs, supplies your answers | treats a chat message as proof |
