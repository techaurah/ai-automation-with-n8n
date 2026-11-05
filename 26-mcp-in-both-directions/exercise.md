# Lesson 26: Exercise

## Expose the price lookup, carefully

1. Rebuild Lesson 22's price lookup behind an MCP Server Trigger in a new workflow, with a tool description written to Lesson 22's standard.
2. Point the 26a agent at it and re-run the price questions from Lesson 22. Compare the executions: same tool contract, new transport.
3. Write the access note for this server: who may call it, with what credential, what it must never expose (anything write-shaped, anything patient-shaped), and where that is enforced.
4. Deliberately call the server with a malformed argument from the twin (weekday as a number) and observe both ends' behaviour.

You are done when the price questions pass over MCP and the access note would satisfy Lesson 13's audit.

## Solution

See `solution/SOLUTION.md` in this folder.
