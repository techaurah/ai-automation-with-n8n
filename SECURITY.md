# Security policy

## Reporting a vulnerability

If you find a security problem in this repository, for example a lesson that teaches an unsafe pattern, example code that leaks credentials, or a workflow file containing a real secret, please do not open a public issue with the details.

Report it privately through the contact form at [techaurah.com](https://techaurah.com), with "AI Automation course security" in the message. We aim to acknowledge reports within three working days and to fix or annotate confirmed problems in the affected lesson.

## Scope notes

- This is a teaching repository. Example workflows favour clarity, and lessons say explicitly where production hardening differs from the teaching version (Lesson 30 is the hardening pass in depth).
- Never commit real API keys, tokens, or instance-specific ids to your fork. Lessons ship `SELECT_` placeholders on purpose. If you accidentally commit a secret, rotate it immediately; deleting the commit is not enough (Lesson 13 explains why).
- The scanners in Lessons 13 and 30 are tripwires for common secret and risk shapes, not guarantees. If you find a shape they miss, that is a lesson improvement worth an issue, filed without the secret itself.
