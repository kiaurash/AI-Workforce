# M0.5 Workspace Rules

For the M0.5 smoke test, Hermes may:

- read `inputs/sample-meeting.md`;
- create `outputs/commitments.md`; and
- explain uncertainty in the output and its run receipt.

Hermes must not:

- alter `inputs/sample-meeting.md`;
- alter this file;
- create or modify files outside `outputs/`;
- send messages or use external systems; or
- treat tentative statements, questions, or possibilities as confirmed commitments.

If an owner or deadline is not explicitly supported by the transcript, label it `unknown`.
