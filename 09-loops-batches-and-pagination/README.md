# Lesson 09: Loops, batches, and pagination: processing more than one screen of data

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 04, 08 · **You need:** Your instance. The example API (JSONPlaceholder) is free and needs no key; the twin runs fully offline.

Real data does not arrive in demo quantities. APIs paginate, spreadsheets have thousands of rows, and services rate-limit. This lesson teaches n8n's three answers: the fact that most nodes already loop over items for you, the Loop Over Items node for batching and re-entry patterns, and the pagination discipline for APIs that hand you data one page at a time. It ends with the failure mode that matters: the harvest that silently stops at page one.

## The loop you already have

Most "looping" in n8n is implicit: a node receiving 200 items processes 200 items. Builders coming from code reach for a loop node where none is needed, and builders coming from spreadsheets miss that this is happening at all. Reach for explicit looping only when the job needs it: processing in **batches** (ten at a time into an API that caps request size), **waiting** between groups (rate limits), **re-entering** with new state (the next page), or **stopping early** on a condition. If none of those apply, the items model is your loop.

## Loop Over Items (Split in Batches)

In workflow JSON the node is `splitInBatches`, and on the canvas it is **Loop Over Items**. It emits its input in batches of a size you set, and it has the unusual topology this lesson's workflow shows: a **loop output** that flows through your processing and back into the node for the next batch, and a **done output** that fires when the input is exhausted. Two settings decide whether it behaves: batch size (1 turns it into a strict one-at-a-time processor, the safe choice for fragile APIs), and the reset option, which matters when a workflow re-enters the node with fresh items, as the pagination pattern does. Wire the done output to something, always: an unmonitored loop that finishes silently teaches you nothing, and one that never finishes teaches you at 3am.

## Pagination: three styles, one discipline

APIs paginate three common ways: **page numbers** (`?_page=2&_limit=10`), **offsets** (`?offset=20&limit=10`), and **cursors** (the response hands you a `next` token to send back). The HTTP Request node has built-in pagination support for these patterns, and it is the right first choice. The manual loop in this lesson's workflow exists so you understand what the built-in support is doing: fetch a page, check whether it was full, advance the cursor, repeat, and **stop on a short or empty page**, never on a page count you assumed.

The discipline underneath: harvests fail silently. A loop that stops early produces a smaller dataset that still looks plausible, and every report downstream is wrong in a way nobody notices for weeks. So a harvest verifies itself: this lesson's twin asserts the exact expected record set, and production harvests log pages fetched, records seen, and the stop reason, which Lesson 31 turns into a monitoring habit.

## Rate limits and politeness

Batching is also courtesy and self-defence. APIs publish rate limits; exceeding them earns throttling or bans, and bursty automations find limits that manual use never would. The tools: batch sizes tuned to the API's documented limits, the Wait node between batches when limits are per-minute, and retries with backoff on 429 responses (Lesson 17 covers the retry settings honestly). Self-hosted builders add one more consideration: a 50,000-item loop monopolises the instance's workers; queue mode and worker scaling are Lesson 29 territory, but the design smell, one workflow eating the whole estate, is worth recognising here.

## Run it

Run the twin first (`python3 pagination_twin.py`): three pages, 23 records, assertion passes. Then import `workflow.json`, run it, and open the execution: watch the Loop node re-enter, the page counter climb, and the done output fire when a page returns fewer than ten posts. JSONPlaceholder serves 100 posts, so expect ten full pages; the fetched counts in the execution are the harvest verifying itself.

## Common failures

- **Stopping on an assumed page count.** The API added data; your loop did not notice. Stop on a short page or an absent cursor, and log the stop reason.
- **Processing inside the loop and also after it.** Pick one. Items processed per batch and then reprocessed from the done output is the double-send factory Lesson 19 dismantles.
- **Batch size as an afterthought.** A batch of 1,000 into an API capped at 100 per request fails on batch one. Read the API's limits before choosing the number.
- **Infinite re-entry.** A cursor that never advances (a copy-paste bug in the advance step) loops forever. Give loops a maximum iteration guard in any Code-based cursor logic, and watch executions while testing.

## Recap checklist

- [ ] I can say when implicit item processing is enough and when a loop node earns its place.
- [ ] I traced a pagination loop through its re-entries to its done output.
- [ ] I know the three pagination styles and the stop-on-short-page discipline.
- [ ] My harvests log pages, counts, and stop reason, starting with this lesson's.

## Resources

- [n8n: Loop Over Items node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches/)
- [n8n: HTTP Request node pagination](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)
- [JSONPlaceholder, the free fake API used here](https://jsonplaceholder.typicode.com/)
- [n8n documentation home](https://docs.n8n.io/)
