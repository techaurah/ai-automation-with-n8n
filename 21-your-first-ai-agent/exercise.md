# Lesson 21: Exercise

## Give the agent a second tool, and a reason to choose

1. Add the clinic fact lookup as a second tool: a Code Tool (or a small workflow tool, previewing Lesson 22) that returns whitening price or emergency days given a fact name. The twin already defines the contract.
2. Write both tools' descriptions so the model can choose correctly: the test is whether the price question uses the fact tool and the total question uses fact then calculator, in that order.
3. Run the three lesson questions plus "What is the total for 2 sessions, and when are emergency slots?" and record the tool sequences from the executions.
4. Deliberately degrade one description to "helper" and rerun. Note the failure, restore the description, and write the sentence that explains what a tool description is for.

You are done when the four-question suite shows correct tool sequences with good descriptions, and the degraded run is documented.

## Solution

See `solution/SOLUTION.md` in this folder.
