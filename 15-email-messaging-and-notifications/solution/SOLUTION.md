# Lesson 15: Solution notes

The gate changes the ladder's meaning: critical no longer means "shout immediately" but "prepare the shout and get a human on it fast", which is why the approval message itself carries the full context (what failed, which records, the execution link) for a one-tap decision. On rejection the workflow should record the rejection as an outcome, not treat it as an error; a human saying no is data. The twin's pending list makes the same state machine visible: an item exists in `pending`, in `outbox`, or nowhere, and confusing those states is how approvals get lost in real systems too.

**What to notice.** You added latency on purpose and the system got better. Automation maturity is mostly knowing where the pauses belong.
