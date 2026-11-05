# Lesson 13: Exercise

## Plant a leak, catch a leak

1. Copy any earlier lesson workflow into this folder of your fork as `workflow-planted.json`, and deliberately plant a fake token (use the shape `sk-` followed by twenty characters) in a Code node string.
2. Run the scanner. Confirm it catches the plant, and note which check fired.
3. Remove the plant by moving the value into a credential and re-exporting, then rescan to zero.
4. In your notes: why does step 3's workflow remain safe to commit while the planted one would not have been, even after deleting the token from the file?

You are done when the scanner's before and after outputs are both in your notes, with the git-history sentence answered correctly.

## Solution

See `solution/SOLUTION.md` in this folder.
