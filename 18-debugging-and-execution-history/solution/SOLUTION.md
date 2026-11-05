# Lesson 18: Solution notes

The fixed workflow lives in `solution/workflow.json`: the mapper reads `body.enquiry`, and the reply names Tom Lee and his whitening question. Compare it with the broken version and the diff is three field paths, which is the point: the bug was never effort, it was epistemology, believing the payload's shape instead of reading it.

The shape check that belongs at this boundary asserts name, email, and message are non-empty strings after mapping, and throws with the offending item printed when they are not. With it in place, the planted bug class becomes a failed execution with a precise message, Lesson 17's alert fires, and the incident is five minutes instead of a wrong email to a customer named undefined.

**What to notice.** Your debugging time was almost all reading, in the execution, one node at a time. That ratio is not a beginner's shame; it is the professional method, and it stays the method at every scale.
