# M1 — Practitioner Demonstration

## Title

The Confident but Incorrect Meeting Commitment Extractor

Duration: 6 minutes in class  
Purpose: Demonstrate a runnable AI responsibility, inspect a plausible failure, and improve instructions based on evidence.

## Preparation

Use the M0.5 fictional transcript in:

`inputs/sample-meeting.md`

If unavailable, the facilitator should use a transcript with:

- Explicit commitments.
- Revised deadlines.
- Tentative suggestions.
- Unassigned ideas.
- Conditional follow-ups.

The builder harness must have access only to the designated training workspace for this exercise.

## Part A — The naive assignment

Open a fresh bounded agent session and submit:

> Read inputs/sample-meeting.md. List the actions people discussed, with owners and due dates. Write your answer to outputs/demo-first-attempt.md.

This instruction is deliberately underspecified. It does not adequately distinguish:

- Suggestions from commitments.
- Initial dates from revised dates.
- Conditional intentions from confirmed dated actions.

## Part B — Plausible flawed result

A failure example for learners to inspect:

| Owner | Action | Due date |
| --- | --- | --- |
| Jordan | Summarize five onboarding failures | October 20 |
| Leo | Draft revised onboarding screen | October 21 |
| Priya | Send three customer examples | October 19 |
| Priya | Create a tutorial video | Next month |
| Jordan | Redesign entire setup flow | Not stated |

This is an illustrative incorrect output. Actual model behavior can differ.

## Part C — Guided Socratic challenge

Show the original transcript and the flawed output.

Ask:

"Which rows are evidence-backed commitments, and which are the model's interpretation of ideas?"

Wait for responses.

If learners notice the invented video assignment, ask:

"What language in the meeting indicates that the video was approved?"

If they notice the incorrect screen deadline, ask:

"Which statement establishes the final agreed date?"

Do not correct every problem immediately. Allow learners to find at least one.

## Part D — Revised bounded employee contract

### Employee

Meeting Commitment Extractor

### Mission

Convert meeting transcripts into a reliable, evidence-linked record of confirmed commitments.

### Authorized input

`inputs/sample-meeting.md`

### Permitted actions

Read the supplied transcript and create a proposed Markdown output.

### Prohibited actions

Do not edit the transcript, update project-management systems, contact participants, invent facts, or treat meeting suggestions as approved work.

### Evidence requirements

For each confirmed action include the owner, action, final agreed deadline if available, and a supporting source quotation.

### Uncertainty rules

Keep proposals, ambiguous assignments, and conditional intentions separate from confirmed dated commitments.

### Deadline handling

If a due date changes during the conversation, use the final agreed date. Do not present an earlier proposal as the active deadline.

### Human boundary

The human reviews the register before it is relied upon or transferred into an authoritative tracking system.

### Output

`outputs/demo-corrected.md`

### Completion

A readable Markdown register exists and distinguishes confirmed actions from unapproved ideas.

## Part E — Improved assignment

Copy to the builder harness:

> You are a Meeting Commitment Extractor.
>
> Read only inputs/sample-meeting.md.
>
> Produce a Markdown table of confirmed meeting commitments with columns: Owner, Commitment, Final agreed due date, Supporting quote.
>
> Use the final agreed date if a deadline was revised. Never invent an owner or deadline. Exclude unapproved suggestions from confirmed commitments.
>
> Add a separate section called "Conditional follow-ups and unassigned ideas" when relevant. Label those items clearly.
>
> Write the result to outputs/demo-corrected.md.
>
> Do not modify the source, send messages, or access external systems. Stop after creating the proposed output for human review.

## Part F — Expected corrected outcome

Confirmed commitments:

| Owner | Commitment | Due date |
| --- | --- | --- |
| Jordan | Summarize five common onboarding setup failures | October 20 |
| Leo | Deliver revised onboarding screen | October 23 |
| Priya | Send three anonymized customer examples | October 19 |

Maya's conditional review may be recorded separately, with no invented calendar due date.

The tutorial video and entire-flow redesign are not assigned commitments.

Each confirmed row should include a quotation or evidence reference.

The facilitator should verify the actual corrected result rather than assuming the new instruction always works.

## Part G — Reflect on the design lesson

Ask:

"Was the first problem that we needed another AI employee, or that our first employee lacked a sufficiently clear contract?"

Expected insight:

The observed failure can be addressed initially through improved definitions, evidence rules, and review—without introducing a second employee.

Do not imply that better instructions alone guarantee reliability.

## Optional edge case for early finishers

Add this line near the end of an otherwise comparable fictional transcript:

> We'll get someone to review the numbers next week.

Ask learners to predict how the extractor should handle it.

A defensible response should mark the owner and timing as uncertain rather than invent them.

## Facilitator preparation record

Before class, record:

- Harness and version/interface.
- Sample input used.
- Actual first-run output.
- Observed failure.
- Contract change.
- Actual corrected output.
- What improved and what did not.

Never present the illustrative failed output as an actual observed execution trace.

## Demonstration completion standard

Learners can explain:

1. Why the first instruction was insufficient.
2. What evidence supports a confirmed commitment.
3. How a revised deadline should be handled.
4. Why human review still matters after the correction.
5. Why adding another agent is not automatically the right response.