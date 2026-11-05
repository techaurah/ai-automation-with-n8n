#!/usr/bin/env python3
"""Lesson 34: the shipping gate for the Lead Machine.

Runs the capstone's non-negotiables as checks over Lesson 33's
files: workflows structurally valid, no placeholder table or
credential references left in the production copies, and the
twin's rules still passing when imported. Exit nonzero on any
failure: a gate that cannot fail is a decoration.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L33 = os.path.join(os.path.dirname(HERE), "33-build-the-lead-machine")
FILES = ["workflow-intake.json", "workflow-followup.json",
         "workflow-digest.json"]

failures = []
for name in FILES:
    path = os.path.join(L33, name)
    with open(path) as f:
        raw = f.read()
    wf = json.loads(raw)
    names = [n["name"] for n in wf["nodes"]]
    if len(names) != len(set(names)):
        failures.append(f"{name}: duplicate node names")
    # Placeholders are correct in the course's teaching copies and a
    # blocker in YOUR production copies: this check runs on your
    # fork's exported files, where SELECT_ must be gone.
    if "SELECT_" in raw and os.environ.get("COURSE_COPY") != "1":
        failures.append(f"{name}: placeholder references remain")

twin = subprocess.run(
    [sys.executable, os.path.join(L33, "lead_machine_twin.py")],
    capture_output=True, text=True)
if twin.returncode != 0:
    failures.append("lead_machine_twin.py failed its assertions")

for f_ in failures:
    print("BLOCKED:", f_)
print("shipping gate:", "PASS" if not failures else "FAIL")
sys.exit(1 if failures else 0)
