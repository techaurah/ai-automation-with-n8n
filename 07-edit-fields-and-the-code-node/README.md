# Lesson 07: Edit Fields and the Code node: the two ways to transform anything

**Time:** about 55 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 04 and 05 · **You need:** Your instance, and Python for the twin.

Every workflow transforms data, and n8n gives you two hammers: the Edit Fields node (still called Set in workflow JSON and older guides) for declarative field work, and the Code node for everything else. Builders get into trouble not by choosing one, but by stretching each past its competence: five-line expressions doing a loop's job, or a forty-line Code node doing a rename's job. This lesson draws the line precisely, and covers what changed in n8n 2.0, where Code nodes now run isolated in task runners.

## Edit Fields: declarative, inspectable, limited

Edit Fields does four things well: add a field (with an expression), rename a field, convert a type, and drop fields you do not want downstream (its "include" modes let you keep only named fields, which is a quiet security feature: strip payloads down before logging or sending them on). Its superpower is inspectability: the mapping is visible in the panel, a colleague can audit it without reading code, and Lesson 05's rule applies: expressions see the node's input, so chained derivations belong in a following node.

Its limits are equally clear: no loops beyond per-item repetition, no lookups against other data, no error handling, and unreadable beyond two or three operations in one expression. When you feel an Edit Fields node getting clever, that feeling is the signal to switch tools.

## The Code node: JavaScript first, Python available, isolated by default

The Code node runs JavaScript by default, with Python available through n8n's task runner setup. Two modes, and confusing them is the classic beginner bug: **run once for all items** gives you `$input.all()` and expects an array back; **run once for each item** gives you `$json` per item (Lesson 04's cleaner used this). Returning the wrong shape in either mode produces the empty-workflow-that-ran-fine symptom.

Three 2.x facts to build habits around. First, **task runners**: since 2.0, Code executes in isolated runner processes by default, so a crashing or runaway script cannot take the instance down, and some things that worked in a 1.x Code node (reaching into the host process) no longer do. Second, **environment variables are blocked** in nodes by default (`$env` does not resolve unless an admin deliberately enables it server-side): secrets belong in credentials, never in code, which Lesson 13 makes a hard rule. Third, the Code node is the right home for the `@n8n` built-in helpers you will meet: `$input`, `$('Node Name')`, `$now`, `$execution`, and `$getWorkflowStaticData()` for small per-workflow state (Lesson 12 weighs it against Data Tables).

## The line between them, as a working rule

Rename, add, convert, drop: Edit Fields. One-line derived value: expression inside Edit Fields. Anything with a condition over text, a loop over a nested array, a join against a list, formatting with edge cases, or a result you would want to unit test: Code node. And the twin rule from Lesson 05 still governs both: if the transform matters, it exists in a Python twin in the lesson folder or your project repo, where it can be tested without the canvas. This lesson's workflow chains the two nodes the way real workflows do: Edit Fields for the visible hygiene (trim, case), Code for the judgement (urgency detection, summary), each step inspectable at its own boundary.

## Run it

Run the twin (`python3 transform_twin.py`), then import and run `workflow.json`. Compare the final item with the twin's dictionary: same fields, same values. Then deliberately break the Code node once: change its mode to run once for each item without changing the code, run it, and look at what `$input` means there. Breaking it in a lesson is how you recognise it in production.

## Common failures

- **Wrong Code mode.** The number one Code bug. If output is empty or a single mangled item, check the mode before the code.
- **Secrets in code.** An API key pasted into a Code node is visible to anyone who can view the workflow, and travels with every export. Credentials exist precisely for this; Lesson 13.
- **Reaching for $env.** Blocked by default in 2.x. A workflow copied from a 1.x blog that reads `$env.MY_KEY` will fail or return nothing; migrate the secret to a credential.
- **A Code node doing a rename's job.** Unreviewable, untestable in the panel, and a smell that the builder did not know Edit Fields. Match the tool to the transform.

## Recap checklist

- [ ] I can name four jobs Edit Fields does well and four that belong in Code.
- [ ] I know both Code modes and can predict each one's input and output shapes.
- [ ] I can explain task runners and the blocked $env default in 2.x.
- [ ] My workflow's chained output matches the twin exactly.

## Resources

- [n8n: Code node](https://docs.n8n.io/code/code-node/)
- [n8n: Edit Fields node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
