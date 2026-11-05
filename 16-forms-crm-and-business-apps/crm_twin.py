#!/usr/bin/env python3
"""Lesson 16 twin: form-to-CRM intake with deduplication.

The workflow takes a form submission, normalises it, computes a
dedupe key, and creates the CRM record only if the key is new.
This twin rehearses the same decisions against a JSON store.
"""
import hashlib
import json

STORE = {}


def dedupe_key(name, email):
    raw = f"{name.strip().lower()}|{email.strip().lower()}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def intake(form):
    lead = {"name": form["Name"].strip(),
            "email": form["Email"].strip().lower(),
            "message": form.get("Message", "")}
    key = dedupe_key(lead["name"], lead["email"])
    if key in STORE:
        return f"duplicate, skipped: {lead['email']}"
    STORE[key] = lead
    return f"created: {lead['email']}"


print(intake({"Name": " Ayesha Khan ", "Email": "Ayesha@Example.com",
              "Message": "Emergency appointment"}))
print(intake({"Name": "Ayesha Khan", "Email": "ayesha@example.com",
              "Message": "Submitting again, sorry"}))
print(intake({"Name": "Tom Lee", "Email": "tom@example.com",
              "Message": "Whitening price?"}))
assert len(STORE) == 2
print(json.dumps(STORE, indent=2))
print("dedupe verified: same person, messier second form, one record")
