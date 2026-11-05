# Lesson 12: Data Tables and state that lasts: memory between executions

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 04, 06 · **You need:** Your instance (Data Tables exist from n8n 1.113.1, Cloud and self-hosted). Python for the twin.

Everything so far forgot everything between runs. Real automations remember: which leads arrived, who was already contacted, what is stale. This lesson teaches n8n's built-in answer, Data Tables: persistent, structured storage inside the instance, managed from the home screen and worked through the Data Table node. It also maps the alternatives honestly, because choosing where state lives is an architecture decision you will make in every serious project.

## What a Data Table is

A **Data Table** is a table you define in the n8n UI (from the Data Tables area of the home screen): named columns with types, and rows. Every table automatically carries system columns, `id`, `createdAt`, and `updatedAt`, which you do not declare. Tables persist across executions and are shared by the workflows in the instance, and the **Data Table node** (`n8n-nodes-base.dataTable`) works them from inside workflows: insert rows, get rows with column filters and sorting, update, upsert, and delete, plus table-level operations like creating a table from a workflow.

The mental model that keeps you out of trouble: a Data Table is a small, honest database with a deliberately small feature set. It has filters and sorts, not joins and transactions. The sources this course checked put a 50 MB size figure on Cloud tables (configurable when self-hosting), which frames the scale correctly: thousands of leads, lookup lists, dedup registers, and workflow state fit comfortably; a product catalogue or an analytics store does not, and belongs in a real database (Lesson 14).

## The insert, get, update rhythm

This lesson's workflow inserts three sample leads. The node ships with a placeholder table reference on purpose: you create the `Leads` table (text columns name, email, status, updated) and select it in the node, because table ids are instance-specific and a course that hardcodes one teaches a lie. Inside the node, column values are expressions mapped from the item, the Edit Fields skill in a new uniform; a Set node before it is redundant for the same reason.

Reading back is where state earns its keep: **Get rows** with a filter (status equals new, updated before a date) is the follow-up chaser's opening move in the capstone. Two settings matter: sorting (oldest first for chase lists), and **Always Output Data** on the node, because a get that matches nothing otherwise stops the flow, and "no stale leads today" is a normal morning, not an error. Updating by a stable key (the lead's email, or the row id returned at insert) closes the rhythm; upsert (insert or update on a key) is Lesson 19's idempotency workhorse.

## The alternatives, honestly compared

Four other homes for state, each with a real use. **Workflow static data** (`$getWorkflowStaticData()` in a Code node) holds a small key-value handful inside one workflow: a counter, a last-seen id. It is per-workflow, invisible in any UI, and wrong for anything a colleague must inspect. **Spreadsheets** (Lesson 14) are state humans can read and edit, at the cost of API quotas and loose typing. **A real database** (Postgres and friends) is the production answer at scale, with n8n nodes to match. **External services** (a CRM) are state owned by another system of record, which your workflow should treat as authoritative rather than mirroring casually.

The twin models Data Table semantics with SQLite, Python's built-in database, using real SQL for the same insert, filter, and update the node performs. The comparison is the lesson: the node is a friendly face on the same operations, and knowing the operations is what transfers when you outgrow the friendly face.

## Run it

Run the twin (`python3 data_table_twin.py`): it inserts three leads, finds Tom stale, and books Ayesha. In n8n, create the Leads table as the sticky note in `workflow.json` describes, import the workflow, select your table in the Data Table node, and run. Open the table in the UI: three rows, with system columns the node filled in. Run it again and look carefully: you now have six rows. That duplication is not a bug in your clicking; it is the absence of a uniqueness rule, and it is exactly what Lesson 19 exists to fix.

## Common failures

- **Expecting uniqueness that is not configured.** Data Tables do not dedupe by email because you feel they should. Insert twice, store twice, until you design the key discipline (Lesson 19).
- **Treating the table like a spreadsheet.** No formulas, no casual human edits mid-automation without consequences, and sorts and filters are query choices, not view decorations.
- **State split across two homes.** Leads in a Data Table and statuses in a sheet will disagree by Friday. One home per fact, named in the workflow's notes.
- **The empty-get dead end.** A filtered get with no matches halting the workflow reads as a failure in the executions list. Always Output Data, plus a branch that treats empty as a fine outcome.

## Recap checklist

- [ ] I can create a Data Table and drive insert, filtered get, and update from a workflow.
- [ ] I can name what Data Tables are not for, with the scale that decides it.
- [ ] I compared the node's operations with the twin's SQL and can translate between them.
- [ ] I watched duplicate inserts happen and can explain the missing discipline.

## Resources

- [n8n: Data Tables documentation](https://docs.n8n.io/data/data-tables/)
- [n8n: Data Table node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
