#!/usr/bin/env python3
"""Lesson 05 twin: what the expressions compute, in plain Python.

The workflow maps order fields with n8n expressions. This script
computes the identical values so the mapping is checkable offline.
"""
ORDERS = [
    {"first": "Ayesha", "last": "Khan", "price": 299, "qty": 1, "member": True},
    {"first": "Tom", "last": "Lee", "price": 45, "qty": 3, "member": False},
]


def map_order(o):
    total = o["price"] * o["qty"]
    discount = round(total * 0.1, 2) if o["member"] else 0
    return {
        "customer": f"{o['first']} {o['last']}",
        "total": total,
        "discount": discount,
        "due": round(total - discount, 2),
        "label": "member" if o["member"] else "standard",
    }


for o in ORDERS:
    print(map_order(o))
