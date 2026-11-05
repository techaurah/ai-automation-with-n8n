# Lesson 08: Conditional logic: IF, Switch, Merge, and the branches nobody tests

**Time:** about 60 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 04, 05, 07 · **You need:** Your instance.

Routing is where workflows stop being pipelines and start being systems. This lesson builds one router three ways in a single workflow: an IF that guards data quality, a Switch that routes on a category, and a Merge that reunites the branches. It also teaches the uncomfortable truth of branching: the branch you did not test is the one production will take, so this course tests branches with data designed to fall into each one, including the ugly fallback.

## IF: two exits and a contract

The **IF** node evaluates conditions and sends each item out of its true or false output. Items are evaluated independently: one execution can send two items left and one right, which surprises builders expecting a single global decision. Conditions combine (all must hold, or any may), compare with typed operators (string equals, number greater than, dates after, exists), and in loose validation mode n8n coerces types for you, convenient and occasionally treacherous when `"10"` meets `10`.

This lesson's IF is a quality gate, not a business router: it checks the category against the exact allowed set with a regular expression. Items that fail are not dropped; they go to a normaliser that repairs the known drift (case), then rejoin. Design pattern worth stealing: **validate at the boundary, repair what is repairable, route only clean data**.

## Switch: one decision, many exits

Where IF is a fork, the **Switch** node is a junction: rules evaluated in order, each with its own named output, plus a fallback output for items matching nothing. Three disciplines make Switch workflows survive contact with reality. Name the outputs (booking, pricing) rather than accepting output 0 and 1; order rules from most to least specific, because the first match wins; and wire the **fallback** to something real, a standard-reply draft here, a human review queue in production. An unwired fallback is a silent data shredder: items that match nothing simply stop, and the execution reports success.

Choose Switch over chained IFs when one field decides; choose IFs when different fields decide at different stages. A canvas of five chained IFs testing the same field is a Switch that has not admitted it yet.

## Merge: reuniting branches without lying

Branches that split usually rejoin, and the **Merge** node is how. Its modes answer different questions. **Append** concatenates the inputs' items into one list (this lesson: three drafted replies become one outbox list). **Combine by index** pairs the first item of branch A with the first of branch B, right for enriching the same records down two paths, wrong for almost everything else. **Combine by position and SQL modes** exist for heavier joins on self-hosted instances. The trap: Merge waits for all connected inputs in an execution, and on branches where an input received zero items, behaviour depends on the node's settings; test the empty branch case (send data that routes everything to one branch) before production does it for you. When no join is needed, skip Merge entirely: parallel branches ending in their own actions is a legitimate, often cleaner shape.

## Filter and the quiet branch

A fourth node belongs in this family: **Filter** keeps only items matching a condition and discards the rest. It is the right tool for genuine selection (only stale leads continue) and the wrong tool for routing, precisely because discarding is silent. Rule of the course: if a discarded item would matter to anyone, it is not a Filter candidate; route it somewhere visible instead.

## Run it

Import `workflow.json` and run it. Trace all four sample items: Ayesha and Tom pass the gate cleanly; Maria's `research` matches no Switch rule and lands in the fallback, by design; Sam's `BOOKING` fails the gate, gets normalised, and routes as a booking. The Merge output should hold four items, each with a reply. Then delete the fallback wire mentally: which item vanishes, and would any view have told you? That silence is the lesson.

## Common failures

- **Unwired fallback output.** Items matching no rule disappear inside a successful execution. Wire fallbacks to something a human sees.
- **Chained IFs testing one field.** Rewrite as a Switch; future-you reads one node instead of five.
- **Case drift at the router.** Routers compare exactly. Normalise values upstream (Lessons 04 and 07), or gate them like this lesson does.
- **Merge by index on unrelated lists.** Index pairing assumes both branches describe the same records in the same order. When in doubt, append, or carry a shared key and join deliberately.
- **Testing only the happy branch.** Your test data must include one item per branch plus one item for the fallback, or you have tested a demo, not a router.

## Recap checklist

- [ ] I can choose between IF, Switch, and Filter for a given decision and defend it.
- [ ] I traced one item through every branch of the lesson workflow, fallback included.
- [ ] I can explain Append versus Combine by index, and when no Merge is needed.
- [ ] My test data always includes a fallback item, starting today.

## Resources

- [n8n: IF node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/)
- [n8n: Switch node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch/)
- [n8n: Merge node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/)
- [n8n documentation home](https://docs.n8n.io/)
