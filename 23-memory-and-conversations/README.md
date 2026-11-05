# Lesson 23: Memory and conversations: what the agent remembers, where, and for how long

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 21 · **You need:** Your instance and the Lesson 21 agent.

Memory is what turns a clever answer machine into something that feels like a conversation, and it is also where AI workflows quietly accumulate risk: cost, confusion between customers, and state that evaporates in production topologies. This lesson teaches n8n's memory nodes with their real semantics: the window, the session key, the difference between Simple Memory for building and database chat memory for production, and the discipline of what should never be remembered at all.

## The window: memory as a sliding excerpt

The **Simple Memory** node (called Window Buffer Memory in earlier versions, and you will see both names in the wild) keeps the last N exchanges of a conversation and hands them to the model with each new message. The **context window length** is that N: at 5, the model sees the last five exchanges; at 20, it sees twenty, and pays for them, because the whole history rides along with every request, in tokens, latency, and failure surface. Memory is therefore a budget decision disguised as a feature toggle. The twin implements the exact semantics in fifteen lines: a per-session list, trimmed to the window, and the trimming is the point: the agent forgets the beginning of long conversations by design, and a well-built agent says so gracefully rather than hallucinating the forgotten middle.

What belongs in the window is the conversation itself. What does not: facts the agent should look up fresh (prices change; memory would serve stale ones, which is why Lesson 22 fetches prices through a tool instead of remembering them), and anything from another customer, which brings us to the key.

## The session key: whose memory is this?

Memory is partitioned by a **session key**. With the Chat Trigger, n8n supplies a session id per conversation, and memory nodes use it by default: each chat is its own partition, and patient B never sees patient A's history (the twin asserts this isolation explicitly, because it is the property your compliance reviewer will ask about). When you wire your own triggers (a webhook behind your website, a messaging app), supplying a stable, correct session key becomes your job: the conversation id from the platform, never the user's message content, never a guess. Key mistakes fail in both directions: too coarse (one global key) leaks context between customers; too fine (a new key per message) gives an agent with amnesia that re-asks everything. If you remember one operational rule from this lesson: **test memory with two interleaved conversations before anything ships**.

## Graduating: Postgres and Redis chat memory

Simple Memory stores history in the instance's memory. That is fine for building and a trap later: n8n's own documentation warns it does not work reliably in **queue mode**, where a follow-up message can be handled by a worker process that never saw the earlier ones. The production answer is a database-backed memory node with the same contract: **Postgres Chat Memory** or **Redis Chat Memory**, keyed by the same session id, durable across workers and restarts. The migration is a sub-node swap plus credentials, which is the AI map's modularity (Lesson 20) paying rent. Decide the graduation trigger in advance (the day the instance moves to queue mode, the day a second worker exists, the day memory must survive a restart) and write it in the workflow notes, so the swap happens as a plan rather than as an incident response.

## What to never store

Memory nodes happily store whatever the conversation contains, including things it should not: payment details a customer pasted, medical details beyond the booking's need, credentials someone was unwise enough to share. Course 1's rule transfers intact: design so the sensitive thing is never needed in the chat (payments happen on a payment page, clinical detail goes to the clinical system), keep windows short, and remember that stored conversations are data you now hold, with retention and access questions attached. The agent's system message should also refuse to treat remembered content as verified fact about identity: a chat that says "I am the account holder" is a claim, not a credential.

## Run it

Run the twin (`python3 memory_twin.py`) and read its assertions as the memory contract. Import `workflow.json`, publish, and run the two-conversation test against the real agent: in chat A, state a name and ask a price; in chat B (a fresh chat session), ask what your name is (it must not know); back in A, ask a follow-up that needs the history ("and for two of us?") and watch it use the window. Then set the window to 1 in a copy, repeat a longer A conversation, and watch the earliest facts fall out of the window exactly as the twin predicted.

## Common failures

- **One global session key.** Every customer shares one memory and the agent greets strangers with other people's details. Partition per conversation, verified by the two-chat test.
- **Window as a storage strategy.** Twenty exchanges of history on every call is a cost and latency decision made by accident. Size the window to the conversation's actual needs.
- **Simple Memory in queue mode.** It works in testing on one worker and fails intermittently in production. Graduate to database memory when the topology changes, on purpose, early.
- **Remembering what should be fetched.** Prices, hours, and stock belong in tools (fresh) not memory (stale). Memory is for the conversation, not the catalogue.

## Recap checklist

- [ ] I can explain window semantics and predict what an agent forgets at a given setting.
- [ ] My session keys partition conversations correctly, proven by an interleaved test.
- [ ] I know the graduation trigger from Simple Memory to database chat memory.
- [ ] I can list what my agent must never store, and where that data goes instead.

## Resources

- [n8n: memory nodes and chat memory](https://docs.n8n.io/advanced-ai/examples/agent-memory/)
- [n8n: Simple Memory node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
