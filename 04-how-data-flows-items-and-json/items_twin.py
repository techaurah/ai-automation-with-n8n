#!/usr/bin/env python3
"""Lesson 04 twin: the items model, in Python.

The workflow in this lesson shapes three raw enquiries into clean
records. This script performs the identical transforms on the
identical data, so you can see the model with no canvas in the way.
An item in n8n is one JSON object; a node's input is a list of items.
"""
import json

RAW = [
    {"name": "  ayesha khan ", "channel": "Website Form",
     "message": "Tooth pain, need an emergency appointment"},
    {"name": "Tom Lee", "channel": "INSTAGRAM",
     "message": "How much is teeth whitening?"},
    {"name": "Maria Gomez", "channel": "email",
     "message": "Just researching for now, thanks"},
]


def clean(item):
    """One item in, one item out: the shape every transform keeps."""
    first = item["name"].strip().split(" ")[0].title()
    return {
        "first_name": first,
        "name": item["name"].strip().title(),
        "channel": item["channel"].strip().lower(),
        "message": item["message"],
        "word_count": len(item["message"].split()),
    }


def main():
    items = [clean(i) for i in RAW]
    for it in items:
        print(json.dumps(it))
    channels = sorted({i["channel"] for i in items})
    print(f"{len(items)} items, channels: {', '.join(channels)}")
    assert channels == ["email", "instagram", "website form"]
    assert items[0]["first_name"] == "Ayesha"
    print("twin checks passed")


if __name__ == "__main__":
    main()
