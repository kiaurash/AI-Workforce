# Inquiry-Driven Learning authoring toolkit

This directory contains reusable authoring guidance and validation tools for designing source-grounded, diagnostic-led courses for AI-workforce learning. It is a toolkit, not a learner-facing course or a generated course instance.

## Contents

- `skills/learner-intake/SKILL.md` — intake and source approval.
- `skills/course-design/SKILL.md` — goal-aligned outcomes, module design, and learner diagnostic design. Includes the agentic-workforce design safeguards.
- `skills/idl-design/SKILL.md` — IDL course map and diagnostic authoring procedure.
- `skills/idl-design/templates/` — normative `COURSE.md` and `DIAGNOSTIC.md` templates.
- `skills/idl-design/scripts/validate_idl_design.py` — mechanical validator for a course map and diagnostic.

## Scope and boundaries

The IDL authoring workflow creates `courses/<slug>/COURSE.md` and `DIAGNOSTIC.md`, plus empty shared `sources/` and `chapters/` directories. It does not generate chapters, learner profiles, evidence, ledgers, or session notes. Keep learner-specific records out of the shared course tree and ensure they are excluded from version control.

A course design remains a draft until a human explicitly approves it. The validator checks structural and cross-file invariants; it cannot replace checking source citations, instructional quality, sensitive-domain safeguards, or human review.

## Use

Read the applicable skill before using this toolkit. For an IDL course, start with `skills/idl-design/SKILL.md`, which requires reading both bundled normative templates before drafting. Run its validator with:

```bash
python skills/idl-design/scripts/validate_idl_design.py \
  courses/<slug>/COURSE.md \
  courses/<slug>/DIAGNOSTIC.md
```

The AI-Workforce M1 materials elsewhere in this repository remain course source material; this directory does not silently convert them into a new COURSE.md or diagnostic.
