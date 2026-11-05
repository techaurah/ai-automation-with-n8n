# Lesson 06: Triggers: schedules, webhooks, and forms, three doors into the same house

**Time:** about 65 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 03 to 05 · **You need:** Your instance. Webhook and form tests use the editor's test URLs; nothing public is published.

Everything a workflow does starts with a trigger deciding *when*. This lesson builds the three trigger types that cover most real automation (schedule, webhook, and form), plus the pattern that makes them maintainable: whatever the door, the data gets normalised into one house shape immediately, so downstream nodes never care which door it came through. The capstone's intake is built on exactly this pattern.

## Schedules: time as a trigger

The **Schedule Trigger** fires on an interval or a cron expression. Cron is worth learning properly in one minute: five fields (minute, hour, day of month, month, day of week), so `0 8 * * *` is 08:00 daily and `*/15 * * * *` is every fifteen minutes. The editor also offers friendly intervals that generate the same thing. Two disciplines: schedules run in the instance timezone (Lesson 02's setup, paying off), and a scheduled workflow must be **published** to fire on its own; in the editor you test it manually. Scheduled jobs are where automations quietly become infrastructure: the morning digest in workflow 06a is trivial, but the follow-up chaser in the capstone is the same shape with teeth.

## Webhooks: the internet knocks

A **Webhook** node gives a workflow a URL. Any system that can send an HTTP request (a form plugin, a CRM, another workflow, a phone app) can start it, and the request's body, headers, and query arrive as the first item. Two URLs exist: the **test URL**, live only while you click Execute and listen, and the **production URL**, live when the workflow is published. Testing against the test URL while building is the professional habit; the data the node shows you is the real payload, headers included.

Two details matter immediately. The payload usually nests the interesting data under `body`, which is why 06b's normaliser checks `$json.body` first (Lesson 04's field-path lesson, in production clothes). And a webhook with no **Respond to Webhook** node answers a bare 200 with no body; adding the respond node lets the workflow answer with its result, which callers that retry on silence will thank you for.

## Forms: the trigger that is also the page

The **Form Trigger** serves a form page itself and starts the workflow on submission: no website plugin, no separate form tool. Fields are defined in the node, submissions arrive as items with the field labels as keys (capitalised exactly as you labelled them, a trap 06c's normaliser handles), and the node offers completion screens and redirects. For a small business intake, a form trigger plus a normaliser is a complete front door in one node. When the form must live inside an existing website, the same intake is a webhook behind the site's form instead; the downstream workflow does not change, which is the point of the pattern.

## One house shape: normalise at the door

All three workflows in this lesson end their first step with the same record shape: `kind`, the fields the business needs, and a `received` timestamp. This is the most valuable architectural habit in the course. Downstream, the classifier, the spreadsheet, and the digest consume one contract, and adding a fourth door (an email trigger in Lesson 15, a chat trigger in Module 5) means writing one small normaliser, not rebuilding the house. When you review other people's workflows, look for this: systems that normalise at the boundary age well, and systems that let five raw payload shapes leak inward rot from the middle.

## Run it

Import all three workflows. Run 06a manually and read its digest item. For 06b, click Execute, then send a test request to the test URL (the node shows it; a free tool like your browser for a GET or `curl -X POST <test-url> -H 'Content-Type: application/json' -d '{"name":"Tom Lee","message":"How much is whitening?"}'` works) and watch the workflow complete and the response return your normalised record. For 06c, execute the workflow and open the test form URL it shows, submit the form, and compare the item shape before and after the normaliser. Three doors, one shape: verify it with your own eyes.

## Common failures

- **Testing against the production URL.** While building, the production URL needs a published workflow and answers real callers. Live in the test URL until Lesson 28 says otherwise.
- **Forgetting the body wrapper.** Webhook data sits under `body` (and headers under `headers`). A normaliser that reads `$json.name` finds nothing and the workflow "works" while recording empty leads.
- **Cron in the wrong timezone.** A digest at 08:00 UTC is a 03:00 or 13:00 digest somewhere. Confirm the instance timezone before blaming the expression.
- **Five doors, five shapes.** Skipping the normaliser because "it is just one extra trigger" is how intake systems rot. Normalise at the door, every door, from the first one.

## Recap checklist

- [ ] I can write and read the cron expressions this course uses.
- [ ] I triggered a workflow by schedule, webhook, and form, and found each execution.
- [ ] I can explain test versus production webhook URLs without notes.
- [ ] Every trigger I build now ends in a normaliser producing one house shape.

## Resources

- [n8n: Webhook node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/)
- [n8n: Schedule Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/)
- [n8n: Form Trigger node](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.formtrigger/)
- [n8n documentation home](https://docs.n8n.io/)
