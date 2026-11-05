#!/usr/bin/env python3
"""Lesson 21 twin: the agent loop, visible.

A fake model decides, in the open, which tool to call next; the loop
runs the tool, appends the result, and repeats until the model
answers. This is precisely the AI Agent node's behaviour with the
reasoning replaced by rules you can read. The tools are real.
"""

TOOLS = {
    "calculator": lambda a: eval(a["expression"], {"__builtins__": {}}),
    "clinic_fact": lambda a: {
        "whitening_price": "GBP 299",
        "emergency_days": "Monday to Thursday",
    }[a["fact"]],
}


def fake_model(messages):
    last = messages[-1]["content"].lower()
    if "total" in last or "cost of" in last:
        return {"tool": "calculator",
                "args": {"expression": "299 * 2"}}
    if "price" in last or "whitening" in last:
        return {"tool": "clinic_fact", "args": {"fact": "whitening_price"}}
    if "emergency" in last:
        return {"tool": "clinic_fact", "args": {"fact": "emergency_days"}}
    return {"answer": "Let me check that with the team and confirm."}


def run_agent(question):
    messages = [{"role": "user", "content": question}]
    for step in range(5):
        decision = fake_model(messages)
        if "answer" in decision:
            return decision["answer"]
        result = TOOLS[decision["tool"]](decision["args"])
        print(f"step {step + 1}: tool {decision['tool']} -> {result}")
        messages.append({"role": "tool", "content": str(result)})
        if decision["tool"] == "calculator":
            return f"That comes to GBP {result} in total."
        messages.append({"role": "user",
                         "content": f"Now answer using: {result}"})
        return f"Based on the clinic's records: {result}."
    return "I could not finish that in five steps."


print(run_agent("What is the whitening price?"))
print(run_agent("What is the total cost of 2 whitening sessions?"))
print("the loop, not the model, is the agent")
