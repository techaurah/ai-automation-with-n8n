# Lesson 03: Solution notes

The two-item version teaches the lesson inside the exercise: n8n nodes are item processors. The Edit Fields node added `clinic` and `status` to both items without being told about either; the final Code node received two items and, if your code used `$input.all()` or the run-once mode correctly, returned two greetings.

A clean channel-aware greeting branches on `d.channel`: form gets "we will confirm by email", Instagram gets "reply here and we will pick it up". If your second greeting came out identical to the first, your code probably read only `$input.first()`, the single most common Code node mistake in this course, and the reason Lesson 04 exists.

**What to notice.** You changed data at the source (the sample node) and every downstream node adapted, because the contract between nodes is the item shape. Keep the shapes honest and workflows compose; let them drift and nothing downstream can be trusted.
