# Lesson 29: Solution notes

The step everyone forgets is the encryption key's role in the restore: with the same key, credentials decrypt and the estate is whole; with a fresh key, the restore *looks* successful (workflows, history, all present) until the first credentialed node runs, which is why the proof in step 3 is a credentialed workflow and not a login. The second forgotten step is usually volume naming: compose project names prefix volumes, so restoring across project names needs the volume flag or an explicit external volume, and your runbook should name your exact approach.

**What to notice.** You did not learn backup theory. You produced a timed, written, *rehearsed* restore, which is the only form in which backups exist. Everything else is storage rent paid on a rumour.
