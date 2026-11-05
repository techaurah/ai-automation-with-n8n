# Lesson 20: AI in n8n: the map (LangChain nodes, models, local vs hosted)

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Module 4, and Course 1 Lessons 03 to 05 help but are not required · **You need:** Your instance. Optional: Ollama installed locally with a small model pulled, for the live chain. The twin needs nothing.

n8n's AI layer is built on LangChain, the agent framework, expressed as nodes: instead of writing LangChain code, you wire LangChain concepts. This lesson is the map for the whole module: the four families of AI nodes (models, chains, agents, and the sub-nodes that feed them), the local-versus-hosted model decision, and your first working chain. Every later AI lesson is a zoom into one part of this map.

## The map: roots and sub-nodes

AI workflows have **root nodes**, which sit in the main flow and do the visible work, and **sub-nodes**, which connect underneath a root and give it capabilities. The roots you will use: the **Basic LLM Chain** (one prompt in, one answer out, no tools), the **AI Agent** (a model that can decide to call tools, Lesson 21), and specialised chains like the **Text Classifier** (Lesson 24) and question-answering chains (Lesson 25). The sub-nodes: **chat models** (OpenAI, Anthropic, Google Gemini, AWS Bedrock, Ollama for local models, and more), **embeddings models**, **memory** (Lesson 23), **tools** (Lesson 22), **output parsers** (Lesson 24), **document loaders and text splitters** (Lesson 25), and **vector stores**. On the canvas, sub-nodes plug into labelled connectors under their root (model, memory, tool), and the connection types in workflow JSON (`ai_languageModel`, `ai_tool`, and friends) say which is which.

Why this architecture matters: swapping a model means rewiring one sub-node, not rebuilding the workflow, and the same tool sub-node can serve a chain today and an agent tomorrow. The map is the modularity. When a tutorial predates this structure (hand-built HTTP calls to a model API, prompt strings in Code nodes), it is teaching the pre-LangChain workaround; the concepts still transfer, the wiring does not.

## Local vs hosted models: the honest trade

A **hosted** model (OpenAI, Anthropic, Gemini and peers, via their chat model nodes) gives you the strongest models with zero operations, billed per use, with your prompts leaving your infrastructure. A **local** model through the **Ollama** chat model node runs on your machine or server: free per call, private by construction, weaker at the small sizes most hardware can run, and yours to keep running. The self-hosted AI starter kit n8n publishes (n8n plus Ollama plus a vector store in Docker) exists because this combination is so common.

This course's AI module runs on Ollama by default so every lesson is zero-credential, and names the hosted swap wherever it matters (usually one sub-node and a credential). Choose per step, not per company: a classifier chewing thousands of tickets may belong on a small local model, while the customer-facing drafting step earns the hosted one. Course 1 Lesson 30's cost and latency engineering is the deeper version of this judgement.

## Your first chain, and the contract idea

The Basic LLM Chain takes a prompt (a system message setting role and rules, plus the incoming text), sends it to its model sub-node, and outputs the reply. This lesson's chain answers BrightSmile questions from a facts block baked into the system message, the smallest possible grounding: the model is told to use only those facts and to defer otherwise. The twin rebuilds the identical chain in Python with a simulated model, which isolates the parts that are *yours*: the **template** (what the model is told) and the **contract** (what shape of answer the rest of the system may assume). Models change quarterly; templates and contracts are the durable engineering, in n8n exactly as in Course 1.

## Run it

Run the twin (`python3 llm_chain_twin.py`): the whitening question is answered from the facts, the payment-plan question defers, and both honour the contract. Then import `workflow.json`. With Ollama running and the named model pulled, execute and compare the chain's real answer with the twin's simulated one; without Ollama, read the chain node's panel carefully, especially how the system message and the incoming text combine into the prompt, because that panel is where you will debug every AI workflow in this module.

## Common failures

- **Learning AI from pre-LangChain tutorials.** HTTP nodes hand-calling model APIs, JSON surgery in Code nodes: the 2023 workaround. If a guide's agent has no sub-nodes, it is archaeology, interesting and obsolete.
- **One model for every step, chosen by habit.** Classification, drafting, and extraction have different price and quality curves. The map exists so each step can pick its own sub-node.
- **No contract, just vibes.** A chain whose output shape is "whatever the model felt like" cannot feed a router. Contracts start in this lesson: small, explicit, checked.
- **Prompt text as a dumping ground.** Facts, rules, format, and tone all crammed into one paragraph age terribly. Structure the system message (role, facts, rules, fallback) from your first chain onward.

## Recap checklist

- [ ] I can draw the AI map: roots, sub-nodes, and the connector types between them.
- [ ] I ran a chain pattern in the twin and can explain template versus contract.
- [ ] I can state the local versus hosted trade and where this course defaults.
- [ ] I know what a pre-LangChain tutorial looks like and why to retire it.

## Resources

- [n8n: advanced AI documentation](https://docs.n8n.io/advanced-ai/)
- [n8n: self-hosted AI starter kit](https://github.com/n8n-io/self-hosted-ai-starter-kit)
- [Ollama, the local model runner](https://ollama.com/)
- [n8n documentation home](https://docs.n8n.io/)
