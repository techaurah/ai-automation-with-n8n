# Lesson 32: Capstone spec and scaffolding: the Lead Machine, specified before it is built

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** All previous modules · **You need:** Your instance, and your fork of this repo (the capstone lives there).

The capstone builds the Lead Machine, the lead-handling system BrightSmile Dental has been assembling in pieces all course: intake, qualification, follow-up, and a daily digest, running unattended with the reliability and control discipline of Modules 4 to 6. This lesson is the spec and the scaffold: read the requirements like a contract, set up the data model, and validate the skeleton, because Lesson 33 builds at speed on decisions made carefully here.

## The spec, read as a contract

The capstone README (in this folder's `capstone/`) states the four jobs and the non-negotiables inherited from the course: an error workflow on everything, idempotency keys checked before side effects, secrets only in credentials with both scanners clean, approvals before customer-facing sends, and the Lesson 28 release routine for going live. Read the non-negotiables as acceptance criteria, because Lesson 34 grades against them literally. Two spec judgements to internalise. The system is deliberately **not** an agent product: classification gets one model step where language demands it (Lesson 24), scoring is a written rubric in code, and the workflows are deterministic everywhere else, per Lesson 01's three-question test applied to a whole business. And the follow-up chaser is **bounded**: two chases, then the lead rests; unbounded chasing is spam with a workflow diagram.

## The data model, and why it comes first

`DATA_MODEL.md` defines the leads table, the dedupe key contract, and the status state machine (new, contacted, chased_1, chased_2, booked, closed). Three design points carry the whole build. The **key contract** is copied from Lesson 19 with the clinic's ingredients, so every intake door computes it identically. The **statuses are a machine**, with named transitions the workflows implement and no others; a status a workflow invents mid-build is a spec change and gets written into the model first. And **closed is sticky** (Lesson 14's carve-out): a do_not_contact lead can never be resurrected by a chase, a sync, or a rerun, and the follow-up workflow's filter encodes that as an exclusion it cannot forget.

## The scaffold, and the smoke test that guards it

The scaffold ships a skeleton intake (trigger, normaliser stub, respond) and `tests/smoke_test.py`, which validates every workflow file in the capstone folder: JSON parses, node names unique, connections sound. It is the repo validator's local twin, and it runs in CI, so a broken export fails loudly before Lesson 33 builds on it. Set up the capstone in **your fork** now: copy the `capstone/` folder into a working directory of your fork (or work in place and let the showcase PR carry the whole project), create the leads Data Table from the model, and run the smoke test against the skeleton. Lesson 33 assumes this ground is prepared.

## Run it

Read `capstone/README.md` and `capstone/DATA_MODEL.md` end to end, pen in hand: mark every place the spec is ambiguous to you, because Lesson 33 will not pause to renegotiate them. Create the leads table in your instance from the model. Then:

```bash
cd 32-capstone-spec-and-scaffolding/capstone
python3 tests/smoke_test.py
```

The skeleton validates. Import `intake-skeleton.json`, POST one test enquiry, and watch the normaliser stub answer: that thin green execution is the scaffold standing up.

## Common failures

- **Building before specifying.** Every hour of Lesson 33 speed is bought here. A status or key invented mid-build costs a redesign; invented here, it costs a sentence.
- **An agent-shaped capstone.** The test from Lesson 01 still applies at system scale. Model steps live where language varies; the machine around them is deterministic, testable, and boring, proudly.
- **A chaser with no bound.** Two chases, recorded, then rest, is a business rule with legal and reputational weight, not a parameter to tune upward in a growth mood.
- **Skipping the table setup.** Lesson 33's workflows reference the leads table in five places. Creating it now, from the model, is the difference between building and plumbing.

## Recap checklist

- [ ] I can state the capstone's four jobs and its non-negotiables without opening the spec.
- [ ] The leads table exists in my instance, built from DATA_MODEL.md.
- [ ] The skeleton validates under the smoke test and answers a test enquiry.
- [ ] My ambiguities are listed and resolved, in writing, before building.

## Resources

- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
- [Agentic AI for Beginners, Lessons 31 to 36 (the sister capstone)](https://github.com/techaurah/agentic-ai-for-beginners)
- [n8n: Data Tables documentation](https://docs.n8n.io/data/data-tables/)
