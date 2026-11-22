# AI Workforce Tutor Profile Distribution

This distribution installs one **Tutor** Hermes profile for the AI Workforce course (Course.md section 3.6). The Tutor is learning support. It is not a workforce role and does not count toward the learner's role count.

## Install

From a local clone of this repository:

```text
hermes profile install <path-to>/hermes-profiles/ai-workforce-tutor
```

or from a published repository, use its Git URL. The installer previews the manifest. Credentials, sessions, and memories are not distributed.

## Sign in (per profile)

Credentials are per profile. Static API keys can be set in the profile's `.env`. Single-use OAuth logins are not shared between profiles, so a learner who signs in with OAuth runs, for example, `hermes -p ai-workforce-tutor auth add <provider>`.

## What is included

- `SOUL.md`: the Tutor's authority model and rules.
- `config.yaml`: a narrow tool surface (clarify, file, memory, session search, skills, todo). There is no terminal, code execution, browser, web, delegation, or cron.
- `skills/m1-first-ai-employee-tutor/`: the M1 Socratic tutor, with its diagnostic, misconception map, and contract field guide.
- `activation-test/` (repository only, not installed): the Tutor activation test and fixture.

## The write limit

The Tutor may write one file: `learning/learning-record.md`.

Tools alone cannot make the Tutor read-only. The `file` toolset bundles `read_file` with `write_file` and `patch`, so a profile that can read the workspace can also write to it. The limit has three layers, and only the third is enforced by software:

1. **Instruction.** `SOUL.md` and the skill say what the Tutor may write. An instruction is guidance, not a lock.
2. **Narrow tools.** With no terminal or code execution, the file tools are the Tutor's only way to write.
3. **Write sandbox.** Hermes supports `HERMES_WRITE_SAFE_ROOT`, an environment variable that makes `write_file` and `patch` refuse any path outside the listed folders. Set it in the Tutor profile's `.env` to the learner's `learning/` folder:

```text
HERMES_WRITE_SAFE_ROOT=C:\path\to\learner-workspace\learning
```

The path is specific to each learner, so a distribution cannot ship it. The sandbox covers the file tools only, which is why the Tutor has no terminal. It also blocks the Tutor from writing anything else outside that folder, including its own skills.

The activation test (`activation-test/README.md`) checks all of this. A person runs it and records the result. Until it has been run in Hermes Desktop on the learner's machine, treat the write limit as unverified.

## Working with the Conductor

The Tutor and the Conductor are separate Bots. The Tutor drafts a Builder instruction and the learner carries it to the Conductor's chat. If the two Bots exchange Bot-to-Bot messages, those messages are notifications only, never assignments and never evidence. The learning record is never an input to a run.

## Evidence rule

Repository artifacts are authoritative. The Tutor's learning record shows what the learner demonstrated about concepts. It does not show that any run happened.
