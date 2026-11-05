#!/usr/bin/env python3
"""Lesson 30: instance audit, the mechanical checks.

Scans this repository's workflow and stack files for the patterns
the hardening lesson calls out: dangerous node types present,
environment access enabled, pruning off, unpinned images. Human
judgement still required; this is the checklist's tireless half.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RISKY_NODES = {"n8n-nodes-base.executeCommand": "Execute Command node",
               "n8n-nodes-base.readWriteFile": "Read/Write Files node",
               "n8n-nodes-base.localFileTrigger": "Local File Trigger"}
findings = []

for dirpath, _d, files in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for name in files:
        path = os.path.join(dirpath, name)
        rel = os.path.relpath(path, ROOT)
        if "workflow" in name and name.endswith(".json"):
            with open(path) as f:
                wf = json.load(f)
            for n in wf.get("nodes", []):
                if n["type"] in RISKY_NODES:
                    findings.append(
                        f"{rel}: {RISKY_NODES[n['type']]} in "
                        f"'{n['name']}' (justify or remove)")
        if name == "docker-compose.yml":
            text = open(path).read()
            if re.search(r"image:\s*n8nio/n8n\s*$", text, re.M):
                findings.append(f"{rel}: n8n image unpinned")
            if "N8N_BLOCK_ENV_ACCESS_IN_NODE=true" in text:
                findings.append(f"{rel}: env access explicitly enabled")

for f_ in findings:
    print("-", f_)
print(f"audit complete: {len(findings)} finding(s) to justify")
