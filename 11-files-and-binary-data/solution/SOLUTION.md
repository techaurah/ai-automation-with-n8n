# Lesson 11: Solution notes

The second Convert to File writes to a differently named binary property (`summary`), which is the entire trick: slot names are the file system's folders here, and collisions, not conversions, cause the losses. The loud inspection checks `Object.keys($binary)` (or `$input.first().binary`) against the expected set and throws with the missing slot's name; silent absence is the enemy, and an execution that errors in testing saves a customer-facing absence in production.

**What to notice.** The workflow now treats files as data with a contract (names, presence) rather than as attachments that usually show up. That is the difference between a demo pipeline and a document system.
