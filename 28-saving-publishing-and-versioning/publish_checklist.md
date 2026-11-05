# The draft-to-publish routine (Lesson 28)

For every workflow that touches the real world:

## Before publishing

- [ ] Name follows the estate convention (system, job, version note)
- [ ] Trigger is the production one, tested against its test URL first
- [ ] No pinned data anywhere in the workflow
- [ ] Credentials are the production ones, named by purpose (Lesson 13)
- [ ] Error workflow is registered (Lesson 17)
- [ ] Placeholders (SELECT_ markers) are gone: run the export audit
- [ ] The workflow's notes state: owner, what it does, rerun safety
      (Lesson 19), and the approval gates it contains (Lesson 27)

## The publish itself

- [ ] Export the current live version first; keep it as the rollback
- [ ] Publish; run one real-shaped test through the production path
- [ ] Watch the first real executions in the Executions view
- [ ] Commit the exported JSON to git with a message that says why

## After

- [ ] Rollback file and its publish steps are findable by a colleague
- [ ] The change is in the changelog or team notes the same day
