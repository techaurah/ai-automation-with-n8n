# Lesson 02: Solution notes

The schedule test proves the timezone lines work: if the ping fired at the minute you set, `GENERIC_TIMEZONE` and `TZ` are doing their job; if it fired offset by your UTC difference, the container did not pick the change up (most often the stack was not fully restarted).

The paragraph should name three losses: **workflows** (the visible one), **credentials** (encrypted, and useless without the encryption key that also lives in that data folder, so a volume loss is a re-connect-everything event), and **execution history** (your debugging record). Bonus marks for noticing the exported JSON from step 2 is a real mitigation for workflows but not for credentials, which is why Lesson 29 treats backup as a designed routine, not a hope.

**What to notice.** Nothing in this lesson was about automation logic, and it is still the lesson that decides whether your automations exist next month. Operations is not the boring part; it is the part that makes the rest real.
