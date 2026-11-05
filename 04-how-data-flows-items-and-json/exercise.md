# Lesson 04: Exercise

## Add a fourth, uglier item

1. Add a fourth raw enquiry to both the twin and the workflow: a walk-in patient with no channel field at all, name in all caps, and an empty message.
2. Update the cleaning step in both so a missing channel becomes `"unknown"` and an empty message gets word_count 0 instead of breaking anything.
3. Rerun both. The summaries should agree exactly: 4 items, channels email, instagram, unknown, website form.
4. In one sentence in your notes: which version (twin or workflow) made the missing-field case easier to handle, and why.

You are done when both summaries match and neither version errors on the ugly item.

## Solution

See `solution/SOLUTION.md` in this folder.
