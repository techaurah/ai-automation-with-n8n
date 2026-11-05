# Hardening checklist (Lesson 30)

Work top to bottom. Each item wants evidence, like Lesson 13's audit.

## Platform defaults (verify, do not assume)

- [ ] Code nodes run under task runners (2.x default); no legacy
      runner exceptions carried from a 1.x upgrade
- [ ] Environment variable access from nodes is blocked
      (N8N_BLOCK_ENV_ACCESS_IN_NODE is not set to false)
- [ ] Execute Command and Local File Trigger nodes are disabled,
      or each use is individually justified in a workflow note
- [ ] The instance is current on a pinned, reviewed version

## Access

- [ ] Editor reachable only over HTTPS, behind your proxy
- [ ] Owner and admin accounts are named people with strong,
      manager-stored passwords; SSO enabled where the plan allows
- [ ] Sharing is deliberate: who can view, who can edit, who can
      see credentials, reviewed quarterly
- [ ] Instance-level MCP access is off, or scoped and justified
      in writing (Lesson 26)

## Workflows and data

- [ ] Public webhooks and forms that need it use authentication
      or an unguessable path plus payload validation
- [ ] Credentials pass the Lesson 13 audit (run both scanners)
- [ ] Agent tools pass the Lesson 22 catalogue review; no tool
      can spend, delete, or message without its gate (Lesson 27)
- [ ] Logs and execution data respect the data you hold:
      retention set (Lesson 29), sensitive payloads not saved
      longer than the debugging need

## The human layer

- [ ] Prompt-injection briefing done for anyone building agents:
      untrusted text is data, never instructions (Lesson 27, 30)
- [ ] A named owner for the instance, and for each production
      workflow, findable from the workflow notes (Lesson 28)
