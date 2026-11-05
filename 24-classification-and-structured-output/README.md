# Lesson 24: Classification and structured output: model answers a router can trust

**Time:** about 65 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 08, 20 · **You need:** Your instance and a model (Ollama as usual, or hosted swap).

The most valuable AI step in business automation is rarely a chatbot; it is a classifier quietly routing work: this ticket is a booking, that one is a complaint, the third needs a human. For routing to be safe, the model's answer must arrive as data with a contract, not as a sentence a workflow then parses with hope. This lesson builds classification two ways (the dedicated Text Classifier node, and a chain with a Structured Output Parser) and adds the confidence discipline that keeps the odd cases human.

## The Text Classifier node: routing as a node type

The **Text Classifier** node takes input text, a set of categories with **descriptions**, and a model sub-node, and gives each category its own output, like a Switch whose rules are meanings instead of string matches. The descriptions are the engineering: "booking: wants an appointment, an emergency visit, or to reschedule" classifies well; a bare label list classifies like a coin flip on anything ambiguous. Categories should be few, mutually exclusive in intent, and designed with the **fallback** in mind: the node's fallback output (here, `other`) is where unmatched and ambiguous items land, and like Lesson 08's Switch fallback, it must be wired to something a human sees, in this case the review queue.

Where does a dedicated node beat Lesson 08's Code classifier? On language that rules cannot enumerate: sarcasm, misspellings, the complaint phrased as a question. Where do rules win? On volume, cost, and determinism: a keyword pass that resolves 80 percent of tickets for free, with the model node judging the remainder, is a legitimate production architecture, and the twin's rule classifier exists so you can measure that split on your own data instead of assuming it.

## Structured output: schemas instead of sentences

When a chain or agent must return data, the **Structured Output Parser** sub-node constrains it to a JSON schema you define: here, a `label` from a fixed enum and a numeric `confidence`, both required. The parser instructs the model, validates the reply, and exposes parsed fields as item data the next node can route on. This is Course 1's output-contract discipline with a node for a face, and its limits deserve the same honesty: a parser raises the rate of valid replies enormously, and a model can still produce schema-valid nonsense (a confident `booking` for a parking question), which is why the contract includes confidence and why the next section exists. Use structured output anywhere a workflow consumes a model's judgement: extraction (Lesson 10's mapping, done by a model), classification, summarisation with fields. Free-text model output should end at a human's eyes, never at a router.

## Confidence and the escalation rule

The twin states the course's rule plainly and enforces it in a validator: below the confidence threshold (0.6 in the twin; tune it on your data), the label is forced to `other` and the ticket goes to a human. Confidence from a model is not a probability in the statistical sense; treat it as a self-reported signal that correlates with correctness well enough to route by, after you have measured it on a labelled sample (the exercise starts that measurement). Two operational corollaries: log label plus confidence on every classified item, because the log is tomorrow's tuning data and drift detector; and review the `other` queue weekly, because a growing `other` share means the world invented a category you have not named yet, and the classifier cannot tell you that any other way.

## Run it

Run the twin (`python3 classifier_twin.py`): four tickets, four contract-valid results, parking escalated. Import `workflow.json`, run it with your model, and compare the classifier's routing with the twin's on the same four tickets; disagreements on the parking question are the interesting ones to read in the execution. Then import `workflow-structured.json`, run it, and inspect the chain's output item: a parsed object, label and confidence as fields, ready for a Switch. That shape, not the label's correctness on one ticket, is the lesson's deliverable.

## Common failures

- **Categories without descriptions.** The model cannot read your mind about what counts as a complaint. Descriptions with an example phrase each are the cheapest accuracy you will ever buy.
- **Parsing free text downstream.** A router testing whether the reply "contains booking" breaks on "this is not a booking". Structured output exists; use it, and validate at the boundary anyway.
- **No fallback wiring.** Unmatched items stop silently inside a green execution, and the angriest ticket of the month is the one most likely to be unmatched. The fallback is a queue a human reads.
- **Confidence theatre.** Routing on a threshold you never measured is decoration. Label fifty real tickets, compare, then set the number.

## Recap checklist

- [ ] I can build a classifier with described categories and a wired fallback.
- [ ] My model steps return schema-shaped data validated at the boundary.
- [ ] I route low-confidence items to humans by rule, not by hope.
- [ ] I log label and confidence on every classified item for tuning.

## Resources

- [n8n: Text Classifier node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.textclassifier/)
- [n8n: Structured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
