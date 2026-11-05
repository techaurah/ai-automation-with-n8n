# Lesson 03: The editor and your first workflow

**Time:** about 50 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 02 (a running instance) · **You need:** Your n8n instance from Lesson 02.

This lesson is a guided tour with a purpose: build one small workflow in the editor, and learn to read the editor itself, because the editor is where you will debug, test, and think for the rest of the course. The workflow greets a new dental enquiry. It is deliberately small. The skill being taught is not the greeting; it is fluency in the canvas, the node panel, and the execution view.

## The canvas is a sentence

Read any workflow left to right like a sentence: a **trigger** starts it, **nodes** transform or act, **connections** are the verbs between them. The workflow in this lesson reads: *when run, take a sample enquiry, add the clinic and a status, write a greeting.* If you cannot say a workflow's sentence out loud, you do not understand it yet, and neither will the colleague who inherits it. Node names carry the meaning: this course names nodes by what they do ("Classify enquiry", "Draft reply"), never by their type ("Code1", "IF2"), because at midnight the names are the documentation.

## The node panel: input, parameters, output

Select any node and the panel shows three zones. **Input** is the data that arrived, which in the editor is real data from your last test run, not a mock-up. **Parameters** are the node's settings: fields, expressions, credentials. **Output** is what the node produced, shown as a table, JSON, or schema view. The habit to build now: after every change, look at the output before wiring the next node. Most beginner pain comes from building three nodes on an assumption the first node's output already disproved.

Two editor features matter from day one. **Execute step** runs one node with the current input. **Pin data** (in the output pane) freezes a node's output so downstream nodes can be rebuilt against stable sample data; Lesson 18 turns pinning into a debugging method.

## Executions: the run is the truth

Every run, test or production, is an **execution**, listed under Executions in the left sidebar. Open one and you see the path the data actually took, node by node, with the real inputs and outputs and, on failure, the node that failed and why. Builders who live in the executions view debug in minutes; builders who only stare at the canvas guess for hours. From this lesson on, "run it and look" means run it and open the execution, not just watch the canvas light up.

## Save, test, publish: the 2.x rhythm

In n8n 2.x, saving keeps a draft; **Publish** makes the workflow live for its triggers. The manual trigger in this lesson works in the editor regardless, which is why learning workflows use it. The rhythm the course teaches: build in the editor with test runs, save as you go, publish only when the workflow should react to the real world. Lesson 28 covers the model in full, including version history; for now, just notice the difference and never publish a half-built trigger to a real form.

## Run it

Import `workflow.json` from this folder. Run it with Execute Workflow. Click each node in turn and read its output pane: the sample enquiry item, then the same item with `clinic` and `status` added by the Edit Fields node, then the finished greeting from the Code node. Open the run in Executions and walk the same path again. Then rename the Code node to something worse ("Code1"), feel the small loss of comprehension, and rename it back. Naming is a feature.

## Common failures

- **Building downstream on unexamined output.** Wire three nodes, run once, debug everywhere. Run after each node and the bug is always in the last place you changed.
- **Confusing test data with production shape.** The sample enquiry is shaped like a real form submission on purpose. When your sample data is tidier than reality, your workflow is trained on fiction.
- **Publishing a learning workflow.** A published webhook or form trigger is a public endpoint. Keep learning workflows unpublished until a lesson tells you to publish, and Lesson 30 covers securing the ones you do.
- **Losing the sentence.** If you add a node and cannot extend the workflow's spoken sentence to include it, the node probably does not belong, or is named wrong.

## Recap checklist

- [ ] I can read a workflow as a sentence and name nodes by what they do.
- [ ] I can find input, parameters, and output for any node, and execute one step.
- [ ] I opened an execution and traced the data path node by node.
- [ ] I can explain save versus publish in one sentence each.

## Resources

- [n8n: build your first workflow](https://docs.n8n.io/try-it-out/)
- [n8n Academy, the official courses](https://learn.n8n.io)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n: importing and exporting workflows](https://docs.n8n.io/courses/level-one/chapter-6/)
