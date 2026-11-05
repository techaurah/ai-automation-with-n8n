# Lesson 01: What automation is, and where n8n fits (workflow vs agent vs code)

**Time:** about 50 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 00 · **You need:** Nothing installed. The Python script runs anywhere; the workflow is for reading until Lesson 02.

Most automation projects fail before the first node, at the moment someone automates the wrong shape of job. This lesson gives you the three shapes (workflow, agent, and plain code), a three-question test for telling them apart, and a worked example of each. It ends with the smallest honest n8n workflow: three nodes that greet a new enquiry at a dental clinic, the fictional company, BrightSmile Dental, whose operations this whole course automates piece by piece.

## What is a workflow, in one paragraph?

A **workflow** is a fixed path: when this happens, do these steps in this order, branching where a rule says to branch. Every step is decided by the designer in advance. A workflow cannot surprise you with a new idea; it can only surprise you with an input you did not design for. That limitation is also its strength: workflows are predictable, testable, and cheap to run, which is why most business automation should be workflows. n8n is a workflow tool first. The canvas, the nodes, the executions view, all of it assumes a path someone designed.

## What is an agent, and why is it not just a better workflow?

An **agent** is a program that uses a language model to decide its next step as it goes: perceive, decide, act through a tool, observe, repeat. Agents handle jobs where the steps cannot be fixed in advance, like reading a messy support inbox and figuring out what each message needs. The price is real: agents are less predictable, harder to test, and cost model calls on every run. Course 1 in this programme teaches agents in depth; this course teaches the discipline of reaching for one only when the job's shape demands it, and then embedding it inside a workflow that keeps it on rails (Module 5). The fashionable error is building an agent for a job that was a workflow all along.

## When is the right answer plain code?

When the steps are fixed and the volume is high, or the logic is intricate in ways a canvas expresses badly. Recalculating prices over tens of thousands of products every night is a script, not a workflow: it needs tests, code review, and cheap compute, not a diagram. n8n does not compete with code; it orchestrates around it. The Code node exists for the ten lines a workflow needs, the HTTP Request node exists to call services your code runs, and sub-workflows exist so a workflow can delegate. A mature automation estate is workflows at the business edge and code at the core, which is why this course ships Python twins beside its workflows: the two views of one design, kept honest against each other.

## The three-question test

For any job, ask: **Do the steps stay the same every run? Does any step need open-ended judgement? How many runs a month?** Fixed steps with no judgement is a workflow. Fixed steps with one fuzzy decision (classify this, draft that) is a workflow with an AI step, the shape this course builds most. Unfixed steps with judgement throughout is an agent's job, ideally inside a workflow frame. Fixed steps at very high volume is code. `decide.py` in this folder encodes exactly this test over four scenarios, including the invoice chaser, which fools many people into an agent when it is really a workflow with one AI drafting step.

## Run it

```bash
cd 01-what-automation-is-and-where-n8n-fits
python3 decide.py
```

Read the reasoning lines, not just the verdicts. Then read `workflow.json`: a Manual Trigger, an Edit Fields node that shapes two fields, and a Code node that writes the greeting. Three nodes, one wire each. In Lesson 02 you will import and run it; for now, notice that you can already predict exactly what it will output, which is the workflow property in action.

## Common failures

- **Automating a broken process faithfully.** A workflow does the wrong thing at scale, faster. If the manual process embarrasses you, fix the process first, then automate it.
- **Reaching for an agent because it demos well.** Agents demo beautifully and bill monthly. If the steps are fixed, the agent is an expensive, less reliable workflow.
- **Counting only build time.** A workflow you cannot debug, rerun safely, or explain to its owner is not finished. Modules 4 and 6 exist because running automations is the job, not the afterthought.
- **Automating judgement you have not made yourself yet.** If a human cannot say what the right reply to an enquiry looks like, no model step will invent the standard. Do the job manually ten times first.

## Recap checklist

- [ ] I can define workflow, agent, and the three-question test without notes.
- [ ] I ran decide.py and can argue with at least one of its verdicts, with reasons.
- [ ] I know which BrightSmile process each module of this course automates.
- [ ] I can read the three-node workflow and predict its output.

## Resources

- [n8n documentation home](https://docs.n8n.io/)
- [n8n workflow templates library](https://n8n.io/workflows/)
- [Agentic AI for Beginners, Course 1 in this programme](https://github.com/techaurah/agentic-ai-for-beginners)
- [n8n community forum](https://community.n8n.io)
