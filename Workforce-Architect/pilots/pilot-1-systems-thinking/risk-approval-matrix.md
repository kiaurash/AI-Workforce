# Risk / Approval Matrix: Systems Thinking in AI Publication Workforce

Status: Design-time proposal only. Hard-gate structure complete, but runtime enforcement is unverified until the proposed profiles are activated and smoke-tested.

| Consequential Action Category | Concrete Action in This Workflow | Approval Owner | Evidence Label |
|---|---|---|---|
| External writes | Publishing finalized post to community blog / CMS | Human editor | Proposed constraint, pending activation smoke test. The human-apply specs omit CMS/API write tools, but no runtime profiles were activated in this Pilot. Governed until verified. |
| Money | Any budget spend, sponsored post fees, advertising, or subscriptions | Not applicable to this workflow / no authority granted | Proposed constraint, pending activation smoke test. The human-apply specs omit financial and purchasing tools; absence is not yet a verified runtime fact. Governed until verified. |
| Production / infra changes | Modifying web servers, DNS, blog hosting infrastructure, or repo deployment workflows | Not applicable to this workflow / no authority granted | Proposed constraint, pending activation smoke test. The human-apply specs omit infrastructure/deployment tools; absence is not yet a verified runtime fact. Governed until verified. |
| Outbound communication | Broadcasting newsletter to email subscriber list, posting to social channels, sending direct messages | Human editor | Proposed constraint, pending activation smoke test. The human-apply specs omit email, messaging, and social tools; absence is not yet a verified runtime fact. Governed until verified. |
| Personnel | Hiring, directing external contractors, or altering human staff roles | Not applicable to this workflow / no authority granted | Proposed constraint, pending activation smoke test. The human-apply specs grant no personnel authority; this is not yet verified on activated profiles. Governed until verified. |
| Legal / contractual | Entering copyright licensing agreements, terms of service commitments, or legal warranties | Not applicable to this workflow / no authority granted | Proposed constraint, pending activation smoke test. The human-apply specs grant no legal/signature authority; this is not yet verified on activated profiles. Governed until verified. |
| Agent / system configuration change | Proposing or altering agent prompts, skills, toolset allocations, or SOUL definitions | Strictly disallowed by policy in this workflow. No agent may modify another agent's configuration. | Proposed constraint, pending activation smoke test. The human-apply specs omit `skill_manage` and configuration-mutation tools; this is not yet a verified runtime fact. Governed until verified. |

---

## Runtime Safety & Board Assumptions
1. The proposed boundary between automated draft preparation (W1-W6) and consequential actions (G1) is **Governed/unverified** until the human-apply profiles are activated and smoke-tested; tool omission in a specification is not runtime enforcement.
2. **Failed board assumption:** multiple non-human profiles on this live shared board have the kanban toolset and can possess `kanban_unblock`. Human-exclusive release is therefore **not Enforced** on this board.
3. `initial_status='blocked'` did prevent normal dispatch for all eight Scaffold tasks. Authorization of any later unblock remains **Governed** by operating procedure and board composition, not identity-enforced here.
