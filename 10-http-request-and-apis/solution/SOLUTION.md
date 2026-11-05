# Lesson 10: Solution notes

The split belongs on the HTTP node (its response format option for arrays), not in a later Code node: once items exist, every downstream node, the mapper, the IF, the counters, works per contact with no array handling anywhere. Branch counts should match the twin exactly; when they do not, the cause is almost always the mapper reading a field path that exists on some records and not others, which the twin exposes faster because it prints all ten contacts at once.

**What to notice.** Nothing in this exercise needed a new node type. Method, split, map, route: the HTTP pattern is small, and mastery is in the settings and the verification, not in more machinery.
