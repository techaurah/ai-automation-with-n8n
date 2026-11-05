# Lesson 05: Expressions and mapping: moving data between nodes without code

**Time:** about 55 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 04 · **You need:** Your instance.

Between the no-code promise and the Code node sits the layer you will use most: **expressions**, small pieces of JavaScript inside double curly braces that pull values from the current item, from earlier nodes, and from n8n itself. This lesson teaches the expression grammar, the drag-and-drop mapping that generates most expressions for you, and the judgment call this course cares about: when an expression is the right tool and when the honest answer is a Code node.

## The grammar in five minutes

An expression lives inside `{{ }}` in a field, usually prefixed with `=` so n8n treats the field as an expression rather than literal text. Inside, `$json` is the current item, so `{{ $json.first }} {{ $json.last }}` builds a full name. Arithmetic works (`$json.price * $json.qty`), conditions work (`$json.member ? 'member' : 'standard'`), and string methods work, because it is JavaScript. Beyond `$json`, three references matter daily: `$('Node Name').item.json.field` reaches back to an earlier node's output for the paired item (Lesson 04's pairing, made visible), `$now` is the current date and time as a Luxon object with formatting methods, and `$execution.id` identifies the current run, which Lesson 19 turns into an idempotency tool.

In the editor you rarely type these from scratch. Dragging a field from the input pane into a parameter writes the expression for you, correctly, including the path through nested objects. Type expressions when dragging is awkward (arithmetic, conditions), and always read what the drag produced before running.

## Mapping: the real skill expressions serve

**Mapping** is deciding which input field becomes which output field, and it is where integrations actually succeed or fail. The workflow in this lesson maps raw orders to a billing shape: a joined customer name, a computed total, a member discount, a label. Notice what the Edit Fields node could not do: `due` depends on `total` and `discount`, which are created in that same node, and expressions in one node cannot see each other's fresh outputs. So a small Code node finishes the job. That boundary (expressions see inputs, not siblings) is not a bug to resent; it is the rule that keeps nodes independently testable, and designing around it is a core n8n skill.

## Dates, the honest hard part

Dates in expressions come as strings from APIs, as Luxon objects from `$now`, and as Unix timestamps from systems that should know better. The rules that keep you sane: convert explicitly with `DateTime.fromISO(...)` or `.toFormat('yyyy-MM-dd')` rather than hoping a string sorts correctly, do comparisons on parsed dates, and remember the instance timezone from Lesson 02 when a schedule and a date expression meet. The exercise makes you format an appointment date three ways; in production you will do it weekly.

## Expression or Code node: the judgment call

Use an expression when the transform fits on one line and a reader can verify it at a glance: rename, join, multiply, pick between two labels. Use a Code node when there is a loop, a lookup, error handling, or more than about two operations chained, because a five-function expression is code that has escaped its editor, untestable and undebuggable. The twin principle applies here too: the workflow's mappings are mirrored in `expressions_twin.py`, and any mapping you cannot reproduce in the twin in a minute is too clever for an expression.

## Run it

Import `workflow.json` and run it. In the Edit Fields node, open each assignment and read the resolved values in the output pane: Ayesha Khan, total 299, discount 29.9, label member; Tom Lee, total 135, discount 0, label standard. Then compare with the twin:

```bash
cd 05-expressions-and-mapping
python3 expressions_twin.py
```

The twin adds `due` (269.1 and 135), which the final Code node computes in the workflow. Same numbers, two notations: that agreement is the lesson.

## Common failures

- **The missing equals sign.** Without the leading `=`, the field holds the literal text `{{ $json.first }}` and your workflow cheerfully sends curly braces to a customer. If output shows braces, this is why.
- **Referencing a sibling field.** An expression that uses a field created in the same Edit Fields node resolves against the input, finds nothing, and yields empty. Compute it in the next node, like this lesson's `due`.
- **Reaching back without pairing.** `$('Some Node').item` fails after a node that broke the paired chain (Lesson 04). Carry needed fields forward instead of reaching across three nodes.
- **String dates sorted as text.** `2026-9-1` sorts after `2026-10-1` alphabetically. Parse dates before comparing or sorting them, every time.

## Recap checklist

- [ ] I can write and read expressions using $json, an earlier node, and $now.
- [ ] I know expressions in a node see its input, not its own new fields.
- [ ] I matched the workflow's mapped output against the Python twin exactly.
- [ ] I can state the expression versus Code node rule and defend a choice.

## Resources

- [n8n: expressions](https://docs.n8n.io/code/expressions/)
- [n8n: Edit Fields node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
