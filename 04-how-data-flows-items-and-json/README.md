# Lesson 04: How data flows: items, JSON, and paired items

**Time:** about 60 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 03 · **You need:** Your instance, and Python for the twin script.

One idea powers all of n8n, and it fits in a sentence: data travels as a list of **items**, each item is one JSON object, and every node receives the whole list, does its job per item, and passes a list on. Builders who internalise this write workflows that compose. Builders who miss it fight the tool for months, usually while saying the words "but it worked with one record". This lesson builds the model three ways: in prose, in a workflow, and in a Python twin.

## Items: the only data shape there is

An **item** is a JSON object: `{"name": "Tom Lee", "channel": "instagram"}`. A node's input is an array of items, one or one thousand. A trigger that receives one form submission produces one item; a spreadsheet node reading forty rows produces forty items; an HTTP node fetching a list produces one item per element only if it is told to split the response (Lesson 10), a detail that bites everyone once.

Nodes declare their relationship to the list. Most process **each item independently**: the Edit Fields node adds a field to every item it receives, which is why Lesson 03's exercise worked on two enquiries without extra wiring. Some nodes **combine** the list (Aggregate, and the Summarise Code node in this lesson's workflow). Some **restructure** it (Split Out turns one item holding an array into many items; Aggregate does the reverse). When a workflow misbehaves, the first question is always: how many items, of what shape, at this node?

## JSON: the contract between nodes

Because items are JSON, the contract between two nodes is a shape: field names, types, nesting. The workflow in this lesson cleans three messy enquiries (stray spaces, shouting case, inconsistent channel names) into one canonical shape. That cleaning step is not cosmetic. Downstream, a router will test `channel` against exact values; "INSTAGRAM" and "instagram" are different strings, and the router does not forgive.

Nested data is where beginners drown. A webhook body like `{"body": {"enquiry": {...}}}` means the name lives at `$json.body.enquiry.name`, and a node configured for `$json.name` finds nothing and, worse, often fails silently with an empty value rather than an error. The defence is Lesson 03's habit: look at the actual output, in JSON view, before configuring the next node.

## Paired items: how n8n remembers where data came from

When a node transforms items, n8n tracks which input item each output item came from. That bookkeeping is **paired items**, and it is what lets a later node reach back, in an expression, to an earlier node's data for the same record (Lesson 05 uses this). Most of the time pairing just works. It breaks in predictable places: Code nodes that build brand-new items without copying the input, Merge nodes combining branches, and aggregations that collapse many items into one. When an expression says it cannot resolve a paired item, the cause is almost always a node in between that discarded the chain. The fix is to carry the fields you need forward explicitly, which is good design anyway: data a node needs should arrive in its input, visibly.

## The twin: the same model with no canvas

`items_twin.py` performs this lesson's transforms in plain Python: a list of dictionaries in, a list of dictionaries out, one `clean()` function applied per item, then a summary over the whole list. It is the workflow with the canvas removed, and it exists to prove the model is not n8n trivia; it is the standard data-pipeline shape (a map, then a reduce) that recurs in every automation tool and most backend code. When a workflow confuses you this course long, ask what the twin would look like. If you cannot write the twin, the workflow is probably overcomplicated.

## Run it

Run the twin first:

```bash
cd 04-how-data-flows-items-and-json
python3 items_twin.py
```

Then import `workflow.json`, run it, and compare node by node: Raw enquiries emits three items, Clean each item (note its mode: run once for each item, so `$json` is the current item) emits three cleaned items, and Summarise collapses them to one. The twin's assertions (channels sorted, first name extracted) describe exactly what the workflow's outputs should show.

## Common failures

- **Assuming one item.** The workflow works in testing with one record and corrupts data at forty. Always test transforms with at least three items, including an ugly one.
- **Losing fields in a Code node.** Returning `{ json: { newField } }` discards everything upstream sent. Spread the input (`...$json`) unless dropping fields is the deliberate point of the node.
- **Case and whitespace drift.** "Instagram", "INSTAGRAM ", and "instagram" are three different channels to a router. Normalise at the boundary, once, like this lesson's cleaning step.
- **Reaching for nested fields that are not there.** An empty result is often a wrong path (`$json.name` versus `$json.body.name`), not missing data. Check the JSON view before blaming the source.

## Recap checklist

- [ ] I can state the items model in one sentence and give a map and a reduce example.
- [ ] I ran the twin and matched its output against the workflow, node by node.
- [ ] I know what paired items are and two places they break.
- [ ] I can find the real field path for any value in the JSON output view.

## Resources

- [n8n: data structure](https://docs.n8n.io/data/data-structure/)
- [n8n: Code node](https://docs.n8n.io/code/code-node/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
