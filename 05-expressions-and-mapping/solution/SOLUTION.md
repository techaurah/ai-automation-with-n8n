# Lesson 05: Solution notes

The date fields belong in the Edit Fields node because `appointment` arrives in its input: `{{ DateTime.fromISO($json.appointment).toFormat('yyyy-MM-dd') }}` and `{{ DateTime.fromISO($json.appointment).toFormat('EEE d MMM, h:mm a') }}`. The `priority` field cannot live there, because `due` is created downstream; it goes in the final Code node beside the `due` computation, or in a third small node after it.

That placement decision is the exercise's real content. Every n8n builder hits the sibling-field wall; the ones who understand it rearrange nodes in seconds, and the ones who do not spend an hour debugging an expression that was never going to see the value.

**What to notice.** The twin did not care where fields were computed. The workflow did. Data flows directionally, and the canvas makes that visible; learn to see it and half of n8n's mysteries evaporate.
