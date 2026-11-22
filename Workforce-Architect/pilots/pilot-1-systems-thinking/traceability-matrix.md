# Workforce Traceability Matrix: Systems Thinking in the Age of AI Newsletter

Outcome: Weekly publication-ready blog post and newsletter draft applying Systems Thinking (Meadows' Leverage Points) to an AI topic, verified by primary sources and awaiting human one-click publication.

## Core Traceability Matrix

| Row ID | Workflow Outcome | Work Unit | Input / Source of Truth | Output Artifact / Schema | Owner Agent | Allowed Tools | Verifier / Evidence | Risk Category | Approval Record | Escalation Path |
|---|---|---|---|---|---|---|---|---|---|---|
| W1 | Fact-checked newsletter draft | Topic Ingestion & Framing | User topic prompt (e.g. 'Systems Thinking in the Age of AI') | `topic-framing-brief.md` (Scope, target keywords, core hypotheses) | systems-researcher | read_file, write_file | Structural check (all required brief sections present) | Low (internal) | None required | Refine topic prompt with human if unparsable |
| W2 (R1) | Fact-checked newsletter draft | Domain Research & Prior Art Discovery | `topic-framing-brief.md` | `research-dossier.md` (Synthesized findings, primary citations, prior art map) | systems-researcher | web_search, web_extract, read_file, write_file | Minimum 5 verified primary sources; no dead links | Low (internal) | None required | R1 escalation: generate Escalation Brief for human guidance |
| D1 | Fact-checked newsletter draft | Novelty & Saturation Triage | `research-dossier.md` + `topic-framing-brief.md` | `decision-record-d1.md` (Decision Record per template) | systems-researcher | read_file, write_file | Explicit novelty criteria applied; dissent/confidence logged | Low (internal branch) | Governed (logged for audit) | Escalates if anomalous / unresolvable branch |
| W3 | Fact-checked newsletter draft | Systems Thinking Analysis | `decision-record-d1.md` (selected topic) + `research-dossier.md` | `systems-analysis.md` (Stocks/flows, feedback loops, Meadows 12 points map) | systems-writer | read_file, write_file | Review against Donella Meadows framework consistency | Low (internal) | None required | Flag missing empirical dynamic back to systems-researcher |
| W4 | Fact-checked newsletter draft | Post & Newsletter Drafting | `systems-analysis.md` + `research-dossier.md` | `first-draft.md` (Full narrative, practical AI context, inline claim tags) | systems-writer | read_file, write_file | Readability score; inline citations mapped to dossier | Low (internal) | None required | If analysis insufficient, trigger W3 revision |
| W5 (R2) | Fact-checked newsletter draft | Fact-Checking & Citation Audit | `first-draft.md` + `research-dossier.md` | `fact-check-report.md` + `verified-draft.md` | fact-checker | web_search, web_extract, read_file, write_file | Pass/fail annotation on 100% of factual assertions | Low (internal) | None required | R2 escalation: flag unverified claims in audit log for human review |
| W6 | Fact-checked newsletter draft | Editorial Packaging | `verified-draft.md` + `fact-check-report.md` | `publication-package.md` (Draft, headlines, newsletter summary, community prompt) | systems-writer | read_file, write_file | Complete publication checklist satisfied | Low (internal) | None required | Return to W4 if packaging reveals narrative flaws |
| G1 | Published community post & newsletter broadcast | Human Publication Approval Gate | `publication-package.md` + `fact-check-report.md` + `decision-record-d1.md` | Published blog post & newsletter send | human-editor | External CMS / Email service (Human only) | Human review of draft, citations, and community prompt | Consequential (External writes & Outbound communication) | Human editor signature & timestamp | Cancel/edit post if rejected by human editor |

**Roster-completeness scope:** `human-editor` is a human-only approval owner, not a rostered Bot. The one-SOUL/profile-spec/skills requirement applies only to rostered Bot owners (`systems-researcher`, `systems-writer`, and `fact-checker`). G1 instead requires a human approval contract: named approver, review inputs, explicit approve/reject decision, and timestamp recorded before any publication or send.

---

## Decision Work Unit: D1 (Novelty & Saturation Triage)

Anticipated Branches:
- Branch A (Novel / Underexplored): Primary topic has sparse prior art combining this specific AI domain with Systems Thinking.
  * Output: Decision Record D1 authorizing task W3 on primary topic.
  * Risk Category: Low.
  * Innovation Envelope: Within standard blog scope, 1500-2500 words, no extra tool grants.
- Branch B (Saturated / Well-Covered): Topic is heavily covered with standard platitudes. Pivot to a specific, underexplored subtopic or contrarian leverage point tailored for practitioner discussion.
  * Output: Decision Record D1 authorizing task W3 on refined subtopic.
  * Risk Category: Low.
  * Innovation Envelope: Within standard blog scope, 1500-2500 words, no extra tool grants, topic must remain rooted in Meadows' leverage points.
- Novel Branch / Unanticipated Branch:
  * If within envelope and low-risk: logged as `NOVEL_AUTO_PROCEEDED`.
  * If out-of-envelope or consequential: logged as `NOVEL_PROPOSED`, task created in blocked status, human unblock required.
  * If unresolvable: `ANOMALOUS_BLOCKED`, escalate to human editor.

---

## Retry Units: Explicit Retry Parameters

### Retry Unit R1 (Row W2: Domain Research)
- Retry Trigger: Search results genuinely inconclusive, contradictory, or fewer than 5 credible primary sources located.
- Max Attempts: 2 retries (3 total attempts).
- Evidence Change Per Attempt:
  * Attempt 1: Baseline queries derived from topic brief.
  * Attempt 2 (Retry 1): Reformulate queries with academic terminology, search preprints (arXiv), and target opposing technical arguments.
  * Attempt 3 (Retry 2): Search adjacent engineering disciplines (sociotechnical systems, cybernetics, safety engineering) and empirical case studies.
- Human Escalation Condition: If after 3 attempts the evidence remains contradictory or insufficient, generate `research-escalation-brief.md` detailing all queries executed, sources inspected, and exact contradictions, then create a blocked task for human guidance.

### Retry Unit R2 (Row W5: Fact-Checking & Citation Audit)
- Retry Trigger: Identification of unverified claims, weak/broken citations, or conceptual mischaracterizations of systems thinking principles in the draft.
- Max Attempts: 2 revision loops back to systems-writer (W4).
- Evidence Change Per Attempt:
  * Attempt 1: Initial draft claim check.
  * Attempt 2 (Revision 1): Writer adjusts wording, supplies alternative citations from dossier, or strikes unverified claims.
  * Attempt 3 (Revision 2): Targeted reverification of adjusted claims.
- Human Escalation Condition: If unverified claims persist after 2 revision rounds, do not loop indefinitely. Mark persistent unverified claims as `FLAGGED_FOR_HUMAN_ADJUDICATION` in `fact-check-report.md`, annotate draft, and pass to W6 with clear human review flags.
