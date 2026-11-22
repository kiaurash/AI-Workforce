---
name: learner-intake
description: Use when starting a source-grounded learning course.
version: 0.1.0
author: Kia, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [course-design, learner-profile, sources, intake]
    related_skills: []
---

# Learner Intake

Collect and confirm the information needed to begin a source-grounded course. This skill ends with a confirmed Learner Profile and an approved Source List. Do not design lessons, sequence content, or propose activities until both exist.

## When to Use

- Use when a learner wants a course, lesson sequence, study plan, or learning program on a topic or source document.
- Use during phases 1–2 of a larger course-design workflow.
- Do not use when the learner uploads a course progress file; follow the progress-file workflow instead.

## Intake Rules

Collect these inputs, asking only for missing information. Ask **one question at a time**. When the learner gives all required information in one message, do not repeat questions; read it back for confirmation.

| Input | Collect | Sufficient when |
|---|---|---|
| **Source** | An uploaded document, a named topic, or both | You can state the course scope in one sentence. |
| **Background** | Existing knowledge, relevant experience, and current study, work, or project context | You can distinguish likely familiar terms from unfamiliar ones. |
| **Goal and time** | What the learner should be able to do at the end, plus session count and duration or a deadline | You could formulate a final performance task that demonstrates the goal. |

Never silently infer a missing input. You may propose a value, but the learner must confirm it.

### Clarify an Unusable Goal

If a goal is vague, ask one follow-up: “What would you be able to do after this course that you cannot do now?” Offer two or three concrete examples at different levels so the learner can select or adapt one.

Ask no more than two goal-clarification follow-ups. If the goal remains loose, propose a concrete, observable version and ask the learner to accept or edit it.

### Establish a Time Budget

If the learner gives no time budget, propose **four sessions of about 30 minutes each** and ask them to accept or change it.

## Source Procedure

### Learner uploads a document

1. Read the complete document with the appropriate document-reading tool. For a long PDF, extract its full text and section headings before characterizing it.
2. Report in three or four sentences: title, coverage, approximate length, and level—introductory, intermediate, or advanced.
3. Compare it to the learner’s goal. If it is broader, propose the sections the course will use. If it is substantially above or below the learner’s background, state that plainly and propose either a prerequisite module or a supplementary source.
4. Assign it **S1**. Thereafter, cite its parts by section heading or page number.

### Learner provides only a topic

1. Search for **2–5** candidate sources using approved web-research tools.
2. Prefer sources in this order:
   1. Open textbooks and university course materials.
   2. Official documentation and standards.
   3. Peer-reviewed review or tutorial articles.
   4. Explanations by a named expert on a reputable site.
3. Exclude unattributed blogs, content farms, likely machine-generated pages, and forum answers as primary sources.
4. For mathematics and computer-science topics, include at least one source with worked examples or exercises.
5. Open and inspect every candidate source before listing or citing it. Do not list a source that was not opened in the current chat.
6. Present candidates in this format, then ask the learner to approve, remove, or add sources:

   `S1 — Title, publisher or author (link). Why it fits; level.`

### Learner provides both a document and a topic

Treat the uploaded document as the primary source (**S1**). Search only to close a specific gap in that document, and state the gap each additional source fills.

## Confirmation Gate

Before any course design, present this exact structure and ask, **“Is this right?”**

```text
LEARNER PROFILE
Topic and scope: …
Background: …
Goal: by the end, you will be able to …
Time: … sessions of about … minutes
Sources: S1 …, S2 …
```

Keep personal details out of the profile. Record only the learner’s role and level; do not record their name, employer, or other identifying details.

Do not proceed to design until the learner confirms both the Learner Profile and the Source List.

## Resuming

If the learner uploads a progress file instead of beginning fresh, use the progress-file workflow and skip this intake. Source documents do not persist across chats, so ask the learner to upload again any source document required for the resumed course.

## Verification

Before ending this intake, verify all of the following:

- [ ] Source, background, goal, and time budget are supplied or explicitly confirmed.
- [ ] The final goal is observable enough to support a final performance task.
- [ ] Every listed web source was opened in the current chat.
- [ ] Every source has an `S` identifier and an appropriate citation locator.
- [ ] The learner approved the source list.
- [ ] The learner explicitly confirmed the Learner Profile.
- [ ] No course design began before those confirmations.
