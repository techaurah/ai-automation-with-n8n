#!/usr/bin/env python3
"""Lesson 09 twin: pagination and batching, simulated offline.

A fake API serves 23 records in pages of 10. The harvester walks the
pages the way the workflow does: keep going until a short page says
the data is done, and process in batches that respect a rate limit.
"""

PAGES = {1: list(range(1, 11)), 2: list(range(11, 21)), 3: [21, 22, 23]}


def fetch_page(page):
    return PAGES.get(page, [])


def harvest(page_size=10):
    records, page = [], 1
    while True:
        batch = fetch_page(page)
        records.extend(batch)
        print(f"page {page}: {len(batch)} records")
        if len(batch) < page_size:
            return records
        page += 1


result = harvest()
assert result == list(range(1, 24)), result
print(f"harvested {len(result)} records, no gaps, no duplicates")
