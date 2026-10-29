# Evidence Labels for Workforce Controls

Label every proposed control in a workforce design with exactly one of:

- **Enforced** — technically constrained by the runtime/tool permissions; an agent cannot violate it even if instructed to. Example in this Hermes runtime: a Bot's enabled toolset genuinely lacking a "publish" tool; `kanban_create(initial_status='blocked')` genuinely halts dispatch until a human calls `kanban_unblock`.
- **Governed** — relies on a human, or an independent reviewer the deployment designates, to catch a violation before consequence. This skill does not assume any specific reviewer skill or role exists elsewhere — it only requires that SOME accountable reviewer checks before a consequential `kanban_unblock`. Example: a human reviewing task content against a Decision Record before unblocking it — the tool itself does not check the content, the human does.
- **Advisory** — prompt/skill instruction only, with no technical or process backstop. Treat as decoration, not a safety control, in any readiness determination.

## Known Hermes-runtime enforcement boundaries (recheck if the platform changes)

- `kanban_create` accepts any assignee string, body, or skills list from the calling agent — there is no allowlist check against an "approved roster" before dispatch. Constraining decision-created tasks to approved templates/assignees is Governed only; it cannot be made Enforced without new platform tooling.
- `kanban_create(initial_status='blocked')` is the one genuine Enforced dispatch-time stop available: no profile is spawned until a human calls `kanban_unblock`. It gates *dispatch timing*, not *content* — a human still has to actually check the content before unblocking for any safety claim to hold.
- No tool in this runtime creates a Bot/profile from inside a skill — profiles live under `profiles/<name>/` and are configured via the desktop app or config.yaml by a human. Treat generated profile definitions as specs requiring human setup, never as "deployed."
- No tool filters or redacts an agent's own output before it writes to a file or kanban comment — a "write structured fields only, exclude raw transcript/credentials" rule (e.g. for a Documentarian-type role) is Advisory only. Verify it with a negative-control canary test, not by trusting a clean-looking passing run.

## Readiness labels for a generated workforce

- **Deployable now** — every consequential row has Enforced or Governed coverage with a verified approval record, AND operational validity was demonstrated (not just artifact existence).
- **Deployable with governance only** — artifacts exist and pass creation checks, but some controls rely on Governed review rather than Enforced mechanics; usable only if the human reviewer step is reliably staffed.
- **Requires additional infrastructure** — a needed control has no Enforced or Governed path yet (e.g., no shared durable blackboard exists for a topology that requires one).
