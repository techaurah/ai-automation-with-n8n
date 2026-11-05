# Lesson 14: Exercise

## Own the conflict

1. Extend the twin with a third lead present only in the database, and a fourth present in the sheet with an older timestamp than the database copy. Rerun and verify the printed decisions handle both correctly.
2. Change the tie rule: ties now go to the sheet. Rerun the original data and identify exactly which final states change, and write one sentence on which system should win ties in a real lead pipeline and why.
3. Add a deleted flag scenario: the database copy of a lead has status `do_not_contact` with an old timestamp, and the sheet copy says `new` with a newer one. Does your rule resurrect the lead? Change the rule so it cannot, and prove it.

You are done when all three scenarios print defensible decisions and the do-not-contact case is provably safe.

## Solution

See `solution/SOLUTION.md` in this folder.
