# Lesson 17: Exercise

## Classify ten failures

1. Write ten realistic failures for the Lesson 16 intake (expired OAuth token, Airtable 429, malformed form JSON, duplicate email, sheet quota, DNS failure, a 500 from the CRM, a missing required field, a timeout after the record was created, disk full on the instance).
2. For each, decide: retry (how many times, what wait), error output as data, or stop and alert. The timeout-after-create case must end with the standard's first move, not a retry.
3.encode your table as data in the twin: extend `error_twin.py` with a classifier function mapping an error kind to a policy, and tests asserting your ten decisions.

You are done when the classifier and your table agree on all ten, and a second person could run your policy without you in the room.

## Solution

See `solution/SOLUTION.md` in this folder.
