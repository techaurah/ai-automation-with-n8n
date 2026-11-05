# Lesson 02: Installing and running n8n (Docker first, Cloud, and the honest npm warning)

**Time:** about 60 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 00 (the setup decision) · **You need:** Docker for the main path. A browser. Nothing paid on any path.

Installation lessons are usually a wall of commands with no reasoning. This one installs n8n the way you would want a colleague to: one recommended path done carefully (Docker Compose, persistent data, your timezone set), the alternatives summarised honestly, and a proof at the end that data survives a restart. Everything after this lesson assumes the instance you build here.

## The Docker Compose path, and why each line exists

The `docker-compose.yml` in this folder is the whole installation:

```bash
cd 02-installing-and-running-n8n
docker compose up -d
```

Open `http://localhost:5678` and create the owner account. Then read the file top to bottom, because each line is a decision. The image is `n8nio/n8n`, the official one, unpinned for a learning instance (Lesson 29 discusses pinning for production). The port mapping exposes the editor on 5678, n8n's standard port. The named volume `n8n_data` mounted at `/home/node/.n8n` is the single most important line: workflows, credentials, and execution history live there, and without the volume a container recreate wipes your work. `GENERIC_TIMEZONE` and `TZ` make schedules mean what you think they mean; a 9am trigger on a UTC container is not 9am where you live. `restart: unless-stopped` means n8n comes back after a reboot, which is what "running" should mean.

One-line alternative for a first look: n8n publishes a setup script, `curl -fsSL https://get.n8n.io | sh`, which writes a Compose file and starts n8n. Knowing what it generates matters more than using it; compare its output with this folder's file.

## The Cloud path, briefly and fairly

Sign up, take the trial, and you have an editor in two minutes with nothing to maintain. For this course, Cloud works for Modules 1 to 5 with two caveats: self-hosting lessons (29, and parts of 30) become reading rather than doing, and some instance-level features differ by plan. If Cloud is your Lesson 00 decision, do the lessons in order anyway and note where your instance's menus differ. Do not start real client workflows on a trial clock.

## The npm path, with its warning label attached

`npx n8n` on Node.js 20.19 to 24.x is a fine way to look at the editor for an afternoon. n8n's documentation says the npm install is not safe to use in production, lacks some features such as the n8n Assistant, and that npm installs are deprecated from n8n 3.0, after which n8n ships through Docker. This course will never ask you to build on it. If it is all you have today, use it to follow along visually, and migrate before the capstone (Lesson 32 assumes an instance whose data persists).

## First-run hygiene

Four things in the first ten minutes save hours later. Create the **owner account** with a password you store in a password manager; the owner can see everything, including other people's credentials metadata. Set the instance timezone before building schedules (above). Run one workflow and find it in the **Executions** view; that view is your black-box recorder for the whole course. Finally, export the Lesson 00 setup ping (Workflows, then the menu on the workflow, Download) so you have felt the export format early: workflow portability in this ecosystem is a JSON file, and Lesson 28 builds your versioning habit on it.

## Run it

With the stack up, import `workflow.json` from this folder (Workflows, Import from File). It is a Schedule Trigger set to 08:00 daily wired to a Code node. Do not wait for tomorrow: open the Schedule Trigger, and for this test, execute the workflow manually from the editor's Execute Workflow button. The execution should show one item: `ping: scheduled run OK` with a timestamp. Then prove persistence: run `docker compose down`, `docker compose up -d`, log in, and confirm the workflow is still there. That round trip is the lesson.

## Common failures

- **No volume, lost work.** The classic first-month disaster. If `docker compose down -v` or a recreate wipes your workflows, the volume line was missing or wrong. The `-v` flag deletes volumes; learn it now, on a lesson, not on a client system.
- **Schedules firing at odd hours.** The container timezone defaults to UTC. If your 9am digest lands at 4am, this is why, and the fix is the environment variables in this lesson's Compose file, not rebuilding the workflow.
- **Port 5678 already in use.** Something else (often an earlier n8n attempt) holds it. Find and stop that process, or change the left side of the port mapping to 5679 and browse there.
- **Building on the trial clock.** Cloud trials end mid-course for someone every cohort. If you are on Cloud, put the trial end date in your progress notes today.

## Recap checklist

- [ ] My instance runs, I am the owner, and I can log in after a restart.
- [ ] I can explain every line of the Compose file, especially the volume.
- [ ] I imported and executed the scheduled ping workflow and found it in Executions.
- [ ] I know my instance version and that this course teaches the 2.x model.

## Resources

- [n8n hosting documentation](https://docs.n8n.io/hosting/)
- [n8n Docker installation guide](https://docs.n8n.io/hosting/installation/docker/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
