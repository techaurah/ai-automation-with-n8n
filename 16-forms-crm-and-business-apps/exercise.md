# Lesson 16: Exercise

## A second form, the same key

1. Add a second intake path to the twin: a webhook-style payload (`{ "body": { "name": ..., "email": ... } }`, different shape, same person as an existing form lead, different casing again).
2. Route it through the same normalisation and key computation (one function, shared; if you copy the code, refactor until you do not).
3. Prove the store still holds one record for the person, now with both doors feeding it.
4. Write the key contract as a comment block at the top of the twin: fields, normalisation, hash, truncation, and what a key collision would mean.

You are done when both doors produce identical keys for the same human and the contract comment could be handed to another builder to implement identically.

## Solution

See `solution/SOLUTION.md` in this folder.
