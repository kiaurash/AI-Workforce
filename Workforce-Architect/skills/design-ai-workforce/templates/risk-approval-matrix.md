# Risk / Approval Matrix

Hard gate: every row below must have a declared approval owner before any roster or scaffold is emitted. Leave no row blank — an undefined owner blocks emission (gap report only).

| Consequential Action Category | Example In This Workflow | Approval Owner (human / Governed review / not yet allowed) | Evidence Label (Enforced / Governed / Advisory) |
|---|---|---|---|
| External writes | Publish to CMS | Human clicks publish | Enforced (Publisher agent's toolset has no publish tool) |
| Money | n/a | | |
| Production / infra changes | n/a | | |
| Outbound communication | Email to community list | Human approves before send | Governed (reviewer checks before unblock) |
| Personnel | n/a | | |
| Legal / contractual | n/a | | |
| Agent / system configuration change | Meta-learner proposes a Soul.md edit to another agent | Human reviews controlled-trial result before applying | Governed (no auto-proceed path exists for this category at any risk level) |

The seventh category exists because a change to another agent's standing configuration (skill, Soul.md, toolset) has a blast radius across every future run of that agent, not just one task's output — it is never eligible for the low-risk auto-proceed path available to other categories (see SKILL.md Pitfalls).
