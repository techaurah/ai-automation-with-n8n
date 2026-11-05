#!/usr/bin/env python3
"""Lesson 11 twin: the file pipeline in stdlib Python.

Writes a CSV of enquiries, reads it back, converts it to a summary
JSON, the same jobs the workflow does with binary data nodes.
"""
import csv
import io
import json

ROWS = [
    {"name": "Ayesha Khan", "category": "booking"},
    {"name": "Tom Lee", "category": "pricing"},
    {"name": "Maria Gomez", "category": "research"},
]

buf = io.StringIO()
writer = csv.DictWriter(buf, fieldnames=["name", "category"])
writer.writeheader()
writer.writerows(ROWS)
csv_text = buf.getvalue()

reader = csv.DictReader(io.StringIO(csv_text))
counts = {}
for row in reader:
    counts[row["category"]] = counts.get(row["category"], 0) + 1

summary = {"rows": sum(counts.values()), "by_category": counts}
print(json.dumps(summary))
assert summary == {"rows": 3, "by_category":
                   {"booking": 1, "pricing": 1, "research": 1}}
print("twin checks passed")
