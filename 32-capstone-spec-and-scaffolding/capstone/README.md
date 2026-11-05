# Capstone: the Lead Machine

The spec lives in Lessons 32 to 34 of the course. This folder is the
project scaffold: the data model, the acceptance tests the finished
system must pass, and the workflow skeletons Lesson 33 completes.

## What the Lead Machine does

For BrightSmile Dental, a fictional clinic:

1. **Intake.** Enquiries arrive by form and webhook, are normalised
   at the door, classified, keyed, and stored exactly once.
2. **Qualification.** New leads are scored on a written rubric, and
   a reply is drafted for human approval.
3. **Follow-up.** Leads that go quiet are chased on a schedule, a
   bounded number of times, with every chase recorded.
4. **Digest.** A daily summary of new, stale, and booked leads goes
   to the owner on the low rung of the notification ladder.

## Non-negotiables (from the course's modules)

- Error workflow registered on every workflow (Lesson 17)
- Idempotency key checked before any side effect (Lesson 19)
- Secrets only in credentials; both scanners clean (Lessons 13, 30)
- Approvals before customer-facing sends, until evidence graduates
  them (Lesson 27)
- Draft, publish, rollback: the Lesson 28 routine, executed in
  Lesson 34

## Files

- `DATA_MODEL.md`: the tables and fields, with the key contract
- `workflows/`: skeleton exports Lesson 33 builds out
- `tests/smoke_test.py`: validates every workflow file in this
  folder (parses, unique node names, sound connections)
