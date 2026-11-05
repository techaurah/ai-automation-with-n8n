#!/usr/bin/env python3
"""Lesson 27 twin: the approval state machine and output checks.

An agent proposes an action. Guardrail checks screen the proposal.
A human approves or rejects. Only then does the action run, and
every transition is recorded. This twin is that machine, small
enough to audit in one reading.
"""
import re

PENDING, APPROVED, REJECTED, BLOCKED = "pending", "approved", "rejected", "blocked"
LOG = []

PII_PATTERNS = {
    "card number": re.compile(r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b"),
    "email in public text": re.compile(r"\b[\w.]+@[\w.]+\.[a-z]+\b"),
}


def guardrail(text):
    hits = [name for name, pat in PII_PATTERNS.items() if pat.search(text)]
    return hits


def propose(action_id, text):
    hits = guardrail(text)
    state = BLOCKED if hits else PENDING
    LOG.append((action_id, state, hits or "clean"))
    return state


def decide(action_id, approved):
    state = APPROVED if approved else REJECTED
    LOG.append((action_id, state, "human decision"))
    return state


def execute(action_id):
    states = [s for a, s, _ in LOG if a == action_id]
    assert states[-1] == APPROVED, f"{action_id} not approved: {states}"
    return f"executed {action_id}"


p1 = propose("email-1", "Hi Ayesha, your appointment is confirmed.")
print("email-1:", p1)
decide("email-1", True)
print(execute("email-1"))

p2 = propose("post-1", "Contact us at ayesha@example.com for details.")
print("post-1:", p2, "(guardrail blocked the public email)")

try:
    execute("post-1")
    raise SystemExit("ERROR: a blocked action executed")
except AssertionError as e:
    print("execution refused, correctly:", e)
print("propose, screen, approve, execute: no step skippable")
