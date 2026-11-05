# Glossary

Every term this course uses, in plain language. If a lesson uses a word that is not defined here or in the lesson itself, that is a lesson problem: please open an issue.

**AI Agent node**: The n8n root node that runs an agent loop: a chat model decides, tools act, results return, until the model answers. Always a Tools Agent in current n8n, and it requires at least one tool connected.

**Binary data**: The file channel of an item, beside its JSON: named slots holding file content and metadata (name, MIME type, size). Files never travel inside the JSON fields.

**Chain**: A fixed AI pipeline, one prompt in and one answer out, with no tool decisions. The Basic LLM Chain is the course's first AI node (Lesson 20).

**Chat model**: A sub-node that connects a language model (hosted, or local through Ollama) to a chain or agent.

**Chunking**: Splitting documents into right-sized pieces before embedding, so retrieval can return the relevant piece. Overlap keeps sentences whole across cuts (Lesson 25).

**Credential**: A named, encrypted connection stored by n8n and referenced by nodes: the only place secrets may live. Workflow exports carry references, never values (Lesson 13).

**Data Table**: Built-in tabular storage inside an n8n instance (from 1.113.1): defined columns, persistent rows, worked through the Data Table node (Lesson 12).

**Dedupe key**: A stable identifier computed from an event's normalised identity fields, checked against a register before any side effect, so replays do not repeat effects (Lessons 16 and 19).

**Draft and Publish**: The n8n 2.x model: saving edits a draft; publishing makes that version live for triggers. Replaced the 1.x Active toggle (Lesson 28).

**Embedding**: A list of numbers representing a text's meaning, produced by an embeddings model. Similar meanings get similar vectors, which is what vector retrieval searches (Lesson 25).

**Error workflow**: A workflow starting with an Error Trigger, registered in other workflows' settings, that receives failure details and turns them into an actionable alert (Lesson 17).

**Execution**: One run of a workflow, recorded with the real data at every node. The primary debugging artefact (Lesson 18).

**Expression**: A small piece of JavaScript inside {{ }} in a field, pulling values from the current item ($json), earlier nodes, or n8n itself ($now, $execution). Lesson 05.

**Guardrails**: Automated checks on text entering or leaving an AI step: PII patterns, URLs, secrets, topics. In n8n, a dedicated node; in design, a boundary discipline (Lesson 27).

**Human-in-the-loop**: A design where a person approves, edits, or rejects a proposed action before it happens. In n8n: send-and-wait operations and tool-call review (Lessons 15 and 27).

**Idempotency**: The property that processing the same event repeatedly has the same effect as processing it once, built from keys, registers, and ordering (Lesson 19).

**Item**: One JSON object in the list that flows between nodes. The only data shape workflows move (Lesson 04).

**MCP (Model Context Protocol)**: The open standard by which AI apps discover and call tools, and by which tools are exposed to AI apps. JSON-RPC underneath (Lesson 26).

**MCP Client Tool**: The n8n sub-node that gives an agent the tools of an external MCP server, discovered at runtime.

**MCP Server Trigger**: The n8n trigger that publishes a workflow's nodes as MCP tools other AI apps can call.

**Memory (chat)**: The conversation history an agent is given with each message. Simple Memory keeps a window in the instance; Postgres and Redis chat memory persist it (Lesson 23).

**Node**: One job on the canvas: a trigger, a transform, an action, or an AI root or sub-node. Named by what it does, never by its type, in this course.

**Output parser**: A sub-node that constrains a model's reply to a schema, returning fields a workflow can route on (Lesson 24).

**Paired item**: n8n's bookkeeping linking an output item to the input item it came from, so expressions can reach back to earlier nodes for the same record. Breaks at nodes that discard their input (Lesson 04).

**Queue mode**: The scaled n8n topology: a main instance coordinating worker processes (with Redis), needed when one instance's execution load saturates. Changes memory and binary behaviour (Lessons 23 and 29).

**RAG (Retrieval-Augmented Generation)**: Answering from retrieved document chunks placed in the model's context, with sources, instead of from the model's training alone (Lesson 25).

**Session key**: The identifier partitioning one conversation's memory from every other. With a Chat Trigger it is the session id; with your own triggers, supplying it correctly is your job (Lesson 23).

**Structured output**: Model output constrained to a defined schema, usually JSON, so programs can consume it directly instead of parsing prose (Lesson 24).

**Sub-node**: A node that connects underneath a root node to supply a capability: a chat model, a tool, memory, an output parser, an embeddings model (Lesson 20).

**Sub-workflow**: A workflow called by another workflow (Execute Workflow node or trigger), or by an agent (Workflow Tool). The platform's reuse unit (Lesson 22).

**Task runner**: The isolated process n8n 2.x runs Code node code in by default, so a bad script cannot take the instance down, and environment access stays blocked (Lessons 07 and 30).

**Text Classifier**: The n8n root node that sorts text into described categories, each with its own output, backed by a model sub-node (Lesson 24).

**Trigger**: The node that starts a workflow: manual, schedule, webhook, form, chat, and others. Every trigger's data gets normalised into one house shape (Lesson 06).

**Vector store**: A store of embeddings that retrieves the chunks most similar to a question's embedding. In-memory for learning; persistent stores for production (Lesson 25).

**Webhook**: A trigger that gives a workflow a URL other systems can call, delivering the request's body, headers, and query as the first item (Lesson 06).

**Workflow**: A designed path of nodes that runs when its trigger fires: predictable, testable, and the right shape for most automation (Lesson 01).

**Workflow Tool**: The sub-node that exposes an entire n8n workflow as one of an agent's tools, with a name and description the model chooses from (Lesson 22).
