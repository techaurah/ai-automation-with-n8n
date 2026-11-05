# Lesson 11: Files and binary data: the second data channel in every item

**Time:** about 55 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 04 · **You need:** Your instance, and Python for the twin.

Items carry JSON, and they also carry files. Invoices as PDFs, photos from a form, a CSV export, an audio message: in n8n these travel as **binary data** attached to the item, in a separate channel from the JSON fields. Builders who do not know the channel exists lose files mysteriously between nodes. Builders who do, build document pipelines with confidence. This lesson maps the binary channel and builds a small file pipeline end to end.

## Two channels: json and binary

An item's JSON is its fields. Its **binary** is a set of named file slots (the default slot is named `data`), each holding the file's content plus metadata: file name, MIME type, size, and how the instance stores it. Nodes that produce files (Convert to File, spreadsheet and PDF tools, email attachments, HTTP downloads with the response format set to file) put them in a slot; nodes that consume files read a named slot. The inspection step in this lesson's workflow reads the metadata of the CSV it just made, which is the debugging move for the whole topic: when a file goes missing, inspect what the item actually carries at that node, in both channels.

Storage is an instance decision with production consequences: small instances keep binaries in memory or on disk with the execution data, and large files or high volume push you toward the external binary storage modes (for example S3-compatible storage) covered in the hosting docs and Lesson 29. A workflow returning big payloads also meets the newer offloading behaviour in recent 2.x releases. The design rule is simple: know your largest file and your daily file count before choosing defaults.

## The working nodes

Four nodes cover most file work. **Convert to File** turns item data into a file (text, CSV or JSON from fields, with more formats via its operations). **Extract from File** does the reverse: parses a file slot into items (a CSV becomes rows, a PDF becomes text where the format allows). **Read/Write Files from Disk** touches the instance's own filesystem, self-hosted only, and restricted for good reason: in 2.x the dangerous filesystem-adjacent nodes are disabled or constrained by default, and Lesson 30 treats enabling them as a security decision, not a convenience. **HTTP Request** with its response set to File downloads into a slot, and service nodes (email, Drive, Sheets) attach and detach slots as their operations require.

Naming slots deliberately (`invoice`, `photo`) matters as soon as an item carries two files; the default `data` slot silently overwritten by the second file is a classic data-loss bug that the execution view will show you plainly if you look.

## The pipeline shape

File workflows compose the same way data workflows do: acquire (download, read, form upload), transform (convert, extract, summarise), deliver (attach to an email, store in Drive, respond to a webhook with the file). This lesson's pipeline is the minimal honest version: build CSV text from rows, convert it to a real file slot, inspect the result. The twin performs the same jobs with Python's `csv` module, in memory, because the logic (rows to CSV to counts) is identical even though the transports differ. Where the twin and the canvas diverge is instructive: Python holds the whole file as a string happily at this size; at 500 MB the canvas's storage mode and the twin's memory would both need rethinking, which is why Lesson 31 budgets executions with file weight in mind.

## Run it

Run the twin (`python3 files_twin.py`), then import and run `workflow.json`. In the final node's output, verify the binary metadata: file name `enquiries.csv`, a text MIME type, and a byte size equal to the CSV's real length (compare with the twin's `csv_text` length in your head, roughly 80 bytes). Download the file from the Convert node's output pane and open it: three rows plus a header, exactly the twin's input.

## Common failures

- **Looking for the file in the JSON.** It is not there; it never is. Files live in the binary channel, and a node that only passes JSON (some transforms rebuilt from scratch) drops them without a word.
- **Two files, one slot.** The second file overwrites `data`. Name slots when an item carries more than one file, and check the slot name the receiving node expects.
- **Assuming the disk is yours.** Read/Write Files paths are the instance's paths, not your laptop's, and on Cloud they do not exist. Design file flows around slots and services, not local paths, unless the instance is deliberately yours.
- **Emailing the metadata instead of the file.** Attachment settings take a slot name. Sending `$json` as the attachment body mails your customer a JSON document about a PDF.

## Recap checklist

- [ ] I can describe an item's two channels and inspect both in the editor.
- [ ] I know which nodes create, extract, and consume file slots, and why slots get names.
- [ ] My pipeline's file matches the twin's CSV, byte count included.
- [ ] I can name the storage question to ask before a file workflow meets production volume.

## Resources

- [n8n: binary data](https://docs.n8n.io/data/binary-data/)
- [n8n: Convert to File node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
