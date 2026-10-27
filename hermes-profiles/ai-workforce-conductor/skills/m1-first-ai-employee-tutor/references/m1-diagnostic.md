---
course: m1-first-ai-employee
items: 4
created: 2026-10-25
---

# M1 — Intake Diagnostic

Four short items for the M1 tutor to run **before** teaching, one at a time. Each distractor maps to a registry id in `m1-misconception-map.md`. The diagnostic exists to find what this learner already believes, not to grade.

## Delivery rules

- Present one item at a time. Show the confidence scale with every item.
- Give **no feedback** between items. Do not say right or wrong. Say only "Thanks, next one."
- Allow "I don't know" without penalty and treat it as information, not a gap to correct.
- After all four, mint the learner's own record: for each distractor chosen, record `tier-3d: <registry_id>` and the stated confidence in the learner's `runs/m1-first-run-review.md` under "Learning record". Never write it into the shared map.
- Prioritize confident wrong answers over unsure ones. Address a held misconception through a prediction on the learner's own run evidence, at the segment listed in the map, never by lecturing at the start.
- If the learner chose the correct option with high confidence, do not spend time re-teaching it. Move to transfer.
- Run before the workshop (3 to 4 minutes). If that was not possible, use the 7–12 minute retrieval window and ask only D1 and D2.

### D1 — A claim of completion
outcomes: [LO-2, LO-8]

> The Builder replies in chat: "Done. I saved outputs/first-proposal.md with all the commitments and a clean summary table." What do you actually know at that point?

- (a) The file exists, because the agent said it saved it. <!-- registry_id=chat-is-proof -->
- (b) The agent claims the file exists; I know only after I open it and compare it to the source. <!-- correct -->
- (c) It is probably right, because the summary is detailed and well organized. <!-- registry_id=fluent-is-faithful -->
- (d) I don't know

**Confidence:** guessing / fairly sure / confident

### D2 — How many employees
outcomes: [LO-1]

> A weekly status brief involves gathering updates, ranking them, summarizing, formatting, and checking the claims. How would you start designing the AI side of this?

- (a) Five employees, one per step, so each step has an owner. <!-- registry_id=agent-per-step -->
- (b) One bounded employee that owns the brief, with formatting and ranking written as reusable procedures, and a second employee only if I can name a specific benefit such as independent checking. <!-- correct -->
- (c) As many specialists as I can assign, each with a distinct name and personality, since a bigger team is a stronger team. <!-- registry_id=persona-is-architecture -->
- (d) I don't know

**Confidence:** guessing / fairly sure / confident

### D3 — An approval rule
outcomes: [LO-4]

> A contract says "Always ask me before emailing a client." The agent has an email tool available. How safe is that boundary?

- (a) Safe, because the rule is written in the contract. <!-- registry_id=instruction-is-control -->
- (b) Not by itself. The instruction guides the agent but does not enforce anything; in this cohort the safer design removes external actions entirely, and real enforcement comes from a control outside the instructions. <!-- correct -->
- (c) Safe as long as the instruction is written in capital letters and repeated. <!-- registry_id=instruction-is-control -->
- (d) I don't know

**Confidence:** guessing / fairly sure / confident

### D4 — One corrected rerun
outcomes: [LO-2, LO-8]

> The first run mislabeled a suggestion as a commitment. You tighten the contract and rerun it. The second output is correct. What should you conclude?

- (a) The problem is fixed, so the employee is now reliable for this workflow. <!-- registry_id=better-contract-fixes-all -->
- (b) The fix helped on one case. I should test it on other inputs, including an ambiguous one, before relying on it. <!-- correct -->
- (c) The fix shows I need a second employee to catch errors like this, since more employees mean fewer mistakes. <!-- registry_id=more-is-better -->
- (d) I don't know

**Confidence:** guessing / fairly sure / confident
