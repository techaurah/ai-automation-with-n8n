# Lesson 20: Solution notes

The fix is almost never "try harder" wording; it is an explicit rule in the system message: *answer the parts the facts cover, name the part they do not, and offer the team's confirmation for that part only*, plus one worked example of a partial answer inside the prompt when the model is small. Local small models need the example more than the rule; hosted frontier models usually need only the rule. That asymmetry is worth writing down, because it decides which steps of your real systems can run on the free local model and which cannot.

**What to notice.** You just did evaluation-driven prompt work: a tiny test set, a failure class (confident completion of partial facts), a targeted change, a rerun. Module 5 keeps the machinery visual, but the method is Course 1's eval loop wearing n8n clothes.
