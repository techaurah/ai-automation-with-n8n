# Lesson 22: AI tools and workflow tools: giving the agent your automations as hands

**Time:** about 70 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 21, Lesson 06 (sub-workflow ideas arrive here in full) · **You need:** Your instance and a working agent from Lesson 21.

An agent with only built-in toys is a demo. An agent that can call your own workflows, the booking checker, the price lookup, the intake pipeline, is a colleague. This lesson teaches n8n's tool family properly: the ready-made tool sub-nodes, the HTTP Request Tool that turns any API into a tool, and the crown jewel, the Workflow Tool, which exposes an entire n8n workflow, with its own trigger contract, as one of the agent's tools.

## The tool shelf, surveyed quickly

Tool sub-nodes come in kinds. **App tools**: many service nodes (Google Sheets, Slack, and more) can connect directly as tools, with the model filling their fields; convenient, and to be scoped carefully, because a Sheets tool that can write any sheet is a broad permission wearing a narrow name. **Utility tools**: Calculator (Lesson 21), Code Tool (a JavaScript function as a tool, for small precise jobs), Wikipedia and search tools for reference lookups. **HTTP Request Tool**: any API endpoint becomes a tool, with placeholders the model fills (the `$fromAI()` expression names a value the model must supply, with a description that acts as its instruction). And **Workflow Tool**: a whole workflow as a tool, the subject of the next section. Across all kinds, the description is the interface (Lesson 21's law), and the return value is what the model reasons over, so return small, structured, unambiguous results; a tool that returns a rambling paragraph returns confusion.

## Workflow Tool and the Execute Workflow trigger: the deep pattern

A workflow becomes callable when it starts with the **Execute Workflow Trigger** (which defines its input contract) instead of a public trigger. Other workflows call it with the **Execute Workflow** node, deterministically, and agents call it through the **Workflow Tool** sub-node, which wraps the same call with a name and description the model can choose from. The sub-workflow in this lesson is a price lookup: treatment name in, price (or null) out, no model inside it at all. That purity is the pattern to copy: **tools do deterministic work; the agent does the deciding**. A sub-workflow with its own error handling, retries, and logging (Modules 4's skills, reused wholesale) is a tool you can trust, and the same sub-workflow usually serves both a deterministic caller (a form intake that needs a price) and the agent, which is code reuse in the truest sense this platform offers.

Version note for your notebook: in n8n 2.x, a parent now receives a sub-workflow's final output even when the sub-workflow pauses for a human approval, so approval-gated tools (a refund workflow that waits for a manager) compose correctly under an agent. Lesson 27 leans on this.

## Scoping: the security section hiding in a tools lesson

Every tool widens what the agent can do, including when the agent is confused or manipulated (Lesson 30 takes the threat model seriously). Scope in three ways. **Narrow tools over broad ones**: a `get_price` tool beats a generic database query tool, because its worst case is a wrong price, not a dumped table. **Read before write**: add write tools one at a time, behind Lesson 27's approvals, after their read-only twins have earned trust. **Credentials stay in the tool's workflow** (Lesson 13), never passed through the agent's context, where they would be visible to the model and the logs. The twin's catalogue print is the review artefact: read your agent's tool catalogue as an attacker and as an auditor, and remove anything you cannot justify in one sentence.

## Run it

Run the twin (`python3 tools_twin.py`) and read the catalogue as the model sees it. Import `subworkflow.json`, then `workflow.json`, select the sub-workflow in the Price lookup tool per the sticky note, publish both, and ask the agent for the whitening price and the hygiene price. In the agent's execution, find the tool call and follow it into the sub-workflow's own execution: two executions, one decision, full visibility. Ask for the price of a root canal (not in the table) and confirm the agent reports the null honestly rather than inventing a figure.

## Common failures

- **Tools that return essays.** The model reasons over the return value; a price tool returning a paragraph about pricing philosophy produces agents that quote philosophy. Small structured returns, always.
- **A generic query tool as a first tool.** Broad tools are broad permissions. Start with named, narrow, read-only tools and widen deliberately.
- **Duplicating logic inside the agent prompt.** Prices hard-coded in the system message and in the price workflow will diverge by next month. The workflow is the source of truth; the prompt points at it.
- **Forgetting the sub-workflow is a workflow.** It needs its own error registration (Lesson 17), its own tests, and its own name discipline. Tool is a role, not an excuse to skip engineering.

## Recap checklist

- [ ] I can name the tool kinds and pick the narrowest that does the job.
- [ ] I built a sub-workflow with an input contract and exposed it as an agent tool.
- [ ] I traced an agent's tool call into the sub-workflow's separate execution.
- [ ] I reviewed my tool catalogue as an auditor and can justify each entry in a sentence.

## Resources

- [n8n: Workflow Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/)
- [n8n: Execute Workflow node and trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
