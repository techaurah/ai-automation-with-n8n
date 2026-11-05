# AGENTS.md

Conventions for AI assistants working in this repository. Human contributors should read CONTRIBUTING.md; this file states the same rules in machine-checkable form.

## Repository shape

- Lessons live in root folders named `NN-kebab-lesson-name`, numbered 00 to 34, matching the lessons table in README.md exactly. Never rename a lesson folder without updating README.md, llms.txt, and PROGRESS.md in the same change.
- Each lesson folder contains: `README.md` (the lesson), runnable artifacts (workflow JSON, Python twins or checkers), `exercise.md`, and `solution/` with the worked solution.
- Root files: README.md (landing page), llms.txt (course index for AI assistants), PROGRESS.md (learner checklist), DESIGN.md (the design this repo was built to), RESEARCH.md (the competitor scan), resources/, showcase/, translations/, assets/, tools/.

## Writing rules

- Plain language, short sentences. Define every technical term on first use or ensure it exists in resources/glossary.md.
- No em dashes anywhere, in prose or code comments. Use commas, colons, or full stops instead.
- Question-shaped headings are welcome in lessons where natural.
- No invented statistics, learner counts, or results. Product facts (versions, pricing, node behaviour) need a source or a check against current n8n documentation; n8n ships weekly and this course teaches the 2.x model.
- Do not promise certificates. The course's completion artifact is the public capstone showcase.

## Workflow and code rules

- Every workflow JSON must pass tools/validate_workflows.py: parses, unique node names, every connection target exists, AI sub-node connection types consistent. CI runs it.
- Workflow files ship with deliberate placeholders (SELECT_ markers) wherever an instance-specific value belongs (table ids, channels, credentials). Never replace a placeholder with a real value, and never commit a secret; Lesson 13's scanner (13-credentials-and-secrets/scan_workflows.py) must report zero findings.
- Python twins and checkers run on the standard library (Python 3.11 or newer) with a zero-credential path. A lesson may ship a `smoke_test.py`; CI runs every file with that name, so keep smoke tests fast, offline, and credential-free.
- Node names describe what the node does, never its type alone. Sticky notes carry setup steps and version notes where a workflow needs them.

## Change rules

- Small fixes may go straight to a pull request. New lessons, rewritten lessons, and new translation languages start with an issue (the two-tier rule in CONTRIBUTING.md).
- If lesson titles change, update README.md, llms.txt, and PROGRESS.md together; the three must never disagree.
- Showcase rows are added by learners via PR, one row per learner, format in showcase/README.md.
