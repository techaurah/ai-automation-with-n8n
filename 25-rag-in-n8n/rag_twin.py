#!/usr/bin/env python3
"""Lesson 25 twin: retrieval over clinic documents, stdlib only.

Chunks the documents, scores chunks against the question by term
overlap with a small ranking function, and answers extractively,
citing the chunk used. This is RAG's shape with the embeddings
replaced by counting, so every step is inspectable. The workflow
does the same job with real embeddings and a vector store.
"""
import re
from collections import Counter

DOCS = {
    "prices.txt": "Teeth whitening costs GBP 299 for a 60 minute "
                  "session. A checkup costs GBP 45. Hygiene polish "
                  "costs GBP 65.",
    "hours.txt": "The clinic opens 8am to 6pm Monday to Friday. "
                 "Emergency slots run Monday to Thursday mornings. "
                 "The clinic is closed on Sundays.",
    "policies.txt": "Cancellations need 24 hours notice. A missed "
                    "appointment fee of GBP 25 applies. New patients "
                    "should arrive 10 minutes early.",
}


def chunk(text, size=1):
    sentences = re.split(r"(?<=[.!?]) +", text)
    return [s.strip() for s in sentences if s.strip()]


CHUNKS = [(name, c) for name, text in DOCS.items() for c in chunk(text)]


def retrieve(question, top=1):
    q = Counter(re.findall(r"[a-z]+", question.lower()))
    scored = []
    for name, c in CHUNKS:
        words = Counter(re.findall(r"[a-z]+", c.lower()))
        score = sum((q & words).values())
        scored.append((score, name, c))
    scored.sort(reverse=True)
    return scored[:top]


def answer(question):
    score, name, text = retrieve(question)[0]
    if score == 0:
        return "No clinic document covers that; the team will confirm."
    return f"{text} [source: {name}]"


print(answer("How much is teeth whitening?"))
print(answer("When are emergency slots?"))
print(answer("Do you offer payment plans?"))
assert "299" in answer("How much is teeth whitening?")
assert "confirm" in answer("Do you offer payment plans?")
print("retrieve, answer, cite: and abstain when retrieval is empty")
