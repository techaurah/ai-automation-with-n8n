# Lesson 06: Solution notes

The email normaliser maps `from` to the sender field, `text` to `message`, takes the name from the part of the email address before the @ if no name is given (and says so in a `name_source` note or accepts `unknown`), and stamps `received` the same way. Structural identity is the test: same keys (`kind`, `name`, `message`, `received`), same types, `kind` set to `enquiry`.

The sentence: the first downstream node that assumes the house shape (the classifier reading `message`, the logger writing `received`) either errors or, worse, writes empty values for every record from the unnormalised door, and the failure looks like a data problem instead of an architecture problem.

**What to notice.** You have now built the capstone's front half in miniature. Lesson 32 will not teach a new trick; it will ask you to do this, carefully, at business scale.
