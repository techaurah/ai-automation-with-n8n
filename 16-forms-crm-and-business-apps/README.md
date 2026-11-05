# Lesson 16: Forms, CRMs, and business apps: intake that lands in the system of record

**Time:** about 65 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 06, 12, 13, 15 · **You need:** A free Airtable account for the CRM table (or another app node of your choice; the design transfers). Python for the twin.

Module 3 closes by assembling its pieces into the shape businesses actually buy: a public form whose submissions land, deduplicated, in the system of record where the team works. This lesson uses Airtable as the CRM stand-in because it is free and its node is typical, but the design (normalise at the door, compute a dedupe key, create deliberately) transfers unchanged to HubSpot, Salesforce, Notion, or a Postgres table. The capstone's intake is this lesson with a clinic's fields.

## App nodes are all the same shape, learn the shape

By now the pattern should feel familiar: an app node offers resources and operations (Airtable: create, get, list, update, search records; HubSpot: companies, contacts, deals, tickets; Notion: pages and databases), a credential governs access, and fields are mapped with expressions from the item. Learn to interrogate any new app node with four questions: what is the **matching key** it updates by, what does a **create** return (you want the new record's id, always store it), what are its **rate limits** and batch behaviour, and which operation is the **search** you will use for dedupe lookups. Vendors' n8n nodes vary in polish; the four questions cut through all of them.

One naming honesty note: calling Airtable "the CRM" is this lesson's simplification for a small clinic. The design does not change when the record system grows up; the node does. That portability is the payoff for normalising at the door in Lesson 06: swap the last node and the intake survives.

## The dedupe key: computed once, everywhere

Duplicates are the tax on every intake, and they are paid by humans merging records at the worst moments. The defence starts at intake: compute a **dedupe key** from stable identity fields (here, a truncated SHA-256 hash of normalised name plus email, computed in the twin so the contract is testable and identical on every path) and store it on the record. Normalisation is the key's foundation: case-folded, trimmed values, because `Ayesha@Example.com` and `ayesha@example.com` are one person and two keys until you fold them.

This lesson computes and stores the key; Lesson 19 completes the pattern by checking it before creation and merging instead of duplicating. Sequencing it this way is deliberate pedagogy: you cannot check a key you never stored, and most real CRMs are missing the key, which is why their duplicates feel inevitable. They are not inevitable; they are unkeyed.

## What the record must carry

A created record that cannot explain itself is future confusion. The intake writes, beyond the form's fields: the dedupe key, the **source** (which form, which campaign field if present), and relies on the store's own created timestamp. In richer intakes add the raw payload or a link to the execution, because the day a record looks wrong, the first question is "what actually arrived", and "the form said so" is not an answer. The twin's store prints in full at the end for exactly this reason: two records, each self-describing, one duplicate refused.

## Run it

Run the twin (`python3 crm_twin.py`): three submissions, two records, the duplicate refused by key even though its form was messier and its message different. In n8n, create a free Airtable base with a Leads table (Name, Email, Message, DedupeKey fields), connect the credential, select base and table in the node, import `workflow.json`, publish it (your first deliberate publish; Lesson 28 will formalise the habit), and submit the form three times as the twin did: same person twice with different casing, plus Tom. The table should show three created rows, because the pre-create check is Lesson 19's; the key column is what you are verifying today. Unpublish when done if the form is public-facing in your setup.

## Common failures

- **Dedupe by eyeball.** "We will merge duplicates weekly" means never, at scale, with feeling. Keys are computed at intake or duplicates are forever.
- **Keys over unnormalised data.** Case and whitespace are part of identity until you fold them. Every key contract starts with its normalisation rules, in writing.
- **Losing the created id.** The create response carries the record's id; workflows that do not store it cannot update the record later without a search, and searches by email find the duplicates you were avoiding.
- **Intake straight to the CEO's CRM.** New intake designs rehearse against a practice base first (this lesson), earn trust in draft mode (Lesson 15's ramp), then point at the real system of record.

## Recap checklist

- [ ] I can interrogate any app node with the four questions: key, create return, limits, search.
- [ ] My intake computes a normalised dedupe key and stores it on every record.
- [ ] I watched the twin refuse a duplicate and can explain the missing half Lesson 19 adds.
- [ ] Records I create carry source and identity, enough to explain themselves later.

## Resources

- [n8n: Airtable node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/)
- [n8n: HubSpot node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
