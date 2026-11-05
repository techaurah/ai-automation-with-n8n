# Lesson 28: Saving, publishing, and versioning: change control for people who ship

**Time:** about 55 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 02, 17, 19 · **You need:** Your instance and this repo.

Module 6 is about running automations like infrastructure, and it starts with the n8n 2.0 change that redefined daily work: saving and publishing are different acts. This lesson builds your change discipline on that model: what a draft is for, what publishing commits you to, how exports become your portable version history, and the release routine (checklist included) that the capstone will follow to go live.

## Save is a draft, Publish is a deployment

In n8n 2.x, editing a workflow changes its **draft**; the **published** version is what triggers actually run. You can break a draft all morning and production never notices, then publish once, deliberately. Older material (and muscle memory from the 1.x Active toggle) collapses these into one act, which is why this course flags it so often: half of "n8n changed my live workflow by itself" stories are really the old model being remembered into the new one. The editor shows a workflow's published state and keeps **version history** you can review and restore from, which covers the small accidents. It does not cover the big ones (instance loss, a bad publish discovered next week, a teammate asking what changed and why), which is what the rest of the lesson is for.

Adopt the vocabulary in your team: nobody "saves to production"; they *publish*, and publishing is an event with a before and an after, a checklist, and a rollback. The words change the care level more than any tool setting.

## Exports are your portable truth

A workflow's exported JSON is the workflow, minus secrets (Lesson 13: credentials travel as references). Committing exports to git gives you diffable history (a changed node is a readable diff), reviewable changes (a pull request can ask "why does the intake now lowercase emails" and get an answer), and instance independence (the estate survives losing the instance, because the repo rebuilds it). This course is itself the proof: every workflow you have imported lived as JSON in a repository first.

n8n also offers built-in **Git sync and environments** on its paid self-hosted plans and source-control features on Cloud plans; if your organisation pays for them, use them, they automate exactly this discipline. The course teaches the export-and-git routine because it works on the free Community Edition everywhere, and because builders who understand the manual routine use the automated one well. The `export_audit.py` script in this folder is the routine's mechanical half: it inventories exports, counts nodes, and flags placeholders and watchlist nodes before a release, in the spirit of Lesson 13's scanner.

## The release routine

`publish_checklist.md` in this folder is the course's routine, and the capstone (Lesson 34) executes it in full. Its beats: verify the draft against production-shaped data, export the *current live* version as the rollback before replacing it, check the mechanical gates (audit clean, error workflow registered, placeholders gone), publish, watch the first real executions with your own eyes, and commit the new export with a message that says why. Two habits inside it deserve emphasis. The **version note in the workflow itself** (this lesson's sticky is the model: owner, change, rerun safety, gates) travels with the workflow into every instance it is imported to, where git messages do not. And **rollback is a file plus steps**, rehearsed once, not a hope plus a prayer at incident time.

## Run it

Run the audit over this repo:

```bash
cd 28-saving-publishing-and-versioning
python3 export_audit.py ..
```

Read its output as a release manager: the course's placeholders are flagged (correctly; in your estate they block a release), and every workflow is inventoried. Import `workflow.json`, read its version-note sticky, then make one trivial draft edit (rename a node), save, and confirm in the workflow list that the published behaviour did not change until you choose Publish. Export the workflow and diff the file against the repo's copy: your rename, visible as JSON. That diff is version control, working.

## Common failures

- **Editing live by reflex.** In 2.x the draft protects you only if you respect the boundary: test in draft, publish on purpose, never "just fix" a published workflow's draft during an incident without the checklist's rollback step.
- **Exports committed with placeholders or, worse, secrets.** The audit and the Lesson 13 scan are pre-commit habits. A placeholder in production is a workflow wired to nothing; a secret is Lesson 13's lecture again.
- **No rollback file.** The time to export the working version is before you replace it. After is archaeology.
- **Change messages that say 'update'.** The next reader is you, at an incident, asking why. Messages and version notes answer with the reason, not the mechanics.

## Recap checklist

- [ ] I can explain draft versus published and catch myself using the old model.
- [ ] My estate's workflows exist as exports in git with meaningful messages.
- [ ] I run the export audit before any release and treat placeholders as blockers.
- [ ] Every workflow I own carries a version note: owner, change, rerun safety, gates.

## Resources

- [n8n: workflow history and publishing](https://docs.n8n.io/workflows/publish/)
- [n8n: source control and environments](https://docs.n8n.io/source-control-environments/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
