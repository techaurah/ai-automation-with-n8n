# Lesson 15: Email, messaging, and notifications: the last mile of every automation

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 08, 13 · **You need:** A Gmail credential for the live send (free Google account, OAuth). The ladder logic and twin need nothing.

Automations earn their keep at the moment a human finds out. This lesson builds a notification ladder (low news gets filed, high news emails the owner, critical news emails and pings the team chat) and teaches the disciplines around sending: drafts before sends while trust is earned, the difference between notification and spam designed into the ladder itself, and the human-approval operations that turn messaging nodes into gates.

## The app nodes: Gmail, Slack, Telegram, and friends

The pattern repeats across services: a node per app, operations per job (Gmail: send, reply, draft, label, get; Slack: post, update, react; Telegram: send message, send photo), a credential from Lesson 13, and fields filled by expressions from the item. The practical differences worth knowing: **Gmail's draft operation** creates a real draft in the mailbox, which makes it the natural "automation proposes, human sends" tool; **Slack and Telegram** are chat-shaped, so messages are short, threaded where the platform supports it, and rate-limited in ways email is not; and every app node has operations learners overlook that solve whole problems (Gmail labels as a filing system an automation can maintain, Slack's ability to update a message so a status board stays one message instead of fifty).

This lesson's workflow ships with placeholder channel and credential selections, deliberately: connect your Gmail credential, pick or create a test chat channel, and the ladder runs. Sending a real email to yourself from a workflow is a small rite of passage; do it in this lesson, to your own address, before any workflow emails a customer in the capstone.

## Send and wait: messaging nodes as approval gates

Several messaging nodes, Gmail and Slack among them, offer a **send and wait for response** operation: the workflow sends a message with approve and reject options and pauses (a specialised Wait) until a human clicks, then continues down the matching path with the decision in the data. In n8n 2.x this composes properly with sub-workflows, whose parents now receive the final output even after such a pause. This is the single most important pattern in applied automation: anything irreversible, customer-facing, or expensive gets proposed by the workflow and approved by a person, in the tool the person already reads. Lesson 27 builds the full human-in-the-loop design on it; here, know it exists before you build send-first habits.

## The ladder: notification is a design, not a default

The twin and workflow encode the same ladder, and its rungs are the lesson. **Low** events (a digest exists) are filed, not sent: attention is the scarcest resource in any business, and an automation that emails everything trains its owner to read nothing. **High** events email one accountable human with a subject that carries the severity, because inboxes are triaged by subject line. **Critical** events add the team chat, where presence is live, and only critical events earn that interruption. Every rung is a sentence a business can argue with and change, written in the workflow where the argument belongs.

The draft-first ramp sits under the whole ladder: new automations start with sending operations swapped for drafts or an outbox file (the twin writes one), a human reviews a week of output, and only then do sends go live. Course 1 taught the same ramp for agents; it is the profession's standard answer to "the automation emailed WHAT to a client?"

## Run it

Run the twin (`python3 notify_twin.py`) and read the outbox: three messages, three different handlings, none sent. Then import `workflow.json`, connect Gmail, choose your test chat channel in the Slack node (or delete that branch and keep email if you have no Slack; the ladder still teaches its lesson), and run. Verify the high alert arrives as an email, the critical one additionally lands in chat, and the low one exists only as a filed item in the execution. Check your spam folder once, and note the from identity: workflow email speaks as the credential's account, which is why role accounts matter (Lesson 13).

## Common failures

- **Everything is urgent.** A ladder with one rung is an alarm that gets muted. If your workflow emails the owner daily, the one email that mattered will be the one they skipped.
- **Sending before the draft week.** New automations send drafts until a human has read enough output to trust the template, the data, and the routing. Skipping the ramp is how a placeholder name reaches a real customer.
- **The automation's voice is a person's.** Email sent from a personal mailbox by a workflow confuses recipients and strands replies when that person is away. Role accounts and clear subjects are part of the design.
- **Notifications with no payload.** "Something failed" without the what, the record, and the link to the execution is a riddle, not a notification. Lesson 17's error messages follow a content standard for this reason.

## Recap checklist

- [ ] I can drive send, draft, and label operations and name a job for each.
- [ ] I know send-and-wait exists and what design it unlocks in Lesson 27.
- [ ] My ladder has at least three rungs and a written reason for each.
- [ ] Every new automation I build starts in draft or outbox mode.

## Resources

- [n8n: Gmail node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/)
- [n8n: Slack node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/)
- [n8n: human-in-the-loop for workflows](https://docs.n8n.io/advanced-ai/human-in-the-loop-tools/)
- [n8n documentation home](https://docs.n8n.io/)
