# Lesson 18: Debugging: executions, pinning, and the discipline of one change

**Time:** about 55 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 03, 04 · **You need:** Your instance. The broken workflow is supposed to be broken; that is the lesson.

Debugging automation is a method, not a talent, and the method is short enough to fit on this folder's checklist card. This lesson hands you a workflow with a real, typical bug (it runs successfully and produces wrong output, the worst kind), and makes you find it the disciplined way: through the execution, with pinned data, changing one thing at a time. The bug is small. The method scales to every failure you will ever meet.

## The execution is the crime scene

Beginners debug from the canvas, re-reading their own intentions. Professionals debug from the **execution**: the recorded run with the real data at every node. The drill in `debugging_checklist.md` starts there deliberately. Walk the execution node by node and find the **first** wrong output; everything after it is downstream noise, and fixing symptoms downstream of the first wrong node is how an afternoon disappears. Note the execution's other gifts: the data each node received (not what you believe it received), the branch each item took, per-node timings that expose the slow API call hiding in a "slow workflow", and, on failure, the exact node and error that Lesson 17's alerts point to.

## Pinning: freezing time so you can think

**Pin data** on a node and its output becomes a fixture: downstream nodes rerun against the pinned output without re-executing upstream. Three uses dominate. Debugging a transform against the exact payload that broke it (this lesson). Building the back half of a workflow without waiting for a slow or rate-limited front half to refetch. And developing against production-shaped data safely, by pinning a real execution's output in a copy of the workflow rather than experimenting on the live one. In the editor, pinned data is marked clearly; unpin before you finish, and never let pinned sample data anywhere near a published trigger's path, because the fixture is not the world.

The twin reproduces the whole method in miniature: a pinned item as a literal, a broken mapping producing `None` fields, a fixed mapping, and assertions. When the canvas is unavailable or the logic lives in a Code node, the twin is not a lesser tool; it is the same discipline in text.

## Successful and wrong: the dangerous failure class

This lesson's bug never errors. The mapper reads fields at paths where they do not live (Lesson 04's nested payload, back again), gets `undefined`, and the workflow cheerfully drafts a reply to nobody about nothing, with a green execution. Error workflows (Lesson 17) cannot see this class at all. The defences are cultural and structural: **verify outputs, not statuses** (read the final node's data during testing, always), put **shape checks** at trust boundaries (a Code node that asserts required fields exist and fails loudly when they do not turns silent corruption into a visible error, which is strictly better), and keep **test data that resembles the ugliest real payload**, because tidy fixtures certify a workflow for a world that does not exist.

## Run it

Import `broken_workflow.json`, run it, and resist fixing anything. Follow the checklist: open the execution, walk to the first wrong output (the mapper), pin the payload node's output, and read the mapper's input in JSON view until the actual shape is undeniable. Fix the paths in the mapper, rerun against the pin, verify the reply names Tom and his question, unpin, run the full path, and write the one-sentence cause in the workflow's notes. The twin (`python3 debug_twin.py`) shows the same arc in four printed lines if you want the method without the mouse.

## Common failures

- **Fixing the node that complains.** The loudest symptom is rarely the first wrong output. Walk from the trigger; the bug is upstream of your frustration.
- **Changing three things, running once.** When it works, you learned nothing; when it does not, you lost ground. One change, one run, one observation.
- **Debugging against fresh sample data.** The original payload broke it; your tidy replacement may not reproduce anything. Pin the real thing.
- **Declaring victory at the fixed node.** Downstream nodes consumed the wrong shape during the bug's life; rerun the whole path and read the final output before closing the incident.

## Recap checklist

- [ ] I debug from the execution and can find a first wrong output methodically.
- [ ] I can pin data, iterate against it, and unpin before calling anything done.
- [ ] I can plant a shape check that turns silent wrongness into a loud error.
- [ ] My fixes land one at a time, and the cause gets written down in the workflow.

## Resources

- [n8n: executions documentation](https://docs.n8n.io/workflows/executions/)
- [n8n: debugging in the editor](https://docs.n8n.io/courses/level-two/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
