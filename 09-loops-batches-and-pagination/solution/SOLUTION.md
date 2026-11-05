# Lesson 09: Solution notes

Sequential ids make the hole findable exactly: after harvesting, compare the sorted id set against `range(min, max + 1)` and report the difference, here 14 and 15. Where ids are not sequential, the honest fallback is reconciling against a total the API reports (JSONPlaceholder exposes counts via headers on some endpoints; many business APIs include a `total` field), and where neither exists, the harvest cannot self-verify and the lesson is to say so in the run log rather than imply completeness.

**What to notice.** The failure was silent in both versions until verification existed. Data pipelines do not announce their gaps; they publish them, downstream, as wrong numbers with confident formatting. Verification is not paranoia, it is the job.
