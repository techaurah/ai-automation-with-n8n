# Lesson 27: Human-in-the-loop and guardrails: approvals before actions, checks on outputs

**Time:** about 70 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 15, 21, 22 · **You need:** A Gmail credential for the live approval (or read the Slack equivalent in the docs). Python for the twin.

Module 5 ends where professional AI automation actually lives: not with a cleverer agent, but with controls around the one you have. Two control families, both built here: **guardrails**, automated checks that screen model output before anyone acts on it, and **human-in-the-loop** approvals, where a person makes the irreversible call. The workflow assembles the course's canonical order: draft, screen, approve, send. The twin implements the same state machine so its logic can be audited without a canvas or a model.

## Guardrails: cheap checks, run every time

n8n's **Guardrails** node screens text against configurable checks, personally identifiable information patterns, URLs, secret-shaped strings, and topic restrictions among them, and routes or blocks accordingly. Its value is not sophistication; it is *invariance*. A model can be charmed, rushed, or injected into drafting a message containing a patient's email or a card number; the regex does not care how persuasive the paragraph is. Place guardrails at trust boundaries: on agent output before it leaves, and (the direction builders forget) on untrusted *input* before it reaches the model, where Lesson 30's injection defences live.

Design rules: checks return a decision the workflow acts on (block, redact where the node supports it, or route to a human), never a log line nobody reads; the blocked path is a real path with an owner, like every fallback in this course; and guardrails complement rather than replace the structural defences (narrow tools, scoped credentials), because a screen that catches 95 percent in front of an over-powered agent is an incident on a timer.

## Approvals: the send-and-wait pattern, generalised

Lesson 15 introduced **send and wait for response** on messaging nodes: the workflow messages a human with the proposed action and Approve or Reject options, pauses, and resumes down the branch matching the click, with the decision in the data. n8n also supports human review for individual AI **tool calls** (added in the 2.x line): mark a sensitive tool as requiring review and the agent pauses before that tool runs, which is the right granularity when the agent composes the action itself. And because 2.x parents receive sub-workflow outputs after Wait pauses, approvals compose through the architecture instead of breaking it.

The approval message is a user interface with the same standard as Lesson 17's alerts: what is proposed, in full (the actual draft, not "an email"), why (which trigger, which record), what each button does, and what happens on timeout. Timeouts are a design decision: an approval that expires should default to *not* doing the irreversible thing, record the expiry, and tell the requester, all three, because a silently expired approval and a silent approval look identical in the logs and opposite in the world.

## The state machine underneath

The twin strips the pattern to its skeleton: a proposal is `pending`, a guardrail can mark it `blocked`, a human marks it `approved` or `rejected`, and `execute` asserts approval before acting, refusing otherwise, loudly. Every transition is logged, because the audit trail of who approved what is a business record, not debug output. Read the workflow beside the twin and map each node to a transition; then notice what the canvas version adds (transport, identity, persistence) and what it must never lose (the assertion: no path from draft to send that skips a state). When you review any approval design, in any tool, draw its state machine and hunt for the skipping path. There usually is one, in the retry logic or the timeout branch, and finding it in review is the whole job.

## Run it

Run the twin (`python3 hitl_twin.py`) and watch the blocked proposal refuse execution. Import `workflow.json`, connect Gmail in the send-and-wait node with your own address as approver, and run it manually: the approval email arrives with the draft in full; click Reject first and watch the execution take the rejection branch (a recorded decision, not an error). Run again and Approve; the send branch fires. Then edit the simulated draft to include an email address and rerun: the Guardrails node should stop the flow before any approval is requested, which is the ordering working exactly as designed.

## Common failures

- **Approval messages that hide the payload.** Approving "an email to a patient" without the text is rubber-stamping with extra steps. The full proposed action, or the gate is theatre.
- **Expiry defaults to go.** A timeout that sends anyway converts every unanswered approval into a yes. Expiry means no, recorded, notified.
- **Guardrails as logging.** A check whose block path goes nowhere is a diary. Blocked items route to a human queue with an owner and a review rhythm.
- **Approving your own agent's work at 2am by habit.** Approval fatigue is real: if everything needs approval, nothing gets attention. Reserve gates for the irreversible and the customer-facing, and graduate proven actions off the gate deliberately, with the eval evidence from Lesson 24.

## Recap checklist

- [ ] My irreversible actions sit behind propose, screen, approve, in that order.
- [ ] I can draw the approval state machine for any design and find its skipping path.
- [ ] Approval messages carry the full payload, the reason, and an expiry that means no.
- [ ] Guardrail blocks route to a human queue, never to a log and a shrug.

## Resources

- [n8n: human-in-the-loop for AI tools](https://docs.n8n.io/advanced-ai/human-in-the-loop-tools/)
- [n8n: Guardrails node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.guardrails/)
- [Agentic AI for Beginners, Lesson 26 (guardrails and approvals)](https://github.com/techaurah/agentic-ai-for-beginners)
- [n8n documentation home](https://docs.n8n.io/)
