# Lesson 15: Exercise

## Add the approval rung

1. Insert a send-and-wait approval (Gmail or Slack, your pick) on the critical path, before the team chat post: the chat message should only post after a human approves the wording.
2. Test both outcomes: approve once, reject once, and capture what the execution shows in each case.
3. In the twin, model the same gate: critical messages wait in a `pending` list until a function `approve(index)` moves them to the outbox.
4. One sentence in your notes: which real message in your working life should have had this gate and did not?

You are done when both approval outcomes are demonstrated and the twin's pending list behaves identically.

## Solution

See `solution/SOLUTION.md` in this folder.
