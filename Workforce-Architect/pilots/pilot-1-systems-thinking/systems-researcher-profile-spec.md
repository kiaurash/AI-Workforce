# Profile Spec — systems-researcher

**Status: spec for human setup. Not activated, not deployed.** A human applies this via the desktop app, `hermes profile` commands, or direct `config.yaml` / profile-directory setup, then verifies it with the activation smoke test below before relying on it.

## Identity
- Profile name: `systems-researcher`
- Owns Traceability Matrix rows: `W1`, `W2 (R1)`, `D1` (re-read the Traceability Matrix for current details).
- SOUL file: `systems-researcher-SOUL.md` (to be placed in profile root or configured system prompt).

## Model / provider
- Recommended family: Fast, reasoning-capable model with high search synthesis capability (e.g. Claude 3.5 Sonnet or Gemini 1.5 Pro).
- Reason: Requires disciplined boolean query generation, accurate parsing of academic and technical literature, and strict adherence to threshold criteria in Decision Work Units without hallucinating saturation consensus.

## Skills
- `research:arxiv` (Search arXiv papers for foundational systems thinking and AI systems preprints).
- `web:blocked-page-recovery` (Fallbacks when crawling academic or industry whitepapers).

## Toolset
- Required: `web_search`, `web_extract`, `read_file`, `write_file`.
- Explicitly NOT granted:
  * CMS publishing tools (Enforced: absent).
  * Outbound communication / email broadcast tools (Enforced: absent).
  * `kanban_unblock` or orchestrator tools (Enforced: absent).
  * `skill_manage` or file modification access to other agents' directories (Enforced: absent).

## Memory / data boundary
- May retain: Research query history, bibliography of verified systems thinking papers, domain glossary.
- Must stay excluded: Raw scrape bodies, unrelated session context, user personal data.

## Governance / approval references
- Touches Traceability rows W1, W2, D1.
- All actions are Low risk internal artifacts.
- Governed audit trail: Decision Record D1 must be stored in the workspace for post-hoc review by the human editor.

## Activation smoke test (required before calling this role ready)
1. Provide a test prompt: "Systems dynamics in transformer attention mechanisms."
2. Verify agent produces:
   - A structured `topic-framing-brief.md`.
   - A `research-dossier.md` citing >=5 primary sources with reachable URLs.
   - A `decision-record-d1.md` choosing Branch A or B based on documented evidence.
3. Verify agent halts at the boundary and does NOT attempt to write article prose (W4) or modify system files.

## Explicitly NOT granted, standing policy
- Any tool that performs external writes or outbound communications.
- Profile-creation or profile-activation tooling.
