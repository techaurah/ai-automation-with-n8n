# Lesson 33: Build the Lead Machine: intake, follow-up, and digest, wired and tested

**Time:** about 2 to 3 hours · **Difficulty:** Advanced · **Prerequisites:** Lesson 32, and the modules it names · **You need:** Your instance, the leads table from Lesson 32, a Gmail credential for drafts.

Building the capstone is deliberately anticlimactic: every mechanism in it appeared in an earlier lesson, and this lesson's work is assembly, wiring, and testing, in that order of importance. Three workflows ship here: the intake (form door, normalise, key, classify, route complaints to a human, score, store), the follow-up chaser (bounded, draft-mode, sticky-closed-safe), and the daily digest. The twin holds the business rules in testable Python, and the smoke test guards the files.

## Intake: the front half of the business

Workflow 01 is Lessons 06, 16, 19, and 24 composed. The form trigger is the door; the normaliser applies the house shape and computes the dedupe key under the data model's contract; the classifier (the simulated rule version here, swappable for Lesson 24's Text Classifier node with the labels unchanged) categorises; complaints branch to a human *before* scoring, because the rubric must never see them; scoring implements your Lesson 32 `RUBRIC.md` exactly (the shipped code follows the solution's reference rubric, so replace its weights with yours and note the change); and the store writes the full record, key and band included. The webhook door from Lesson 19, with its register check, is the intake's twin path in the full design: the lesson ships the form door complete and names the webhook wiring as the same pattern, because two doors were Lesson 06's exercise and the pattern has not changed.

## Follow-up: the bounded chaser

Workflow 02 runs the state machine. It reads contacted leads, computes due-ness from the `updated` date against the chase windows, drafts the chase, and stops at drafts: Lesson 27's gate, kept until the clinic graduates it on evidence. Status advances (`contacted` to `chased_1` to `chased_2`) happen in the production wiring after the approved send, described in the workflow's sticky note so the shipped file's draft-mode honesty is explicit rather than a silent gap. The sticky-closed rule needs no code here, and that is the design working: closed leads carry a status the chaser's query never selects, so no filter bug can resurrect them. Chase copy follows the ladder's tone discipline: specific, brief, one clear next step, and an easy out, because a follow-up a lead cannot decline gracefully is a complaint generator wearing a CRM's clothes.

## Digest, testing, and the twin as arbiter

Workflow 03 is Lesson 31 in miniature: a daily count of new leads by band, delivered on the low rung, with the zero case written as a real sentence ("a quiet day is also a report"), because silence cannot be distinguished from breakage and this system does not do silent. Testing closes the lesson: `lead_machine_twin.py` implements classification, scoring, and chase selection over sample leads with assertions matching the lesson text (Ayesha scores 100 and hot, Tom 45 and warm, Ayesha alone is due a chase), and `smoke_test.py` validates the three workflow files structurally for CI. When canvas and twin disagree during your build, the twin's tested rules win and the canvas gets fixed; that arbitration rule, stated once here, is how the two views stay one system (Lesson 04's twin principle, at capstone scale).

## Run it

Select your leads table in every Data Table node across the three workflows (the placeholders are deliberate, one last time), connect the Gmail credential in the chaser, and import all three. Submit the form three times with the twin's sample enquiries. Verify in the table: three rows, categories and bands matching the twin's printed output, the complaint test (submit a fourth, angry one) stored as closed with the human note and no score. Run the chaser manually and find its drafts in Gmail. Run the digest and read it. Then the offline gates:

```bash
cd 33-build-the-lead-machine
python3 lead_machine_twin.py
python3 smoke_test.py
```

Both green is the build's definition of done; Lesson 34 ships it.

## Common failures

- **Weights drifted from the rubric.** If the Code node's numbers differ from RUBRIC.md, the document or the code is wrong, and the twin's assertions are how you find out today instead of at the clinic.
- **Status advanced before the send.** Marking a lead chased when the draft was created, not when the approved send happened, corrupts the state machine quietly. The order is the data model; keep it.
- **The complaint that got scored.** If the branch order lets a complaint reach the scorer, the system's most sensitive input got its least sensitive handling. Branch order is policy (Lesson 08); test the angry path explicitly, as Run it does.
- **Digest silence on quiet days.** A missing digest and a broken digest look identical to the owner. The zero case is a feature; do not "optimise" it away.

## Recap checklist

- [ ] Intake, chaser, and digest run end to end against the real table.
- [ ] Twin and canvas agree on categories, scores, bands, and due chases.
- [ ] Complaints reach a human unrouted by the rubric, provably.
- [ ] The smoke test passes on all three workflow files.

## Resources

- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
- [n8n: Data Tables documentation](https://docs.n8n.io/data/data-tables/)
- [Course 1, Lesson 31: anatomy of a business assistant](https://github.com/techaurah/agentic-ai-for-beginners)
