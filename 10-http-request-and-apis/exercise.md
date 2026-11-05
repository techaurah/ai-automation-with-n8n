# Lesson 10: Exercise

## Fetch the list, properly

1. Change the workflow to fetch `/users` (all of them). Configure the node so the array arrives as items, and verify the item count in the execution.
2. Map every user to the contact shape, and route those missing an email domain of `.biz` (a nonsense rule, deliberately) to the review branch, so both branches carry traffic.
3. Add the twin: extend `http_twin.py` to load a recorded list response. Record it yourself from the API while you have internet, save it as `api_response_list.json`, and make the twin map it identically.

You are done when the workflow reports the same contacts and the same branch counts as the twin, and you can say where the split happened.

## Solution

See `solution/SOLUTION.md` in this folder.
