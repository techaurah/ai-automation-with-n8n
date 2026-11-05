#!/usr/bin/env python3
"""Capstone smoke test: every workflow file in this folder is valid.

Mirrors the repo-wide validator in tools/: parses as JSON, node
names unique, every connection target exists. CI runs this file.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF_DIR = os.path.join(HERE, "..", "workflows")


def check(path):
    with open(path) as f:
        wf = json.load(f)
    names = [n["name"] for n in wf["nodes"]]
    assert len(names) == len(set(names)), f"{path}: duplicate node names"
    for src, conns in wf.get("connections", {}).items():
        assert src in names, f"{path}: connection from unknown node {src}"
        for outputs in conns.values():
            for targets in outputs:
                for t in targets:
                    assert t["node"] in names,                         f"{path}: connection to unknown node {t['node']}"


files = [f for f in os.listdir(WF_DIR) if f.endswith(".json")]
assert files, "no workflow files found"
for name in files:
    check(os.path.join(WF_DIR, name))
print(f"capstone smoke: {len(files)} workflow file(s) valid")
