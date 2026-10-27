# M1 — Misconception Map

Shared design-time map for the M1 tutor. It is a **hypothesis space**, not a claim about any individual learner.

## Rules for using this map

- **There is no tier 3 here.** Tier 3 means one learner's own record. It is minted at run time, per learner, by the diagnostic (`tier-3d`) or by observation in the session (`tier-3v`), and it is recorded in that learner's own `learning/learning-record.md`. Never write learner evidence into this shared file.
- **Tier 1** — a repo or course source names the mistake itself. Once a specific learner exhibits it, the tutor may challenge it directly, using a predict-then-compare question on that learner's own run.
- **Tier 2** — education or domain literature establishes it as common. None is claimed here; no external search was performed for this map. Add rows only with a citation.
- **Tier 4** — inferred, no source. Quarantined. Use a prediction question that would expose it, but never challenge it head-on unless this learner shows it. Observed practitioner misconceptions also enter at tier 4 with their origin recorded.
- **Order of operations.** Do not state the misconception first and then refute it. Ask the learner to predict an outcome, let the evidence show the result, then ask them to explain the gap. Naming the false belief first can strengthen it.
- Grounding floor (three tier 1 or tier 2 misconceptions): met with seven tier-1 rows. Their evidence is internal course design documents, not independent research. Treat the tiers as "named by the course's own sources", and say so if asked.

## Sources

| Key | Source | Location |
| --- | --- | --- |
| S1 | Course design, "Build Your AI Workforce with Hermes", v4.0 | `Course.md` (this repo), §1 and §2 |
| S2 | M1 package README and Facilitator Guide | this repo, `M1-First-AI-Employee/` |
| S3 | Course design v3.1 | `AI-Workforce-Course-Design-v3.1.md` (local design document, not in this repo), §2.4, §2.5, §6, §8 Stage 5, §10 |
| S4 | "Module 1 — Architect Your AI Workforce" architecture proposal | local design document, not in this repo, §10 and §16 |

## Registry

| registry_id | kind | statement | tier | evidence | origin | diagnostic item | addressed at |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `chat-is-proof` | misconception | If the agent says it saved or finished the work, the work exists | 1 | S1 §2 principle 4 ("a chat claim is never proof that a file exists"); S3 §8 Stage 5 | source | D1 | 25–32, 32–38 |
| `fluent-is-faithful` | misconception | A well-formatted, confident output is a faithful one | 1 | S1 §2 principle 4 ("a fluent response … is never proof"); S3 §10 demo lesson | source | D1 | 0–7, 32–38 |
| `agent-per-step` | misconception | Each step in a workflow should become its own AI employee | 1 | S4 §16 ("a common design failure is converting every workflow step into an agent"); S1 §2 principle 5 | source | D2 | 38–45 |
| `more-is-better` | misconception | A bigger workforce is a better workforce | 1 | S1 §1 ("Success is not agent count"); S3 §1 | source | D2 | 7–12, 55–60 |
| `persona-is-architecture` | misconception | Giving an agent a name and personality defines its role | 1 | S4 §16 ("Names and personalities … are not architecture") | source | D2 | 38–45 |
| `instruction-is-control` | misconception | Writing "ask me first" in the contract enforces the approval boundary | 1 | S2 README limitation ("An instruction file is not a deterministic security mechanism"); S3 §2.5 | source | D3 | 18–25, 38–45 |
| `better-contract-fixes-all` | misconception | Once the instructions are corrected, the employee is reliable | 1 | S2 demo Part G ("Do not imply that better instructions alone guarantee reliability"); S1 §2 principle 4 | source | D4 | 32–38, 55–60 |
| `ladder-is-staircase` | misconception | Prompt, skill, employee, workforce is a required progression, and more autonomy means more specialization | 1 | S3 §6 ("teaching modes, not mandatory successive stages"; autonomy and specialization are separate decisions) | source | — | 18–25 |
| `formatter-is-employee` | misconception | A repeatable procedure such as formatting deserves its own employee | 4 | Implied by S4 §10 discussion question; not stated there as a common error | LLM inference | — (prediction question only) | 38–45 |
| `tool-is-small-employee` | misconception | A tool and an employee differ only in size | 4 | Inference from S4 §7 ("A tool does something. An employee owns a responsibility.") | LLM inference | — (prediction question only) | 38–45 |
| `boundary-is-implicit` | misconception | The agent will know what it must not do without being told | 4 | Inference; related to S1 §2 principle 6 | LLM inference | — (prediction question only) | 18–25 |
| `employee-owns-responsibility` | principle | An employee is justified by owning a responsibility with its own context, tools, permissions, or verification; a tool performs an action; a skill is a reusable method | — | S4 §7 (Four-Bucket); S1 §2 principle 5 | source | D2 | 38–45 |
| `evidence-over-claims` | principle | Completion and quality are established by inspecting saved artifacts against the source | — | S1 §2 principles 4 and 7 | source | D1 | 25–38 |
| `authority-before-autonomy` | principle | Decide what the AI may not do before deciding what it may do; labels are a map, enforcement is separate | — | S1 §2 principle 6; S4 §11 | source | D3 | 38–45 |

## Prediction questions for tier-4 rows

Use these instead of confrontation. Let the learner predict, then compare with the evidence from their own run.

- `formatter-is-employee`: "If we removed this proposed employee and gave its steps to the first employee as a written procedure, what would you expect to break?"
- `tool-is-small-employee`: "Which of these responsibilities does something, and which one is answerable for an outcome?"
- `boundary-is-implicit`: "If the contract said nothing about contacting participants, what would you predict the Builder is able to do, and what would stop it?"
