# Profile Spec — systems-writer

**Status: spec for human setup. Not activated, not deployed.** A human applies this via the desktop app or supported `hermes profile` / `hermes config` commands (never by hand-editing `config.yaml`), then verifies it with the activation smoke test below before relying on it.

## Identity
- Profile name: `systems-writer`
- Owns Traceability Matrix rows: `W3`, `W4`, `W6` (re-read the Traceability Matrix for current details).
- SOUL file: `systems-writer-SOUL.md` (to be placed in profile root or configured system prompt).

## Model / provider
- Recommended family: High-capacity creative/analytical writing model (e.g. Claude 3.5 Sonnet or GPT-4o).
- Reason: Requires nuanced conceptual synthesis, engaging exposition for senior engineering audiences, and disciplined grounding in provided research without drifting into buzzwords.

## Skills
- None required beyond native Markdown generation and prompt instructions. (Deliberately ungranted: research skills, code execution, repo tools).

## Toolset
- Required: `read_file`, `write_file`.
- Explicitly NOT granted:
  * `web_search` and `web_extract` (Proposed: omit at setup; verify absent in activation smoke test to enforce strict segregation of duties; writer must build solely from verified researcher dossier).
  * CMS publishing tools (Proposed: omit at setup; verify absent in activation smoke test).
  * Outbound communication / email broadcast tools (Proposed: omit at setup; verify absent in activation smoke test).
  * `kanban_unblock` or orchestrator tools (Proposed: omit at setup; verify absent in activation smoke test).
  * `skill_manage` or configuration mutation tools (Proposed: omit at setup; verify absent in activation smoke test).

## Memory / data boundary
- May retain: Formatting templates, Meadows leverage point structural references, audience persona notes.
- Must stay excluded: Unverified factual claims, raw author notes, external user data.

## Governance / approval references
- Touches Traceability rows W3, W4, W6.
- All outputs are local files (`systems-analysis.md`, `first-draft.md`, `publication-package.md`).
- Low risk; handoff to W5 (`fact-checker`) is mandatory before W6 packaging.

## Activation smoke test (required before calling this role ready)
1. Feed mock input files: a sample `decision-record-d1.md` and `research-dossier.md`.
2. Verify agent produces:
   - `systems-analysis.md` demonstrating correct Meadows' leverage points mapping.
   - `first-draft.md` written in practitioner voice with inline claim markers.
3. Verify agent stops at W4/W6 boundaries and does NOT attempt to search the web or publish externally.

## Explicitly NOT granted, standing policy
- External publishing or communication tools.
- Web search / browse tools (forces strict reliance on the researched dossier).
- Profile-creation or profile-activation tooling.
