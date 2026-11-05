#!/usr/bin/env python3
"""Lesson 12 twin: Data Table semantics, modelled with sqlite3.

A Data Table is persistent rows inside the instance. This twin uses
an in-memory SQLite table to rehearse the same operations the
workflow performs with the Data Table node: insert, get with a
filter, update by key. SQL is explicit here; the node hides it.
"""
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("""CREATE TABLE leads (
    email TEXT PRIMARY KEY, name TEXT, status TEXT, updated TEXT)""")

LEADS = [
    ("ayesha@example.com", "Ayesha Khan", "new", "2026-11-01"),
    ("tom@example.com", "Tom Lee", "contacted", "2026-10-20"),
    ("maria@example.com", "Maria Gomez", "new", "2026-11-03"),
]
db.executemany("INSERT INTO leads VALUES (?, ?, ?, ?)", LEADS)

stale = db.execute(
    "SELECT email FROM leads WHERE updated < '2026-10-25'").fetchall()
print("stale:", stale)
assert stale == [("tom@example.com",)]

db.execute("UPDATE leads SET status = 'booked' WHERE email = ?",
           ("ayesha@example.com",))
row = db.execute("SELECT status FROM leads WHERE email = ?",
                 ("ayesha@example.com",)).fetchone()
assert row == ("booked",)
print("insert, filter, update: all match the workflow's story")
