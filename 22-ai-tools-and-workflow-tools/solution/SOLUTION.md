# Lesson 22: Solution notes

The design that survives review: `book_slot` takes weekday, time, treatment, and a patient reference (never free-text medical detail), returns a booking reference or a specific failure (slot taken, outside hours), writes through the same sub-workflow the deterministic intake uses (one implementation, two callers), and requires human approval until its error rate is measured and boring, per Lesson 27. Its auditor sentence: "Books one emergency slot per approved request, into the clinic's own calendar workflow, returning a reference the patient can quote." If a tool cannot produce that sentence, it is not ready to be a tool.

**What to notice.** The catalogue review is a security review conducted with a printer. Teams that do it quarterly find the forgotten debug tool and the over-broad sheet writer before an incident does it for them.
