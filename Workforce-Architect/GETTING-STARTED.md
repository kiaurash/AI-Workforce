# Getting Started: Build Your First AI Workforce

A step-by-step guide for students new to Hermes who want to design a multi-agent AI
workforce using the `design-ai-workforce` skill. No prior Hermes experience assumed.

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
`Workforce-Architect/skills/design-ai-workforce/`. It is **not** in the official Hermes
skill catalog (you can't `hermes skills install` it) — it's a personal skill you install
from this repo's content. Two ways to do it:

### Option A — ask your Hermes agent to do it for you (recommended)

Start a normal Hermes chat and say something like:

> Clone `https://github.com/kiaurash/AI-Workforce` to a local folder, read the contents
> of `Workforce-Architect/skills/design-ai-workforce/`, and install it as a personal
> skill on this profile using `skill_manage(action='create')` plus the matching
> `write_file` calls for its `templates/` and `references/` subfolders.

Your Hermes agent has the tools to clone the repo and create the skill directly — this
is the easiest path and avoids any manual file-copying mistakes.

### Option B — do it manually

```
git clone https://github.com/kiaurash/AI-Workforce.git
```

Then copy `AI-Workforce/Workforce-Architect/skills/design-ai-workforce/` into your own
Hermes skills directory, preserving the `templates/` and `references/` subfolders:

```
# Linux/macOS
cp -r AI-Workforce/Workforce-Architect/skills/design-ai-workforce ~/.hermes/skills/design-ai-workforce

# Windows (git-bash / MSYS, matches Hermes's terminal tool)
cp -r AI-Workforce/Workforce-Architect/skills/design-ai-workforce "$LOCALAPPDATA/hermes/skills/design-ai-workforce"
```

(If you're running a Hermes **profile** rather than the default install, use that
profile's `skills/` directory instead — see `hermes profile` or ask your instructor
which profile you should be using for this course.)

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
