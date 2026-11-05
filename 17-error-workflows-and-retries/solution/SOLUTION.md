# Lesson 17: Solution notes

The defensible table: expired token, stop and alert (a human must re-consent OAuth; retries cannot). 429, retry with a growing wait, then alert. Malformed JSON and missing field, error output as data (the record is quarantined, the workflow lives). Duplicate email, data, handled by Lesson 19's logic. Sheet quota, retry after a real wait (quotas are per-minute) then alert. DNS, retry briefly then alert (infrastructure). CRM 500, retry twice then alert. Disk full, alert immediately with no retry (every retry writes more). Timeout after create is the exam question: the correct policy is **verify, then decide**; check whether the record exists (Lesson 19's key lookup) before any re-creation, because the failure happened after the side effect.

**What to notice.** Only three of ten answers were "retry". Reliability is mostly classification, not persistence.
