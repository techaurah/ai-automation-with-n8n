#!/usr/bin/env python3
"""Generate the course diagram set as clean, branded SVGs.

Style: white canvas, navy (#0B1F4A) primary boxes with white text,
light blue (#E0F2FE) secondary boxes with navy text, cyan (#0891B2)
arrows, amber (#F59E0B) accent for warnings/gates. Every diagram is a
simple grid layout so text never overlaps. Run: python3 generate_visuals.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
NAVY = "#0B1F4A"
LIGHT = "#E0F2FE"
CYAN = "#0891B2"
AMBER = "#F59E0B"
GREY = "#475569"
FONT = "Segoe UI, Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class SVG:
    def __init__(self, w, h, title, subtitle):
        self.w, self.h = w, h
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
            f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>',
            f'<text x="40" y="52" font-family="{FONT}" font-size="30" font-weight="700" fill="{NAVY}">{esc(title)}</text>',
            f'<text x="40" y="82" font-family="{FONT}" font-size="17" fill="{GREY}">{esc(subtitle)}</text>',
            f'<rect x="40" y="98" width="90" height="5" fill="{CYAN}"/>',
        ]

    def box(self, x, y, w, h, label, sub="", style="navy"):
        fill, tcol, scol = (NAVY, "#FFFFFF", "#BFE3F2") if style == "navy" else (LIGHT, NAVY, "#33506E")
        if style == "amber":
            fill, tcol, scol = "#FEF3C7", NAVY, "#7C5A03"
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}"/>')
        if sub:
            self.parts.append(f'<text x="{x + w/2}" y="{y + h/2 - 4}" text-anchor="middle" font-family="{FONT}" font-size="19" font-weight="700" fill="{tcol}">{esc(label)}</text>')
            self.parts.append(f'<text x="{x + w/2}" y="{y + h/2 + 20}" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{scol}">{esc(sub)}</text>')
        else:
            self.parts.append(f'<text x="{x + w/2}" y="{y + h/2 + 7}" text-anchor="middle" font-family="{FONT}" font-size="19" font-weight="700" fill="{tcol}">{esc(label)}</text>')

    def arrow(self, x1, y1, x2, y2, label=""):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{CYAN}" stroke-width="3" marker-end="url(#ah)"/>')
        if label:
            self.parts.append(f'<text x="{(x1+x2)/2}" y="{(y1+y2)/2 - 8}" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="600" fill="{CYAN}">{esc(label)}</text>')

    def note(self, x, y, text):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="15" fill="{GREY}">{esc(text)}</text>')

    def save(self, name):
        defs = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                'markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" '
                f'fill="{CYAN}"/></marker></defs>')
        body = "\n".join(self.parts[:2] + [defs] + self.parts[2:]) + "\n</svg>"
        with open(os.path.join(OUT, name), "w") as f:
            f.write(body)
        print("wrote", name)


def hflow(name, title, subtitle, steps, note=""):
    """Horizontal chain of boxes with arrows between them."""
    n = len(steps)
    w = 1200
    bw = (w - 80 - (n - 1) * 50) // n
    s = SVG(w, 300, title, subtitle)
    y = 140
    for i, (label, sub) in enumerate(steps):
        x = 40 + i * (bw + 50)
        s.box(x, y, bw, 90, label, sub, "navy" if i in (0, n - 1) else "light")
        if i < n - 1:
            s.arrow(x + bw + 4, y + 45, x + bw + 46, y + 45)
    if note:
        s.note(40, 275, note)
    s.save(name)


def grid(name, title, subtitle, cells, cols=4, note=""):
    """Grid of labelled boxes, row by row."""
    rows = (len(cells) + cols - 1) // cols
    w, h = 1200, 140 + rows * 120 + 40
    s = SVG(w, h, title, subtitle)
    bw = (w - 80 - (cols - 1) * 40) // cols
    for i, (label, sub) in enumerate(cells):
        r, c = divmod(i, cols)
        x, y = 40 + c * (bw + 40), 140 + r * 120
        s.box(x, y, bw, 90, label, sub, "light")
        if c < cols - 1 and i + 1 < len(cells):
            s.arrow(x + bw + 4, y + 45, x + bw + 36, y + 45)
    if note:
        s.note(40, h - 18, note)
    s.save(name)


def agent_anatomy():
    s = SVG(1200, 470, "Anatomy of an AI agent in n8n",
            "One root node, its capabilities supplied by sub-nodes underneath.")
    s.box(430, 130, 340, 95, "AI Agent", "the root node: decide, act, observe", "navy")
    s.box(60, 300, 320, 95, "Chat Model", "required: the reasoning engine", "light")
    s.box(440, 300, 320, 95, "Tools", "required: what the agent can do", "light")
    s.box(820, 300, 320, 95, "Memory", "optional: the conversation so far", "light")
    s.arrow(220, 295, 520, 232)
    s.arrow(600, 295, 600, 232)
    s.arrow(980, 295, 680, 232)
    s.note(40, 440, "Sub-nodes connect by type: ai_languageModel, ai_tool, ai_memory. Swap one without rebuilding the workflow.")
    s.save("ai-agent-anatomy.svg")


def mcp_directions():
    s = SVG(1200, 430, "MCP in both directions",
            "Your agent calls out through the Client Tool; the world calls in through the Server Trigger.")
    s.box(40, 140, 250, 90, "Your AI Agent", "inside n8n", "navy")
    s.box(390, 140, 300, 90, "MCP Client Tool", "discovers tools at runtime", "light")
    s.box(790, 140, 330, 90, "External MCP Server", "databases, docs, dev tools", "light")
    s.arrow(294, 185, 386, 185, "calls out")
    s.arrow(694, 185, 786, 185)
    s.box(40, 290, 250, 90, "External AI App", "Claude, Cursor, ChatGPT", "light")
    s.box(390, 290, 300, 90, "MCP Server Trigger", "your workflow, published", "light")
    s.box(790, 290, 330, 90, "Your Workflows", "exposed as tools", "navy")
    s.arrow(294, 335, 386, 335, "calls in")
    s.arrow(694, 335, 786, 335)
    s.save("mcp-directions.svg")


def production_layers():
    s = SVG(1200, 560, "The production layers around a workflow",
            "Each layer is a module of this course; none is optional for long.")
    layers = [("Publish", "draft to published, exports in git, rollbacks ready", "light"),
              ("Hosting", "Postgres, pinned versions, backups rehearsed", "light"),
              ("Security", "credentials, hardened defaults, approvals", "amber"),
              ("Monitoring", "four numbers, daily digest, weekly trend", "light")]
    for i, (label, sub, style) in enumerate(layers):
        y = 130 + i * 100
        s.box(240, y, 720, 80, label, sub, style)
    s.note(40, 545, "A workflow is production when all four layers hold, not when it merely runs.")
    s.save("production-layers.svg")


# 1. Course map
grid("course-map.svg", "Course map: 35 lessons, one arc",
     "Every module automates one more piece of BrightSmile Dental. The capstone assembles them.",
     [("M0 Start here", "Lessons 00 to 01"), ("M1 Foundations", "Lessons 02 to 06"),
      ("M2 Core nodes", "Lessons 07 to 12"), ("M3 Real services", "Lessons 13 to 16"),
      ("M4 Reliability", "Lessons 17 to 19"), ("M5 AI in n8n", "Lessons 20 to 27"),
      ("M6 Production", "Lessons 28 to 31"), ("M7 Capstone", "Lessons 32 to 34")],
     note="The Lead Machine (capstone) reuses every module before it. Nothing is throwaway.")

# 2. Workflow anatomy
hflow("workflow-anatomy.svg", "Anatomy of a workflow: read it like a sentence",
      "A trigger starts it, nodes do the work, connections are the verbs.",
      [("Trigger", "when it runs"), ("Nodes", "one job each"),
       ("Connections", "data flows"), ("Execution", "the recorded run")],
      note="If you cannot say the workflow's sentence out loud, you do not understand it yet.")

# 3. Items and JSON
hflow("items-and-json.svg", "The items model: a list in, a list out",
      "Each item is one JSON object. Nodes process every item they receive.",
      [("Items in", "a list of objects"), ("Node", "works per item"),
       ("Items out", "same shape discipline"), ("Next node", "and so on")],
      note="Test with three items, including an ugly one. One-item tests certify a fiction.")

# 4. Expressions
hflow("expressions-flow.svg", "Expressions: mapping without code",
      "Double curly braces pull values from the current item, earlier nodes, and n8n itself.",
      [("Input fields", "the item arrives"), ("Expression", "{{ $json.field }}"),
       ("Mapped output", "renamed, computed"), ("Next node", "sees clean data")],
      note="Expressions see the node's input, not fields created in the same node. That boundary is a feature.")

# 5. Trigger types
grid("trigger-types.svg", "Five doors into a workflow",
     "Whatever the door, normalise into one house shape immediately after it.",
     [("Manual", "you click"), ("Schedule", "the clock"),
      ("Webhook", "a system calls"), ("Form", "a person submits"),
      ("Chat", "a conversation starts")], cols=5,
     note="Downstream nodes should never learn which door the data came through.")

# 6. Error workflow
hflow("error-workflow.svg", "The error workflow: failure becomes a message a human can act on",
      "Registered once, it serves every workflow on the instance.",
      [("A run fails", "any workflow"), ("Error Trigger", "receives the facts"),
       ("Build the alert", "workflow, node, record"), ("A human acts", "with the first move named")],
      note="Alerts carry the execution id. Open the execution; do not guess.")

# 7. AI agent anatomy (custom)
agent_anatomy()

# 8. RAG pipeline
hflow("rag-pipeline.svg", "RAG: answer from your documents, with sources",
      "Load once, retrieve per question, answer from what came back.",
      [("Load", "your documents"), ("Split", "right-sized chunks"),
       ("Embed", "meaning as numbers"), ("Store", "the vector store"),
       ("Retrieve", "top chunks"), ("Answer", "with citations")],
      note="If retrieval returns nothing relevant, the correct answer is an abstention.")

# 9. MCP both directions (custom)
mcp_directions()

# 10. Production layers (custom)
production_layers()

# 11. Capstone flow
hflow("capstone-flow.svg", "The Lead Machine: the capstone pipeline",
      "One system, four jobs, every course module inside it.",
      [("Intake", "form and webhook"), ("Qualify", "classify and score"),
       ("Follow up", "bounded chases"), ("Digest", "daily, to the owner")],
      note="Complaints exit to a human before scoring. Closed leads are never chased.")
