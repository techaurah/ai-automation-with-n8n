# Lesson 04: Solution notes

In the twin, the fix is one line: `item.get("channel", "unknown")`, plus treating an empty message as zero words naturally falls out of `len("".split())` being 0 in Python (note: in JavaScript, `" ".split(' ')` behaves differently, which is why the workflow's cleaner filters empty parts). In the workflow's per-item Code node, the equivalent is `($json.channel || 'unknown')`.

The sentence worth writing: the twin usually wins for spotting data problems, because running it prints every intermediate value with no clicking; the workflow wins for seeing the shape of the whole system at a glance. Professional builders keep both views, which is the entire reason this course ships twins.

**What to notice.** The ugly item was not an edge case; it was Tuesday. Real intake data always contains the record with the missing field, and pipelines are judged on that record, not the tidy ones.
