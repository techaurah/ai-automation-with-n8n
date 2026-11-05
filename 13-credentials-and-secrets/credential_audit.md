# Credential audit worksheet (Lesson 13)

Work through your instance with this list. Every row wants evidence,
not vibes: the credentials screen, the workflow, or the export.

| # | Check | Where to look | Pass looks like |
|---|-------|---------------|-----------------|
| 1 | Every service connection is a credential, not a pasted value | Credentials screen vs workflow parameters | No tokens in any node field |
| 2 | No secrets in Code nodes or expressions | Search exports for key shapes (run scan_workflows.py) | Zero findings |
| 3 | Credentials are named by service and purpose | Credentials screen | "Gmail, Lead Machine sending", not "Credential 7" |
| 4 | OAuth credentials are owned by a role account, not a person who may leave | The connected account on each OAuth credential | A company account owns the connection |
| 5 | Test and production credentials are separate | Names and the instances using them | No production key reachable from a learning instance |
| 6 | Exports in git contain no credential values | scan_workflows.py over the repo | Zero findings, exports reviewed before commit |
| 7 | Each credential has a rotation note | Your ops notes | Owner, created date, where the secret also lives |
| 8 | Departed teammates' personal connections are revoked | OAuth account's connected apps | No orphaned access |
