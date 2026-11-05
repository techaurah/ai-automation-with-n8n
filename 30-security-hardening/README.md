# Lesson 30: Security hardening: defaults, access, and the automation threat model

**Time:** about 65 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 13, 26, 29 · **You need:** Your instance and this repo for the audit script.

An n8n instance is a machine that holds credentials to your business and executes logic on internet input. That sentence should set the security posture for this whole lesson: verify the platform's hardened defaults, control access like it matters, treat every public trigger as an attack surface, and give AI workflows their own threat model on top. The checklist and audit script in this folder turn the posture into evidence.

## The 2.x defaults: verify them, never assume them

n8n 2.0 shipped a deliberate hardening set, and your first job is confirming it survived your install and upgrade history. **Task runners** isolate Code node execution, so a hostile or broken script is contained. **Environment access from nodes is blocked** by default: an expression reading `$env` gets nothing unless an admin set `N8N_BLOCK_ENV_ACCESS_IN_NODE=false` server-side, which on a production instance should read as a finding, not a setting. The **Execute Command** and **Local File Trigger** nodes are **disabled by default**: both hand workflows the host's authority, and enabling them is a written decision per use, not a convenience toggle. The audit script checks the repo-visible halves of these (risky nodes in workflows, env flags and unpinned images in compose files); the instance-side halves are the checklist's first section, verified in the settings and your server configuration, with evidence.

## Access: the editor is the keys to the kingdom

Whoever can edit workflows can wield every credential the instance holds, indirectly but completely (a workflow that emails a sheet to an attacker is three nodes). So: HTTPS only, through your proxy; owner and admin accounts minimal, named, and strongly authenticated, with SSO where your plan provides it; sharing reviewed like firewall rules, quarterly, with leavers removed the day they leave (Lesson 13's credential ownership, at the access layer). Public triggers get the same seriousness: authenticated webhooks (header auth or better) for anything that writes, unguessable paths as a supplement and never a substitute, payload shape validation at the door (this lesson's workflow shows both layers), and form triggers treated as public input, because they are. Execution data is part of the surface too: it stores payloads, including the sensitive ones, so retention (Lesson 29) and who-can-view are data-protection decisions, not storage trivia.

## The AI layer's threat model

Agents add three threats the checklist names explicitly. **Prompt injection**: text the agent reads (an email, a web page, a tool result, and, Lesson 26 warned, a third-party tool's *description*) contains instructions that try to override yours. Defences are structural: untrusted content is data, tools are narrow (Lesson 22), approvals gate the irreversible (Lesson 27), and guardrails screen both ways. **Over-broad tools**: the catalogue review is a security control, repeated whenever a tool is added, including MCP servers joining the catalogue at runtime. **Memory and logs as data stores**: conversations and executions accumulate personal data by default; retention and access decisions from Lesson 23 apply with legal force in many jurisdictions. Course 1 Lesson 29 develops the full agent threat model; this lesson's job is ensuring the n8n estate gives those defences somewhere solid to stand.

## Run it

Run the audit:

```bash
cd 30-security-hardening
python3 instance_audit.py
```

It scans the course repo itself: expect it to flag the risky-node watchlist only where a lesson deliberately discusses a node in JSON (most lessons will be clean, and any finding should be one you can justify from the lesson text, which is what a justified finding looks like). Import `workflow.json`, attach a Header Auth credential to the webhook, publish, and prove both layers: a request without the header is refused before the workflow runs, and a request with the header but a malformed body is rejected by the shape check inside it. Then work the checklist's first section against your own instance and write the evidence beside each item.

## Common failures

- **Defaults assumed after an upgrade.** A 1.x-era instance can carry old runner and access settings into 2.x clothing. Verify, with evidence, per the checklist.
- **A public write webhook with no auth.** Unguessable paths leak (logs, referrers, screenshots). Authenticate, validate, and still assume the payload is hostile.
- **The editor on the open internet with a weak owner password.** Every credential in the store is one login away. HTTPS, strong auth, minimal admins, SSO where available.
- **Injection treated as a prompting problem.** Nicer system prompts do not patch structure. Narrow tools, approvals, and screened I/O are the patch; wording is garnish.

## Recap checklist

- [ ] I verified the 2.x hardened defaults on my instance with evidence, not memory.
- [ ] My public triggers authenticate and validate shape, in two layers.
- [ ] Access and sharing on my instance are minimal, named, and reviewed on a cadence.
- [ ] I can state the AI threat model and point each threat at its structural defence.

## Resources

- [n8n: security documentation](https://docs.n8n.io/hosting/security/)
- [n8n: hardening task runners and nodes](https://docs.n8n.io/hosting/configuration/task-runners/)
- [Agentic AI for Beginners, Lesson 29 (the agent threat model)](https://github.com/techaurah/agentic-ai-for-beginners)
- [n8n documentation home](https://docs.n8n.io/)
