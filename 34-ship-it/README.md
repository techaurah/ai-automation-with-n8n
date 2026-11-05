# Lesson 34: Ship it: publish, document, hand over, and join the showcase

**Time:** about 90 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 33 · **You need:** The built Lead Machine, your fork, and the Lesson 28 checklist.

Shipping is a discipline, not a button, and this final lesson runs it in full: the non-negotiables verified as a gate, the release executed by the book, the documentation written for the colleague who inherits the system (often future you), the operations baseline set, and the finished capstone submitted to the course showcase, which is this programme's completion artifact in place of a certificate. When this lesson ends, you do not merely know n8n; you operate a system built with it, in public, where anyone can inspect how it was made.

## The gate: non-negotiables as checks, not sentiments

`ship_check.py` and `completion-checklist.md` convert Lesson 32's promises into pass or fail evidence: structural validity, no placeholders in the production copies, the twin's rules green, plus the manual proofs (a forced failure producing the standard alert, a replay refused, a restore rehearsed) that scripts cannot do for you. Run the gate on your fork's production exports, not on the course's teaching copies; the script knows the difference and says so. A gate that cannot fail is a decoration, so expect this one to catch something real on its first run (a placeholder in the digest's table reference is the traditional catch) and treat the catch as the gate earning its keep.

## The release, in order, watched

Publish in the checklist's order: intake first (nothing else matters if leads cannot land), digest second (the owner's visibility, live from day one), chaser last (the workflow that acts on people, published only when its approvals have been tested end to end). Each publish follows Lesson 28: previous version exported as rollback, publish, one real-shaped test through the production path, first real executions watched. Then the operational baseline: record the four numbers (Lesson 31) for the first week somewhere durable, because every future "is it getting worse" question is unanswerable without a beginning. Handover documentation uses `project-readme-template.md`: what it does, how it runs, where keys and backups live, who owns it, and the guarantees section kept verbatim in spirit, because a system's promises are part of its interface.

## The showcase, and what this course leaves you with

Submit the finished project to the course showcase (the `showcase/` folder explains the one-row pull request). The entry links your public repository: workflows, twin, rubric, README, and the honest state of the system. That public, inspectable artifact is the programme's answer to certificates, here as in Course 1: proof that travels because it can be run.

What you hold at the end: the vocabulary and judgement to choose between workflow, agent, and code; the core and AI node craft to build either; the reliability, security, and operations discipline to run them like infrastructure; and one complete business system as the evidence. The honest next steps are in this lesson's exercise, and the sister course (Agentic AI for Beginners) deepens the agent side for those who want it. Keep the four numbers green, and the system, and this course, have done their jobs.

## Run it

Work `completion-checklist.md` top to bottom, evidencing each line. Run the gate:

```bash
cd 34-ship-it
python3 ship_check.py
```

(against your production exports in your fork; on the course's own teaching copies it will flag the deliberate placeholders, which is the gate working as designed). Publish in order, watch the first executions, baseline the four numbers, finish the project README from the template, and open the showcase pull request. Then re-read Lesson 01's three questions one last time and notice what you would now automate differently in your own working life; that list is your next project backlog, and it is the real graduation.

## Common failures

- **Shipping the teaching copies.** Placeholders, simulated classifier, draft-mode shortcuts: all correct in lessons, all blockers in production. The gate exists because builders ship the files they have, not the files they meant to make.
- **Publishing the chaser first.** The workflow that acts on people goes live last, after its approvals and its state machine are proven. Order is a safety property.
- **A README that describes the dream.** Handover docs state what the system does today, including its draft-mode limits. The next maintainer's trust is set by the first gap they find between doc and system.
- **No baseline.** Without week one's numbers, month three's argument about whether the system degraded is unfalsifiable folklore. Baseline while it is boring.

## Recap checklist

- [ ] The gate passed on my production copies, with evidence for every manual check.
- [ ] Intake, digest, and chaser published in order, first executions watched.
- [ ] The project README tells the truth about what the system does today.
- [ ] My capstone is in the showcase, and my next-project list exists.

## Resources

- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
- [Agentic AI for Beginners, the sister course](https://github.com/techaurah/agentic-ai-for-beginners)
- [TechAura, the company behind TechAurah Academy](https://techaurah.com)
