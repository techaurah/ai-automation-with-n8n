# Lesson 19: Exercise

## Break it, then fix the ordering

1. In the twin, move the register write to after the outbox append, and simulate a crash between them (raise between the two steps on the first delivery, then deliver again). Show the duplicate email that results.
2. Restore the safe ordering, this time with a `processing` status written before the act and `created` after. Replay the crash scenario and show the second delivery now finds the processing row. Decide and document what a human should do with a row stuck in `processing`.
3. Write the one-paragraph rerun policy for the Lesson 16 intake as if for a team handbook.

You are done when the broken version demonstrably duplicates, the fixed version demonstrably does not, and the stuck-row policy is written.

## Solution

See `solution/SOLUTION.md` in this folder.
