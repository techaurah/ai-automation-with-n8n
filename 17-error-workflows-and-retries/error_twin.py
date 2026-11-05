#!/usr/bin/env python3
"""Lesson 17 twin: what a good error alert contains.

Given a failed execution's essentials, build the alert a human can
act on at 3am: what workflow, which node, what error, which record
was being processed, and where to look. The workflow's error
workflow builds the same payload from the Error Trigger's data.
"""

FAILED = {
    "workflow": "Lead Machine intake",
    "node": "Create lead in CRM table",
    "error": "Airtable: rate limit exceeded (429)",
    "execution_id": "88412",
    "record": {"email": "ayesha@example.com", "source": "website form"},
}


def build_alert(f):
    lines = [
        f"FAILED: {f['workflow']}",
        f"Node: {f['node']}",
        f"Error: {f['error']}",
        f"Record: {f['record']}",
        f"Execution: {f['execution_id']} (open it, do not guess)",
        "First move: check whether the record was written before the "
        "failure. Rerunning blind is how duplicates are born.",
    ]
    return "\n".join(lines)


alert = build_alert(FAILED)
print(alert)
assert "88412" in alert and "rate limit" in alert
print("alert contains everything the runbook asks for")
