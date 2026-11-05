# Lesson 29: Exercise

## The restore rehearsal, now, while it is cheap

1. Stand up a second, scratch stack from the same compose file on a different port.
2. Restore your backup into it: database from the dump, data volume from the archive, `.env` with the *same* encryption key.
3. Log in and prove the three survivals: workflows present, a credential still functional (run a workflow that uses one), execution history visible.
4. Time it, and write the restore runbook from what you actually did, including every step the backup script did not tell you.

You are done when the scratch instance runs a credentialed workflow from restored data and the runbook exists.

## Solution

See `solution/SOLUTION.md` in this folder.
