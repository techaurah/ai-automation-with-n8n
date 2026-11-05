# Lesson 27: Exercise

## Move the gate

1. In the twin, add a third decision-maker: an auto-approver that approves proposals under a stated value threshold (a booking change under GBP 50) and sends everything else to the human. Keep the guardrail before both.
2. Prove with tests: a clean small proposal auto-approves and executes; a clean large one waits for the human; a blocked one never executes even if the auto-approver would have said yes.
3. Write the one-paragraph gate policy for the capstone's follow-up emails: which go free, which need a human, which are blocked outright, and the evidence you would need to loosen each rule.

You are done when the state machine's tests all pass and the policy paragraph names thresholds a business owner could argue with productively.

## Solution

See `solution/SOLUTION.md` in this folder.
