# Lesson 12: Exercise

## Build the stale-lead finder

1. Add a second workflow: a Schedule Trigger (daily), a Data Table Get on Leads filtering `updated` earlier than a date you choose, sorted oldest first, with Always Output Data on.
2. Add a Code node that formats the result as one digest item (count plus names), including the zero case ("no stale leads today" as a real output, not silence).
3. Seed the table with two more leads at different dates so the filter has something interesting to do, and run both workflows.
4. Mirror the finder in the twin against your seeded data.

You are done when the digest matches the twin's stale list exactly, and a second run with a future cutoff date produces the zero-case message.

## Solution

See `solution/SOLUTION.md` in this folder.
