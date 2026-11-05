#!/usr/bin/env python3
"""Lesson 07 twin: one transform, two notations.

The workflow cleans an enquiry with Edit Fields, then again with a
Code node, so the outputs can be compared. This script is the Code
node version, checkable offline.
"""


def clean(item):
    name = item["name"].strip()
    return {
        "first_name": name.split(" ")[0],
        "name": name.title(),
        "channel": item.get("channel", "unknown").strip().lower(),
        "urgent": any(w in item["message"].lower()
                      for w in ("pain", "emergency", "broken")),
        "summary": item["message"][:40].rstrip() + "...",
    }


sample = {"name": "  ayesha KHAN ", "channel": " Website Form ",
          "message": "Tooth pain since Monday, getting worse"}
print(clean(sample))
assert clean(sample)["urgent"] is True
print("twin checks passed")
