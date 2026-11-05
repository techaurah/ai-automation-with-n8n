#!/usr/bin/env python3
"""Lesson 18 twin: debugging by pinning.

A pinned input is a frozen sample you run transforms against while
you change them. This twin pins the exact item the broken workflow
receives, runs the broken mapping, shows the wrong output, then
runs the fixed mapping. Same method as the editor, no canvas.
"""

PINNED = {"body": {"enquiry": {"name": "Tom Lee",
                               "email": "tom@example.com",
                               "message": "Whitening price?"}}}


def broken_map(item):
    # The bug, faithfully reproduced: reads top-level fields that
    # live under body.enquiry in the real payload.
    return {"name": item.get("name"), "email": item.get("email")}


def fixed_map(item):
    e = item["body"]["enquiry"]
    return {"name": e["name"], "email": e["email"]}


print("broken:", broken_map(PINNED))
print("fixed: ", fixed_map(PINNED))
assert broken_map(PINNED) == {"name": None, "email": None}
assert fixed_map(PINNED)["email"] == "tom@example.com"
print("pin, reproduce, fix, verify: the whole method in four lines")
