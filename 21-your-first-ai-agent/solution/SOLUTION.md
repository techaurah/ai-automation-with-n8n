# Lesson 21: Solution notes

Correct sequences: price goes to the fact tool alone; total goes fact, then calculator with the fetched price (an agent that multiplies a remembered price is hallucinating with extra steps); the combined question uses fact twice and calculator once, in dependency order. The degraded description fails in the instructive direction: the model either ignores the tool or calls it for everything, because from the model's seat the description *is* the tool; there is no other specification to consult. That sentence is the one to write down.

**What to notice.** You tuned behaviour without touching a prompt paragraph about reasoning, only the tools' contracts. In agent systems, most "prompt engineering" that works is actually interface design, and n8n's canvas makes the interfaces visible, which is its quiet advantage over code-first frameworks for this class of system.
