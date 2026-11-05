# Lesson 12: Solution notes

The zero case is where most attempts fail: without Always Output Data the Get returns nothing and the workflow ends invisibly, so the digest node never runs and "no stale leads" is indistinguishable from "the workflow is broken". With it on, the Code node receives either rows or an empty item and can honestly report both. Sorting oldest first matters once the digest is acted on by a human: the stalest lead is the most urgent, and the table should present it first without the reader re-sorting mentally.

**What to notice.** You have built the read half of the capstone's follow-up system. The write half (marking chased leads so they are not chased twice) is the state discipline of Lessons 16 and 19, arriving in order.
