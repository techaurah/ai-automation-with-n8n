# Lead Machine data model

## Table: leads (Data Table, Lesson 12)

| Column | Type | Notes |
|--------|------|-------|
| name | text | Normalised at the door: trimmed |
| email | text | Normalised: trimmed, lower-cased |
| channel | text | website form, webhook, instagram, email, unknown |
| message | text | The enquiry as received |
| category | text | booking, pricing, complaint, other (Lesson 24) |
| score | number | Qualification score, 0 to 100 (Lesson 33 rubric) |
| band | text | hot, warm, nurture (from the score) |
| status | text | new, contacted, chased_1, chased_2, booked, closed |
| dedupe_key | text | sha256(normalised name + email + message id), 16 chars |
| updated | text | ISO date of the last state change |

System columns id, createdAt, updatedAt are provided by n8n.

## Key contract (Lesson 19)

- Ingredients: normalised name, normalised email, provider message
  id when one exists (form submissions carry a generated one).
- Algorithm: SHA-256 over `name|email|message_id`, hex, first 16
  characters.
- Collisions: at clinic scale, a collision is treated as the same
  person; the second delivery is answered as a duplicate.
- The register is this table: check `dedupe_key` before inserting.

## State machine

new -> contacted (first reply approved and sent)
contacted -> chased_1 -> chased_2 (scheduled follow-ups)
any -> booked (appointment made), any -> closed (declined, done,
or do_not_contact; closed is sticky and sync-proof, Lesson 14)
