# Build Your AI Workforce with Hermes

**Version:** 4.0 — Hermes Desktop reference design

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
5. **Specialization must earn its place.** Add a separate role only for a clear benefit in expertise, context, permissions, independent verification, or justified parallelism.
6. **Human authority precedes autonomy.** Agents can research, draft, and propose; humans retain consequential decisions, external commitments, money, sensitive people judgments, and production promotion.
7. **Repository-first operation.** Bot messages and agent responses coordinate work; saved contracts, artifacts, handoffs, review decisions, and approval records are authoritative.
8. **Improve from comparable evidence.** Observe, propose, test, compare, approve or reject, then monitor. Never let an observer self-promote a change.

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
| M3 | Conductor → Builder → Reviewer | independent challenge earns a second role |
| M4–M5 | governed Builder–Reviewer operation | controls and knowledge require operational evidence |
| M6 | add Observer | improvement is separated from production execution |

### 3.4 Hermes mechanisms

- **Hermes Desktop / Bot Mode:** durable named specialist profiles with their own role context, skills, memory, configuration, and canonical Bot Chat.
- **`message_agent`:** asynchronous Bot-to-Bot coordination from canonical Bot Chats. It is a trigger or notification, not the authoritative handoff.
- **`delegate_task`:** fresh-context, short-lived child work, appropriate for temporary source checks or bounded parallel research. It does **not** invoke an existing named Builder/Reviewer profile and does not create a hard filesystem, credential, or tool-permission boundary.
- **Cron routines:** optional recurring operation after a manual workflow is proven. A scheduled job must write repository evidence and preserve the same approval rules.
- **Skills:** reusable procedures. A skill is not a workforce itself; a Conductor skill can initiate the repository-first protocol among earned roles.

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
- 5 min: reflection, recorded next action, and module gate.

---

# Part I — Preparation

## 5. M0 — Socratic AI Workforce Opportunity Discovery

**Anchor question:** *Where would additional AI capacity create meaningful leverage, and what must remain human-owned?*

M0 is discovery, not architecture construction. The learner examines actual work episodes and creates an **AI Workforce Opportunity Map** containing:

- desired future human role;
- candidate workflows, constraints, and value hypotheses;
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
4. Run the bounded Builder task in the learner’s workspace.
5. Inspect the saved result against source material, record one defect/unknown/edge case, revise one rule if justified, and rerun if practical.
6. Create a provisional Workforce Blueprint distinguishing human decisions, employee work, reusable skills, tools, and only justified future roles.

### M1 evidence and gate

- `01-workforce-blueprint.md`;
- `employees/first-employee.md`;
- one representative input;
- one saved output;
- `runs/first-run-review.md` with evidence of verification and one observed limitation.

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
4. Record the decision: remain with one role, or create a separate Builder profile because the benefit is demonstrable.
5. If a Builder profile is created, perform its activation test: read only the designated input, write only the proposal plus receipt, and record the human activation decision.

### M2 evidence and gate

- one tested `SKILL.md`;
- repeat-run comparison;
- updated employee contract and tool/path boundaries;
- Builder activation log, if a separate Builder is used; and
- written rationale for or against specialization.

Do not create a second role merely because the curriculum contains one.

---

## 9. M3 — Coordinate Through Evidence: Builder to Reviewer

**Anchor question:** *How can two roles collaborate without carrying each other’s unstated assumptions?*

**Core topology:** Conductor → Builder → Reviewer.

### Practitioner demonstration

Show a Builder producing a plausible artifact and a deficient handoff. Show a downstream role accepting an unsupported claim. Repair it by requiring a minimal packet and a structured review decision.

### Guided build

1. The Conductor creates `runs/<run-id>/` and a manifest.
2. The Builder saves its proposed artifact and run receipt before signaling the Conductor.
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

### M3 boundary lesson

A fresh `delegate_task` conversation provides conversational isolation but not hard workspace, credential, or tool isolation. Bot-to-Bot messages are asynchronous coordination signals, not authoritative handoffs. The packet and saved repository artifacts define the evidence boundary. High-sensitivity variants require separate access-restricted staging and read-only tool controls.

### M3 evidence and gate

- run manifest;
- Builder proposal and receipt;
- minimal review packet;
- `review-decision.md` with cited evidence;
- decision-resolution record; and
- Reviewer activation log.

The Reviewer’s acceptance never authorizes a consequential action; the human approval boundary remains intact.

**Advanced variant:** Add a Researcher/Extractor only when separate source sets, time sensitivity, or independently collected evidence justify parallelism.

---

## 10. M4 — Govern, Measure, and Recover

**Anchor question:** *How do I know whether the workforce is reliable, and how do I prevent a failure from causing harm?*

### Guided build

1. Define an authority matrix for every action: propose, review, approve, execute, and log.
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

1. Activate the Observer using deliberately sufficient or insufficient approved evidence.
2. Inspect whether it writes one proposal or correctly returns `collect more evidence`.
3. Choose one repeated issue or high-severity failure.
4. Form a narrow improvement hypothesis and propose one change to a contract or skill.
5. Establish the baseline using comparable evaluation cases.
6. Test the candidate in an isolated candidate workspace or branch/worktree when appropriate.
7. Compare baseline and candidate outcomes and check regressions.
8. Human approves, rejects, or defers the change; record rationale.
9. If approved, apply the change deliberately and monitor subsequent runs.

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
- human approval/rejection/deferment decision; and
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
- Knowledge Record;
- Knowledge Promotion Decision;
- Observer Improvement Proposal; and
- Baseline/Candidate Comparison.

Each template must distinguish observed evidence from assumptions and must leave unknown information explicitly unknown.

## 15. Role activation tests

| Role | Required smoke test | Pass condition |
| --- | --- | --- |
| Conductor | expected downstream artifact is deliberately absent | creates manifest, records `blocked`, and does not invent completion |
| Builder | designated input and output path | reads only the input; writes only proposed artifact plus receipt |
| Reviewer | minimal review packet | writes only evidence-cited disposition: accept, return, or escalate |
| Observer | sufficient or insufficient approved historical evidence | writes one narrow proposal or correctly returns `collect more evidence` |

Every result is logged with role, allowed paths/tools, test input, expected output, observed result, evidence inspected, defects/uncertainty, and human activation decision.

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

Artifact production alone does not prove Level 3. Learners must defend their allocation of work, evidence, approval boundary, memory decision, and improvement decision.

## 18. Final capstone assessment

The learner demonstrates:

1. the original human/business problem and independently valuable first workflow;
2. the current role/skill architecture and why each role is justified;
3. one complete end-to-end run with inspectable repository evidence;
4. one failed or incomplete run and controlled recovery;
5. a meaningful human approval boundary and proof it stops work appropriately;
6. measured performance evidence and limitations;
7. one governed memory decision; and
8. one evidence-backed, human-governed improvement decision.

Assess five dimensions:

- **Value:** Does the workflow solve a meaningful problem?
- **Architecture:** Are roles and skills appropriately separated?
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
- ensure no core exercise requires paid API access beyond the learner’s chosen supported access path;
- provide templates and a peer-help route; and
- test Claude/Codex adapters separately before presenting them as supported alternatives.

---

## 20. Governing principle

**Start with work worth improving. Prove one bounded capability. Make repeated work reusable. Add a role only when it earns separation. Coordinate with inspectable artifacts. Require human authority for consequential action. Preserve knowledge with provenance. Improve only from sufficient evidence, comparative tests, and explicit approval.**
