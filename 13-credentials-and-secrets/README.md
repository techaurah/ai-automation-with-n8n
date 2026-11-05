# Lesson 13: Credentials and secrets done right: the rule with no exceptions

**Time:** about 50 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 10 · **You need:** Your instance, and this repo cloned for the scanner.

One rule runs through this whole course, and this lesson is where it gets its own hour: **secrets live in n8n's credential store, never in workflows**. Not in a Code node, not in a header expression, not in an Edit Fields default, not in an exported JSON committed to git. The rule sounds obvious and is violated constantly, usually by a copied blog workflow. This lesson explains how the credential store protects you, the shapes authentication takes, and gives you a scanner and an audit worksheet to police your own estate.

## How the credential store protects you

Credentials are stored separately from workflows, encrypted at rest with an instance key (which lives with your data volume, one more reason Lesson 02 and Lesson 29 treat that volume as crown jewels). Nodes reference a credential by id; the secret value is injected at execution time and is not part of the workflow definition, which is why **exported workflow JSON contains references, not secrets**, and can be committed, shared, and reviewed safely. The moment a secret is pasted into a node field, it becomes part of the definition: visible to anyone who can view the workflow, copied into every export, and immortal in git history even after you delete it.

Access follows the instance's sharing model: credentials can be shared with specific users or projects on plans that support it, and the personal-versus-shared distinction matters when a teammate leaves. The audit worksheet in this folder turns these ideas into eight checks with evidence.

## The three shapes of authentication

Nearly every API you will meet uses one of three. **API key or token in a header** (Header Auth credential: a name like `Authorization` and a value like a bearer token), the simplest and the most commonly leaked. **Basic auth** (username and password), mostly legacy and internal tools. **OAuth2**, the connect-your-account dance used by Google, Slack, HubSpot and friends, where n8n stores refresh material and the credential is really a governed connection to an account: which account owns it is an operational decision (a role account, not the intern's personal Gmail), and Lesson 16's CRM work depends on getting it right.

The HTTP Request node speaks all three (predefined credential types for known services, generic ones for the rest), and dedicated service nodes consume the same store. One credential per service per purpose: "Gmail, Lead Machine sending" and "Gmail, personal tests" are different credentials, so revoking the experiment never kills the business system.

## The scanner: trust, but verify mechanically

`scan_workflows.py` in this folder walks every workflow JSON in this repository and flags parameters that look like pasted secrets: suspicious key names holding long literal values, and strings matching known token shapes. Run it now; it should report zero findings on the course repo, and that zero is itself a checked claim (the script exits nonzero on any finding, so CI could gate on it). Then understand its limits: it is a tripwire for the common shapes, not a proof of purity. A secret in a Code node's string will match the token shapes if it looks like one, and a short or oddly formatted secret sails through. The scanner supports the rule; it does not replace the habit.

## Run it

```bash
cd 13-credentials-and-secrets
python3 scan_workflows.py
```

Expect a clean scan of the whole course repo. Then import `workflow.json`, create a Header Auth credential with any test value, select it in the HTTP node as the sticky note directs, and run: the fetch works, and the workflow file on disk still contains no secret, which you can prove by searching the file for your test value. Finish by working the first three rows of `credential_audit.md` against your own instance and writing down the evidence.

## Common failures

- **The helpful blog paste.** A copied workflow arrives with the author's demo key in a header. It works, so it ships, so two companies now share one leaked key. Scan every import, including this course's (we do; you watched).
- **Rotating by editing the workflow.** If changing a key means opening a canvas, the key lives in the wrong store. Rotation should be a credentials-screen edit with zero workflow changes.
- **Personal OAuth for business systems.** The connection owned by a departed teammate's account is an outage with a calendar invite. Role accounts own production credentials.
- **Committing first, scanning later.** Git remembers. Scan before the commit, and treat any committed secret as compromised: rotate it, do not just delete the line.

## Recap checklist

- [ ] Secrets in my estate live only in the credential store; I scanned to prove it.
- [ ] I can name the three auth shapes and which credential type serves each.
- [ ] My credentials are named by service and purpose, owned by the right account.
- [ ] I ran the audit worksheet's first rows against my own instance with evidence.

## Resources

- [n8n: credentials](https://docs.n8n.io/credentials/)
- [n8n: external secrets (paid plans)](https://docs.n8n.io/external-secrets/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
