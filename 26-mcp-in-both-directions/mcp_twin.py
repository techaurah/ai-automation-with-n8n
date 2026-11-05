#!/usr/bin/env python3
"""Lesson 26 twin: MCP, shown as the messages it actually is.

The Model Context Protocol is JSON-RPC between an AI app (client)
and a tool server. This twin prints a tools/list exchange and a
tools/call exchange for a tiny clinic server, so the protocol is
demystified before n8n's two MCP nodes hide it again.
"""
import json

TOOLS = [
    {"name": "get_opening_hours",
     "description": "Return BrightSmile's opening hours for a weekday.",
     "inputSchema": {"type": "object",
                     "properties": {"weekday": {"type": "string"}},
                     "required": ["weekday"]}},
]

HOURS = {"monday": "8am to 6pm", "tuesday": "8am to 6pm",
         "wednesday": "8am to 6pm", "thursday": "8am to 6pm",
         "friday": "8am to 6pm", "saturday": "closed",
         "sunday": "closed"}


def handle(request):
    if request["method"] == "tools/list":
        return {"jsonrpc": "2.0", "id": request["id"], "result": {"tools": TOOLS}}
    if request["method"] == "tools/call":
        args = request["params"]["arguments"]
        day = args["weekday"].lower()
        text = HOURS.get(day, "unknown day")
        return {"jsonrpc": "2.0", "id": request["id"],
                "result": {"content": [{"type": "text", "text": text}]}}
    raise ValueError(request["method"])


for req in [
    {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
     "params": {"name": "get_opening_hours",
                "arguments": {"weekday": "Saturday"}}},
]:
    print("->", json.dumps(req))
    print("<-", json.dumps(handle(req)))
print("a client discovers tools, then calls them: that is all MCP is")
