# Lesson 20: Exercise

## Teach the chain a boundary

1. Extend the facts block with opening hours and the hygienist's name.
2. Ask the chain (twin first, then live if you have Ollama) three questions: one the facts cover, one they partly cover (hours on a day not listed), and one they do not cover at all.
3. Score the three answers against the contract: grounded, honest about the gap, no invented detail. Adjust the system message until the partial question gets a partial answer (what is known, plus a defer on the rest) instead of a confident invention.
4. Record the three prompts and answers in your notes; they are your first eval set, and Lesson 24 formalises this.

You are done when the partial question is answered partially and honestly in both twin and chain.

## Solution

See `solution/SOLUTION.md` in this folder.
