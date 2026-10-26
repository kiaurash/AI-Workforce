# DIAGNOSTIC-TEMPLATE.md

Template for `courses/<slug>/DIAGNOSTIC.md` — the intake instrument. **Authored by
`/idl-design`, run by `/idl-study`** (once per learner per course, before chapter 1).
No fourth skill: a 10-minute questionnaire does not earn one.

**This file is what turns a shared course into a personalized tutor.** It is the only
mechanism that mints tier 3 for a stranger, and therefore the only thing that makes
per-learner pause activation possible. Without it, every misconception pause is a guess.

It does four jobs at once:
1. **Bootstraps tier 3 for a stranger** — the learner's answers *are* their record.
2. **Un-quarantines tier-4 items safely, per learner** — direct evidence *this* person holds it.
3. **Teaches, by itself** — the pretesting effect: a diagnostic pretest improves later
   learning *even when the learner gets it wrong*, most strongly at expectancy-violating
   items. Intake is not overhead.
4. **Bootstraps aggregate base rates** (`evidence.md`) without anyone finishing a chapter.

---

## Frontmatter

```yaml
---
course: <slug>
items: 4                  # 3–4 per skill/chapter
created: YYYY-MM-DD
---
```

## Item format

```markdown
### D1 — <one-line topic>
outcomes: [LO-2]

> The question, stated neutrally.

- (a) <option>            <!-- registry_id=<id> -->
- (b) <option>            <!-- correct -->
- (c) <option>            <!-- registry_id=<id> -->
- (d) I don't know        <!-- no-belief -->

**Confidence:** guessing / fairly sure / confident
```

## Item requirements — normative

- **Every distractor maps to a `registry_id`.** Exactly one correct option. A distractor
  that maps to nothing is measuring nothing.
- **An explicit "I don't know" option on every item.** Forcing a choice *manufactures*
  misconceptions the learner does not hold. This is the anti-backfire safeguard at intake
  and it is **not optional**.
- **A confidence rating on every item.** This is the whole difference between a diagnostic
  and a guessing game:

  | Answer | Confidence | Interpretation | Pause eligibility |
  |---|---|---|---|
  | wrong (picks misconception X) | confident | **genuinely held belief** — the highest-value refutation target | ✅ activate X's pauses |
  | wrong (picks misconception X) | guessing | a guess, **not a belief** | ❌ **never** anchor a refutation on X — this is exactly the backfire case |
  | "I don't know" | — | no belief to refute | ❌ present as `prediction`, not `misconception` |
  | correct | confident | already holds the correct model | ❌ suppress the pause |

- **P8 format neutrality is mandatory.** No emphasis on the correct option; randomized
  position; comparable distractor length and specificity; no wrong-to-right ordering.
  Without it the instrument measures test-taking, and **every downstream personalization
  inherits the noise**.
- **Where a validated instrument exists, use it verbatim.** Financial literacy has one
  (Lusardi–Mitchell "Big Three"), which brings published population base rates for free.

## Coverage gate (mechanical — `/idl-design` refuses to ship without it)

> **Every registry item that may anchor a `misconception` pause has ≥1 diagnostic item
> whose distractor carries its `registry_id`.**

Grep the `registry_id`s in `COURSE.md`'s registry against this file. An item that cannot be
diagnosed cannot be personalized, so it must not anchor a refutation pause — the runner
would be refuting a belief it has no evidence the learner holds.

## What is written from it

`/idl-study` writes `learners/<id>/profile.md`:

`registry_id | intake_answer | confidence | status | last_observed`

`status ∈ held-confident (tier-3d) | held-uncertain | unknown | not-held | observed (tier-3v)`

**Observation outranks intake** when they disagree — people mis-report their own beliefs,
and what they *do* under a live question is the better evidence.

## The line that must not be crossed

**The system may quote the learner. It may never diagnose them.**

- ✅ *"On the intake you picked (b) — that a failure means something is wrong with you.
  Curiosus is about to take that apart."* — grounded in their own words.
- ❌ *"You probably believe your failures are permanent."* — an inference about a person's
  psychology. Banned. It is both the refutation-backfire mechanism and, in a personal
  domain, insulting enough to end the session.
