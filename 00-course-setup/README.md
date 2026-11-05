# Lesson 00: Course setup: environment, accounts, free paths, how to use this repo

**Time:** about 40 minutes · **Difficulty:** Beginner · **Prerequisites:** None · **You need:** A computer, and Python 3.11 or newer for the checker script. No n8n yet, no accounts, no keys.

Every course that starts with "install the thing" loses people in the first ten minutes, so this one starts with a decision and a checker. By the end of this lesson you will know which of the three ways to run n8n is yours, what is free and what is not, stated before you meet a paywall rather than after, and you will have run a script that verifies your machine against exactly what this course needs. The actual installation is Lesson 02, done properly, once you know why you are doing it.

## What are the three ways to run n8n?

n8n is a workflow automation tool: you connect nodes on a canvas, each node does one job (watch for a form submission, read a spreadsheet, call an API, ask a model a question), and a run of the workflow is called an **execution**. You can run it three ways.

**Self-hosted Community Edition.** You run n8n yourself, usually in Docker. It is free, with no execution cap, and your data stays on your machine. The cost is that you are the operations team: updates, backups, and security are yours. This is the course's main path, because it is the only one where every lesson, including the production module, works exactly as written.

**n8n Cloud.** n8n's hosted service. It starts with a 14-day trial and has no permanent free plan; paid plans are metered by executions (guides reading n8n's pricing page in October 2026 report Starter at 20 EUR per month billed annually for 2,500 executions, Pro at 50 EUR for 10,000; check the pricing page yourself before budgeting, because plans change). Cloud is the right choice when nobody on your team wants to run a server.

**npm on your laptop.** `npx n8n` with Node.js 20.19 to 24.x gets an editor open in minutes for a throwaway look. n8n's own docs say this route is not safe for production, and npm installs are deprecated from n8n 3.0. This course treats it as a demo path only and says so wherever it appears.

## What is free in this course, exactly?

The course itself: everything, under the MIT license. The tools: the Community Edition is free to self-host; Docker is free; Python is free; the model steps in the AI module run on Ollama, a free local model runner, or on simulated steps that need no model at all. The optional costs are named at the top of any lesson that has one: an n8n Cloud plan if you choose Cloud over self-hosting, and hosted model API usage if you choose a hosted model over Ollama in the AI module. No lesson springs a cost on you midway, and no lesson needs a credit card to complete its exercise.

## How is this repository organised?

Lessons live in numbered folders, `00` to `34`, in eight modules. Every lesson folder holds the same four things: `README.md` (the lesson), the runnable artifacts (usually `workflow.json`, an importable n8n workflow, plus a Python twin or checker where the logic can be tested offline), `exercise.md`, and `solution/` with the worked solution. Root files matter too: `PROGRESS.md` is your checklist, `llms.txt` is the course index written for AI assistants, and `resources/glossary.md` defines every term the course uses.

Two habits pay off all course long. First, **fork this repository**: your fork is your workbook and, at the end, holds your capstone. Second, **every workflow in this repo is machine-checked**: the repo's CI parses each `workflow.json`, confirms node names are unique, and confirms every connection points at a real node. When a lesson says a workflow imports cleanly, that is a tested claim, not a hope.

## What if I already have n8n?

Skim, do not skip. Run the checker anyway (it also validates that this repo cloned completely), then in Lesson 02 compare your instance against the course baseline: a current 2.x release, persistent storage, and an owner account. Version matters in this course: it teaches the n8n 2.x model, where saving a workflow edits a draft and **Publish** makes it live. Material written for the old Active toggle will confuse you here, and Lesson 28 covers the draft and publish model properly.

## Run it

Run the checker:

```bash
cd 00-course-setup
python3 check_environment.py
```

You want no FAIL lines. WARN lines are decisions, not errors: no Docker is fine on the Cloud path, no Node.js is fine everywhere except the npm demo route.

Then open `workflow.json` and read it before you have anywhere to import it. It is plain JSON: a `nodes` array (a Manual Trigger and a Code node) and a `connections` object wiring one to the other. Everything in this course is built from files shaped like this one, and being able to read them is a skill the course deliberately teaches. In Lesson 02 you will import this exact file and run it as your setup ping.

## Common failures

- **Treating the Cloud trial as the free plan.** The trial ends; the Community Edition does not. Decide in this lesson which one your capstone will live on, or Lesson 34 will involve a migration you did not plan.
- **Installing before deciding about data.** A throwaway `npx n8n` run keeps its data in a local folder you will forget. Lesson 02 sets up persistent storage deliberately; do not build real workflows before it.
- **Skipping the fork.** Reading lessons in the web UI feels faster until the capstone, when you need your own copy of everything. Fork now, read in the fork.
- **Assuming your old n8n knowledge transfers unchanged.** If you learned n8n before version 2.0, the Publish model, blocked environment variables, and task runners are all new defaults. The course flags each where it bites.

## Recap checklist

- [ ] I can name the three ways to run n8n and which one is mine, and why.
- [ ] I ran check_environment.py and have no FAIL lines.
- [ ] I can state what is free in this course and where the optional costs live.
- [ ] I forked the repository and can find PROGRESS.md and the glossary.
- [ ] I read workflow.json and can point at its nodes and connections.

## Resources

- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
- [n8n hosting documentation](https://docs.n8n.io/hosting/)
- [n8n pricing page (check before budgeting)](https://n8n.io/pricing/)
