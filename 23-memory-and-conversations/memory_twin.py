#!/usr/bin/env python3
"""Lesson 23 twin: conversation memory, honestly modelled.

A window buffer keeps the last N exchanges per session. Sessions are
isolated by key. This twin is the exact semantics of the Simple
Memory node, small enough to hold in your head, plus a printed
warning about where the model breaks in production.
"""


class WindowMemory:
    def __init__(self, window=5):
        self.window = window
        self.sessions = {}

    def add(self, session, role, text):
        self.sessions.setdefault(session, []).append((role, text))
        self.sessions[session] = self.sessions[session][-2 * self.window:]

    def history(self, session):
        return self.sessions.get(session, [])


mem = WindowMemory(window=2)
mem.add("patient-A", "user", "How much is whitening?")
mem.add("patient-A", "agent", "GBP 299.")
mem.add("patient-A", "user", "And for two of us?")
mem.add("patient-B", "user", "When are emergency slots?")
mem.add("patient-A", "agent", "GBP 548 for two sessions.")

assert len(mem.history("patient-A")) == 4
mem.add("patient-A", "user", "Book us in for Saturday.")
mem.add("patient-A", "agent", "Booked: Saturday 10:30.")
assert len(mem.history("patient-A")) == 4
assert mem.history("patient-A")[0][1].startswith("And for two")
assert mem.history("patient-B")[0][1].startswith("When")
assert "emergency" not in str(mem.history("patient-A"))
print("A remembers whitening, B starts clean, windows hold 2 exchanges")
print("Production warning: this store lives in the instance's memory.")
print("In queue mode a follow-up can land on a worker that never saw")
print("the conversation. That is when Postgres chat memory earns its")
print("place: same contract, durable store, keyed by session id.")
