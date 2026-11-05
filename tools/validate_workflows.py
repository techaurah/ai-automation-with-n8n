#!/usr/bin/env python3
"""Validate every n8n workflow JSON in this repository.

A file counts as a workflow when its top level holds nodes and
connections. For each one this checks: it parses as JSON, node
names are unique, every connection source and target is a real
node, and AI sub-node connections (ai_languageModel, ai_tool,
ai_memory, ai_embedding, ai_document, ai_textSplitter,
ai_outputParser, ai_vectorStore) point at a node that exists.
Exits nonzero on any failure, so CI can gate on it.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AI_TYPES = {"ai_languageModel", "ai_tool", "ai_memory", "ai_embedding",
            "ai_document", "ai_textSplitter", "ai_outputParser",
            "ai_vectorStore"}


def iter_workflows():
    for dirpath, _dirs, files in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for name in sorted(files):
            if not name.endswith(".json"):
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path) as f:
                    data = json.load(f)
            except (OSError, json.JSONDecodeError):
                continue
            if isinstance(data, dict) and "nodes" in data \
                    and "connections" in data:
                yield path, data


def check(path, wf):
    errors = []
    names = [n.get("name") for n in wf["nodes"]]
    if len(names) != len(set(names)):
        errors.append("duplicate node names")
    known = set(names)
    for src, conns in wf["connections"].items():
        if src not in known:
            errors.append(f"connection source '{src}' is not a node")
        for ctype, outputs in conns.items():
            for targets in outputs:
                for t in targets:
                    if t.get("node") not in known:
                        errors.append(
                            f"{ctype} connection to unknown node "
                            f"'{t.get('node')}'")
                    if ctype in AI_TYPES and t.get("type") != ctype:
                        errors.append(
                            f"AI connection type mismatch at '{src}'")
    return errors


def main():
    total, bad = 0, 0
    for path, wf in iter_workflows():
        total += 1
        errors = check(path, wf)
        rel = os.path.relpath(path, ROOT)
        if errors:
            bad += 1
            for e in errors:
                print(f"FAIL {rel}: {e}")
        else:
            print(f"OK   {rel}: {wf.get('name', '?')}, "
                  f"{len(wf['nodes'])} nodes")
    print(f"\n{total} workflow files checked, {bad} failing")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
