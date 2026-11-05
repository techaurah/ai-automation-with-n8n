# Lesson 10: HTTP Request and APIs: the universal integration node

**Time:** about 65 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 04, 05, 08 · **You need:** Your instance and an internet connection for the live fetch. The twin and its recorded response work offline.

n8n ships hundreds of service nodes, but the HTTP Request node is the one that matters most, because every service with an API is reachable through it, including the ones with no dedicated node and the ones whose dedicated node lacks the operation you need. This lesson teaches the node properly: methods, URLs built from expressions, headers and query parameters, JSON bodies, response shapes, and the two settings that decide whether failures wake you up or vanish.

## Anatomy of a request, mapped to the node

A request is a **method** (GET reads, POST creates, PUT and PATCH update, DELETE deletes), a **URL**, **query parameters** (the `?_page=2` part), **headers** (metadata, including authentication), and sometimes a **body** (usually JSON for APIs). The node mirrors this exactly, and its URL and fields accept expressions, which is how Lesson 09 built page URLs dynamically. Two habits: build query parameters in the node's parameter fields rather than string-gluing them into the URL (n8n encodes them correctly), and send JSON bodies with the node's JSON body option rather than hand-quoting strings in an expression, which is where malformed payloads are born.

Authentication gets its own field on the node, wired to a credential (Lesson 13). If you find yourself pasting a token into a header expression, stop: that token is now visible in the workflow and in every export.

## Reading responses: status, shape, and the split question

A response gives you a **status code** and a body. The 2xx family is success, 4xx means your request was wrong (auth, not found, validation), 5xx means their side failed and a retry may help; Lesson 17 turns that taxonomy into retry policy. The body of a list endpoint is an array, and the node's response settings include the option to split a JSON array response into items; leave it off and you get one item holding the whole array, which downstream nodes then mishandle in the exact ways Lesson 04 predicted. When an API wraps results (`{ "data": [...] }`), split at the wrapper path instead.

This lesson's workflow maps one user record into a contact shape. The mapping code reads nested fields (`u.address.city`), the kind of path work you will do weekly, and the twin reproduces it from the recorded response in `api_response.json`, captured from the same free API, so the logic is testable on a plane.

## Failure settings: the two toggles that matter

On the node's settings tab, **On Error** decides what a failure does: stop the workflow (right while building), continue to a dedicated error output (right in production, wired like Lesson 08's branches), or continue with the regular output passing error details through. And **Retry on Fail**, with its wait between tries, handles the transient 5xx and network blips. Neither setting is a substitute for the error workflow of Lesson 17; they are the local policy, that is the global one. Set both deliberately per node, because the defaults assume a human is watching the run, and in production nobody is.

## Reading API documentation like a builder

Every API integration in your career follows this lesson's rhythm: find the endpoint in the docs, note the auth scheme, make one request work with real sample data (the docs' example payload or a tool like curl), then map the response, then handle its failures. Documentation pages that matter and are easy to skip: rate limits (Lesson 09), pagination style (Lesson 09 again), error body format (what a 4xx actually returns, which your error branch will need to parse), and versioning policy. The workflow that skips these pages works on demo day and pages you later.

## Run it

Import `workflow.json` and run it: one user fetched, mapped, checked, and marked contact ready. Run the twin (`python3 http_twin.py`) and confirm the mapped contact matches the workflow's exactly; it reads the recorded response, so it works with the wifi off. Then change the URL in the HTTP node to `/users/999` and run again to meet a 404 with your eyes open: note where the execution shows the failure, because Lesson 17 builds on exactly this moment.

## Common failures

- **Auth pasted into a header expression.** Visible in exports, committed to git, rotated never. Credentials, Lesson 13, no exceptions.
- **The array that was not split.** One item containing 100 records flows downstream and every per-item node sees a blob. Check item counts after every fetch.
- **Ignoring status codes in mapping code.** A 404 body mapped as if it were a user produces a contact with undefined fields and a successful execution. Check for error shapes before mapping, or route errors at the node.
- **Hand-built JSON bodies.** String-concatenated payloads break on the first name containing a quote. Use the node's JSON body and expressions inside it.

## Recap checklist

- [ ] I can build a request (method, URL, parameters, headers, JSON body) from an API's docs.
- [ ] My fetched lists arrive split into items, verified by count.
- [ ] I set On Error and Retry on Fail deliberately, per node.
- [ ] The twin and the workflow agree on the mapped contact, field for field.

## Resources

- [n8n: HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)
- [JSONPlaceholder API guide](https://jsonplaceholder.typicode.com/guide/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
