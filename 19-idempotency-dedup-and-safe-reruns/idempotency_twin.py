#!/usr/bin/env python3
"""Lesson 19 twin: idempotent intake, proven by replay.

The same webhook delivery arrives three times (a retry, a double
click, a provider resend). The handler keys each event, checks the
register before acting, and the side effect (creating the lead)
happens exactly once. Replays are answered, not re-executed.
"""
import hashlib
import json

REGISTER = {}
OUTBOX = []


def key_for(event):
    raw = f"{event['email'].strip().lower()}|{event['message_id']}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def handle(event):
    key = key_for(event)
    if key in REGISTER:
        return f"duplicate delivery, answered from register: {key}"
    REGISTER[key] = {"email": event["email"], "status": "created"}
    OUTBOX.append(f"welcome email to {event['email']}")
    return f"created lead and queued welcome: {key}"


EVENT = {"email": "Ayesha@Example.com", "message_id": "msg-1001",
         "name": "Ayesha Khan"}
for attempt in range(3):
    print(f"delivery {attempt + 1}:", handle(EVENT))

assert len(REGISTER) == 1 and len(OUTBOX) == 1, (REGISTER, OUTBOX)
print(json.dumps(REGISTER, indent=2))
print("three deliveries, one lead, one email: idempotency holds")
