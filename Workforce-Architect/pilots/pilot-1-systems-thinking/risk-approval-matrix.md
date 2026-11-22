# Risk / Approval Matrix: Systems Thinking in AI Publication Workforce

Status: Evaluated and Enforced. Hard gate complete.

| Consequential Action Category | Concrete Action in This Workflow | Approval Owner | Evidence Label |
|---|---|---|---|
| External writes | Publishing finalized post to community blog / CMS | Human editor | Enforced. No agent profile possesses CMS publishing tools, API keys, or web write permissions. All agent outputs are local Markdown artifacts. |
| Money | Any budget spend, sponsored post fees, advertising, or subscriptions | Not applicable to this workflow / no authority granted | Enforced. No financial, purchasing, or token-spending tools granted to any agent. |
| Production / infra changes | Modifying web servers, DNS, blog hosting infrastructure, or repo deployment workflows | Not applicable to this workflow / no authority granted | Enforced. No infrastructure, cloud provider, or hosting deployment tools granted to any agent. |
| Outbound communication | Broadcasting newsletter to email subscriber list, posting to social channels, sending direct messages | Human editor | Enforced. No agent holds email broadcast (SMTP/SES), messaging, or social API tools. Delivery terminates at internal artifact creation. |
| Personnel | Hiring, directing external contractors, or altering human staff roles | Not applicable to this workflow / no authority granted | Enforced. No personnel management tools or authority exist. |
| Legal / contractual | Entering copyright licensing agreements, terms of service commitments, or legal warranties | Not applicable to this workflow / no authority granted | Enforced. No legal or signature authority granted to any agent. |
| Agent / system configuration change | Proposing or altering agent prompts, skills, toolset allocations, or SOUL definitions | Strictly disallowed by policy in this workflow. No agent may modify another agent's configuration. | Enforced. Skill-editing (`skill_manage`), profile configuration, and file modification tools targeting agent configuration files are explicitly omitted from all agent profiles. |

---

## Runtime Safety & Board Assumptions
1. The boundary between automated draft preparation (W1-W6) and consequential actions (G1) is Enforced by technical omission of publishing tools.
2. No agent possesses `kanban_unblock` or orchestrator-level override tools.
3. Standing assumption: No non-human-gated bot on the shared board holds unconstrained orchestrator permissions to unblock tasks or deploy external changes.
