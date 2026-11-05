# Lesson 25: Exercise

## Break retrieval, fix retrieval

1. Add a fourth document to both twin and store: a refunds policy that mentions whitening explicitly ("whitening is non-refundable once started"). Reload, and ask the whitening price again. Note what retrieval returns now and whether the answer stays correct.
2. Deliberately mismatch the asking workflow's embeddings model in a copy (any other model name) and observe the retrieval quality collapse; restore it.
3. Extend your question-pair set to ten, with expected sources, including two abstention cases. Record pass rates for twin and workflow.

You are done when the refunds document coexists with correct price answers, the mismatch failure is documented, and your ten-pair set runs green on the workflow.

## Solution

See `solution/SOLUTION.md` in this folder.
