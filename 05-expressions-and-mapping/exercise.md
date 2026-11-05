# Lesson 05: Exercise

## Three date formats and a threshold

1. Extend the sample orders with an `appointment` field holding an ISO date string (for example `2026-11-12T14:30:00`).
2. In a new Edit Fields node, produce `appointment_day` formatted as `2026-11-12`, and `appointment_human` formatted like `Thu 12 Nov, 2:30 pm`, using date expressions.
3. Add a `priority` field: `high` when `due` is 200 or more, else `normal`. You will need to decide which node can see `due`, and put the field there.
4. Mirror all three in the twin and make both outputs agree.

You are done when both versions print identical records for both orders, dates included.

## Solution

See `solution/SOLUTION.md` in this folder.
