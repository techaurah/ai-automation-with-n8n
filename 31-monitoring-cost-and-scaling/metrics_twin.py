#!/usr/bin/env python3
"""Lesson 31: reading execution data like an operator.

Consumes a sample of execution records (the shape an export or the
n8n API gives you) and reports the four numbers this lesson runs an
estate on: volume, failure rate per workflow, slowest runs, and
where executions concentrate. Your estate's real numbers come from
your instance; the method is what transfers.
"""
import json
import os
from collections import defaultdict

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "executions_sample.json")) as f:
    runs = json.load(f)

by_wf = defaultdict(list)
for r in runs:
    by_wf[r["workflow"]].append(r)

print(f"{'workflow':28} {'runs':>4} {'fail%':>6} {'avg s':>7}")
for name, rs in sorted(by_wf.items()):
    fails = sum(1 for r in rs if r["status"] == "error")
    avg = sum(r["seconds"] for r in rs) / len(rs)
    print(f"{name:28} {len(rs):>4} {100 * fails / len(rs):>5.0f}% {avg:>7.1f}")

slowest = max(runs, key=lambda r: r["seconds"])
print(f"\nslowest run: {slowest['workflow']} at {slowest['seconds']}s")
print("decisions this table drives: retry policy (Lesson 17), loader")
print("schedule (off-peak), and which workflow earns an error budget")
