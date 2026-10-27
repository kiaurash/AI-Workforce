# M1 — Contract Field Guide (tutor reference)

For the tutor. It gives, for each field of `employees/first-employee.md`, the question to ask, what a good answer looks like, a weak answer to watch for, and a follow-up that moves the learner without supplying the answer.

## How to use this guide

- Ask **one field at a time**, and ask the question before showing anything.
- If the learner's Workflow Card or M0 Opportunity Map already answers the field, read it back and ask them to confirm or sharpen it. Do not re-ask a question they have answered.
- Use the faded-example approach: show the example for *one* field, ask the learner to write the next field, then withdraw support. Do not reveal the full example contract up front.
- The "good example" column is **illustrative**. It comes from the facilitator demonstration (the Meeting Commitment Extractor on `demo/fixtures/m1-demo-meeting.md`). It is not the only valid answer, and a learner's domain will change the wording. Never paste it as the learner's answer.
- After the learner drafts a field, test it with the follow-up. Accept an answer that survives the follow-up, even if the wording differs from the example.
- The contract is read by the Builder at run time, and it is the only instruction file the Builder may read besides the representative input. Write each field so a reader with no other context could act on it.

## The fields

### 1. Employee name and version

**Ask:** "What would you call this employee so that its job is obvious from the name?"

**Good example:** `Meeting Commitment Extractor`, contract version `0.1`.

**Weak answer:** A persona such as "Sage, my friendly assistant."

**Follow-up:** "If a colleague saw only the name, what would they expect it to produce?" A name is a label for a responsibility, not a personality.

### 2. Mission

**Ask:** "In one sentence, what outcome does this employee own, and what file would exist if it went perfectly?"

**Good example:** "Turn one meeting transcript into an evidence-linked register of confirmed commitments that I can review in five minutes."

**Weak answer:** "Help me with meetings and follow-ups."

**Follow-up:** "Could you tell whether that mission was achieved by opening one file?" If not, the mission is an activity, not an outcome.

### 3. Trigger

**Ask:** "What event starts this work, and who starts it?"

**Good example:** "I save a new transcript as `inputs/representative-input.md` and ask the Conductor to run the M1 task. This is a manual trigger; nothing starts it automatically."

**Weak answer:** "Whenever it's needed."

**Follow-up:** "Could someone else start this run from your description alone?" In M1 a manual trigger is correct; scheduled triggers come later.

### 4. Authorized input

**Ask:** "Which exact files may this employee read, and which files must it never read?"

**Good example:** "It may read this contract (`employees/first-employee.md`) and `inputs/representative-input.md`. It may not read anything else."

**Weak answer:** "My project folder."

**Follow-up:** "If the folder also held a confidential file, would this wording let the Builder read it?" Name exact paths. The contract itself is always a permitted read; the Builder may not edit it.

### 5. Permitted actions

**Ask:** "List what the employee is allowed to do. Which action would you be uncomfortable seeing it take that is not on your list?"

**Good example:** "Read the two authorized files. Write `outputs/first-proposal.md` and `runs/m1-first-run-receipt.md`. Create or update `runs/m1-workshop-manifest.md`."

**Weak answer:** "Analyze the transcript and do whatever helps."

**Follow-up:** "Which of those verbs touches something outside your two output paths?" Permissions should be a short, checkable list.

### 6. Prohibited actions

**Ask:** "What must it never do, even if it believes that would help?"

**Good example:** "Do not edit the transcript or this contract. Do not contact anyone or use any external system. Do not update any tracker. Do not invent owners, dates, or quotations. Do not create other files."

**Weak answer:** "Be careful and don't do anything risky."

**Follow-up:** "Could you tell, from a saved file, whether it broke that rule?" Each prohibition should be something you can verify. Name the cohort-one external actions explicitly: send, publish, purchase, update authoritative records.

### 7. Required output and path

**Ask:** "What exactly should the output look like, where does it go, and what must it contain?"

**Good example:** "`outputs/first-proposal.md`: a Markdown table with columns Owner, Commitment, Final agreed due date, Supporting quote, and Note. Below it, a separate section titled 'Conditional, unassigned, or rejected ideas', with each item labeled."

**Weak answer:** "A summary of the meeting."

**Follow-up:** "If two different employees produced two files from this description, would you know which one was right?" Specify structure so a deviation is visible.

### 8. Evidence rules

**Ask:** "What must the employee show you so that you can trust each claim without re-reading the whole source?"

**Good example:** "Every row carries a verbatim quotation from the transcript. If a deadline was revised and accepted, use the final date and note the earlier one. A row without a quotation is not allowed."

**Weak answer:** "Make sure it's accurate."

**Follow-up:** "How would you check 'accurate' in five minutes?" Evidence is something a reviewer can find: a quotation, a line number, a section.

### 9. Uncertainty rules

**Ask:** "What should it do when the source is missing, ambiguous, or conditional?"

**Good example:** "Write `unknown` for any missing owner or date. Keep weekday deadlines relative and mark the calendar date `unknown`. Words such as 'if', 'could', or 'might' mean the item is conditional and never goes in the commitments table. If unsure, list it in the separate section with the reason."

**Weak answer:** "Use its best judgment."

**Follow-up:** "What would you rather see: a confident guess, or the word `unknown`?" This field is where the demonstration's planted failure lives. Link it to the learner's own run if one has happened.

### 10. Human review and approval boundary

**Ask:** "What stays provisional until you have looked at it, and what are you keeping for yourself?"

**Good example:** "Nothing in the proposal is relied on or copied into a tracker until I have read it against the transcript. Following up with a participant (for example, asking for a missing date) is mine to do, outside this workflow."

**Weak answer:** "I'll glance at it."

**Follow-up:** "Which action in your workflow is the most consequential, and who has authority to perform it?" In cohort one, every external or consequential action is human-only.

### 11. Completion criteria

**Ask:** "How will you know the Builder is finished, and how will you check it without taking its word?"

**Good example:** "Done when both files exist, the table and the separate section are present, and the receipt lists what was left `unknown`. I check by opening the files. The Builder saying it is done does not count."

**Weak answer:** "When it tells me it's done."

**Follow-up:** "If the Builder said 'done' but the file was missing, which line of your contract would reveal that?" Completion must be verifiable from saved artifacts.

## Then ask the contract challenge

After the learner has drafted all eleven fields:

> What could the Builder do incorrectly while technically following this contract, and what one rule would reduce that risk?

Accept a rule that targets a specific, observable gap. If the learner says nothing could go wrong, ask them to predict how the Builder would treat a statement such as "we'll get someone to review the numbers next week."

## Time and sequencing notes

- Eleven fields in about seven minutes is tight for a first-timer. Fields 1, 3, and 5 usually take seconds. Spend the time on 6, 8, 9, and 10, which are where contracts most often fail.
- If time runs short, accept a draft of fields 1–5 and the learner's own words for 6 and 8–10, then continue to the run. Record the incomplete fields as `todo` and revisit them in the inspect step. Do not let the learner run the Builder without a prohibited-actions list and a stated output path.
- The contract is a specification, not a lock. It guides the Builder; it does not technically prevent an action. Say so if the learner treats it as protection.
