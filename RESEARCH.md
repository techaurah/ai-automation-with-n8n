# Competitor research: free n8n and AI automation courses

Written 2026-11-05, before any lesson was drafted, per the TechAurah
GitHub programme rule: competitor research first, always. Every fact
below was observed in web search results on that date. Star counts are
point-in-time observations from the named source, not live guarantees,
and where two sources disagree the disagreement is recorded rather
than smoothed over.

## The official path: n8n Academy

Source: n8n community forum, Class Central's best n8n courses guide,
The AI School's n8n courses guide (checked 21 October 2026), and the
n8n Academy course pages at learn.n8n.io, all read 2026-11-05.

- n8n Academy at learn.n8n.io soft-launched on 16 June 2026 with four
  free courses: QS101 Quickstart (3 to 5 hours) and the Foundations
  programme, N8N101 Essentials (2 to 4 hours), N8N102 Integrations
  (4 to 6 hours), and N8N103 In Practice (3 to 4 hours).
- The older text-based Level One and Level Two courses that lived in
  the docs were retired on 30 June 2026. Anyone following older blog
  posts to those courses now lands on redirects.
- Grading is uniform: quizzes 10 percent, hands-on workflow exercises
  55 percent, final exam 35 percent, with a 70 percent pass mark.
  Badges and certificates of completion are issued through Accredible.
- The arc is sound: triggers and scheduling, data mapping and merging,
  flow control, sub-workflows, error handling, the HTTP Request node
  with API keys and OAuth2, webhooks, Data Tables, then the AI Agent
  node with tools and memory, debugging, and Try/Catch patterns.
- Exercises run against practice APIs hosted by the Academy, so no
  external accounts are needed, but most Foundations courses need a
  publicly accessible n8n instance (Cloud trial or self-hosted).

Strengths to respect: it is official, current with n8n 2.x, free, and
its exercises are real builds. Weaknesses we can beat: it is exam and
certificate shaped, it lives on a learning platform rather than in a
repository a learner can fork and keep, it has no public showcase of
finished learner projects, and its production coverage stops well
short of self-hosting operations, security hardening, and cost
engineering.

## GitHub template collections: huge, and not courses

- enescingoz/awesome-n8n-templates: 280 plus templates across Gmail,
  Telegram, Slack, WhatsApp, AI agents, RAG chatbots, and more.
  Observed at 26,200 stars in a scanner report dated 2026-10-31 and
  at 26.3k stars on star-history.com on 2026-11-05. The largest
  template collection of its kind, and purely a library: import and
  adapt, with no lesson sequence, no exercises, and no solutions.
- ScraperNode/awesome-n8n-templates: 8,697 templates scraped from
  n8n.io and organised by category, integration, and use case
  (dev.to announcement, March 2026). Browsing infrastructure, not
  teaching.
- wassupjay/n8n-free-templates: 200 plus import-ready AI workflows
  across 20 plus categories. Observed at 5,942 stars and 1,597 forks
  as of 1 August 2025 (BrightCoding write-up). Its own README flags
  that some templates are incomplete.
- GetPrompting's free n8n workflow library: twelve practical
  workflows under MIT, built around a shared beginner pattern (input,
  prompt preparation, a local Ollama model, parsing, human review,
  output). The closest in spirit to this course's zero-credential
  approach, but twelve workflows is a starter pack, not a course.

Lesson for us: template scale is not the gap. Nobody needs a 281st
template repo. The gap is pedagogy wrapped around workflows: why a
workflow is shaped this way, what breaks, and how you know it works.

## GitHub courses and guides

- leonvanzyl/n8n-course: beginner n8n course materials on GitHub,
  listed in curated AI automation resource lists (for example
  ShakeLv/oar-ai-automation). Video-led, with the repo as supporting
  material rather than the course itself. No star count was observed
  in this scan.
- justhassann/learn-n8n-automations: a single-document "n8n Workflow
  Automation Training Guide" (also distributed as a PDF master
  guide). Module 1 covers automation concepts, setup, community, and
  templates. One long guide, last crawled copy dated about 674 days
  before this scan, so it predates n8n 2.0 and the current AI nodes.
- ShakeLv/oar-ai-automation: a curated list spanning OpenClaw, Claude
  Code, n8n, Make, and more, with an n8n resources section. Lists are
  discovery tools, not courses.

## Platform courses

- FreeAcademy.ai, "n8n for Beginners": free, text-first, 3 modules
  and 7 lessons, built on importing ready-made JSON workflows and
  editing them. Certificate on passing a final exam. Good
  zero-to-first-workflow path, far too short to reach production or
  AI agents in depth.
- Stepthrough (Ynteractive): a 13-part free AI course with 144
  modules live, including an n8n automation toolkit part. Broad
  multi-tool coverage (Custom GPTs, Lovable, voice agents), so n8n
  depth is traded for breadth.
- AiAdvisors, "How to Build an AI Agent" (free, about 2 hours): an
  AI assistant connected through n8n-mcp builds workflows for you.
  Interesting and current, but it teaches directing an assistant,
  not building workflows yourself, and it leans on paid AI plans.
- KodeKloud, "n8n: Zero to Hero": paid, lab-based, covers Docker and
  AWS self-hosting, RAG agents with Pinecone, and multi-agent builds.
  The production and hosting depth here is the paid benchmark our
  free production module has to be honest competition for.
- Udemy beginner courses (for example "N8N for Beginners: Build
  Automations from Scratch", listed at 14.99 USD in search results):
  video-first, app-connection tours, little on reliability,
  idempotency, or security.

## The product facts this course must teach correctly

Observed across n8n's own materials and multiple current guides,
November 2026 unless noted:

- Current stable line is n8n 2.42.x (2.42.6 noted 10 October 2026,
  2.42.7 in an October 2026 install guide). n8n 2.0 (beta 8 December
  2025, stable mid-December 2025) replaced the Active toggle with
  Save versus Publish: saving edits a draft, publishing makes it
  live.
- 2.0 security defaults: Code nodes run in isolated task runners,
  environment variable access from nodes is blocked by default
  (N8N_BLOCK_ENV_ACCESS_IN_NODE), and the Execute Command and Local
  File Trigger nodes are disabled by default. MySQL and MariaDB
  support was dropped; PostgreSQL is the production database.
- A parent workflow now receives a sub-workflow's final output even
  when the sub-workflow pauses at a Wait node for human approval.
  This makes human-in-the-loop designs practical.
- AI is LangChain-based and first class: the AI Agent node (a Tools
  Agent since the agent-type selector was removed in v1.82.0; the
  node now requires at least one tool connected), chat model nodes
  (OpenAI, Anthropic, Gemini, Bedrock, Ollama, and more), memory
  nodes (Simple Memory, formerly Window Buffer Memory, plus Postgres
  and Redis chat memory), the Basic LLM Chain for no-tool jobs, Text
  Classifier, vector store nodes, the AI Agent Tool node for
  single-canvas multi-agent work, human review for individual AI
  tool calls (v2.6), and MCP in both directions (MCP Client Tool,
  MCP Server Trigger, and instance-level MCP access).
- Data Tables (from 1.113.1) are built-in tabular storage inside the
  instance, managed from the home screen and used through the Data
  Table node (n8n-nodes-base.dataTable), with system columns id,
  createdAt, and updatedAt.
- Installation today is Docker-first: the one-line setup
  (curl -fsSL https://get.n8n.io | sh) or Docker Compose, editor on
  port 5678. The npm route needs Node.js 20.19 to 24.x, is documented
  as not safe for production, and npm installs are deprecated from
  n8n 3.0.
- Money facts, as reported by multiple October 2026 guides from
  n8n's pricing page: the self-hosted Community Edition is free with
  no execution cap; n8n Cloud has a 14-day trial and no permanent
  free plan; Cloud Starter is 20 EUR per month billed annually for
  2,500 executions and Pro is 50 EUR for 10,000. This course quotes
  these as reported figures with dates, and tells learners to check
  the pricing page before budgeting.
- n8n itself: the curated list read in this scan said "46k plus
  stars" for n8n-io/n8n while another site said "100K plus stars";
  the two figures are stale in opposite directions, so this course
  does not quote an n8n star count at all. The czlonkowski/n8n-mcp
  server was observed at 23,198 stars (GStars snapshot, early
  November 2026) and described on n8n.io as 16k plus in an older
  template page.

## Gaps we can beat

1. **No forkable, text-first, complete course.** The Academy is a
   platform course with exams; GitHub offerings are template dumps
   or single guides. A repository course where the fork is the
   workbook, every lesson has an exercise and a worked solution, and
   progress is a checklist, does not exist yet for n8n.
2. **Workflows nobody validates.** Template repos ship JSON that may
   or may not import cleanly, and some admit incompleteness. A
   course whose every workflow JSON is machine-checked in CI
   (parses, connections point at real nodes, node names unique) can
   promise importable on day one.
3. **AI lessons that skip the boring, decisive parts.** Most agent
   tutorials stop at a chat demo. Error workflows, retries,
   idempotency, deduplication, human approval, and security
   hardening are where automations earn trust, and they are
   systematically under-taught.
4. **Pre-2.0 material everywhere.** Video courses and guides built
   on the Active toggle, $env in expressions, and npm installs now
   teach habits the current product blocks by default.
5. **Business-shaped capstones.** Courses end with chatbots and
   scrapers. A capstone that runs a small service business's lead
   handling end to end (intake, qualification, follow-up, daily
   digest) matches what learners actually get paid to build.

## The differentiation this course takes

See DESIGN.md for the full design. In short: the Course 1 house
standard applied to n8n. Thirty-five lessons in eight modules, one
arc, one capstone (the Lead Machine for a fictional dental clinic).
Every lesson is a complete unit with an importable, CI-validated
workflow, a Python twin or checker where the logic is testable
offline, one exercise, and a worked solution. The zero-credential
rule holds: self-hosted Community Edition, simulated model steps,
and local Ollama for the AI module, with paid swaps named at the top
of the lesson, never midway. No certificate; the completion artifact
is the learner's public capstone, indexed in the course showcase.
