# COURSE-TEMPLATE.md

Template for `courses/<course-slug>/COURSE.md` — authored by `/idl-design`, **immutable
after approval** (`--rebuild` to change). Format rules for *chapters* live in
`CHAPTER-FORMAT.md`, not here.

**Why `courses/` sits inside `Inquiry-Driven-Learning/`** rather than
`AI-Driven-Learning/courses/`: project-owner directive to contain this work here while the
suite is unproven. Revisit if the suite graduates.

---

```yaml
---
course_id: <slug>
title: "..."
audience:                    # REQUIRED SCHEMA — prompt for missing fields, never infer
  background: "..."          #   who they are
  assumed_prior: "..."       #   what they already know — see "Prerequisites" below
  goal: "..."                #   what they want to do with it
source_profile: "..."        # one line: what the sources are and what they cover
course_kind: concept | skill # METADATA ONLY. No skill branches on this. See §5 of the plan.
anchor_ledger: <path>        # optional — a KG Learnings/_index.md to mirror at session end
grounding: ok | weak         # `weak` if the ≥3 misconception items at tiers 1–2 floor is not met — banner it
created: YYYY-MM-DD
status: draft | approved
---
```

### The audience is a ROLE, never a person

`audience:` must describe a role a **stranger can match** — *"an engineer or PM who builds
or buys ML decision systems; assumes no systems-dynamics vocabulary; wants to avoid shipping
a model that confirms its own mistakes."*

**Never** a named individual, their employer, or their job title. The person who commissions
the course is **learner #1, not the specification.** Their record is the richest source of
*hypotheses* you will get — it is not grounding, and it is not the audience. If a course
only works for the person who ordered it, it is a tutoring session with extra files.

`/idl-design` **prompts for every audience field and never infers one.**

## 1. Source registry

| key | source | location | tier role |
|---|---|---|---|

Commentary cites resolve against this table. **Cite keys follow the source's own
addressing** — atom ids for atomized KG sources, `§section` for Markdown, `p.X` for paged
documents. Do not invent page numbers for unpaged sources.

## 2. Persona pair

Expert (Curiosus-role) + learner (Ignotus-role): names, voice notes, and the contract.

The learner-character: proposes analogies, completes patterns, pushes back, asks
deep-reasoning questions — **and never goes silent inside a reveal** (CHAPTER-FORMAT §4.2).
Registry misconceptions concentrate at pause points; most turns are productive.

## 3. Registry — misconceptions and principles

| registry_id | kind | statement | tier (1, 2, or 4) | evidence / cite | origin | diagnostic item | planned chapter |
|---|---|---|---|---|---|---|---|

**`kind` is a closed enum: `misconception | principle`.** A `principle` row names a positive
pattern or skill that a `completion` pause targets — nothing to refute, nothing to diagnose.
The floor, tier-as-safety rules, diagnosability, and pause-eligibility below apply to
`kind=misconception` rows only; a principle row still needs a source cite. **Downstream
consumption filters by `kind`:** `/idl-chapter` aborts on a pause whose `type` mismatches
its target's `kind` (misconception → `kind=misconception`; completion → `kind=principle`),
and `/idl-study` updates misconception status only from `kind=misconception` rows —
completion performance is mastery evidence, never misconception evidence.

**Floor: ≥3 misconception items at tiers 1–2**, else `grounding: weak` and every tier-4 item flagged.

- **tier 1** — the source names this misconception itself (strongest)
- **tier 2** — domain literature supports it as a population-level error
- **tier 3** — ❌ **NOT AUTHORABLE.** See below.
- **tier 4** — LLM-inferred hypothesis. **Quarantined**: may appear as a minor dialogue
  moment but may **not anchor a misconception-type pause** until validated per learner.

### Tier 3 is minted at run time, never authored

**A course is shared; a learner is not.** Tier 3 means *this learner's own record* — so
writing it into `COURSE.md` asserts that every reader holds a belief for which you have
evidence about exactly one. That is the refutation-backfire mechanism, delivered by the
author instead of avoided by them.

Tier 3 is created **per learner**, at intake (`tier-3d` — they endorsed it on the
diagnostic) or by observation (`tier-3v` — they committed the error live), and lives only in
`learners/<id>/profile.md`.

**A misconception observed in one real learner is a hypothesis, not grounding.** It enters
the registry at **tier 4**, with its provenance in the `origin` column ("observed in a
practitioner, 2026-06-06") — which makes it a *high-priority diagnostic item*, exactly where
it belongs. If independent tier-1 or tier-2 evidence turns up, promote it on that evidence,
not on the anecdote.

### The diagnosability gate (hard, mechanical)

> **Every registry item that may anchor a `misconception` pause MUST have a diagnostic item
> in `DIAGNOSTIC.md` whose distractor carries its `registry_id`.**

**Pause-eligibility is derived, never declared:** a row is pause-eligible iff
`kind=misconception` ∧ tier ∈ {1, 2} ∧ some chapter-map row plans a `misconception` pause on
it. Dialogue-only demotion = dropping the item from the map's planned pauses; there is no
flag to maintain. Principle rows are exempt by construction.

If a misconception cannot be diagnosed, it cannot be personalized — the runner can never
learn whether *this* learner holds it, so refuting it is a coin flip with a known downside.
`/idl-design` refuses to approve a COURSE.md that fails this grep.

This is a registry of **candidate** misconceptions — a hypothesis space, not a claim about
any individual. Per-learner belief status lives in `profile.md`, never here. Observed
outcome marks live in `ledger.md`, never here.

## 4. Prerequisites — the vocabulary contract

**Every term that a pause question depends on is either (a) defined in the chapter before
the pause that tests it, or (b) listed here.** Nothing else may be assumed.

| term | supplied by |
|---|---|

*(This section exists because the Phase-0 pilot got it wrong: a pause asked the learner to
classify a loop as "reinforcing or balancing" — terms imported from the author's own prior
session and never defined. Invisible to that one learner; unanswerable for every other. It
is the rule that makes shared chapters safe for strangers.)*

## 5. Learning outcomes

Top 5–10, Bloom-tagged. `LO-N` ids; chapters and exercises reference them.

## 6. Chapter map

| chapter | title | source sections | outcomes | planned pause types | interleave / spacing note |
|---|---|---|---|---|---|

Sequenced so chapter *k* builds on *k−1*. Chapter splitting and merging is owned here — a
chapter generator that finds its section too large **aborts with a split recommendation**;
it never splits unilaterally.

## 7. Safety / Consumption envelope

**Required for sensitive domains** (personal, psychological, health, or similar material);
optional elsewhere. A course-level contract, not a runtime note. Declares:

- boundaries of instruction — what the course teaches and what it does not claim to do;
- situations the course must **not** attempt to handle;
- when to redirect to professional or crisis support;
- whether fictional scenarios must always be offered as alternatives to personal material;
- feedback constraints (e.g. quote the learner's words, never diagnose them).

**Ownership across the suite:** `/idl-design` authors it here · `/idl-chapter` incorporates
it into framing, exercises, and fictional alternatives · `/idl-study` enforces it during
interaction. No skill may weaken it at run time.

## 8. Consumption note

Tutored `/idl-study` is the **default** consumption path. Standalone reading is a
**known-degraded** mode (ICAP: observing dialogue beats monologue chiefly for *active*
observers) — and, per the Phase-0 render test, standalone reading in Obsidian carries an
accepted residual leak: the search pane can preview a few words of an unreached reveal.
