#!/usr/bin/env python3
"""Lesson 22 twin: tools as functions with contracts.

An agent picks tools from their names and descriptions, and calls
them with arguments matching a schema. This twin registers two
Python functions as tools, prints the catalogue the way a model
sees it, and dispatches two calls through the same contract the
n8n workflow exposes via its Workflow Tool sub-workflow.
"""
import json

TOOLS = {}


def tool(name, description, schema):
    def deco(fn):
        TOOLS[name] = {"description": description, "schema": schema,
                       "fn": fn}
        return fn
    return deco


@tool("get_price",
      "Return the price in GBP for a named BrightSmile treatment. "
      "Use for any price question.",
      {"treatment": "string"})
def get_price(treatment):
    return {"whitening": 299, "checkup": 45, "hygiene": 65}[
        treatment.lower()]


@tool("open_slots",
      "Return the count of free emergency slots on a weekday name. "
      "Use for availability questions.",
      {"weekday": "string"})
def open_slots(weekday):
    return {"monday": 3, "tuesday": 0, "wednesday": 2,
            "thursday": 1}.get(weekday.lower(), 0)


catalogue = {n: {"description": t["description"], "schema": t["schema"]}
             for n, t in TOOLS.items()}
print(json.dumps(catalogue, indent=2))

for name, args in [("get_price", {"treatment": "whitening"}),
                   ("open_slots", {"weekday": "Tuesday"})]:
    result = TOOLS[name]["fn"](**args)
    print(f"{name}({args}) -> {result}")
    assert result in (299, 0)
print("catalogue, contracts, dispatch: a tool is an interface")
