---
name: course-design
description: Use after intake to design a diagnostic-led course.
version: 0.1.0
author: Kia, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [course-design, outcomes, misconceptions, diagnostic, modules]
    related_skills: [learner-intake]
---

# Course Design

Use this phase-3 skill only after a Learner Profile and Source List have been explicitly confirmed. Build, in order: outcomes; a principle and misconception map; vocabulary; a module plan; a diagnostic; and a gate check. Keep the misconception map and diagnostic private until the learner approves the presented course design.

## When to Use

- Use after the learner has confirmed the Learner Profile and approved the Source List.
- Use to produce outcomes, a module sequence, and a misconception-informed diagnostic before instruction begins.
- Do not use for intake, source approval, progress-file resumption, or delivery of Module 1.

## Prerequisite Gate

Before designing, confirm that the learner has approved:

- a Learner Profile containing topic/scope, background, observable goal, and time budget; and
- a Source List with stable `S` identifiers.

If either is absent or unconfirmed, return to the learner-intake workflow. Do not design the course yet.

## 1. Write Outcomes

Create **3–6** numbered outcomes: `LO-1`, `LO-2`, and so on.

- Start each with **“You will be able to…”**
- Describe an observable action, not exposure to information.
- Tag each with one level: **remember, understand, apply, analyze, evaluate,** or **create**.
- Test each against the learner’s stated goal. Do not add an outcome only because the source includes it.
- Include at least one outcome at **apply** level or higher.
- Make the last outcome the learner’s own goal expressed as a concrete task.

## 2. Build the Principle and Misconception Map

Create a private map of the ideas the course must teach correctly. Every row must use one of these kinds:

- **principle** — a correct idea or skill on which an outcome depends. It requires a citation to an approved source.
- **misconception** — a specific incorrect belief learners may hold.

Use this row structure:

| id | kind | statement | tier | citation | module |
|---|---|---|---|---|---|
| `short-kebab-id` | misconception | One sentence stating the incorrect belief. | 1 | `S1`, section 3.2 | `M2` |

### Misconception evidence tiers

| Tier | Meaning | Evidence method |
|---|---|---|
| **1** | An approved source names the mistake. | Scan for wording such as “a common mistake,” “students often think,” “note that this does not mean,” or “a frequent error.” |
| **2** | Education research or instructor material establishes the mistake as common. | Search for `common misconceptions <topic>`; prefer discipline-based education research and instructor guides. Open and inspect every source before using it. |
| **4** | Your inference without a source. | Record it only as a hypothesis to watch for. |

There is **no tier 3**. A misconception becomes “held by this learner” only when their diagnostic response or later statement supplies evidence. Record that learner-specific evidence in the progress record, not in this design.

### Quarantine tier 4

A tier-4 misconception may inform a prediction question or observation. Never challenge it directly unless this learner has shown it.

Aim for at least three tier-1 or tier-2 misconceptions. If fewer are supported, do not pad the map with guesses. Tell the learner the evidence about common sticking points is thinner, then continue.

## 3. Set Vocabulary Boundaries

Create two lists:

- **Assumed vocabulary:** terms the learner’s confirmed background supports.
- **Taught vocabulary:** terms that the course will introduce, with the module where each appears.

Every term in a question must be assumed or taught before that question. A question using an untaught term is unanswerable, not difficult.

## 4. Plan the Modules

Fit the design to the confirmed time budget. Usually plan **3–8 modules**, one per **20–40 minute** session. Put prerequisites first so that module `M(k)` builds on prior modules.

For each module, specify:

1. **Title** and the outcomes it serves.
2. **Anchor question:** one concrete opening problem the learner should answer by the end, preferably connected to their goal.
3. **Principles taught** and **misconceptions targeted**, by map ID.
4. **Practice:** the problem or task types the learner will do. For mathematics and computer-science instruction, apply the dedicated practice-design workflow when available.
5. **Transfer task:** one application to a new case, preferably from the learner’s own work or study context.

### For agentic-workforce courses

Make the learner’s own selected workflow the capstone from the first build session onward. Use a common workflow only for demonstrations, troubleshooting, or a tightly bounded readiness test; do not substitute it for transfer to the learner’s work.

Treat a preferred agent environment as a reference implementation and alternative harnesses as adapters. Require every adapter to produce the same observable learning evidence rather than assuming feature parity.

Turn setup into an operational readiness gate. Require learners to demonstrate the active role/environment, role-specific workspace and source access, a durable handoff artifact with provenance and uncertainty, an explicit human approval record, and an inspected downstream artifact. Do not treat a model’s success claim or conversational context as evidence that a role can execute, share authority, or safely hand off work.

Keep role contracts, output locations, handoff schemas, and approval criteria as durable project artifacts. Require a human approval boundary before consequential external actions; instructions alone do not enforce one.

Additional rules:

- From `M2` onward, open with a brief retrieval check from earlier modules.
- Make the final module a capstone that applies the whole course to the learner’s goal.
- Ensure every module serves at least one outcome and every outcome is served by at least one module.

## 5. Write the Private Diagnostic

Prepare **3–5** multiple-choice pretest items. Its purpose is to determine which mapped misconceptions this learner actually holds, while supporting learning even when answers are incorrect.

For every item:

- Include exactly one correct option.
- Make each incorrect substantive option a specific mapped misconception and record its ID.
- Include **“I don’t know.”** Do not force an answer that could manufacture a belief.
- Ask for confidence: **guessing, fairly sure,** or **confident**.
- Preserve format neutrality: do not emphasize the correct answer; rotate its position; use comparable option length and detail; and avoid an obvious wrong-to-right order.
- For math, derive each wrong numerical option from a named misconception or error. Compute each value with an appropriate calculation tool before use.
- Include each misconception scheduled for a head-on challenge as a wrong option in at least one item. If it cannot work as an item option, use it only in prediction questions.

Do not reveal items or the misconception map before design approval.

## 6. Gate Check

Before presenting anything to the learner, repair every failed condition:

- [ ] Every outcome supports the learner’s goal.
- [ ] At least three tier-1 or tier-2 misconceptions exist, **or** the learner is told the evidence is thin.
- [ ] Every misconception planned for direct challenge appears in a diagnostic item.
- [ ] No tier-4 misconception is scheduled for direct challenge.
- [ ] Every module serves an outcome, and every outcome is served by a module.
- [ ] Every principle cites an approved source.
- [ ] The modules fit the confirmed time budget.
- [ ] Vocabulary prerequisites are satisfied for every diagnostic and module question.

## 7. Present Only the Approval Summary

Show the learner the following and ask them to approve or change it:

```text
COURSE DESIGN — <title>
Goal: …
Outcomes: LO-1 … (level), LO-2 …
Modules:
  M1 <title> — anchor question: … — serves LO-…
  M2 …
Sources: S1 …, S2 …
Next: a short diagnostic (3–5 questions, about 5 minutes), then Module 1.
```

Do not show the misconception map or diagnostic items. Say:

> I’ve also prepared a short diagnostic and a list of common sticking points I’ll watch for. You’ll see them after the diagnostic.

If the learner requests changes, revise the design and present the summary again. Do not begin the diagnostic until they approve. After approval, assign a short lowercase hyphenated course slug, such as `intro-probability`, for use in the progress record.

## Verification

Complete this skill only when:

- [ ] The learner has approved the course design summary.
- [ ] A course slug exists.
- [ ] The private map and diagnostic comply with the gate check.
- [ ] The next action is the approved 3–5 item diagnostic, not premature module delivery.
