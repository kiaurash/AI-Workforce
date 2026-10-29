# Risk / Approval Matrix

Hard gate: every row below must have a declared approval owner AND a declared evidence label before any roster or scaffold is emitted. A blank cell blocks emission exactly like an undefined owner — "not applicable" is itself a decision that must be stated explicitly, never left empty.

| Consequential Action Category | Example In This Workflow | Approval Owner (human / Governed review / not yet allowed) | Evidence Label (Enforced / Governed / Advisory) |
|---|---|---|---|
| External writes | Publish to CMS | Human clicks publish | Enforced (Publisher agent's toolset has no publish tool) |
| Money | Not applicable to this workflow / no authority granted | Not applicable to this workflow / no authority granted | Enforced — no agent in this roster holds money-movement tools |
| Production / infra changes | Not applicable to this workflow / no authority granted | Not applicable to this workflow / no authority granted | Enforced — no agent in this roster holds production/infra tools |
| Outbound communication | Email to community list | Human approves before send | Governed (reviewer checks before unblock) |
| Personnel | Not applicable to this workflow / no authority granted | Not applicable to this workflow / no authority granted | Enforced — no agent in this roster holds personnel tools |
| Legal / contractual | Not applicable to this workflow / no authority granted | Not applicable to this workflow / no authority granted | Enforced — no agent in this roster holds legal/contractual tools |
| Agent / system configuration change | Meta-learner proposes a Soul.md edit to another agent | Human reviews controlled-trial result before applying | Governed (no auto-proceed path exists for this category at any risk level) |

The seventh category exists because a change to another agent's standing configuration (skill, Soul.md, toolset) has a blast radius across every future run of that agent, not just one task's output — it is never eligible for the low-risk auto-proceed path available to other categories (see SKILL.md Pitfalls).
