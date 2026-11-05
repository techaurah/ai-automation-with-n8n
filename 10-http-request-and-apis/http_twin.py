#!/usr/bin/env python3
"""Lesson 10 twin: reading an API response the way the workflow does.

Uses the recorded response in api_response.json (captured from the
free JSONPlaceholder API) so the twin runs offline. The workflow
fetches the same record live and maps it to the same shape.
"""
import json
import os

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "api_response.json")) as f:
    user = json.load(f)

contact = {
    "name": user["name"],
    "email": user["email"].lower(),
    "city": user["address"]["city"],
    "company": user["company"]["name"],
}
print(contact)
assert contact["city"] == "Gwenborough"
print("twin checks passed")
