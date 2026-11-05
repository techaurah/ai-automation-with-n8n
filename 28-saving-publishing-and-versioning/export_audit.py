#!/usr/bin/env python3
"""Lesson 28: audit a folder of exported workflow JSON files.

A release habit in script form: for every export, report the
workflow name, node count, whether it still carries placeholder
values (the SELECT_ markers this course ships deliberately), and
whether any node type is on your watchlist. Exports are how
workflows move between instances and into git, so exports are
what you audit.
"""
import json
import os
import sys

WATCHLIST = {"n8n-nodes-base.executeCommand",
             "n8n-nodes-base.readWriteFile"}


def audit(path):
    with open(path) as f:
        wf = json.load(f)
    text = json.dumps(wf)
    nodes = wf.get("nodes", [])
    flags = []
    if "SELECT_" in text or "REPLACE" in text:
        flags.append("placeholders present (expected in course files, "
                     "a release blocker in yours)")
    risky = [n["name"] for n in nodes if n["type"] in WATCHLIST]
    if risky:
        flags.append(f"watchlist nodes: {', '.join(risky)}")
    return wf.get("name", "?"), len(nodes), flags


def main(root):
    bad = 0
    for dirpath, _d, files in os.walk(root):
        if ".git" in dirpath:
            continue
        for name in sorted(files):
            if "workflow" in name and name.endswith(".json"):
                path = os.path.join(dirpath, name)
                wf_name, count, flags = audit(path)
                rel = os.path.relpath(path, root)
                print(f"{rel}: '{wf_name}', {count} nodes")
                for flag in flags:
                    print(f"   - {flag}")
    print("audit complete")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else
         os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
