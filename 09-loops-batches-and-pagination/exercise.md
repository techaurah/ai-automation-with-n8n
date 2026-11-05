# Lesson 09: Exercise

## Harvest with a hole in the middle

1. In the twin, delete page 2's records 14 and 15 (simulate an API that silently drops two records) and rerun. The assertion fails, as it should.
2. Improve the twin's harvester to detect the hole: it should report exactly which record ids are missing, not just fail. (Hint: contiguity is checkable when ids are sequential; when they are not, a count check against the API's reported total is the fallback. Use whichever yours supports and say which.)
3. Apply the same thinking to the workflow: add a node on the done path that reports the total fetched and the number of pages.

You are done when the twin names the missing records precisely and the workflow reports its own harvest totals.

## Solution

See `solution/SOLUTION.md` in this folder.
