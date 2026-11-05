# The Lead Machine: lead handling for BrightSmile Dental

An n8n system built as the capstone of TechAurah's free course
AI Automation with n8n. It takes enquiries from a form (and a
webhook door), classifies and scores them on a written rubric,
stores each lead exactly once in a Data Table, drafts follow-ups
for human approval, chases quiet leads a bounded number of times,
and sends the owner a daily digest.

## Workflows

| File | Job |
|------|-----|
| workflow-intake.json | Form in, normalise, key, classify, score, store |
| workflow-followup.json | Daily: find due leads, draft the chase |
| workflow-digest.json | Daily: new and hot leads, summarised for the owner |

## Running it

1. Self-host n8n (the course's Lesson 29 stack) or use n8n Cloud.
2. Create the leads Data Table from the data model in the course's
   Lesson 32 folder, and select it in each workflow's Data Table
   nodes.
3. Connect a Gmail credential for drafts; register the course's
   error workflow on all three workflows.
4. Publish in order: intake, digest, chaser.

## Guarantees this system was built to

- Duplicate deliveries create one record and one side effect.
- Complaints reach a human unrouted by the scoring rubric.
- A lead marked closed is never chased again.
- Every customer-facing send is a draft until a human approves it,
  or evidence graduates it under the course's Lesson 27 rules.

## Tests

`python3 lead_machine_twin.py` runs the business rules offline.
`python3 smoke_test.py` validates the workflow files structurally.
