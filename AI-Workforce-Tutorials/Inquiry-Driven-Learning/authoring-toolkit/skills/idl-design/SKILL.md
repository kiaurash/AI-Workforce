---
name: idl-design
description: "Design source-grounded IDL course maps and diagnostics."
version: 0.1.0
author: Kia, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [idl, course-design, diagnostic, misconceptions, socratic]
    related_skills: [learner-intake, course-design]
---

# Inquiry-Driven Learning Design

Author the shared, portable half of an Inquiry-Driven Learning (IDL) course: `COURSE.md` and `DIAGNOSTIC.md`. Mine supplied sources for grounded principles and candidate misconceptions, define a role-based audience and outcomes, derive dialogue personas, and plan chapters. This skill does not generate chapters or conduct learner sessions.

The bundled templates are normative format specifications; this file is procedure. Before authoring, load `templates/COURSE-TEMPLATE.md` and `templates/DIAGNOSTIC-TEMPLATE.md`. Do not duplicate or improvise rules that the templates own.

## When to Use

- Use when the user invokes `/idl-design`.
- Use when the user wants a new dialogue course designed from source material.
- Use with `--rebuild` when an approved course map must be replaced.
- Do not generate `chapters/*.md`; route that request to `/idl-chapter`.
- Do not administer a diagnostic or run a session; route that request to `/idl-study`.

## Required Inputs

Collect only missing fields, one question at a time. Never infer them.

1. **Course slug** — lowercase and hyphenated. If absent, inspect `courses/`: use the sole existing course; list choices and ask if several exist; ask for a slug if none exists.
2. **Sources** — one to seven readable paths or URLs. Read every source fully enough to establish its structure and stable citation locators. Abort and name any missing or unreadable source; never invent its content.
3. **Audience role** with all three fields:
   - `background`
   - `assumed_prior`
   - `goal`

The audience must describe a role a stranger can match, not the commissioning person. Exclude names, employers, and person-specific job titles. If the user describes only themselves, ask: **“Who else is this for?”** and generalize only from their confirmed answer.

## State Detection

Inspect the target before writing:

| Condition | Action |
|---|---|
| No slug and exactly one course exists | Use it. |
| No slug and several courses exist | List them and ask; never guess. |
| `COURSE.md` exists without `--rebuild` | Stop, report it as immutable after approval, and offer `--rebuild`. |
| `COURSE.md` exists with `--rebuild` | Name existing chapters and learner sessions that would be invalidated; require explicit confirmation before replacement. |
| Chapters exist without `COURSE.md` | Treat as a legitimate retrofit; read every chapter and include all misconceptions already voiced. |
| A source is missing or unreadable | Abort and name it. |

## Procedure

### 1. Bootstrap only the shared tree

Create:

```text
courses/<slug>/
  sources/
  chapters/
```

Do not create `learners/`, `evidence.md`, any ledger, or chapter files. Ensure the repository `.gitignore` contains exactly one effective line:

```gitignore
Inquiry-Driven-Learning/courses/*/learners/
```

Use `read_file` before editing `.gitignore`, and `patch` for an existing file.

### 2. Build the source registry

Assign stable source keys and use each source’s real addressing: page numbers for paged documents, section headings for Markdown or web documents, and atom IDs for atomized knowledge sources. Never invent page numbers for unpaged material. Cite substantive claims, registry principles, and misconception evidence to these locators.

### 3. Mine the principle and misconception registry

Treat the registry as a hypothesis space, never as a claim about an individual.

- **Tier 1:** the supplied source explicitly names the misconception. Search this first.
- **Tier 2:** independent domain literature or instructor research establishes a population-level error. Use when needed; open and verify every supporting source before citation.
- **Tier 4:** an LLM inference or practitioner anecdote. Record its origin, but quarantine it from misconception pauses.
- **Tier 3 never appears in shared course design.** It is created per learner at runtime from a diagnostic response or observed behavior.

Every registry row uses the closed `kind` enum: `misconception` or `principle`. Principles express correct patterns or skills and require citations. Misconceptions express specific wrong beliefs. If a prior learner or practitioner voiced a misconception, enter it only as tier 4 until independent tier-1 or tier-2 evidence promotes it.

Aim for at least three tier-1 or tier-2 misconception rows. If the evidence falls short, do not pad with tier-4 guesses: set `grounding: weak`, visibly banner the limitation, and tell the user.

### 4. Write practical outcomes

Create 5–10 Bloom-tagged outcomes with IDs `LO-1`, `LO-2`, and so on. Each must name an observable capability the audience wants, not merely content the sources contain. Include source-grounded core constructs, essential skills, and threshold concepts where they support the audience goal.

### 5. Establish the vocabulary contract

List every term the course will rely on but not teach. Any other load-bearing term must later be defined in a chapter before a pause tests it. Do not import vocabulary from the author’s experience or prior learner sessions.

### 6. Derive the persona pair

Create an expert persona and learner persona from the confirmed audience role and registry, not from the author. The expert is a warm, concise Socratic mentor who challenges reasoning without sycophancy. The learner persona is productive and questioning; it voices only population-grounded registry misconceptions at planned pause points rather than acting confused continuously.

### 7. Build the chapter map

Sequence chapters so chapter `k` depends only on established prerequisites from earlier chapters. For each chapter specify title, source sections, outcomes, planned pause types with registry targets, and interleaving/spacing. Chapter splitting and merging belong here: if later chapter generation reports an oversized section, rebuild the map rather than allowing the generator to split it.

Plan misconception pauses only against tier-1 or tier-2 `kind=misconception` rows. Plan completion pauses only against `kind=principle` rows. Prediction pauses may target either kind but do not update misconception status.

### 8. Author `DIAGNOSTIC.md` now

Follow `templates/DIAGNOSTIC-TEMPLATE.md`. Write 3–4 neutral multiple-choice items whose distractors map to registry misconceptions. Include exactly one correct option, an explicit “I don’t know” option, and a confidence rating on every item. Where a validated instrument exists, prefer it verbatim with proper attribution.

The diagnostic must cover every misconception row that the chapter map plans to use for a misconception pause. If a registry item cannot support a valid diagnostic item, remove it from planned pauses or cut it; do not declare a separate eligibility flag.

### 9. Add a safety envelope when required

For personal, psychological, health, legal, financial, or similarly sensitive material, author the template’s Safety / Consumption envelope. Include instructional boundaries, prohibited situations, professional-support redirects, fictional-scenario alternatives, and constraints on feedback. The system may quote a learner’s own words but must never diagnose the learner.

### 10. Write drafts, validate, and present

Write only:

- `courses/<slug>/COURSE.md`
- `courses/<slug>/DIAGNOSTIC.md`
- the shared `sources/` and `chapters/` directories
- the `.gitignore` line when absent

Run the mechanical validator:

```text
python <skill-dir>/scripts/validate_idl_design.py courses/<slug>/COURSE.md courses/<slug>/DIAGNOSTIC.md
```

Resolve every failure; do not accept a partial pass. Then show the user the full registry, outcomes, chapter map, and diagnostic. Keep `status: draft` until the user explicitly approves. Only after their approval set `status: approved`. Once approved, treat `COURSE.md` as immutable unless the user invokes `--rebuild` and confirms invalidation.

## Mechanical Gates

Refuse to ship unless all applicable gates pass:

- **Grounding floor:** at least three tier-1 or tier-2 misconception rows, or `grounding: weak` plus a visible warning.
- **Kind closure:** every registry row is `misconception` or `principle`; misconception and completion pauses target compatible kinds.
- **Diagnosability:** every misconception that may anchor a planned pause has at least one diagnostic distractor carrying its `registry_id`.
- **No shared tier 3:** the registry contains no tier-3 row.
- **Audience role:** audience fields contain no learner name, employer, or other person-specific identity.
- **Map coverage:** every pause-eligible misconception maps to at least one chapter; every chapter maps to at least one outcome.
- **Vocabulary:** prerequisites list every assumed load-bearing term.
- **Sensitive-domain safety:** the Safety / Consumption envelope exists when required.
- **Retrofit coverage:** every misconception voiced in an existing chapter appears in the registry.

## Error Handling

- Unreadable source: abort, name it, and do not fabricate.
- Thin misconception evidence: mark weak grounding and let the user decide after a clear warning.
- Undiagnosable misconception: remove it from planned misconception pauses or remove it entirely.
- Personal audience description: ask who else the course serves, then write a role.
- Existing course without `--rebuild`: stop and offer the rebuild path.
- Rebuild request: warn about named invalidated chapters and learner sessions, then wait for confirmation.

## 10. Delivery and file boundary

The skill authors only the shared course-design artifacts: `COURSE.md`, `DIAGNOSTIC.md`, and the empty shared `sources/` and `chapters/` directories, plus the `.gitignore` exclusion when missing. It never creates learner records, session notes, evidence files, ledgers, or chapter files.

This skill does not itself commit or push course artifacts. After local validation and human approval, the user may request a separate repository delivery workflow.