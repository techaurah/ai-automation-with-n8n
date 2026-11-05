# Lesson 08: Solution notes

The complaint rule goes **first** in the Switch: rule order is priority order, and a complaint that also mentions a booking price must escalate, not get a price list. For the gate, the cleaner answer is to add `complaint` to the allowed set in the IF's regular expression: it is a legitimate category arriving clean, and the normaliser's job is repairing drift, not blessing vocabulary. Routing policy (what categories exist) lives in the gate; repair (case) lives in the normaliser; priority lives in rule order. Three different concerns, three different homes.

**What to notice.** Tone was a routing property. The escalation draft differs not in facts but in register, and the workflow encodes that judgement where a reviewer can see and change it: in the branch structure, not buried in a prompt.
