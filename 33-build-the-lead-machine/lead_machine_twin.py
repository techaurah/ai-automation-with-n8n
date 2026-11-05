#!/usr/bin/env python3
"""Lesson 33 twin: the Lead Machine's brain, testable offline.

Classification, scoring (the Lesson 32 rubric), and chase selection,
implemented once in Python so the rules can be tested without the
canvas. The workflows implement the same rules; where they ever
disagree, the twin's tests are the arbiter and the canvas is fixed.
"""
import re

SAMPLE = [
    {"name": "Ayesha Khan", "email": "ayesha@example.com",
     "channel": "website form", "status": "contacted",
     "updated": "2026-10-28",
     "message": "Tooth pain, need an emergency appointment tomorrow"},
    {"name": "Tom Lee", "email": "tom@example.com",
     "channel": "instagram", "status": "contacted",
     "updated": "2026-11-04",
     "message": "How much is whitening?"},
    {"name": "Maria Gomez", "email": "maria@example.com",
     "channel": "email", "status": "new", "updated": "2026-11-05",
     "message": "Just researching clinics for now"},
]


def classify(message):
    m = message.lower()
    if re.search(r"unacceptable|disgrace|manager|lawyer|refund", m):
        return "complaint"
    if re.search(r"book|appointment|emergency|pain|reschedule", m):
        return "booking"
    if re.search(r"price|cost|much|offer", m):
        return "pricing"
    return "other"


def score(lead):
    s = 0
    cat = classify(lead["message"])
    if cat == "booking":
        s += 40
    elif cat == "pricing":
        s += 25
    m = lead["message"].lower()
    if re.search(r"pain|emergency|broken|swollen", m):
        s += 25
    if re.search(r"today|tomorrow|monday|tuesday|wednesday|thursday|friday", m):
        s += 15
    if lead.get("email"):
        s += 10
    if lead.get("channel") not in (None, "unknown"):
        s += 10
    band = "hot" if s >= 65 else "warm" if s >= 40 else "nurture"
    return s, band


def due_chases(leads, today="2026-11-05"):
    out = []
    for lead in leads:
        if lead["status"] == "contacted" and lead["updated"] <= "2026-11-02":
            out.append(lead["name"])
    return out


for lead in SAMPLE:
    s, band = score(lead)
    print(f"{lead['name']}: {classify(lead['message'])}, score {s}, {band}")
assert score(SAMPLE[0]) == (100, "hot")
assert score(SAMPLE[1]) == (45, "warm")
assert due_chases(SAMPLE) == ["Ayesha Khan"]
print("rubric, classifier, and chaser agree with the lesson text")
