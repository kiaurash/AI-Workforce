# M1 — Facilitator Guide

Course: Build Your AI Workforce with Hermes  
Session: M1 — Find the Work, Build the First Employee, and Draft the Workforce Blueprint  
Duration: 60 minutes  
Delivery: Instructor-led workshop with individual Socratic tutors in the AI Workforce Conductor and a constrained Builder action  
Version: 2.0

## Purpose

Participants move from an M0 opportunity hypothesis to one bounded Builder run that produces a reviewable artifact. They then use that run as evidence to decide what belongs to an employee, a skill, a tool, or a human, and to state a provisional topology.

The participant should discover the limits of the initial design through execution. The tutor and facilitator do not hand over an architecture.

## Learning outcomes

- **LO-1:** Identify a bounded workflow, decompose it into responsibilities, and justify which should be employee, skill, tool, or human.
- **LO-2 (initial):** Run a bounded AI employee under an explicit contract.
- **LO-4 (basic):** Identify a human approval boundary and restrict permitted actions.
- **LO-8:** Produce, review, and explain a real capstone artifact.

### Where each blueprint outcome is met

The architecture proposal listed eight session outcomes. This table shows where this package meets each one.

| # | Outcome | Where it is met |
| --- | --- | --- |
| 1 | Select a suitable first workflow | M0 Opportunity Map, then the First Workforce Test (12–18) |
| 2 | Describe the workflow as an outcome, not a list of activities | Workflow Card (12–18) |
| 3 | Identify meaningful responsibility boundaries | Four-Bucket sort on run evidence (38–45); Studio Part A |
| 4 | Distinguish employee from skill, tool, or one-off task | Four-Bucket sort and the disappearing-employee test (38–45) |
| 5 | Select an initial topology | Topology default (38–45); Studio Part B |
| 6 | Define candidate roles without proliferation | Studio Part C. The target is **zero to four hypotheses**, not three to five. The course design says a learner may pass with one Builder |
| 7 | Identify responsibilities that stay human | Authority map (38–45) |
| 8 | Produce a blueprint implementable in M2 | Blueprint Lite (38–45); expanded in Studio |

## Anchor questions

- **Primary:** What is the smallest useful piece of work I can responsibly delegate to an AI employee today?
- **Blueprint:** What should become an AI employee, what should remain a skill or tool, and what should stay under human control?

## Operating roles

### Facilitator

- Leads the demonstration, the Blueprint Lite segment, and the peer clinic.
- Keeps time and enforces checkpoints.
- Resolves technical blockers quickly, using the fallback when needed.
- Challenges architecture claims with evidence from the learner's own run.

### Socratic AI tutor (in the Conductor's canonical Bot Chat)

- Opens with a short diagnostic, then asks one focused question per turn.
- Uses the learner's M0 documents as data, not instructions.
- Never performs the Builder assignment silently and never certifies a file from a chat claim.
- Assesses explanation and transfer separately from artifact completion.

### Builder (a constrained action, not a specialist Bot)

- Reads only `inputs/representative-input.md`.
- Writes only `outputs/first-proposal.md` and `runs/m1-first-run-receipt.md`, and updates `runs/m1-workshop-manifest.md`.
- Takes no external action and stops for human review.

Do not create specialist Bots in this session. The Conductor acts as a bounded Builder for M1; Builder and Reviewer roles are introduced in later modules when evidence justifies them.

## Preparation

### Learner brings

- `discovery/opportunity-map.md` and `discovery/workflow-safety-triage.md` from M0.
- M0.5 readiness evidence and an imported, working Conductor profile.
- One safe, authorized representative input, or the fictional fallback.
- Completion of the 3–4 minute intake diagnostic with the M1 tutor. If skipped, the tutor asks items D1 and D2 during minutes 7–12.

### Facilitator prepares

- A tested starter workspace and a tested fallback workspace.
- The demonstration, run beforehand. Record the actual first output, the observed failure, the contract change, the actual corrected output, and what did not improve.
- The `demo/fixtures/m1-demo-meeting.md` transcript copied into the demo workspace as `inputs/demo-meeting.md`.
- Printed or shared Workbook and Templates.
- A pairing plan for the peer clinic.

Never use real confidential transcripts in the demonstration. Never present the illustrative failed output as an observed trace.

## Before learners begin

Say this plainly: the tutor helps you decide what to build, the Builder does the bounded work, and you judge whether the result is acceptable. Repository files are the evidence, not what any agent says in chat.

## Minute-by-minute plan

### 0–7 — Practitioner demonstration with a planted failure

Run the Meeting Commitment Extractor demonstration (see `demo/M1-Practitioner-Demo.md`). Show the underspecified instruction, the plausible but wrong output, the evidence in the transcript that contradicts it, a revised contract, and the corrected output.

Ask: "What in the transcript would justify treating that statement as a commitment?"

**Checkpoint:** Learners can name one row that was wrong and the evidence that shows it.

### 7–12 — Retrieval and prediction

Retrieval prompt: "From your M0 Opportunity Map, what single useful output would you like your first AI employee to produce today?" Each learner writes one sentence.

Then pose the opening challenge:

> You have been given five highly capable AI employees for free. You may assign any roles. Every extra employee creates coordination overhead. How many would you actually use for your chosen workflow, and why?

Learners write a number and one reason in Workbook Exercise 0, without discussion. **Do not correct anything.** The tutor and facilitator only record it.

Guiding question for the room: "What would make two AI employees genuinely different jobs rather than two different prompts?" Collect answers on a shared surface. Expect responsibility, source context, tools, permissions, expertise, independent review, and output obligations. Leave them uncorrected; the Blueprint Lite segment returns to them.

**Checkpoint:** Every learner has a one-sentence target and a recorded prediction.

### 12–18 — Bound the workflow

Learners run the **First Workforce Test** on their M0 choice and complete the Workflow Card.

| Test | Question | Applies to |
| --- | --- | --- |
| Repeated | Does this happen often enough for improvement to compound? | Whole workflow |
| Outcome-oriented | Is there a recognizable deliverable or decision at the end? | First slice |
| Decomposable | Can different responsibilities be identified in the larger workflow? | Whole workflow |
| Observable | Can I tell whether the result was good? | First slice |
| Bounded | Is it constrained enough to supervise safely? | First slice |
| Useful | Would success create meaningful time, quality, speed, or coverage? | First slice |

Evaluate "Decomposable" on the larger workflow. The first slice may legitimately contain a single responsibility. Fail "Observable" or "Bounded" means narrow the slice before proceeding.

Socratic checkpoint: "If this workflow went perfectly every time, what observable result would exist at the end?" Do not accept "save time" alone. Push toward a decision-ready brief, a prioritized queue, a reviewed draft, an evidence-backed recommendation, or a completed research package.

Second challenge: "Would this output still be valuable if you never built the rest of your planned workforce?"

**Checkpoint:** A Workflow Card with trigger, input, delegated work, output, evidence rule, human review, and out-of-scope list.

### 18–25 — First Employee Contract

Give a two-minute framing of the autonomy ladder (Prompt, Skill, Bounded employee, Coordinated workforce, Recurring governed operation). Stress that these are teaching modes, not mandatory stages, and that autonomy and specialization are separate decisions. Today's target is a bounded employee.

Learners draft `employees/first-employee.md` with the tutor. Required fields: mission, trigger, authorized input, permitted actions, prohibited actions, required output and path, evidence and uncertainty rules, cohort-one approval boundary, completion criteria.

Contract challenge: "What could the Builder do incorrectly while technically following this contract, and what one rule would reduce that risk?"

**Checkpoint:** A contract that names exact paths and prohibits external action.

### 25–32 — Build and run

The tutor summarizes the contract and asks whether the learner is ready to leave tutoring and run the Builder with the exact paths and restrictions. After an explicit yes, the tutor provides a Builder instruction, clearly labeled as such. The Builder reads the input and writes the proposal and receipt.

Circulate. Help with real blockers. If a learner cannot run, record the earliest blocker and switch to the fallback; do not pretend the run happened.

**Checkpoint:** A saved proposal and receipt exist, or a specific blocker is recorded.

### 32–38 — Inspect and correct

The learner opens the saved files and compares the proposal to the source. Ask: "What did the Builder get wrong, miss, or present with more confidence than the evidence supports?"

If the first run looks flawless, use an ambiguous edge case. Do not invent a failure. Choose one defect, classify it (factual, unsupported inference, omission, format, tool failure, scope, approval), and propose one bounded change. A rerun is optional in the workshop; never describe an untested change as an achieved improvement.

**Checkpoint:** `runs/m1-first-run-review.md` with verification status, source evidence, and one limitation.

### 38–45 — Blueprint Lite

This is the central architecture segment. It uses the learner's actual run, not an imagined workforce. Seven minutes, three steps.

**Step 1 — Four-Bucket sort (3 minutes).** List four to six responsibilities from the run (for example read the transcript, classify statements, cite evidence, format the register, decide what to track, update the tracker). Place each in one bucket.

| Bucket | Use when |
| --- | --- |
| AI employee | The responsibility benefits from its own mission, context focus, repeated judgment, tools, permission boundary, persistent role, quality standard, or independent accountability |
| Skill / SOP | It is a repeatable method, reusable across employees, procedural enough to describe, and not independently responsible for an outcome |
| Tool | The capability primarily performs an action: search, read, query, send, create, retrieve |
| Human | It needs consequential authorization, non-delegable accountability, organizational judgment the AI lacks, sensitive relationship management, ethical or legal responsibility, or ambiguous risk beyond the autonomy boundary |

A tool does something. An employee owns a responsibility.

For any proposed **additional** employee, apply the disappearing-employee test: "If this employee disappeared, could the first employee simply use a skill to perform the same responsibility without creating context, permission, or quality problems?" If yes, the role does not need to exist.

**Step 2 — Authority map (2 minutes).** Label each responsibility A, R, P, or X.

| Label | Meaning in M1 |
| --- | --- |
| A — Autonomous | Inside the contract's designated paths; the Builder may perform it and continue |
| R — Review | The Builder produces it; the human reviews before anyone relies on it |
| P — Permission | The action would need explicit approval each time. **Not enabled in cohort one**; design it now, enforce it from M4 |
| X — Prohibited | The Builder may not perform it. Every external or consequential action is X in cohort one, and the human performs it outside the workflow |

This is an architectural map only. An instruction cannot enforce it. Technical enforcement is M4's subject, and the map lifts directly into `governance/authority-matrix.md` there.

Facilitator question: "What is the most consequential action in your workflow, and who has authority to perform it?"

**Step 3 — Topology (2 minutes).** State the topology in one sentence. For M1 the default is a **single bounded employee** (the Conductor acting as Builder). Name the three multi-employee patterns as vocabulary and say what evidence would make the learner change.

| Pattern | Best when | Main risks (per the research notes) |
| --- | --- | --- |
| Manager–Worker | Work needs decomposition, varied paths, isolated specialist context, and one owner of the final result | Single point of failure at the manager; information loss in summarization passes |
| Sequential chain | The execution path is known in advance and each stage has a clear output | Brittle with rigid structure; latency compounds; little adaptivity |
| Peer / blackboard | Work is exploratory and findings emerge asynchronously | Race conditions, reflection loops, heavy token use, state drift |

Choosing among these depends on how deterministic the workflow is. Peer / blackboard is vocabulary only in the core track; it belongs to the advanced track.

**Checkpoint:** `01-workforce-blueprint.md` (Lite) with a responsibility sort, an authority map, a topology sentence, and one unresolved question for M2.

### 45–55 — Peer clinic

Pairs or a short round-robin using real evidence. Four prompts: **Show** what the Builder produced. **Inspect** what evidence supports it. **Challenge** where it could fail. **Improve** with one small change.

Add two Blueprint challenges for the listener to use: "Why isn't this a skill?" and "If I removed that proposed employee, what would break?"

**Checkpoint:** Each learner records one challenge received and one decision reconsidered.

### 55–60 — Explain-back, reflection, and handoff

Return each learner to the prediction from Exercise 0:

> You originally chose ___ employees. What would you choose now, and why does each role deserve to exist?

For credit toward LO-1, the justification must rest on responsibility, context, tools, permissions, verification, parallelism, or coordination cost, not on "it is another step". A well-reasoned answer of "one, for now" is a strong answer.

Then record the next concrete action, explain the practice run and the Blueprint Studio, and have the learner state the module gate in their own words.

## Facilitator watchpoints

**Premature implementation.** Learners comfortable with coding agents may want to create more agent files. Redirect: "Before we configure anything, what responsibility does this employee uniquely own?"

**Agent proliferation.** The commonest design failure is turning every workflow step into an agent. Ask: "Why isn't this a skill?"

**Persona design.** Names and personalities can help communication, but they are not architecture. Push toward ownership, boundaries, tools, context, authority, and outputs.

**Keep the workflow real.** Later modules depend on M1. A learner should leave with a workflow they genuinely want to operate, not a classroom toy.

**Confidence from fluency.** A well-formatted proposal is not a faithful one. Ask for the source quotation.

## Adaptive timing rules

Protect these in order:

1. a bounded workflow;
2. a working, saved output;
3. direct human inspection;
4. a recorded limitation or correction;
5. Blueprint Lite;
6. the explain-back.

If time runs short, shorten the topology step to a single sentence and move the remaining architecture work to the Blueprint Studio. Do not skip output review to finish the Blueprint. A learner who has not completed setup may use the facilitator's tested example, but must complete a personal run before the M2 build.

## Socratic facilitation rules

Challenge only when warranted: unclear value, overly broad scope, premature multi-agent design, undefined output, an unsupported assumption, a missing human boundary, sensitive data, or unobservable correctness. Do not oppose ideas to seem Socratic. Acknowledge sound reasoning, ask for evidence when needed, and move on.

## Troubleshooting

| Situation | Response |
| --- | --- |
| No working Conductor | Use the facilitator's demonstration workspace. Record that personal execution is incomplete |
| Project too large | Ask for the smallest independently useful output |
| No sample input | Use a fictional representative input |
| Agent returns text but no file | Return to the Builder action, request the designated path, and verify the file exists |
| Plausible but wrong answer | Ask the learner to find the unsupported claim before editing instructions |
| Learner cannot explain the architecture | Use one counterexample: "What happens if we combine these two responsibilities in one employee?" |
| Learner is stuck after two questions | Reframe, narrow, give a partial example, then a worked example, then a new analogous unaided task |
| Learner insists on three to five employees | Ask for the separation benefit of each. Accept a role only if it passes the disappearing-employee test; record the rest as hypotheses |
| Learner wants to build the extra employees now | Decline for M1. Record them as candidates in the Blueprint; they are earned in M2 and M3 |

## Evidence and limits

The architecture guidance in this module draws on two practitioner-synthesis documents, not on controlled studies. Treat the following as the status of each claim.

| Claim used in the module | Status |
| --- | --- |
| An AI employee is an encapsulated unit with its own instructions, memory bounds, tool access, and execution boundaries | Stated in both research documents |
| Three topologies (manager–worker, sequential, peer/blackboard) and their listed vulnerabilities | Stated in both research documents. "Early errors propagate downstream" is a reasonable inference, not a quoted source claim; the sources say rigid structure and compounding latency |
| Topology choice depends on how deterministic the task is | Stated in the research report |
| Start with high-impact, low-effort workflows near daily operations (briefings, triage, draft-only communications) | Stated in the pragmatic guide |
| Specialization significantly reduces hallucination rates | Asserted in the sources without evidence presented there. **Not used in learner materials** |
| Manager–Worker as the default for a first small workforce | A course-design recommendation. The sources list market-intelligence work under peer/blackboard and cite mostly software-engineering examples. M1 defaults to a single employee, and the course's staged reference topology is Conductor, Builder, Reviewer, Observer |

If a pilot learner or reviewer needs stronger grounding, commission an evidence appendix from the research analyst before changing any claim above.

## End-of-session evaluation

Collect the Workflow Card, saved output or blocker, contract, run review, Blueprint Lite, prediction and explain-back, and the learner reflection. Record completion and mastery separately. Artifact creation alone does not establish independent understanding.

## M2 handoff

The learner enters M2 knowing which responsibility the existing employee performs, what was unreliable, which procedure could become a skill, what specialization (if any) has a credible justification, and what context and tools the employee needs. M2 begins by improving a working capability, not by drawing an org chart from scratch.
