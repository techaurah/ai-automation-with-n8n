#!/usr/bin/env python3
"""Lesson 13: scan workflow JSON for secrets that should not be there.

Walks every workflow JSON in this repository and flags values that
look like credentials pasted into parameters: long token-shaped
strings, bearer headers, and keys named like secrets. It is a
tripwire, not a guarantee: a clean scan is necessary, not sufficient.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUSPECT_KEYS = re.compile(r"(api[_-]?key|token|secret|password|authorization)",
                          re.IGNORECASE)
TOKEN_SHAPE = re.compile(r"\b(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|"
                         r"xox[baprs]-[A-Za-z0-9-]{10,})\b")


def walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        yield path, obj


def scan_file(path):
    findings = []
    with open(path) as f:
        wf = json.load(f)
    for node in wf.get("nodes", []):
        for key_path, value in walk(node.get("parameters", {})):
            last = key_path.split(".")[-1]
            if SUSPECT_KEYS.search(last) and len(value) > 12 \
                    and "={{ " not in value and "SELECT_" not in value \
                    and "REPLACE" not in value:
                findings.append(f"{node['name']}: parameter {last} "
                                "holds a long literal value")
            if TOKEN_SHAPE.search(value):
                findings.append(f"{node['name']}: value at {key_path} "
                                "matches a known token shape")
    return findings


total = 0
for dirpath, _dirs, files in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for name in files:
        if name.endswith(".json") and "workflow" in name:
            path = os.path.join(dirpath, name)
            for finding in scan_file(path):
                total += 1
                print(f"{os.path.relpath(path, ROOT)}: {finding}")
print(f"scan complete: {total} finding(s)")
sys.exit(1 if total else 0)
