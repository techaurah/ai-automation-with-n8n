# Lesson 17: Error workflows and retries: designing for the day it breaks

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 10, 15 · **You need:** Your instance.

Every workflow you publish will fail eventually: an API rate-limits, a credential expires, a payload arrives in a shape nobody predicted. The difference between a hobby automation and a system is what happens in that minute. This lesson builds the two-layer answer: local policy on each node (continue, retry, error output) and a global error workflow that turns any failure into a specific, actionable alert, following the content standard the twin defines.

## Local policy: the node's own settings

Every node carries error behaviour in its settings, and Lesson 10 introduced the pair that matters: **On Error** (stop the workflow, continue to an error output, or continue passing error data through) and **Retry on Fail** (attempts and wait between them). The thinking that goes with them: retry what is **transient** (network blips, 429 rate limits, 5xx from a healthy service), with a wait that respects the cause (a rate limit wants seconds to minutes, and exponential patience beats hammering). Never retry what is **deterministic** (a 400 validation error, a 404, a malformed payload you generated): retrying a deterministic failure is just failing more slowly and billing yourself for it. Route errors you expect (a lookup that may miss) to the error output and handle them as data; let errors you do not expect stop the run and summon the global layer.

## The error workflow: one instance-wide safety net

An **error workflow** is a workflow that starts with an **Error Trigger** and is registered in another workflow's settings. When that workflow fails, the error workflow receives the failure's essentials: which workflow, which execution, which node ran last, and the error itself. The production shape is almost always: format an alert to the Lesson 17 standard, send it on the ladder's high rung (Lesson 15), and stop. One well-built error workflow serves every workflow on the instance, which is why this lesson builds it once, carefully, as infrastructure.

Two operational truths. The error workflow must itself be published and is itself capable of failing, so keep it brutally simple: the alert path that depends on the failing system (emailing via the very API that is down) is a known trap, and a second channel for the error workflow's own failures is a Lesson 31 refinement. And error workflows fire on execution failure, not on bad outcomes: a workflow that succeeds while writing wrong data needs the monitoring of Lesson 31, not this net.

## The alert content standard

An alert is a user interface for a stressed human, and most alerts are terrible at it ("workflow failed" is a riddle). The twin encodes this course's standard; every alert carries: the **workflow name**, the **node** that failed, the **error message**, the **execution id** with the instruction to open it rather than guess, **the record being processed** when there is one, and the **first move** (usually: check whether the side effect already happened before rerunning, because the failure often occurs after the write, and a blind rerun is Lesson 19's duplicate factory). Alerts following the standard get acted on; alerts that do not get muted, and a muted error workflow is worse than none, because it felt like coverage.

## Run it

Import both workflows. Save the error workflow, open the fragile workflow's settings, set its Error Workflow to the one you just imported, save, and run the fragile workflow. It throws deliberately. Within moments the error workflow executes: open its execution and read the built alert, then check it against the twin (`python3 error_twin.py`) field by field. Finally, remove the error workflow registration and rerun the fragile workflow to feel the silence you just engineered away.

## Common failures

- **Retrying deterministic errors.** A 400 retried five times is five failures and a slower page. Classify by status code family before enabling retry.
- **The error workflow that emails through the broken thing.** If the alert path shares the failure, you learn about outages from customers. Give the net its own simple channel.
- **Alerts without the record or the execution id.** The responder's first ten minutes become archaeology. The standard exists so the first move takes one minute.
- **Error workflows on learning workflows.** Register the net on systems that matter; a net that fires for every lesson experiment trains you to ignore it before the capstone even ships.

## Recap checklist

- [ ] I can set On Error and Retry on Fail from a failure's classification, not from vibes.
- [ ] My instance has one published error workflow registered on a real workflow.
- [ ] My alerts carry workflow, node, error, execution id, record, and first move.
- [ ] I can state what error workflows cannot catch (successful wrong outcomes).

## Resources

- [n8n: error workflows](https://docs.n8n.io/flow-logic/error-handling/)
- [n8n: Error Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
