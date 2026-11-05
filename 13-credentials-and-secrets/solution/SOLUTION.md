# Lesson 13: Solution notes

The scanner's token-shape check catches the plant regardless of which parameter holds it, which is why the scan walks all parameter strings rather than only fields named like secrets. The git answer is the lesson's core: deleting a value from the current file does not remove it from history, clones, or CI artifacts, so a once-committed secret is a compromised secret and rotation is the only remedy. The credential-based workflow never carried the value in any revision, which is the entire point of the architecture.

**What to notice.** The rule is cheap on day one and expensive on day ninety. Every lesson after this assumes it, and the capstone's review checklist (Lesson 34) includes the scan as a shipping gate.
