# Course design: AI Automation with n8n

The design this repository was built to. Research behind it:
[RESEARCH.md](RESEARCH.md). House standard inherited from Course 1,
Agentic AI for Beginners: numbered lesson folders, every lesson a
complete unit (written lesson, runnable artifact, exercise, worked
solution), zero-credential demo path, no em dashes, no invented
statistics, no certificates.

## Title and promise

**AI Automation with n8n** is a free, complete course that teaches
you to design, build, debug, and run n8n workflows that do real
work, from your first two-node workflow to an AI agent with tools
and memory, and a production instance you can defend.

## Audience

- Operators, founders, and agency teams who run processes by hand
  today and want automations they understand, not templates they
  cargo-cult.
- Developers who can read JSON and a little JavaScript or Python
  and want the visual-automation skill set clients ask for.
- Learners from Course 1 who met n8n in Lesson 08 there and want
  the full treatment. This course stands alone; Course 1 is not
  required.

Not for: complete beginners who have never seen JSON or a terminal
(the prerequisites below are real), or anyone shopping for a
certificate. There is none; the capstone showcase is the artifact.

## Prerequisites

- Comfort reading JSON, and basic JavaScript or Python (functions,
  objects, arrays). The Code node lessons teach the n8n-specific
  parts, not the language itself.
- A computer that can run Docker, or an n8n Cloud trial account.
- Python 3.11 or newer for the offline twin and checker scripts.
- No paid API keys. AI lessons run on a local Ollama model or a
  simulated model step; paid swaps are named at the top of the
  lesson that offers them.

## The arc

One fictional company, BrightSmile Dental, runs through the whole
course (learners of Course 1 met it there). Every module automates
one more piece of its operations, and the capstone assembles the
pieces into the Lead Machine: intake, qualification, follow-up,
and a daily digest, running on a schedule with error handling and
human approval where it matters.

## Lesson map: 35 lessons, 8 modules

### Module 0: Start here

| # | Lesson | Builds |
|---|--------|--------|
| 00 | Course setup: environment, accounts, free paths, how to use this repo | A verified setup checker and an instance decision you can defend |
| 01 | What automation is, and where n8n fits (workflow vs agent vs code) | A decision worksheet and a hello workflow |

### Module 1: n8n foundations

| # | Lesson | Builds |
|---|--------|--------|
| 02 | Installing and running n8n (Docker first, Cloud, npm honestly labelled) | A running local instance with persistent data |
| 03 | The editor and your first workflow | A two-node workflow you can read like a sentence |
| 04 | How data flows: items, JSON, and paired items | A data-shaping workflow plus a Python twin |
| 05 | Expressions and mapping | Field mapping without the Code node, and knowing when to use it anyway |
| 06 | Triggers: schedules, webhooks, and forms | Three entry points into the same workflow shape |

### Module 2: Core nodes in depth

| # | Lesson | Builds |
|---|--------|--------|
| 07 | Edit Fields and the Code node | Transformations both ways, and the judgment to pick |
| 08 | Conditional logic: IF, Switch, Merge, Filter | A router that handles the awkward enquiry, not just the happy one |
| 09 | Loops, batches, and pagination | A paginated API harvest that respects rate limits |
| 10 | HTTP Request and APIs | A credential-free public API integration with error branches |
| 11 | Files and binary data | A file pipeline: read, convert, write, attach |
| 12 | Data Tables and state that lasts | Persistent lead state without an external database |

### Module 3: Connecting real services

| # | Lesson | Builds |
|---|--------|--------|
| 13 | Credentials and secrets done right | A credential audit of your own instance |
| 14 | Spreadsheets and databases | A two-way sheet sync with a database twin in Python |
| 15 | Email, messaging, and notifications | A notification ladder: draft, send, escalate |
| 16 | Forms, CRMs, and business apps | A form-to-CRM intake with deduplication |

### Module 4: Reliability

| # | Lesson | Builds |
|---|--------|--------|
| 17 | Error workflows and retries | A global error workflow that pages a human with context |
| 18 | Debugging: executions, pinning, and logs | A debugging drill on a deliberately broken workflow |
| 19 | Idempotency, deduplication, and safe reruns | A workflow you can rerun after a crash without double-sending |

### Module 5: AI in n8n

| # | Lesson | Builds |
|---|--------|--------|
| 20 | AI in n8n: the map (LangChain nodes, models, local vs hosted) | A Basic LLM Chain on a local model, and the vocabulary for the module |
| 21 | Your first AI agent | A chat agent with a model, a tool, and honest limits |
| 22 | AI tools and workflow tools | An agent that calls your own workflows as tools |
| 23 | Memory and conversations | Session memory done right, and when to graduate to Postgres |
| 24 | Classification and structured output | A ticket classifier whose output a router can trust |
| 25 | RAG in n8n | A question-answering workflow over clinic documents |
| 26 | MCP in both directions | An agent using an MCP server, and a workflow exposed as one |
| 27 | Human-in-the-loop and guardrails | Approvals before actions, and checks on model output |

### Module 6: Production

| # | Lesson | Builds |
|---|--------|--------|
| 28 | Saving, publishing, and versioning | A draft-to-publish routine with exported, reviewable workflow files |
| 29 | Self-hosting in production | A Docker Compose stack with Postgres, backups, and an update drill |
| 30 | Security hardening | A hardening pass: task runners, env access, webhook security, access control |
| 31 | Monitoring, cost, and scaling | An operations dashboard habit and an execution budget |

### Module 7: Capstone

| # | Lesson | Builds |
|---|--------|--------|
| 32 | Capstone spec and scaffolding: the Lead Machine | The spec, the data model, and validated skeleton workflows |
| 33 | Build the Lead Machine | Intake, qualification, follow-up, and digest workflows, tested |
| 34 | Ship it: publish, document, showcase | A published capstone and a showcase submission |

## Capstone

The Lead Machine for BrightSmile Dental: a form and webhook intake
that classifies and qualifies enquiries, stores them in a Data
Table, drafts replies for human approval, sends follow-ups on a
schedule for leads that go quiet, and posts a daily digest of new
and stale leads. It ships with an error workflow, an idempotency
key per lead, and a Python test harness that validates every
workflow file and simulates the classification contract offline.

## Visuals

Generated by assets/visuals/generate_visuals.py in the Course 1
branded style (navy, light blue, cyan, amber gates):

| Diagram | Teaches | Used in |
|---------|---------|---------|
| course-map.svg | The whole course on one page | README |
| workflow-anatomy.svg | Trigger, nodes, connections, executions | Lessons 01, 03 |
| items-and-json.svg | Items in, items out, one JSON object per item | Lesson 04 |
| expressions-flow.svg | Mapping fields with expressions vs Code | Lesson 05 |
| trigger-types.svg | Manual, schedule, webhook, form, chat | Lesson 06 |
| error-workflow.svg | Failure to error workflow to human with context | Lesson 17 |
| ai-agent-anatomy.svg | Agent, model, memory, tools as sub-nodes | Lessons 20, 21 |
| rag-pipeline.svg | Load, split, embed, store, retrieve, answer | Lesson 25 |
| mcp-directions.svg | MCP Client Tool in, MCP Server Trigger out | Lesson 26 |
| production-layers.svg | Publish, hosting, security, monitoring layers | Lessons 28 to 31 |
| capstone-flow.svg | Intake, qualify, follow up, digest | Lessons 32 to 34 |

## Verification built into the repo

- tools/validate_workflows.py checks every workflow JSON in the
  repo: it parses, node names are unique, every connection points
  at a real node, and AI sub-node connections use the right types.
  CI runs it on every push.
- CI also compiles every Python file and runs every smoke_test.py,
  same as Course 1.
- Internal links are checked before release by
  tools/check_links.py (relative links resolve to files on disk).
