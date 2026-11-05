#!/usr/bin/env python3
"""Lesson 00 setup checker for AI Automation with n8n.

Run: python3 check_environment.py
Checks only what this course actually needs. Nothing here phones home,
needs a credential, or changes your machine.
"""
import json
import os
import shutil
import socket
import sys

OK, WARN, FAIL = "OK  ", "WARN", "FAIL"


def report(level, what, detail=""):
    print(f"[{level}] {what}" + (f": {detail}" if detail else ""))
    return level != FAIL


def main():
    all_ok = True

    version = sys.version_info
    all_ok &= report(OK if version >= (3, 11) else FAIL,
                     f"Python {version.major}.{version.minor}.{version.micro}",
                     "course twin scripts need Python 3.11 or newer")

    docker = shutil.which("docker")
    compose = shutil.which("docker-compose") or docker
    if docker:
        report(OK, "Docker found", docker + " (the recommended n8n path)")
    else:
        report(WARN, "Docker not found",
               "fine if you use an n8n Cloud trial; needed for self-hosting")

    node = shutil.which("node")
    if node:
        report(OK, "Node.js found", "only needed for the optional npm route")
    else:
        report(WARN, "Node.js not found", "only matters for the npm route")

    sock = socket.socket()
    try:
        sock.bind(("127.0.0.1", 5678))
        report(OK, "Port 5678 is free", "the port the n8n editor uses")
    except OSError:
        report(WARN, "Port 5678 is in use",
               "something is already listening; it may be n8n itself")
    finally:
        sock.close()

    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    readme = os.path.join(root, "README.md")
    all_ok &= report(OK if os.path.exists(readme) else FAIL,
                     "Course README found", "you are inside the course repo")

    sample = os.path.join(root, "03-the-editor-and-your-first-workflow",
                          "workflow.json")
    if os.path.exists(sample):
        with open(sample) as f:
            wf = json.load(f)
        names = [n["name"] for n in wf["nodes"]]
        all_ok &= report(OK, "Sample workflow parses",
                         f"{wf['name']}: {len(names)} nodes")
    else:
        report(WARN, "Sample workflow not found yet", "clone the full repo")

    print()
    print("Setup check finished.", "All essentials OK." if all_ok
          else "Fix the FAIL lines before Lesson 01.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
