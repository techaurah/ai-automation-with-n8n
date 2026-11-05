# Lesson 31: Monitoring, cost, and scaling: running the estate on four numbers

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 17, 28, 29 · **You need:** Your instance. The twin runs on the sample data in this folder.

The production module closes with the operating habit that keeps everything else true: watching the estate on a small set of numbers, knowing what each execution costs on your chosen platform, and recognising the signals that say scale, in topology or in discipline, before users report them for you. The twin teaches the reading; the workflow skeleton wires it into the daily digest your Lesson 15 ladder already knows how to deliver.

## The four numbers

Run any estate on these, reviewed daily as a digest and weekly as a trend. **Volume**: executions per workflow per day; a sudden drop is as alarming as a spike, because silent triggers die quietly (an expired credential stops an intake without a single error to alert on, which is why Lesson 17's net cannot see it and this number can). **Failure rate per workflow**: not a global average, because one workflow at 40 percent hides inside an estate at 2 percent. **Duration**: the slowest runs and their trend; automations rot by slowing (bigger sheets, longer lists, an API degrading) long before they break. **Concentration**: which workflows consume the estate, in executions and in model spend where AI steps exist, because optimisation and Lesson 30's reviews both belong where the volume is.

The n8n surfaces: the Executions view for the human glance, the public REST API (API key from instance settings) for the programmatic digest this lesson's skeleton builds, execution data retention choices from Lesson 29 shaping what history you can trend, and on Cloud plans, the built-in insights and usage views. The method is platform-independent: sample data here, API there, same four numbers.

## Cost: executions, models, and attention

Cost has three currencies and beginners count only the first. **Platform cost**: self-hosted Community Edition has no per-execution charge, so its cost is the server and your operations time; Cloud meters executions (the pricing shapes from Lesson 00), so chatty designs (a workflow per form field, polling every minute) are literally a pricing decision. **Model cost**: AI steps bill per call in tokens on hosted models; the concentration number tells you which chain or agent eats the budget, and Lesson 20's per-step model choice is the lever. **Attention cost**: every alert, approval, and digest spends a human's focus, the scarcest currency, and Lesson 15's ladder is the budgeting tool. A mature estate review asks, quarterly: which automations earn their three costs, which should be batched, cached, or given a cheaper model, and which should be retired, because an automation nobody would rebuild is a liability with a schedule.

## Scaling signals and the honest responses

Scale problems announce themselves in the four numbers first: durations climbing (data growth outpacing the design: revisit Lesson 09 batching and Lesson 12 storage choices), failure rates rising at peak hours (the instance is saturated: queue mode and workers, Lesson 29, or shed load by scheduling heavy jobs off-peak), model spend concentrated in one classifier (a rules pre-pass from Lesson 24 takes the easy volume), and approval queues ageing (a human bottleneck: Lesson 27's graduated autonomy, earned by evidence). The discipline is to respond at the layer the signal names, rather than reflexively buying a bigger server for a design problem or redesigning around a capacity fact. Write the signal thresholds down (failure rate above X for Y days pages a review) so the response is a policy, not a mood.

## Run it

Run the twin (`python3 metrics_twin.py`) over `executions_sample.json` and read the table as an operator: the knowledge loader is your slowest and half its runs fail, which in a real estate review outranks everything else on the page. Then import `workflow.json`, point it at your instance with an API key credential, and run it once manually to see your real by-status counts. Finally, set the four numbers' review rhythm in your notes: the digest files daily as low (Lesson 15), the trend review is weekly, and name the thresholds that would page you.

## Common failures

- **Watching only failures.** A dead trigger produces no failures, just absence. Volume dropping to zero is an alarm; nobody configures it because nobody imagines success-shaped silence.
- **Global averages.** Estate-level 98 percent success can conceal the one workflow that handles money at 60 percent. Per-workflow, always.
- **Counting platform cost only.** The free self-hosted estate that pages its owner nightly is the most expensive system in the building. Attention is a cost line; budget it.
- **Scaling by vibes.** A bigger server applied to a batching problem buys a month. Read the signal, name the layer, respond there.

## Recap checklist

- [ ] I can produce the four numbers for my estate and read them as decisions.
- [ ] I can state each automation's cost in all three currencies, roughly and honestly.
- [ ] My scaling signals and thresholds are written down, with the layer each one points at.
- [ ] The daily digest runs on a ladder rung that respects attention.

## Resources

- [n8n: public REST API](https://docs.n8n.io/api/)
- [n8n: execution data settings](https://docs.n8n.io/hosting/configuration/environment-variables/executions/)
- [n8n documentation home](https://docs.n8n.io/)
- [n8n Academy, the official courses](https://learn.n8n.io)
