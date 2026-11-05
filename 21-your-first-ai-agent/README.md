# Lesson 21: Your first AI agent: model, tools, memory, and honest limits

**Time:** about 70 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 20 · **You need:** Your instance, plus Ollama with the named model (or a hosted chat model credential for the swap).

The AI Agent node is the centre of n8n's AI story: a root node that runs the perceive, decide, act, observe loop from Course 1, with its capabilities supplied by sub-nodes you wire underneath. This lesson builds a small front-desk agent for BrightSmile: a chat trigger, a model, one real tool, and simple memory. It also teaches the current product facts that older tutorials get wrong, because the node changed under them.

## Anatomy: one root, three kinds of sub-node

Under the agent sit three connector types. The **chat model** is required (no model, no reasoning). **Tools** are what the agent can do in the world; since n8n 1.82 the agent is always a **Tools Agent** (the old agent-type selector is gone), and current versions **require at least one tool connected** before the agent will run, which is why this lesson's Calculator is structural, not decorative: an agent-shaped job with no tools is a chain's job, and the Basic LLM Chain from Lesson 20 is the right node for it. **Memory** is optional and Lesson 23's whole subject; the Simple Memory wired here holds the recent conversation so follow-up questions work.

The **Chat Trigger** ("when chat message received") opens the workflow: it provides a test chat panel in the editor and, once published, a hosted chat page or embeddable widget, keyed by a session id that the memory node uses to keep conversations separate. Swapping the trigger for a Webhook later moves the same agent behind your own interface without touching the agent itself, Lesson 06's door pattern at the AI layer.

## The loop, watched once with your eyes open

Send the agent "What is the total cost of 2 whitening sessions?" and open the execution. You will see the loop turn: the model reads the question, decides the calculator is needed (because the system message forbids mental arithmetic, a rule worth stealing), the tool runs `299 * 2`, the result returns to the model, and the model phrases the answer. The twin performs the identical loop in Python with a rule-based fake decider, printing each tool call, so the mechanics are demystified before you trust the model's version of them.

The agent settings that matter from day one: the **system message** (role, tools discipline, scope limits, tone, in that order), the **maximum iterations** (the loop's budget; an agent that cannot finish in its budget should say so, like the twin's five-step guard), and the model choice itself, because tool-calling reliability varies enormously between models and is the first thing to suspect when an agent misbehaves.

## Honest limits, stated while you still control the demo

This agent is a front desk, not a clinician, and its system message says so by scope: bookings, prices, hours, and deferral for everything else. Three limits to internalise now. The agent **invents** when its tools and facts run out unless the prompt and the design forbid it (Lesson 20's grounding discipline applies doubly when the model also acts). Tool calls are **side effects**: a booking tool books, so Lesson 27's approvals exist. And the agent is only as good as its **worst tool description**: models choose tools from their names and descriptions, so write those like API documentation for a smart stranger, because that is literally the reader.

## Run it

Run the twin (`python3 agent_twin.py`) and watch the two tool calls print. Import `workflow.json`, ensure the model sub-node matches a model you actually have (pull the Ollama model or swap sub-nodes per the sticky note), publish, and open the chat. Ask the price question, the two-session total, and an out-of-scope question (diagnose a symptom). Open the executions and identify the loop turns for the total question. The out-of-scope question should produce a deferral; if it produces medical advice, your system message needs the scope sentence strengthened before anything else is built on this agent.

## Common failures

- **No tool connected.** Current agents refuse to run tool-less. If you truly need no tools, you needed the Basic LLM Chain; the product is telling you something true about your design.
- **Maths in the model's head.** Language models are unreliable calculators. Any arithmetic that matters goes through the Calculator tool or a Code node, enforced in the system message.
- **Tool descriptions written for humans in a hurry.** The model picks tools by description. "Gets stuff" loses to a one-line contract saying what the tool returns and when to use it.
- **Scope creep by politeness.** An agent that tries to answer everything becomes a liability with a friendly tone. Deferral is a feature; test it like one (the third question in Run it exists for this).

## Recap checklist

- [ ] I can wire an agent's model, tool, and memory sub-nodes and name each connector type.
- [ ] I traced one full loop turn in an execution: decide, tool, observe, answer.
- [ ] My agent defers out-of-scope questions instead of improvising.
- [ ] I know the system message's four jobs: role, tool discipline, scope, tone.

## Resources

- [n8n: AI Agent node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)
- [n8n: Chat Trigger node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chattrigger/)
- [Agentic AI for Beginners, Course 1 (the agent loop, Lesson 09)](https://github.com/techaurah/agentic-ai-for-beginners)
- [n8n documentation home](https://docs.n8n.io/)
