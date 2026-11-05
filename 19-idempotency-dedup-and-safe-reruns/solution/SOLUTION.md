# Lesson 19: Solution notes

The crash test is the entire argument: with act-then-record, the replay sees an empty register and acts again, and no amount of careful coding elsewhere prevents it, because the information about the first act never survived. Record-first with a processing status converts the same crash into a visible, reconcilable state: the register says an attempt began, and the policy (check the side effect's own store for the record, then mark created or clear and reprocess) resolves it deliberately. Stuck rows should be rare, alarmed (Lesson 31 counts processing rows older than an hour), and owned by a named human.

**What to notice.** Exactly-once delivery does not exist; exactly-once *effect* is a design you build from keys, registers, and ordering. Every payment, booking, and message you automate from here on deserves the three questions: what is the key, where is the register, which side of the act is it written on?
