#!/usr/bin/env python3
"""Lesson 01: workflow, agent, or code? A tiny decision scorer.

Each scenario is scored on three questions from the lesson:
  fixed_steps: does the job always follow the same steps? (0 or 1)
  judgement:   does a step need open-ended judgement? (0 or 1)
  volume:      rough runs per month (int)
The scorer is a teaching toy: it prints the reasoning, not just a verdict.
"""

SCENARIOS = [
    {"name": "New enquiry gets a drafted reply and a spreadsheet row",
     "fixed_steps": 1, "judgement": 0, "volume": 300},
    {"name": "Support inbox: read each message, decide what it needs, act",
     "fixed_steps": 0, "judgement": 1, "volume": 800},
    {"name": "Nightly price recalculation over 40,000 products",
     "fixed_steps": 1, "judgement": 0, "volume": 1200000},
    {"name": "Chase overdue invoices with a polite, varied email",
     "fixed_steps": 1, "judgement": 1, "volume": 60},
]


def decide(s):
    if s["volume"] > 100000 and s["judgement"] == 0:
        return "code", "fixed steps at very high volume: code is cheaper and testable"
    if s["judgement"] and not s["fixed_steps"]:
        return "agent in a workflow", "open-ended judgement inside a controlled frame"
    if s["judgement"] and s["fixed_steps"]:
        return "workflow with an AI step", "fixed path, one fuzzy decision: keep the path, add a model step"
    return "workflow", "fixed steps, no fuzzy decision: a plain workflow, no model needed"


for s in SCENARIOS:
    kind, why = decide(s)
    print(f"{s['name']}\n  -> {kind}: {why}")
