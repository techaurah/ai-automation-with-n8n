# Lesson 30: Exercise

## Red-team your own intake

1. Take the Lesson 19 idempotent webhook (or the capstone intake if you have started it). List every way an unauthenticated stranger could abuse it: volume, malformed payloads, replayed deliveries, payloads carrying instructions aimed at a downstream agent.
2. For each abuse, name the control that answers it and where it lives (trigger auth, shape check, key and register, guardrail, approval). Any abuse with no control gets one added, or a written risk acceptance.
3. Add one abuse you invent that this lesson did not mention, with its control.
4. Run both scanners (Lessons 13 and 30) over the final design's files and attach the clean outputs.

You are done when the abuse table has no empty control cells and the invented abuse is genuinely new.

## Solution

See `solution/SOLUTION.md` in this folder.
