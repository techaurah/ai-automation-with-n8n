# Lesson 19: Idempotency, deduplication, and safe reruns: doing it exactly once, eventually honestly

**Time:** about 65 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 12, 16, 17 · **You need:** Your instance. Python for the twin.

Distributed systems deliver at least once: webhooks retry, users double-click, providers resend, and you will rerun failed workflows by hand at the worst moments. A system that performs its side effect per delivery sends two welcome emails, creates two CRM records, and books two appointments. **Idempotency** is the design property that saves you: processing the same event three times has the same effect as processing it once. This lesson builds it properly, with the key, the register, and the ordering that makes it hold.

## Keys: what makes two deliveries the same event?

Idempotency starts with identity. Prefer a **provider-supplied id** when one exists (a message id, a payment intent id, a form submission id): the sender has already decided what counts as the same event. When none exists, compute a **dedupe key** over the event's stable content, as Lesson 16 did for leads (normalised email plus the message id here), and write the key contract down. Beware keys over unstable content: include a timestamp or a retry-varying field and every retry looks like a new event, and the whole apparatus silently does nothing. Beware also over-broad keys: two genuinely different enquiries from the same email must not collapse into one, which is why the message id, not the sender alone, is in this lesson's key.

## The register and the ordering that makes it true

The pattern is three steps in a strict order: **compute the key, check the register, act and record**. The register is any durable store keyed by the dedupe key: a Data Table here, a database table or the CRM itself in bigger systems. The ordering subtleties are the lesson. Record the key **before or atomically with** the side effect wherever the store allows (upsert semantics), because a crash between acting and recording invites a replay to act again; where you cannot be atomic, record first with a `processing` status and complete it after the act, so a replay finds evidence and a human can reconcile the rare stuck row. The workflow in this lesson checks the register, branches duplicates to a polite answer (callers deserve a success response for a duplicate, or they will keep retrying), and lets only unseen keys reach the side-effect node.

n8n also gives you smaller tools in the family: the **Remove Duplicates** node cleans repeated items inside one execution (useful, and no substitute for a register, because duplicates mostly arrive across executions), and `$execution.id` identifies a run for logging, though it identifies the delivery, not the event, so it is never the dedupe key.

## Safe reruns: the human half of the property

Idempotency is also what makes operations humane. With keys and a register, rerunning yesterday's failed intake is safe: the processed events answer as duplicates and only the genuinely failed ones act. Without it, every rerun is a duplicate generator and operators learn to fear the rerun button, leaving failed work stranded. Design the rerun path explicitly: which workflows are safe to rerun wholesale, which need a filtered rerun (by date, by source), and what the register says about partial completion. Lesson 17's first move (check whether the record was written before the failure) is this lesson, viewed from the incident side; builders who design Lesson 19 in from the start get to skip that detective work.

## Run it

Run the twin (`python3 idempotency_twin.py`): three identical deliveries, one register row, one queued email, and the assertion that proves the property. In n8n, create the Deliveries table from the workflow's sticky note, import `workflow.json`, select the table in both Data Table nodes, publish, and POST the same JSON body to the webhook three times (any HTTP tool; include an `email` and a `message_id`). First response: created. Second and third: duplicate, already processed, with the table still holding one row. Then change only the `message_id` and send again: a new lead, correctly, because identity changed.

## Common failures

- **Keys over volatile fields.** A key containing the delivery timestamp or a random request id dedupes nothing. Audit key ingredients for stability before anything else.
- **Act first, record later, crash in between.** The replay cannot see the act and repeats it. Order and upsert are the fix; hope is not.
- **Answering duplicates with errors.** A 500 to a duplicate tells the sender to retry harder. Duplicates get a success-shaped answer that says already processed.
- **Deduping within the run only.** Remove Duplicates inside one execution does nothing for the retry that arrives as tomorrow's execution. Registers persist; nodes do not.

## Recap checklist

- [ ] I can choose or compute an event key and defend its ingredients.
- [ ] My intake checks a durable register before any side effect, in the right order.
- [ ] Duplicates get a success-shaped answer; only unseen keys act.
- [ ] I can state which of my workflows are safe to rerun wholesale, and why.

## Resources

- [n8n: Remove Duplicates node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/)
- [n8n: Data Tables documentation](https://docs.n8n.io/data/data-tables/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
