# Getting Started: Build Your First AI Workforce

A step-by-step guide for students new to Hermes who want to design a multi-agent AI
workforce using the `design-ai-workforce` skill. No prior Hermes experience assumed.

## Current maturity — what's actually been tested

Design and Scaffold's first-run blocking were verified against real cold-start Pilot
runs (PRs #3–#6): decomposition-before-roster-naming, the Risk/Approval Matrix hard
gate, Decision Work Unit mechanics (including a fail-closed provenance rule added
after a real Pilot failure), and the first-run all-blocked Scaffold rule all held on
blind runs with no accumulated design context. A fresh Meta-learner role was also
tested and correctly could not act on its own improvement proposal — it could only
draft a file for human review.

**Task execution (an agent actually doing the designed work, e.g. W1–W6) was
deliberately never exercised.** Profile activation remains a human-applied step, and
no Pilot run has validated that an activated role actually produces correct output
against its row's acceptance evidence. Treat any workforce you design as **Design/
Scaffold-validated, execution-unproven** until you've activated and smoke-tested each
role, then run a bounded execution Pilot of your own — before trusting it with
anything consequential.

## What you'll end up with

By the end of this guide you will have: a `design-ai-workforce` skill installed and
loadable in your own Hermes session, and a **Design-phase package** for one real
workflow of your choosing — a decomposed set of work units, a Traceability Matrix, a
completed Risk/Approval Matrix, and an honestly-labeled (Enforced/Governed/Advisory)
set of proposed controls. You will NOT, in this first pass, have agents actually
running production work — that comes later, deliberately, after a Pilot.

## Step 0: Prerequisites

- Hermes installed and running (`hermes --help` works in your terminal). If you don't
  have Hermes yet, see the main Hermes docs: https://hermes-agent.nousresearch.com/docs/
- Access to this repository (`kiaurash/AI-Workforce`) — ask your instructor if you
  don't have it yet.
- A model/provider already configured in your Hermes install (`hermes model` to check
  or set one). Any provider works; you don't need a specific one to follow this guide.

## Step 1: Get the skill onto your machine

The `design-ai-workforce` skill lives in this repo under
`Workforce-Architect/skills/design-ai-workforce/`. It is not in the official Hermes
skill catalog by name, but `hermes skills install` does accept a direct URL to a raw
`SKILL.md`, and Hermes automatically fetches that skill's linked `templates/` and
`references/` files from the same location — so for this specific skill, the URL
install pulls the complete bundle, not just one file. Two ways to install it:

### Option A — install directly from the repo (simplest, no git clone needed)

```
hermes skills install --yes "https://raw.githubusercontent.com/kiaurash/AI-Workforce/main/Workforce-Architect/skills/design-ai-workforce/SKILL.md"
```

That's it — no manual file copying. (`--yes` skips the interactive confirmation
prompt; drop it if you'd rather review the install prompt first.) If you're running a
Hermes **profile** rather than the default install, run this from inside that
profile's own session so it installs into the right `skills/` directory.

### Option B — create a local directory (clone the whole repo)

Use this if you want your own editable copy, or Option A doesn't work on your setup:

```
git clone https://github.com/kiaurash/AI-Workforce.git
```

Then copy `AI-Workforce/Workforce-Architect/skills/design-ai-workforce/` into your own
Hermes skills directory, preserving the `templates/` and `references/` subfolders:

```
cp -r AI-Workforce/Workforce-Architect/skills/design-ai-workforce "$HERMES_HOME/skills/design-ai-workforce"
```

`$HERMES_HOME` resolves to the right location automatically — the default install
(`~/.hermes` on Linux/macOS, `%LOCALAPPDATA%/hermes` on Windows) or your active
profile's own directory if you're using a Hermes **profile** rather than the default
install (see `hermes profile` or ask your instructor which profile to use for this
course). Run the `cp` command from inside that session/profile's own shell so the
variable resolves correctly.

## Step 2: Start a fresh session and confirm the skill loaded

**Important:** Hermes loads its skill list once per session start. If your agent was
already running when you installed the skill, start a new session/chat before
continuing — otherwise the skill won't be visible yet.

In a fresh chat, ask: "What skills do you have available?" or just start describing
your workflow (the skill's description — "Use when designing a multi-agent AI
workforce" — should cause it to load automatically when relevant).

## Step 3: Bring a real workflow idea, not a hypothetical one

This skill works best on something you actually want to build. Before your first
session, write down in plain language:

- What outcome you want (e.g. "a weekly competitor-news digest emailed to my team").
- The rough steps you imagine, in order, as you currently picture them.
- Any point in that process where you'd want a human to approve something before it
  goes out, gets spent, or gets changed (publishing, sending, spending money, touching
  production systems, affecting a person's record).

You do NOT need to have this fully thought through — the skill's whole point is to help
you decompose it properly. A rough sketch is enough to start.

## Step 4: Work through Design mode with your Hermes agent

Tell your agent your workflow idea and that you want to design a workforce for it. The
skill will guide the session through, in this order (don't let your agent skip ahead —
if it tries to name agent roles before this, push back):

1. **Decomposition** — breaking your workflow into work units, including any decision
   points (places where the next step depends on what's found) and any retry loops.
2. **Traceability Matrix** — one row per work unit: what it produces, who/what owns it,
   what tools it needs, how its output gets checked, and what happens if something goes
   wrong. Your agent roster comes FROM this matrix — you shouldn't see role names before
   this step is done.
3. **Risk/Approval Matrix** — this is a hard gate. Every category of consequential
   action (external writes, money, production changes, outbound communication,
   personnel, legal/contractual, and changes to another agent's own configuration) must
   have a stated approval owner before anything moves forward. If you leave a category
   genuinely unanalyzed, your agent should refuse to produce a roster and instead show
   you a gap report — that's the skill working correctly, not a bug.
4. **Evidence labels** — every control your agent proposes should be labeled Enforced
   (the tooling genuinely prevents the bad outcome), Governed (a human/reviewer catches
   it before it matters), or Advisory (just an instruction, no technical backstop). Ask
   "what makes this Enforced rather than Advisory?" if a label doesn't make sense to
   you — a vague answer means the label is wrong.

## Step 5: Understand what happens next — but don't rush there yet

After Design, the skill defines two more modes you'll use in later sessions, not this
first one:

- **Scaffold** — your agent actually creates the kanban tasks and skill files for your
  roster, but only after you explicitly confirm the exact list of what it's about to
  create. On your very first Scaffold run for a brand-new design, every task starts
  intentionally paused (`blocked`) — even the low-risk ones — until you've run one
  successful Pilot. This is deliberate: an unproven design shouldn't start dispatching
  real work just because the tasks exist.
- **Pilot** — one bounded, low-stakes test run of your design, picked to exercise at
  least one non-default decision branch (not just the easy path). This is where you
  find out whether your design actually works, before trusting it with anything real.

For this first session, your deliverable is just the completed Design package. Resist
the temptation to jump to Scaffold/Pilot in the same sitting — reviewing the Traceability
and Risk/Approval matrices carefully is the actual learning exercise here.

## Exercise: your first Design package

Produce, with your Hermes agent's help:

1. A one-paragraph description of your chosen workflow.
2. A completed Traceability Matrix (use `templates/traceability-matrix.md` as the
   starting structure).
3. A completed Risk/Approval Matrix with every category explicitly addressed — no
   blank cells, no leftover "not applicable" copied from the template without you
   actually having checked it (per `templates/risk-approval-matrix.md`'s own instructions).
4. For every category you label Enforced or Governed, one sentence saying exactly what
   mechanism backs that label (a missing tool? a human review step? what, specifically?).

Bring this to class/review. Common mistakes to watch for in your own work:
- Naming roles ("a researcher agent," "a reviewer agent") before the matrix is built —
  if this happened, the roles are probably generic rather than justified by your actual
  workflow.
- Leaving a risk category "not applicable" without having actually asked whether any
  proposed agent could touch it.
- Labeling something "Enforced" because it sounds safe, not because you can point to
  the actual tool-permission fact that makes it true.

## Where to get help

- Skill questions / stuck decomposing your workflow: ask your Hermes agent directly —
  that's what the skill is for.
- Hermes setup/installation issues unrelated to this skill: see
  https://hermes-agent.nousresearch.com/docs/
- Everything else: your instructor / course channel.
