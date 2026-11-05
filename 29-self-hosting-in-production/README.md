# Lesson 29: Self-hosting in production: Postgres, an encryption key, backups, and updates

**Time:** about 70 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 02, 28. Cloud learners: read actively; the decisions transfer. · **You need:** Docker. The lesson's stack is a second instance; your learning instance from Lesson 02 can stay as it is.

Lesson 02 got n8n running. This lesson makes it survivable: a real database instead of the embedded default, an encryption key you control and have backed up, execution data pruned before it fills the disk, backups that exist as files you can point at, and an update drill that treats new versions as changes to manage rather than surprises to receive. This is the stack the capstone ships on if it self-hosts.

## Postgres, and the end of SQLite's shift

The default embedded database is for evaluation. Production self-hosting uses **PostgreSQL**: n8n 2.x dropped MySQL and MariaDB support entirely, and Postgres is the documented path for anything beyond a toy, including queue mode. The compose file wires it plainly: a `postgres:16` service with its own volume, and n8n pointed at it through the `DB_POSTGRESDB_*` environment variables. Migration between the two exists (export workflows, re-import, re-select credentials) and is a planned afternoon, not an incident, if you do it before the data matters. Decide on day one of any real deployment; the capstone's data model (Lesson 32) assumes a database that enforces and survives.

## The encryption key: the one secret that guards the others

Credentials are encrypted with a key n8n generates into its data folder on first run. Setting `N8N_ENCRYPTION_KEY` explicitly makes that key *yours*: known, portable between instances, and backable-up. The `.env.example` in this folder treats it with the ceremony it deserves, because the failure mode is absolute: lose the key and every stored credential is unreadable, permanently, and every workflow needs reconnecting by hand. The key goes in your password manager or secrets store, in the backup set, and nowhere else: not in the repo (the filled `.env` is gitignored in this course's template for exactly this reason), not in a workflow, not in a chat message. Rotating it is a planned operation with a maintenance window, not a Friday experiment.

## Backups, pruning, and updates: the boring trio that is the job

**Backups.** `backup.sh` produces the two artefacts that matter: a `pg_dump` of the database and an archive of the n8n data volume. Read its header: it deliberately does not decide off-site copies, retention, or restore rehearsals, because those are yours, and it says the course's backup law out loud: an untested backup is a rumour. Rehearse a restore onto a scratch instance quarterly; the first rehearsal teaches you what the script forgot. **Pruning.** Executions are data and they accumulate; the stack sets `EXECUTIONS_DATA_PRUNE` with a 14-day max age (336 hours), and production instances additionally choose which executions to save at all (error runs always; successful manual runs, usually not). **Updates.** The image is pinned (`n8nio/n8n:2.42.7` in the file, a version this course's research observed as current) so updates happen when you change the pin: read the release's breaking changes (2.x taught everyone why), snapshot a backup, update a test instance first if the estate matters, then production, then watch executions. Unpinned `latest` in production is not agility; it is unplanned change with extra steps.

## Topology, in one paragraph

A single instance with Postgres serves most small estates honestly. **Queue mode** (a main instance plus worker processes, backed by Redis) is the step when execution volume or long-running workflows start starving interactive work; it changes operational facts you have already met, notably that Simple Memory stops being reliable (Lesson 23) and binary storage wants a shared home (Lesson 11). A reverse proxy with TLS in front is not optional for anything public: webhook URLs, the editor, and MCP endpoints all assume HTTPS in the real world, and `WEBHOOK_URL` in the stack exists so generated URLs are the public ones. The lesson's stack stays single-instance deliberately; knowing the name of the next step, and the signal that demands it, is the production judgement being taught.

## Run it

Copy `.env.example` to `.env`, set real values (generate the key: `openssl rand -hex 32`), and `docker compose up -d`. Create the owner account, then run the health checker:

```bash
cd 29-self-hosting-in-production
python3 health_check.py
```

Expect an OK line from `/healthz`. Run `backup.sh` (source your `.env` first so the database variables exist) and inspect the two artefacts it wrote. Finally, find the encryption key's footprint: change nothing, but write down, in your ops notes, the three places the key now legitimately lives (the `.env` on the host, your password manager, the backup set) and confirm it is in none of the places it must not be.

## Common failures

- **The key that lived only in the volume.** One lost container later, the credentials are ciphertext forever. Explicit key, backed up separately, from the first production day.
- **Backups that were never restored.** Corrupt dumps and missing volumes are discovered at restore time by people who skipped rehearsals. Quarterly, on a scratch instance, timed.
- **Disk full of executions.** Unpruned execution data, especially with binary payloads saved, fills disks quietly and stops the instance rudely. Prune settings are production settings, set them at birth.
- **Chasing latest.** An unpinned image plus a weekly release cadence equals unreviewed breaking changes in production. Pin, read, rehearse, then move.

## Recap checklist

- [ ] My production stack runs on Postgres with a pinned image and pruned executions.
- [ ] The encryption key is explicit, and I can name its three legitimate homes.
- [ ] I produced a backup and know the date of my first restore rehearsal.
- [ ] I can state the signal that would move this estate to queue mode.

## Resources

- [n8n: hosting documentation](https://docs.n8n.io/hosting/)
- [n8n: Docker installation](https://docs.n8n.io/hosting/installation/docker/)
- [n8n: queue mode](https://docs.n8n.io/hosting/scaling/queue-mode/)
- [n8n documentation home](https://docs.n8n.io/)
