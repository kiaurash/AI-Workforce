# Decision Record

Produced by a Decision Work Unit before any branch task is created.

- Decision ID / workflow version:
- Evidence / artifacts evaluated and their provenance:
- Explicit criteria / thresholds applied (not "used judgment"):
- Selected branch and rationale:
- Confidence / uncertainty, and any dissent or missing information:
- Applicable risk/approval-matrix reference:
- Innovation envelope check (if novel branch): allowed artifact/destination types / tool-data scope / iteration-task budget / cost-time budget / prohibited objective changes — `envelope_check = pass` or `fail`, limits consumed, remaining budget, review due date.
- Authorized next task template(s), or `ESCALATE_UNPLANNED_BRANCH`:
- Novel-branch flag (if applicable): `NOVEL_AUTO_PROCEEDED` (risk=low/no AND envelope_check=pass) / `NOVEL_PROPOSED` (consequential, OR envelope_check=fail, OR category=agent/system configuration change — always blocked) / `ANOMALOUS_BLOCKED` (stuck, no proposal)
- Human override field and timestamp:
