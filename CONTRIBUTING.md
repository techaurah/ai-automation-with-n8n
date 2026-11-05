# Contributing to AI Automation with n8n

Thank you for helping improve this course. Learners who fix lessons become the reason the next learner finishes.

## The two-tier rule

- **Small fixes: open a pull request directly.** Typos, broken links, a wrong command, a clearer sentence, a small fix in one lesson or one workflow file. No issue needed, no permission needed.
- **Big changes: open an issue first.** A new lesson, a rewritten lesson, a new translation language, a restructure, anything touching many files. Use the lesson proposal template so a maintainer can agree the shape with you before you invest the work. This rule exists to protect your time from duplicated or unwanted effort, not to gatekeep.

Showcase submissions (adding your finished capstone row) are small fixes: PR directly, following [showcase/README.md](showcase/README.md).

## The lesson quality bar

Every lesson, new or edited, must hold to the standard the course launched with:

1. **Complete unit.** A lesson folder holds a written lesson (README.md), runnable artifacts, an `exercise.md`, and a worked solution under `solution/`. No part may be a stub or a "coming soon".
2. **Valid workflows.** Every workflow JSON passes `tools/validate_workflows.py` (CI runs it): parses, unique node names, connections sound. If a workflow needs an instance-specific value, ship a `SELECT_` placeholder and a sticky note explaining the setup, never a real id.
3. **Zero-credential demo path.** Every lesson works on the free self-hosted Community Edition, with simulated steps or a local Ollama model where AI is involved. Anything needing a paid account or key says so at the top of the lesson, never midway.
4. **Exercise plus solution.** The exercise must change the worked example in a meaningful direction, not repeat it, and it ships with a worked solution and an explanation.
5. **Plain language.** Short sentences, every technical term defined on first use or present in [resources/glossary.md](resources/glossary.md), and no em dashes anywhere.
6. **Honest numbers and current facts.** No invented statistics. n8n changes weekly: check node names, defaults, and version claims against current n8n documentation before submitting.
7. **Resources.** Each lesson ends with 3 to 6 curated links, official documentation first.

## Pull request checklist

- One lesson or one concern per PR; small PRs review faster.
- If you edited the lessons table in the root README, check every folder link still resolves.
- If you edited a workflow, run `tools/validate_workflows.py` and say so in the PR description.
- If you edited code, confirm any `smoke_test.py` in that lesson passes; CI runs them.
- Translations follow [translations/README.md](translations/README.md).

## Reporting problems

Lesson bugs (invalid workflow, broken links, instructions that do not work) are issues, filed with the lesson problem template. Questions about content belong in Discussions, not issues.

## Code of conduct

Participation is covered by the [Code of Conduct](CODE_OF_CONDUCT.md).
