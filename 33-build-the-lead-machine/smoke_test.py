#!/usr/bin/env python3
"""Lesson 33 smoke test: validates the Lead Machine's workflow files.

CI runs every smoke_test.py in the repo. This one checks the three
production workflows parse, keep unique node names, and wire every
connection to a real node, the same guarantees tools/ enforces
repo-wide, scoped to the capstone.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["workflow-intake.json", "workflow-followup.json",
         "workflow-digest.json"]

for name in FILES:
    with open(os.path.join(HERE, name)) as f:
        wf = json.load(f)
    names = [n["name"] for n in wf["nodes"]]
    assert len(names) == len(set(names)), f"{name}: duplicate names"
    for src, conns in wf.get("connections", {}).items():
        assert src in names, f"{name}: unknown source {src}"
        for outputs in conns.values():
            for targets in outputs:
                for t in targets:
                    assert t["node"] in names, f"{name}: bad target"
    print(f"{name}: valid, {len(names)} nodes")
print("Lead Machine workflows: structurally sound")
