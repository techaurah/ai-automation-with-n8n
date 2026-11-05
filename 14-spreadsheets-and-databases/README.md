# Lesson 14: Spreadsheets and databases: the two places rows want to live

**Time:** about 65 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 12, 13 · **You need:** A Google account for the Sheets node (free), or read along and use the twin. Python for the twin.

Ask a room of operators where their business data lives and half will say a spreadsheet. This lesson treats that honestly: sheets are a legitimate automation surface with real strengths, databases are the step up when the sheet starts bending, and syncing the two is a design problem with a decision rule, not a copy-paste. You will append to a sheet from a workflow, model a two-way sync in the twin, and learn the matching discipline that keeps syncs from duplicating or resurrecting rows.

## The Google Sheets node, used properly

The Sheets node reads ranges as items, appends rows, updates rows it can match, and clears or creates sheets. Three working habits separate reliable sheet automation from the usual mess. First, **the first row is a contract**: column names are how the node maps values, so renaming a column in the sheet is a breaking change to every workflow that touches it, and the sheet's owner may not know workflows exist. Second, **append is not upsert**: appending the same lead twice gives two rows (Lesson 12's duplication, wearing a Google uniform); the node's update operation needs a matching column and a value to match on, which is a design decision you make before the data arrives. Third, **quotas are real**: Google enforces read and write quotas per minute, and a chatty loop over a big sheet finds them; batch reads, and let Lesson 09's politeness rules apply.

This lesson's workflow appends one lead with a placeholder document reference: connect a Google credential (OAuth, Lesson 13), pick a practice sheet, and run it. The placeholder is deliberate again: document ids are yours, and a course repo that shipped a live one would be teaching on someone else's sheet.

## When the database earns its place

The Postgres node (and its MySQL, and hosted cousins like Supabase and Airtable in the next lesson) offers what sheets cannot: types that are enforced, uniqueness that is guaranteed (an email primary key ends the duplicate conversation at the storage layer), transactions, and queries with joins. The crossover signs are practical, not snobbish: multiple workflows writing the same rows, any need for "this email exists exactly once", reporting that joins two tables, or volume where sheet latency and quotas bite daily. Data Tables (Lesson 12) sit between the two: structured and inside n8n, deliberately lighter than a database. Choosing among sheet, Data Table, and database per dataset, and writing the choice down, is a Lesson 32 capstone decision.

## Sync: a decision rule, not a direction

Two-way sync fails in the imagination first: people picture copying, but sync is **deciding**, per row, which side is right. The twin implements the course's default rule in the open: match rows by a stable key (email); the side with the newer `updated` timestamp wins; ties go to the designated system of record (here, the database); every decision prints, so the rule is auditable rather than vibes. Rows only on one side are inserts, not conflicts.

The rule's honesty matters more than its details: your projects may choose last-writer-wins, or record-level ownership (the CRM owns status, the sheet owns notes), but they must choose, in writing, before the first sync runs. The failure mode the rule prevents is resurrection: a lead deleted or booked on one side reappearing from the other's stale copy, which in a lead business means a human calls someone who already bought, or already said no.

## Run it

Run the twin (`python3 sheet_sync.py`) and read its three decisions line by line: Ayesha's sheet row is newer and updates the database; Tom's database row is newer and the sheet row is skipped; the final state matches the assertion. Then run the workflow append against your practice sheet and confirm the row lands under the right columns. Change one column's name in the sheet and run again to see the mapping failure with your own eyes; fix the name, and note how a rename in a friendly UI became a production incident in miniature.

## Common failures

- **Append where upsert was needed.** Duplicates accumulate silently until a human notices two rows for one customer. Decide the matching key when you design the sheet, not after the third duplicate.
- **The renamed column.** Sheets invite casual edits that are schema changes to your workflows. Protect header rows, and treat renames as deployments.
- **Sync without a written rule.** First conflict resolves by whichever code path runs, and every later conflict inherits the accident. Write the rule; print the decisions.
- **Reading a whole sheet per item.** A loop that fetches the sheet inside its body multiplies quota burn by row count. Fetch once, work in memory, write in batches.

## Recap checklist

- [ ] I appended a row via the Sheets node and can explain its mapping contract.
- [ ] I can state the crossover signs for moving a dataset to a database.
- [ ] My sync rule is written down, and the twin's printed decisions follow it.
- [ ] I know why a renamed column is a breaking change and how to blunt it.

## Resources

- [n8n: Google Sheets node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/)
- [n8n: Postgres node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
