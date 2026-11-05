# Lesson 33: Solution notes

Parity is achievable precisely because the rules live in one place per door at most: classification and scoring implemented twice will drift, so the strong builds factor them into a sub-workflow both doors call (Lesson 22's pattern in deterministic dress), leaving each door only its normaliser, which is the one part that is genuinely door-shaped. If you duplicated the logic for speed, the twin's parity tests are now your drift alarm, and the exercise's real deliverable is knowing which of those two positions you are in, in writing.

**What to notice.** The system now has the property the whole course aimed at: its behaviour is specified in documents, implemented in two views that check each other, and boring in operation. Boring is the compliment. Lesson 34 makes it public.
