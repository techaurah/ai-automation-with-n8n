# The Lesson 18 debugging drill

Work in order. Do not skip to step 4; step 4 is where time goes to die.

1. **Open the execution, not the canvas.** Find the failing or wrong
   run in Executions. The canvas shows intentions; the execution
   shows facts.
2. **Walk the data.** Click node by node through the execution and
   find the first node whose output is wrong. Everything downstream
   of that node is a symptom.
3. **Pin the input.** Pin the output of the node before the broken
   one, so you can rerun the broken node against identical data
   while you change it.
4. **Change one thing.** One field path, one setting, one line.
   Rerun. Read the output, not your hope.
5. **Unpin, run the real path, and check the whole execution**,
   not only the node you fixed.
6. **Write the cause in the workflow notes** in one sentence: what
   shape the data actually had, and what the node assumed.
