# Lesson 14: Solution notes

Scenario 3 is the heart of it: pure timestamp logic resurrects the suppressed lead, because `new` is newer. The fix is a precedence carve-out above the timestamp rule: certain statuses are **sticky** and can only be cleared by a human in the system of record, never by a sync. Compliance states (do_not_contact, unsubscribed, deleted) almost always deserve this treatment, in every automation you will ever build, not just this exercise. For ties, the defensible sentence is that the system of record wins because it is the side with constraints and audit history; a tie means no evidence of change, so authority decides.

**What to notice.** The sync rule ended up encoding business ethics (never re-contact the suppressed) as precedence logic. That is normal in production automation, and it is why syncs are designed in the open with printed decisions, not assembled from copy-pasted nodes.
