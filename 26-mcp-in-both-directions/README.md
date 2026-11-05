# Lesson 26: MCP in both directions: your agent uses tools, your workflows become tools

**Time:** about 65 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 21, 22, and Course 1 Lesson 14 helps · **You need:** Your instance. An external MCP server is optional; the lesson's own server workflow can play that role.

The Model Context Protocol is the standard way AI applications discover and call tools, and n8n speaks it in both directions. As a client, an n8n agent can use any MCP server's tools through the MCP Client Tool. As a server, an n8n workflow can present itself as tools that Claude, Cursor, ChatGPT, or another agent can call, through the MCP Server Trigger. Confusing the two directions is the common beginner error; this lesson builds both, with the twin showing the plain JSON-RPC underneath so the magic has a floor.

## Direction one: the MCP Client Tool (your agent, their tools)

Add the **MCP Client Tool** sub-node to an agent, give it a server URL and its credentials, and the agent gains every tool that server exposes, discovered at runtime through the protocol's `tools/list`. The ecosystem is the point: servers exist for databases, documentation, developer tools, and n8n itself (the community n8n-mcp server, which exposes n8n's node documentation and, with instance credentials, workflow management, is the well-known example this course's research observed at over twenty thousand GitHub stars). Two cautions scale with that power. A connected server's tools join your catalogue instantly, so Lesson 22's catalogue review now includes someone else's code and intentions: vet servers as dependencies, prefer read-only scopes, and pin what the agent may call. And tool *descriptions* from a third-party server are instructions your model will read; Lesson 30's prompt-injection section treats hostile descriptions as a real attack surface, because they are.

## Direction two: the MCP Server Trigger (your workflows, their agents)

A workflow starting with the **MCP Server Trigger** publishes the nodes after it as MCP tools at its own endpoint. Workflow 26b exposes one tool, opening hours, in a dozen lines: the trigger defines the server, the following node is the tool's implementation, and its naming and description are the contract a calling agent sees. Published, this makes your clinic logic callable by any MCP client, which is a genuinely new distribution channel for the automations in this course: the Lead Machine's lookup, built in the capstone, could serve a website's separate AI assistant without either system knowing the other's internals. n8n additionally offers instance-level MCP access, letting authorised AI apps search, run, and even edit workflows inside your instance; powerful for your own AI-assisted building, and an access decision to make with Lesson 30 open on the desk, not a default to drift into.

Authentication is part of the design, not an afterthought: the trigger supports credential-based access, and an unauthenticated tools endpoint on the public internet is an invitation. Treat the server URL plus its credential like any API key from Lesson 13.

## The protocol under both, in one screen

The twin prints a complete `tools/list` and `tools/call` exchange: JSON-RPC requests with ids, a catalogue of tools with names, descriptions, and input schemas, and a call answered with content. Everything in this lesson is those two messages wearing n8n panels. Holding the protocol in your head pays off when something misbehaves: a client that cannot see a tool has a discovery problem (list), a call with wrong arguments has a schema problem (the description and inputSchema are the contract, Lesson 22's law at protocol scale), and a server that answers nonsense has an implementation problem in one node you own.

## Run it

Run the twin (`python3 mcp_twin.py`) and read the exchange aloud once; MCP stops being mystical at exactly that moment. Import `workflow-server.json`, publish it, and note its endpoint. Import `workflow-client.json`, point the MCP Client Tool at a server you trust (your own 26b endpoint, with its credential, is the cleanest first run), publish, and ask the agent for Saturday's hours through chat. In the execution, find the tool call; in your head, map it to the twin's second exchange. If the agent guesses hours instead of calling, its system message or the tool's description failed Lesson 22's test, and you know the fix.

## Common failures

- **Connecting an unvetted server because it was popular.** Stars are not a security review. A server's tools execute with your agent's authority and its descriptions steer your model; read what you connect.
- **Publishing a tools endpoint without access control.** Your workflow logic is now an API. Credential it like one, and keep write-shaped tools off public servers until Lesson 27's approvals are in the design.
- **Direction confusion.** Client tool: your agent calls out. Server trigger: the world calls in. Naming the direction in the workflow title (this lesson does) prevents the special misery of debugging the wrong end.
- **Instance-level MCP by default.** Letting external AI apps edit workflows in your production instance is a governance decision. Start with a learning instance, scoped credentials, and a reason.

## Recap checklist

- [ ] I can state both MCP directions and which node serves each.
- [ ] My agent called a tool through an MCP server and I mapped the call to the protocol.
- [ ] My own workflow is exposable as an MCP server, with access control considered.
- [ ] I vet external servers like dependencies, descriptions included.

## Resources

- [n8n: MCP Client Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp/)
- [n8n: MCP Server Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/)
- [Model Context Protocol specification](https://modelcontextprotocol.io/)
- [Agentic AI for Beginners, Lesson 14 (MCP)](https://github.com/techaurah/agentic-ai-for-beginners)
