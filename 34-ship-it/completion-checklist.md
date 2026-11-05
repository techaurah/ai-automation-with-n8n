# Lead Machine completion checklist (Lesson 34)

## The non-negotiables, evidenced

- [ ] Error workflow registered on all three workflows; a forced
      failure produced the standard alert (Lesson 17)
- [ ] Replay test passed: the same delivery twice, one record,
      one side effect (Lesson 19)
- [ ] Both scanners clean on the production exports (Lessons 13, 30)
- [ ] Approvals in place for every customer-facing send; expiry
      means no (Lesson 27)
- [ ] Restore rehearsal done on the production stack (Lesson 29)

## The release, by the Lesson 28 routine

- [ ] Previous live versions exported as rollbacks
- [ ] `ship_check.py` passes on the production copies
- [ ] Published in order: intake, digest, chaser
- [ ] First real executions watched in the Executions view
- [ ] Exports committed with messages that say why

## The handover

- [ ] README in the project repo: what it does, how it runs, where
      the keys and backups live, who owns it
- [ ] The four numbers baselined (Lesson 31): volume, failure rate,
      duration, concentration
- [ ] Showcase pull request opened (see showcase/README.md)
