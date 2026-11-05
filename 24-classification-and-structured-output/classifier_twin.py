#!/usr/bin/env python3
"""Lesson 24 twin: classification with a contract.

Two classifiers, one contract: the label is one of a fixed set, with
a confidence, or the ticket is escalated. The rule-based stand-in
runs offline; the workflow's Text Classifier node (model-backed)
must produce the same shape, and the validator below is the exact
check a downstream router should apply to either.
"""

LABELS = {"booking", "pricing", "complaint", "other"}


def validate(ticket):
    assert ticket["label"] in LABELS, ticket
    assert 0.0 <= ticket["confidence"] <= 1.0, ticket
    if ticket["confidence"] < 0.6:
        assert ticket["label"] == "other", "low confidence must escalate"
    return True


def classify_rules(text):
    t = text.lower()
    if any(w in t for w in ("unacceptable", "disgrace", "lawyer")):
        return {"label": "complaint", "confidence": 0.9}
    if any(w in t for w in ("book", "appointment", "emergency")):
        return {"label": "booking", "confidence": 0.85}
    if any(w in t for w in ("price", "cost", "much")):
        return {"label": "pricing", "confidence": 0.8}
    return {"label": "other", "confidence": 0.3}


TESTS = ["Need an emergency appointment tomorrow",
         "How much is whitening?",
         "This is unacceptable, I want the manager",
         "Do you validate parking?"]
for t in TESTS:
    r = classify_rules(t)
    validate(r)
    print(f"{t!r} -> {r}")
print("contract holds on every test, including the escalated one")
