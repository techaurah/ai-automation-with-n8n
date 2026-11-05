# Lesson 06: Exercise

## Add a fourth door

1. Pick a fourth entry point: an email-style payload simulated by a Manual Trigger plus a Code node that emits `{ subject, from, text }` shaped like a parsed email.
2. Write its normaliser so the output matches the house shape from this lesson exactly: same field names, same kinds.
3. Prove it: feed all four doors the same enquiry content and show the four normalised records are structurally identical (same keys, same types).
4. In your notes: one sentence on what breaks downstream if a door skips normalising.

You are done when the four records could be merged into one list and no downstream node could tell them apart.

## Solution

See `solution/SOLUTION.md` in this folder.
