#!/usr/bin/env python3
"""Lesson 20 twin: a Basic LLM Chain with the model simulated.

A chain is: render a prompt template with real values, send it to a
model, parse the reply against a contract. The model here is a
stand-in function, so the template and the contract (the parts that
are actually yours) can be tested offline. Swap fake_model for a
real call and the rest of the lesson survives unchanged.
"""

TEMPLATE = """You are the front desk of BrightSmile Dental.
Answer the patient's question in one or two sentences.
Use only the facts given. If the facts do not cover it, say the
team will confirm.

Facts: {facts}
Question: {question}
"""

FACTS = "Whitening costs GBP 299. Emergency slots run Mon to Thu."


def fake_model(prompt):
    if "whitening" in prompt.lower():
        return "Teeth whitening costs GBP 299 for a 60 minute session."
    return "The team will confirm that for you."


def run_chain(question):
    prompt = TEMPLATE.format(facts=FACTS, question=question)
    reply = fake_model(prompt)
    assert isinstance(reply, str) and reply, "contract: non-empty text"
    return reply


print(run_chain("How much is whitening?"))
print(run_chain("Do you offer payment plans?"))
print("template rendered, contract checked, model swappable")
