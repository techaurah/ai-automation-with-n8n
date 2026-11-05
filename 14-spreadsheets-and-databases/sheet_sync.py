#!/usr/bin/env python3
"""Lesson 14 twin: two-way sync between a sheet-like CSV and SQLite.

The workflow syncs a Google Sheet with a Postgres-style table. This
twin rehearses the decision logic offline: newest updated_at wins,
ties go to the database (the system of record), and every decision
is printed so the rule is auditable.
"""
import csv
import io
import sqlite3

SHEET = """email,name,status,updated
ayesha@example.com,Ayesha Khan,booked,2026-11-04
tom@example.com,Tom Lee,new,2026-11-02
"""

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE leads (email TEXT PRIMARY KEY, name TEXT,"
           " status TEXT, updated TEXT)")
db.executemany("INSERT INTO leads VALUES (?, ?, ?, ?)", [
    ("ayesha@example.com", "Ayesha Khan", "contacted", "2026-11-01"),
    ("tom@example.com", "Tom Lee", "contacted", "2026-11-05"),
])


def sync():
    for row in csv.DictReader(io.StringIO(SHEET)):
        current = db.execute("SELECT updated FROM leads WHERE email = ?",
                             (row["email"],)).fetchone()
        if current is None:
            db.execute("INSERT INTO leads VALUES (?, ?, ?, ?)",
                       (row["email"], row["name"], row["status"],
                        row["updated"]))
            print(row["email"], "inserted from sheet")
        elif row["updated"] > current[0]:
            db.execute("UPDATE leads SET name = ?, status = ?, updated = ?"
                       " WHERE email = ?",
                       (row["name"], row["status"], row["updated"],
                        row["email"]))
            print(row["email"], "sheet is newer, database updated")
        else:
            print(row["email"], "database is newer or tied, sheet row skipped")


sync()
rows = db.execute("SELECT email, status FROM leads ORDER BY email").fetchall()
print(rows)
assert rows == [("ayesha@example.com", "booked"),
                ("tom@example.com", "contacted")]
print("sync decisions verified")
