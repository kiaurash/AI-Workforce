# M1 — Practitioner Demonstration

## Title

The Confident but Incorrect Meeting Commitment Extractor

Duration: 7 minutes in class  
Purpose: Show a runnable AI responsibility, inspect a plausible failure, repair the contract from evidence, and set up the Blueprint Lite segment.

## Honesty rule

The "flawed result" in Part B and the "expected corrected outcome" in Part F are **illustrative**. Actual model behavior differs run to run. Before class the facilitator runs the demo, saves the real outputs, and fills in the preparation record at the end of this file. In class, say which outputs are real. Never present an illustrative table as an observed execution trace.

## Preparation

1. Copy `demo/fixtures/m1-demo-meeting.md` into the demo workspace as `inputs/demo-meeting.md`. The fixture is a fictional refund-delays meeting that learners have not seen. Do not use the M0.5 `sample-meeting.md`; learners already processed it.
2. The demo Builder may read only its saved contract and the fixture. Save the Part D contract as `employees/first-employee.md` in the demo workspace.
3. Keep the fixture's answer key out of sight until learners inspect the output.

## Part A — The naive assignment (about 1 minute)

Open a fresh bounded Builder session and submit:

> Read inputs/demo-meeting.md. List the actions people discussed, with owners and due dates. Write your answer to outputs/demo-first-attempt.md.

This is deliberately underspecified. It does not separate suggestions from commitments, initial dates from revised dates, or conditional ideas from assigned work.

## Part B — Plausible flawed result (about 1 minute)

An illustrative failure for learners to inspect:

| Owner | Action | Due date |
| --- | --- | --- |
| Ben | Pull and tag refund tickets | Tuesday noon |
| Chloe | Survey ten longest-waiting customers | Wednesday |
| Dev | Check payment provider status page | Wednesday |
| Unassigned | Review new refund policy | This week |

Four typical faults are planted: the stale deadline (Ben), a conditional idea promoted to an assignment (the survey), an invented date (Dev), and a rejected suggestion treated as a task (the policy review).

## Part C — Guided Socratic challenge (about 2 minutes)

Show the transcript beside the output. Ask:

> Which rows are evidence-backed commitments, and which are the model's interpretation?

Wait. Let learners find at least one fault before you name any. Prompts if they are stuck:

- On Ben: "Which statement establishes the final agreed date?"
- On Dev: "What in the transcript gives Wednesday?"
- On the survey: "What word in Chloe's sentence makes it conditional, and what did Ana decide?"
- On the policy: "What did Ana say about it?"

## Part D — Revised bounded employee contract (about 1 minute)

**Employee:** Meeting Commitment Extractor  
**Mission:** Turn a transcript into an evidence-linked record of confirmed commitments.  
**Authorized input:** this contract (`employees/first-employee.md`, read-only) and `inputs/demo-meeting.md`  
**Permitted actions:** Read the transcript; write one proposed Markdown register and one receipt.  
**Prohibited actions:** Edit the transcript, update any tracker, contact anyone, invent facts, or treat suggestions as approved work.  
**Evidence rule:** Every row carries owner, action, final agreed due date if one exists, and a supporting quotation.  
**Uncertainty rule:** Mark missing owner or date `unknown`. Keep conditional ideas, unassigned suggestions, and rejected suggestions in a separate, labeled section.  
**Deadline rule:** If a date is revised and accepted, use the final date.  
**Human boundary:** A human reviews the register before anyone relies on it or copies it to a tracker.  
**Output:** `outputs/demo-corrected.md`  
**Completion:** A readable register exists that separates confirmed commitments from everything else.

## Part E — Improved assignment (about 1 minute)

> You are a Meeting Commitment Extractor.
>
> Follow the contract in employees/first-employee.md. Read only that file and inputs/demo-meeting.md.
>
> Produce a Markdown table of confirmed commitments with columns: Owner, Commitment, Final agreed due date, Supporting quote.
>
> Use the final agreed date when a deadline was revised and accepted. Never invent an owner or deadline; write `unknown`. Keep deadlines relative if the transcript gives only a weekday.
>
> Add a separate section called "Conditional, unassigned, or rejected ideas" and label each item.
>
> Write the result to outputs/demo-corrected.md. Do not modify the source, send messages, or access external systems. Stop after writing the proposed output for human review.

## Part F — Expected corrected outcome (illustrative)

| Owner | Commitment | Final agreed due date | Note |
| --- | --- | --- | --- |
| Ben | Pull last month's refund tickets and tag delays by cause | Tuesday end of day | Revised from Tuesday noon; accepted by Ana |
| Chloe | Draft the survey questions | Wednesday | Assigned by Ana; acceptance not recorded |
| Dev | Check the payment provider's status page for incidents | unknown | Dev gave no date pending access |

Separate section: the ten-customer survey (conditional, deferred), and the new refund policy review (unowned suggestion; explicitly not this week).

The facilitator verifies the real corrected output rather than assuming the new instruction always works.

## Part G — Bridge to the Blueprint (about 1 minute)

Ask:

> Was our first problem that we needed another AI employee, or that our first employee lacked a clear contract?

Expected insight: the observed failure was repaired with a better contract, evidence rules, and human review, without adding a second employee. Do not imply that better instructions alone guarantee reliability; one corrected run is one observation.

Then show the Blueprint Lite for this run (see `M1-Worked-Example-Workforce.md`, Example 1). Point out that "format the register" and "cite evidence" ended up as skills, that "update the tracker" is X in cohort one, and that the topology is one bounded employee. This previews what learners do themselves at minute 38.

## Optional edge case for early finishers

Add this line near the end of the fixture:

> We'll get someone to review the numbers next week.

Ask learners to predict how the extractor should treat it. A defensible answer marks owner and timing as unknown and lists it as an unassigned suggestion.

## Facilitator preparation record (complete before class)

- Harness and version / interface:
- Fixture used:
- Actual first-attempt output (file path):
- Observed failure (quote the faulty row):
- Contract change made:
- Actual corrected output (file path):
- What improved:
- What did not improve or was still wrong:
- Date run and by whom:

## Demonstration completion standard

Learners can explain:

1. why the first instruction was insufficient;
2. what evidence supports a confirmed commitment;
3. how a revised deadline is handled;
4. why human review still matters after the correction; and
5. why adding another employee was not the first fix.
