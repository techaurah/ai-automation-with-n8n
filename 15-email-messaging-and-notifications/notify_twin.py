#!/usr/bin/env python3
"""Lesson 15 twin: the notification ladder, filed to an outbox.

The workflow sends through Gmail and Slack nodes once credentials
exist. The twin rehearses the identical decisions and writes the
would-be messages to an outbox list, which is also the pattern to
use while any automation is earning trust: draft first, send later.
"""
import json

ALERTS = [
    {"severity": "low", "text": "Daily digest is ready"},
    {"severity": "high", "text": "Intake workflow failed 3 times"},
    {"severity": "critical", "text": "Payments webhook returning 500"},
]
CHANNEL = {"low": "digest file", "high": "email to owner",
           "critical": "email to owner + team chat"}

outbox = []
for a in ALERTS:
    msg = {"channel": CHANNEL[a["severity"]],
           "subject": f"[{a['severity'].upper()}] {a['text']}",
           "draft_only": a["severity"] == "low"}
    outbox.append(msg)
    print(json.dumps(msg))

assert [m["channel"] for m in outbox][2].endswith("team chat")
print(f"outbox holds {len(outbox)} messages, none sent: that is the point")
