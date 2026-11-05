#!/usr/bin/env python3
"""Lesson 29: probe the instance health endpoint and report plainly.

n8n serves /healthz on the editor port. This checker is the seed of
Lesson 31's monitoring: boring, explicit, and runnable from cron.
"""
import json
import sys
import urllib.request

URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5678/healthz"
try:
    with urllib.request.urlopen(URL, timeout=5) as r:
        body = json.loads(r.read().decode())
    print(f"OK {URL} -> {body}")
    sys.exit(0 if body.get("status") == "ok" else 1)
except Exception as e:
    print(f"DOWN {URL} -> {e}")
    sys.exit(2)
