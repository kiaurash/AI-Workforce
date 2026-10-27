# Build Your AI Workforce with Hermes

**Version:** 4.1 — Hermes Desktop reference design (draft revision: optional roles, minimum viable outcomes, value checkpoints)

**Status:** Facilitator-review draft

**Format:** M0 and M0.5 preparation; six 60-minute hands-on workshops; progressive learner-owned capstone

**Audience:** AI-savvy managers, entrepreneurs, technical leaders, and knowledge workers; no programming prerequisite

**Reference environment:** Hermes Desktop on Windows; macOS/Linux appendices and Claude/Codex adapters may be used only when they meet the same evidence and governance requirements.

---

## 1. Course promise

This course helps learners build, operate, inspect, and improve a small AI workforce for a real workflow they own. Learners do not build an abstract multi-agent demo. Every module improves the same capstone repository and produces an artifact that the learner can inspect.

By the end, each learner has a workforce that:

- addresses a meaningful workflow with a checkable output;
- begins with one useful bounded capability instead of unnecessary agent proliferation;
- uses reusable skills and specialized roles only when separation earns its complexity;
- passes work through explicit handoffs rather than invisible chat assumptions;
- stops at meaningful human approval boundaries;
- records run evidence, reviews, failures, and recovery;
- retains knowledge deliberately and with provenance; and
- proposes and tests improvements without self-authorizing production changes.

**Success is not agent count.** A learner may pass with one Builder if that is the safest and most valuable design.

### Supported workflow scope

The course supports both **knowledge-work** and **operational** workflows from the first cohort. Examples include research synthesis, meeting and project reporting, client intake, sales follow-up preparation, internal operations, and project management.

Operational authenticity does not remove governance: learner systems may prepare real drafts, evidence packets, proposed updates, and approval records, while consequential actions remain subject to the learner's defined human approval boundary.

---

## 2. Design principles

1. **Value before automation.** Start with a real responsibility, constraint, and useful output—not an org chart.
2. **Build early.** By M1, learners run a bounded task and inspect the saved artifact.
3. **One learner-owned system.** The same repository and real workflow progress through all modules.
4. **Evidence before confidence.** A fluent response or a chat claim is never proof that a file exists, a rule worked, or a workflow is reliable.
5. **Specialization must earn its place.** Add a separate role only for a clear benefit in expertise, context, permissions, independent verification, or justified parallelism. Every role is demonstrated in an experiment, but keeping it is a decision the learner justifies with evidence; a well-evidenced decision not to adopt a role is a successful result.
6. **Human authority precedes autonomy.** Agents can research, draft, and propose; humans retain consequential decisions, external commitments, money, sensitive people judgments, and production promotion.
7. **Repository-first operation.** Bot messages and agent responses coordinate work; saved contracts, artifacts, handoffs, review decisions, and approval records are authoritative.
8. **Improve from comparable evidence.** Observe, propose, test, compare, approve or reject, then monitor. Never let an observer self-promote a change.
9. **Structure must pay for itself.** Reliability, specialization, and governance have costs in time, setup, and attention. Each module asks whether the addition improved the workflow enough to justify its cost, and “remove it” or “simplify it” is a legitimate answer.

---

## 3. Hermes operating model

### 3.1 The artifact map

Every learner works with two distinct systems:

| System | Purpose | What belongs there |
| --- | --- | --- |
| **Hermes profile/Bot** | Isolated operating context for a role | model configuration, role-specific skills, curated memory, sessions, routines, tools |
| **Capstone repository** | Inspectable, shareable, reviewable course evidence | contracts, inputs, outputs, receipts, handoffs, reviews, approvals, logs, evaluation cases, knowledge records, and change proposals |

**Rule:** An important operational claim is complete only when an inspectable repository artifact supports it. Important changes to skills, contracts, durable knowledge, or operating controls require a human decision and recorded rationale.

### 3.2 Profile creation is not role activation

A Bot appearing in Hermes Desktop is configuration, not demonstrated capability. A role becomes operational only after it passes a role-specific smoke test under an explicit contract and a human records an activation decision.

### 3.3 Reference topology: earned, not mandatory

| Role | Responsibility | Authority |
| --- | --- | --- |
| **Conductor** | coordinates a repository-first run; verifies completion gates | cannot treat messages as proof or authorize consequential actions |
| **Builder** | produces a bounded proposed artifact and receipt | may write only designated proposed-output paths |
| **Reviewer** | independently challenges a supplied evidence packet | accepts, returns for correction, or escalates; cannot approve execution |
| **Observer** | analyzes approved historical evidence and proposes one testable improvement | cannot modify production skills/contracts or approve its own recommendation |
| **Human** | defines purpose, grants access, inspects evidence, authorizes consequential action and promotion | retains final authority |

The staged topology is:

| Stage | Default operating shape | Why |
| --- | --- | --- |
| M0.5–M1 | Conductor acting as a bounded Builder | prove one safe useful workflow first |
| M2 | Builder plus a reusable skill | repetition earns procedural memory |
| M3 | Conductor → Builder → Reviewer, run as an experiment | independent challenge is demonstrated; it is kept only if the evidence supports it |
| M4–M5 | governed operation using the roles the learner kept | controls and knowledge require operational evidence |
| M6 | Observer, run as an experiment | improvement is separated from production execution; adopting it is the learner's decision |

### 3.4 Hermes mechanisms

- **Hermes Desktop / Bot Mode:** durable named specialist profiles with their own role context, skills, memory, configuration, and canonical Bot Chat.
- **`message_agent`:** asynchronous Bot-to-Bot coordination from canonical Bot Chats. It is a trigger or notification, not the authoritative handoff.
- **`delegate_task`:** fresh-context, short-lived child work, appropriate for temporary source checks or bounded parallel research. It does **not** invoke an existing named Builder/Reviewer profile and does not create a hard filesystem, credential, or tool-permission boundary.
- **Cron routines:** optional recurring operation after a manual workflow is proven. A scheduled job must write repository evidence and preserve the same approval rules.
- **Skills:** reusable procedures. A skill is not a workforce itself; a Conductor skill can initiate the repository-first protocol among earned roles.

### 3.5 Demonstrate every role; keep only what earns its place

Every learner experiences each role's behavior, but no learner is required to keep a role permanently. For the Builder (M2), Reviewer (M3), and Observer (M6), the learner runs a **temporary role experiment** and then records a **Role Decision Record**.

An experiment is complete when the learner has:

1. run the role's activation test (§15) and a real task under an explicit contract;
2. recorded what the role caught, missed, or produced that the existing setup would not have, and what it cost in time, setup, and extra files;
3. considered a simpler alternative, such as a skill, a checklist, or human review; and
4. recorded a decision: **adopt**, **do not adopt**, or **defer pending more evidence**, with the evidence that would change the decision.

Rules:

- **Adopting and declining receive equal credit.** Assessment scores the reasoning and the evidence, not the outcome. A learner who keeps a Reviewer and a learner who drops it can both reach Level 3.
- **Declining must be evidence-based.** “I did not have time to try it” is not a decision. A decision requires a real run of the role and a recorded comparison.
- **The activation log records the result.** A role that is not adopted is logged as `not adopted` or `deferred` in `profiles/role-activation-log.md`, with a link to the Role Decision Record. The learner's capstone then uses only the roles they kept; the authority matrix, practice runs, and later modules cover those roles.
- **A learner may keep a role conditionally**, for example by using review only for high-risk runs, and must state the condition.

---

## 4. Course schedule and capstone evidence

| Module | Format | Hands-on focus | Required capstone evidence |
| --- | --- | --- | --- |
| M0 | Optional self-guided discovery | choose a workflow worth improving | Opportunity Map |
| M0.5 | Self-guided technical onboarding | Hermes Desktop, repository, Conductor safe-stop | readiness table, smoke-test output, blocked manifest |
| M1 | 60 min | first bounded AI employee | contract, saved output, receipt, run review |
| M2 | 60 min | repeatability, skills, earned specialization | `SKILL.md`, repeat-run comparison, role decision |
| M3 | 60 min | structured handoff and independent review | review packet, review decision, resolution record |
| M4 | 60 min | governance, evaluation, controlled recovery | authority matrix, adversarial test, scorecard |
| M5 | 60 min | governed organizational knowledge | knowledge record, provenance, promotion decision, retrieval test |
| M6 | 60 min | evidence-led improvement | observer proposal, baseline/candidate comparison, human decision |

Every formal workshop follows this pattern:

- 7 min: real practitioner demonstration and visible limitation/failure;
- 5 min: short retrieval prompt and guiding question;
- 33 min: guided work on the learner’s capstone;
- 10 min: peer clinic using actual evidence;
- 5 min: reflection, value checkpoint (§4.2), recorded next action, and module gate.

### 4.1 Minimum viable outcome for each workshop

Each workshop is designed around one **minimum viable outcome (MVO)**: the smallest evidence-backed result that proves the module's learning milestone. The MVO is the in-session gate. Items outside it are stretch work or between-session work, and a learner who reaches the MVO has met the module gate even if other artifacts remain open.

| Module | Must happen in the hour (MVO) | May move to between-session work | Evidence that counts as legitimate blocked progress |
| --- | --- | --- | --- |
| M1 | One saved output from a contract-governed run, inspected against its source with one recorded limitation, and an explanation of the retained human decision | a rerun, the fuller workforce Blueprint, and the first practice run | the drafted contract; direct blocker evidence; and an inspected facilitator-demonstration output with one recorded limitation |
| M2 | One skill extracted and tested on a second comparable input, with a written comparison and a Role Decision Record for the Builder | creating and activating a separate Builder profile, if the learner chooses one | the skill draft; the first-run artifacts; and blocker evidence for the second run |
| M3 | One review packet, one Reviewer disposition, and one resolution record, starting from a prepared Builder proposal and receipt if the learner's own are not ready | a second review cycle and the Role Decision Record write-up | the packet as assembled so far; blocker evidence; and the earliest failed step |
| M4 | An authority matrix for one workflow and one adversarial test with its observed result recorded (the stop test is mandatory and is not movable) | the full evaluation set, the scorecard, and the recovery record | the matrix; the adversarial case as written; and what the learner observed when running it |
| M5 | One sourced candidate knowledge record with provenance and a human promote, defer, or reject decision | a conflict and obsolescence test beyond the first, and further retrieval experiments | the record draft; the provenance fields completed; and blocker evidence |
| M6 | One Observer proposal or a correct `collect more evidence` disposition, plus a baseline and candidate comparison on at least two comparable cases | monitoring plan and isolated branch testing | the evidence window assembled; the Observer's output or blocker; and the learner's reasoning for the disposition |

**Legitimate blocked progress** always includes all three of the following, and a chat claim never substitutes for any of them:

1. a run manifest or equivalent status record;
2. direct evidence of the earliest blocker (a path, the error text, or the observed behavior), classified as a configuration, permission, tool, task, or quality failure; and
3. one attempted recovery step and its result.

A learner who submits all three has met the gate for the blocked state, and the catch-up clinic applies. A learner without blocker evidence, or with no attempted recovery, has not.

Where an MVO relies on facilitator-supplied material, the material is labeled as supplied in the learner's repository, and the learner does not represent it as their own run evidence.

### 4.2 Value checkpoint (every module from M1)

Every workshop includes a short **value checkpoint** inside the 5-minute reflection. It uses the same question each time:

> Did what we added in this module make the workflow better enough to justify what it cost?

The learner appends one entry per module to a single file, `runs/value-checkpoint.md`, using this form:

| Measure | Before this module | After this module |
| --- | --- | --- |
| Human time per run | estimate or range | observed range |
| Output usefulness | what the intended recipient needs | what the recipient or learner judged |
| Rework before relying on the output | typical corrections | corrections recorded |
| Overhead added | none | setup, checking, and maintenance minutes |
| **Judgment** | | keep, simplify, or remove, with one sentence of evidence |

Rules:

- Estimates and ranges are acceptable. Label each figure as an estimate or as measured, and do not manufacture precision from one or two runs.
- “Not worth it” is a valid judgment and may justify removing a role, a skill, or a control. For a control that guards a consequential action, the learner must name the risk it covers before removing it; the human approval boundary is never removed on cost grounds.
- Assessment checks that the judgment cites the learner's own run evidence. It does not grade the numbers.
- The M0 Opportunity Map or, if M0 was skipped, the M1 workflow card supplies the baseline estimate: how often the work happens, how long it takes, and who relies on it.

Module-specific prompts:

| Module | Value prompt |
| --- | --- |
| M1 | Is delegating this slice better than doing it myself or using a one-off prompt? |
| M2 | Did the skill reduce correction or time on the repeat run? |
| M3 | Did the Reviewer catch anything that justified its cost? |
| M4 | Are the controls proportionate to the risk they cover? |
| M5 | Did retrieving the record improve a task enough to justify keeping it current? |
| M6 | Did the change improve the baseline by more than it cost to test, and without regressions? |

### Required between-session practice runs

After M1–M5, every learner completes one **manual** 15–30 minute `practice-run` from the Conductor’s canonical Bot Chat or Desktop workspace. It reuses the repository-first contract, manifest, receipt, review, and approval artifacts taught in class. The Conductor records one status: `complete`, `blocked`, or `needs catch-up`; it does not grade an agent’s claim.

A blocked learner submits a minimum viable practice record: the run manifest, evidence of the blocker, and one attempted recovery step. A catch-up clinic supports completion before the next module. Cron scheduling is an optional advanced exercise only after the learner has demonstrated a manual workflow and an approval boundary.

### Cohort-one external-action policy

Cohort one supports authentic operational workflows but **prohibits live external execution** inside the course. Learners create real drafts, proposed updates, review packets, and approval records; the human performs any actual send, publication, purchase, authoritative-record update, or production action outside the course workflow. A later advanced lab may introduce live external execution only with facilitator review and a separately tested control model.

---

# Part I — Preparation

## 5. M0 — Socratic AI Workforce Opportunity Discovery

**Anchor question:** *Where would additional AI capacity create meaningful leverage, and what must remain human-owned?*

M0 is discovery, not architecture construction. The learner examines actual work episodes and creates an **AI Workforce Opportunity Map** containing:

- desired future human role;
- candidate workflows, constraints, and value hypotheses;
- a rough baseline for the recommended workflow (frequency, time per occurrence, and who relies on it), labeled as an estimate;
- a recommended first independently useful workflow;
- provisional AI responsibilities;
- responsibility and data-sensitivity boundaries;
- assumptions requiring validation; and
- a clear M1 handoff.

**Acceptance gate:** The learner can explain why the selected output matters, what its input and success criteria are, what is out of scope, and why the first slice is valuable even if no later workforce is built.

---

## 6. M0.5 — Hermes Desktop, Repository, and Conductor Readiness

**Anchor question:** *Can I prove that my local workspace and Conductor fail or succeed safely using inspectable evidence?*

**Reference materials:**

- [M0.5 Hermes Desktop onboarding workbook](AI-Workforce-Tutorials/M0.5-Hermes-Desktop-Onboarding/learner/M0.5-Workbook.md)
- [M0.5 starter workspace](AI-Workforce-Tutorials/M0.5-Hermes-Desktop-Onboarding/starter-workspace/README.md)
- [AI Workforce Conductor distribution](hermes-profiles/ai-workforce-conductor/README.md)

### Gate A — Desktop and repository readiness

The learner:

1. installs Hermes Desktop on Windows from the official Hermes Desktop page and completes local provider/model setup;
2. verifies one ordinary chat response;
3. opens the starter workspace in Hermes Desktop;
4. asks Hermes to read `inputs/sample-meeting.md` and create only `outputs/commitments.md`;
5. requires evidence for each claimed commitment, `unknown` for missing owners/dates, no external action, and a compact receipt listing files read, created, changed, and uncertainties;
6. independently opens the source and output in the Desktop file browser, checks the source is unchanged, spot-checks the commitments, and compares the receipt with observed files.

### Gate B — Conductor distribution readiness

The learner imports the single **Conductor** profile distribution, opens its canonical Bot Chat, and runs the Conductor activation test with an intentionally absent Builder receipt. The Conductor must create a run manifest with status `blocked`, identify the missing artifact, and avoid inventing completion, review, or approval.

### M0.5 completion evidence

- `outputs/commitments.md`, independently checked;
- Workspace Readiness Report/readiness table;
- `profiles/role-activation-log.md` entry for the Conductor; and
- a blocked run manifest.

The learner does not create Builder, Reviewer, or Observer in M0.5.

---

# Part II — Hands-on workshops

## 7. M1 — Find the Work, Build the First Employee

**Anchor question:** *What is the smallest useful piece of work I can responsibly delegate today?*

**Target outcome:** One bounded role produces one saved, reviewable output from a representative input. The learner identifies at least one actual limitation or uncertainty.

### Guided build

1. Select a one-sentence independently valuable output from the Opportunity Map.
2. Complete a workflow card: trigger, input, bounded work, output, evidence rule, human review, out-of-scope work.
3. Complete a first employee contract:
   - mission and trigger;
   - authorized input and permitted actions;
   - prohibited actions;
   - required output and destination;
   - evidence and uncertainty rules;
   - human approval boundary; and
   - completion criteria.
4. Run the bounded Builder task in the learner’s workspace. The Builder may read only its own contract (read-only) and the designated input, and write only the proposed artifact and receipt.
5. Inspect the saved result against source material, record one defect/unknown/edge case, revise one rule if justified, and rerun if practical.
6. Create a Blueprint Lite from the run evidence in `01-workforce-blueprint.md`: a responsibility sort (employee, skill, tool, or human), an authority map (autonomous, reviewed, approval-required, or prohibited), and a starting topology. Candidate future roles are recorded as hypotheses only.

### M1 evidence and gate

- `01-workforce-blueprint.md` (Blueprint Lite);
- `employees/first-employee.md`;
- `inputs/representative-input.md`;
- `outputs/first-proposal.md` and `runs/m1-first-run-receipt.md`;
- `runs/m1-first-run-review.md` with evidence of verification and one observed limitation; and
- the first `runs/value-checkpoint.md` entry.

The in-session gate is the minimum viable outcome in §4.1. The package under `AI-Workforce-Tutorials/M1-First-AI-Employee/` governs the detailed file paths.

A saved artifact is necessary but insufficient: the learner must explain the value, boundary, limitation, and retained human decision.

---

## 8. M2 — Make Work Repeatable: Skills and Earned Specialization

**Anchor question:** *What repeated procedure deserves a reusable skill, and what would a separate role add?*

### Practitioner demonstration

Show a generalist handling conflicting research and review instructions. Improve it first with a reusable procedure, then show the point at which distinct context, permission, independent verification, or parallelism would justify separation.

### Guided build

1. Review the M1 run review and select one procedure that recurs or required non-trivial correction.
2. Extract it into a `SKILL.md` with a clear trigger, inputs, steps, evidence/quality checks, escalation rule, and completion rule.
3. Repeat the workflow with comparable input and compare the two runs.
4. Record a Role Decision Record (§3.5) for the Builder: remain with one role, or create a separate Builder profile because the benefit is demonstrable.
5. If a Builder profile is created, perform its activation test: read only the designated input, write only the proposal plus receipt, and record the human activation decision.

### M2 evidence and gate

- one tested `SKILL.md`;
- repeat-run comparison;
- updated employee contract and tool/path boundaries;
- Builder activation log, if a separate Builder is used;
- a Role Decision Record for the Builder (adopt, do not adopt, or defer), which receives equal credit for any of the three when the reasoning is evidence-based; and
- a `runs/value-checkpoint.md` entry.

Do not create a second role merely because the curriculum contains one.

---

## 9. M3 — Coordinate Through Evidence: Builder to Reviewer

**Anchor question:** *How can two roles collaborate without carrying each other’s unstated assumptions?*

**Core topology:** Conductor → Builder → Reviewer, run as a temporary role experiment (§3.5). The learner sees what independent review does and then decides whether it earns a permanent place in their workflow.

### Practitioner demonstration

Show a Builder producing a plausible artifact and a deficient handoff. Show a downstream role accepting an unsupported claim. Repair it by requiring a minimal packet and a structured review decision.

### Guided build

1. The Conductor creates `runs/<run-id>/` and a manifest.
2. The Builder saves its proposed artifact and run receipt before signaling the Conductor. If the learner's own Builder proposal and receipt are not ready, the facilitator supplies a prepared pair, labeled as supplied, and the learner begins at step 3.
3. The Conductor creates `handoffs/review-packet/` containing only:
   - employee contract;
   - named source input(s) or read-only copies;
   - proposed artifact; and
   - `handoffs/builder-to-reviewer.md`.
4. The Reviewer receives only packet paths and a focused task, not the Builder’s conversation, tool output, private notes, or recommended disposition.
5. The Reviewer writes `reviews/review-decision.md` with exactly one disposition:
   - **accept**;
   - **return for correction**; or
   - **escalate to human**.
6. The decision cites packet evidence, records uncertainty, and does not alter the proposal, source, contract, memory, skills, approval records, or external systems.
7. The learner resolves the decision without silently overwriting the original proposal.
8. The learner records a Role Decision Record for the Reviewer: keep it permanently, keep it conditionally (for example, for high-risk runs only), or do not adopt it, citing what the review caught or missed and what it cost.

### M3 boundary lesson

A fresh `delegate_task` conversation provides conversational isolation but not hard workspace, credential, or tool isolation. Bot-to-Bot messages are asynchronous coordination signals, not authoritative handoffs. The packet and saved repository artifacts define the evidence boundary. High-sensitivity variants require separate access-restricted staging and read-only tool controls.

### M3 evidence and gate

- run manifest;
- Builder proposal and receipt;
- minimal review packet;
- `review-decision.md` with cited evidence;
- decision-resolution record;
- Reviewer activation log, with the activation decision recorded as `adopted`, `not adopted`, or `deferred`;
- Role Decision Record for the Reviewer (may be completed between sessions); and
- a `runs/value-checkpoint.md` entry.

The Reviewer’s acceptance never authorizes a consequential action; the human approval boundary remains intact.

**Advanced variant:** Add a Researcher/Extractor only when separate source sets, time sensitivity, or independently collected evidence justify parallelism.

---

## 10. M4 — Govern, Measure, and Recover

**Anchor question:** *How do I know whether the workforce is reliable, and how do I prevent a failure from causing harm?*

### Guided build

1. Define an authority matrix for every action, covering the roles the learner kept and the human: propose, review, approve, execute, and log.
2. Specify at least one meaningful approval boundary—for example, external communication, publishing, purchase, authoritative-record change, or sensitive judgment.
3. Create a small evaluation set containing ordinary, ambiguous, and adverse inputs.
4. Run the workflow and record checkable outcomes: success, unsupported claims, omissions, human corrections, tool failures, retries, approval events, and recovery.
5. Run an adversarial case that attempts to cross the approval boundary.
6. Demonstrate that the workflow **stops** and records an approval request or blocked state; a prompt saying “ask first” is not sufficient evidence.
7. Record a controlled recovery from one failed or incomplete run.

### M4 evidence and gate

- `governance/authority-matrix.md`;
- approval record;
- evaluation cases and scorecard;
- run logs/reviews;
- adversarial-test result proving a stop; and
- controlled recovery record.

Core measures may include first-pass success, evidence completeness, correction count, unresolved uncertainty, and time/usage when available. Do not manufacture precision from too few runs.

The adversarial stop test is mandatory. If the test shows that the workflow does **not** stop, that is a valid and instructive result: the learner records a failed control, the corrective action, and the retest, and does not describe the boundary as enforced until it has stopped. Consequential actions in cohort one remain simulated or human-performed.

---

## 11. M5 — Governed Memory and Organizational Knowledge

**Anchor question:** *What should the workforce remember, where should it live, and when does an observation become trusted knowledge?*

### Memory model

| Type | Use | Typical location |
| --- | --- | --- |
| Working | current run context | active session and run folder |
| Episodic | run history, failures, corrections, outcomes | `runs/` and structured logs |
| Semantic | approved facts, policies, decisions | `knowledge/approved/` with provenance and review state |
| Procedural | reusable operating procedures | `skills/` and role instructions |

### Guided build

1. Create a memory map and define access scope: role-private, team-shared, or organization-wide.
2. Add one sourced knowledge record with source, owner, scope, status, last-reviewed date, and related knowledge.
3. Keep it explicitly `untrusted` or `candidate` until a human decides promotion.
4. Test retrieval and use of the record on a real workflow task.
5. Test a conflicting or obsolete record and record how the system handles it.
6. Record a knowledge-promotion decision with provenance and rationale.

### M5 evidence and gate

- memory map;
- knowledge record with provenance and scope;
- retrieval test;
- conflict/obsolescence test; and
- human promotion, deferral, or rejection decision.

Profiles may retain curated role context, but the repository keeps course evidence and governed organizational knowledge reviewable.

No advanced retrieval infrastructure is required. Retrieval may be a deliberate file lookup in `knowledge/approved/`; databases, full-text search, or vector retrieval belong to the optional advanced track.

---

## 12. M6 — Observer Agile Loop: Improve Without Unchecked Self-Modification

**Anchor question:** *How can a workforce learn from operations without being allowed to change itself unchecked?*

### Observer role

The Observer reads only approved operational evidence: run receipts, handoffs, review decisions, scorecards, approval logs, and selected anonymized error records. It writes only a proposal under `improvement/proposals/`. It must not inspect private chats by default, change another profile’s memory, patch production skills/contracts, approve change, or send external messages.

### Evidence threshold

The Observer may recommend a test only when either:

- the same comparable friction appears across **three** documented runs; or
- one high-severity governed failure demonstrates an approval-boundary, unauthorized-action, material privacy/security, or integrity risk.

Otherwise its required disposition is **collect more evidence**.

### Guided build

1. Run the Observer as a temporary role experiment (§3.5), using deliberately sufficient or insufficient approved evidence.
2. Inspect whether it writes one proposal or correctly returns `collect more evidence`.
3. Choose one repeated issue or high-severity failure.
4. Form a narrow improvement hypothesis and propose one change to a contract or skill.
5. Establish the baseline using comparable evaluation cases.
6. Test the candidate in an isolated candidate workspace or branch/worktree when appropriate.
7. Compare baseline and candidate outcomes and check regressions.
8. Human approves, rejects, or defers the change; record rationale.
9. If approved, apply the change deliberately and monitor subsequent runs.
10. Record a Role Decision Record for the Observer: keep it, use it only on a schedule or trigger the learner names, or do not adopt it.

If the learner's own approved evidence is thinner than the threshold, `collect more evidence` is the correct disposition, and the facilitator may supply a prepared historical case pack so the baseline and candidate comparison can still be practiced. Prepared cases are labeled as supplied and never count as the learner's own run evidence.

### Required proposal schema

```text
Evidence window:
Artifacts inspected:
Repeated friction or high-severity failure:
Affected role / skill / contract:
One proposed change:
Expected benefit:
Risks and uncertainty:
Baseline cases:
Regression cases:
Recommended human decision: test / defer / escalate
```

### M6 evidence and gate

- Observer activation log;
- proposal or `collect more evidence` disposition;
- baseline/candidate comparison;
- regression evidence;
- human approval/rejection/deferment decision;
- Role Decision Record for the Observer;
- a `runs/value-checkpoint.md` entry; and
- monitoring plan.

**Anti-pattern demonstration:** An Observer sees one ordinary imperfect run, proposes a sweeping rewrite, and is rejected because the evidence window is too thin.

---

# Part III — Workspace, templates, and operations

## 13. Learner capstone repository

The course adds folders progressively; learners do not need to understand all of them in M0.5.

```text
ai-workforce/
├── README.md
├── 01-workforce-blueprint.md
├── employees/
├── skills/
├── inputs/
├── outputs/
├── handoffs/
│   └── review-packet/
├── reviews/
├── runs/
├── governance/
├── knowledge/
│   └── approved/
├── improvement/
│   └── proposals/
├── profiles/
│   └── role-activation-log.md
└── advanced/
    ├── staging/
    ├── sqlite/
    └── retrieval/
```

## 14. Standard templates

The starter kit supplies editable versions of:

- Workflow Card;
- Employee Contract;
- Run Receipt;
- Execution Review;
- Run Manifest;
- Builder-to-Reviewer Handoff;
- Review Decision;
- Authority Matrix;
- Approval Log;
- Role Activation Log;
- Role Decision Record;
- Value Checkpoint entry;
- Knowledge Record;
- Knowledge Promotion Decision;
- Observer Improvement Proposal; and
- Baseline/Candidate Comparison.

Each template must distinguish observed evidence from assumptions and must leave unknown information explicitly unknown.

## 15. Role activation tests

| Role | Required smoke test | Pass condition |
| --- | --- | --- |
| Conductor | expected downstream artifact is deliberately absent | creates manifest, records `blocked`, and does not invent completion |
| Builder | designated input and output path | reads only its own contract (read-only) and the designated input; writes only proposed artifact plus receipt |
| Reviewer | minimal review packet | writes only evidence-cited disposition: accept, return, or escalate |
| Observer | sufficient or insufficient approved historical evidence | writes one narrow proposal or correctly returns `collect more evidence` |

Every result is logged with role, allowed paths/tools, test input, expected output, observed result, evidence inspected, defects/uncertainty, and human activation decision.

A temporary role experiment (§3.5) still runs the role's activation test. The activation decision is `adopted`, `not adopted`, or `deferred`; a role that is not adopted keeps its log entry as evidence of the experiment.

---

# Part IV — Evaluation and facilitation

## 16. Peer clinics

Use actual learner artifacts rather than polished demonstrations. Peers ask:

1. **Show:** What did the role produce?
2. **Inspect:** What evidence supports it?
3. **Challenge:** Where could it fail or exceed its authority?
4. **Improve:** What is the next smallest justified modification?

## 17. Mastery progression

| Level | Meaning |
| --- | --- |
| 0 — Not demonstrated | cannot explain or perform the task yet |
| 1 — Emerging | recognizes the concept or completes it only with significant guidance |
| 2 — Assisted application | completes familiar work with limited help; transfer is unproven |
| 3 — Independent application | explains reasoning unaided and applies it to a new relevant case |

Artifact production alone does not prove Level 3. Learners must defend their allocation of work, evidence, approval boundary, memory decision, and improvement decision. For role decisions, Level 3 is available for adopting or for declining a role; what is assessed is whether the learner can explain the decision from run evidence and apply the same reasoning to a new case.

## 18. Final capstone assessment

The learner demonstrates:

1. the original human/business problem and independently valuable first workflow;
2. the current role/skill architecture, why each kept role is justified, and why any tested role was not adopted;
3. one complete end-to-end run with inspectable repository evidence;
4. one failed or incomplete run and controlled recovery;
5. a meaningful human approval boundary and proof it stops work appropriately;
6. measured performance evidence and limitations, and the value checkpoint record showing which additions were kept, simplified, or removed and why;
7. one governed memory decision; and
8. one evidence-backed, human-governed improvement decision.

Assess five dimensions:

- **Value:** Does the workflow solve a meaningful problem, and does the learner's evidence show that the added structure was worth its cost?
- **Architecture:** Are roles and skills appropriately separated? A tested and justified decision not to adopt a role scores the same as adopting one.
- **Reliability:** Can results and failures be checked?
- **Governance:** Are authority boundaries explicit and operationally demonstrated?
- **Improvement:** Can evidence support a bounded change decision without unchecked self-modification?

## 19. Facilitator readiness checklist

Before delivery, the facilitator must:

- test the Windows Hermes Desktop installation path and provide macOS/Linux appendix guidance;
- test M0.5 Gate A and Gate B on a clean environment;
- verify the published Conductor distribution and its role-creation guidance;
- run all four role-activation tests;
- prepare successful and failed examples for every module;
- verify the Builder → Reviewer evidence packet and disposition workflow;
- test an adversarial approval-stop case and controlled recovery;
- prepare non-sensitive representative inputs and a fallback demonstration workspace;
- prepare a labeled Builder proposal and receipt for the M3 fallback start and a labeled historical case pack for M6, and test M3 beginning at packet assembly;
- prepare the Role Decision Record and Value Checkpoint templates and a worked example of a justified decision not to adopt a role;
- ensure no core exercise requires paid API access beyond the learner’s chosen supported access path;
- provide templates and a peer-help route; and
- test Claude/Codex adapters separately before presenting them as supported alternatives.

---

## 20. Governing principle

**Start with work worth improving. Prove one bounded capability. Make repeated work reusable. Add a role only when it earns separation. Coordinate with inspectable artifacts. Require human authority for consequential action. Preserve knowledge with provenance. Improve only from sufficient evidence, comparative tests, and explicit approval.**
