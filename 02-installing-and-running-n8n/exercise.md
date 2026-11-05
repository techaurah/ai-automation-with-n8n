# Lesson 02: Exercise

## Make it yours, then break it safely

1. Change the timezone in `docker-compose.yml` to your own, restart the stack, and set the ping workflow's schedule to five minutes in the future. Watch it fire on time in Executions.
2. Add a second workflow of your own, anything with two nodes. Export it to a file in this lesson folder of your fork.
3. Now run `docker compose down` (without `-v`), bring the stack back, and verify both workflows survived. Delete the throwaway container state any other way you like, except the volume.
4. Write one paragraph in your notes: what exactly would you lose if the `n8n_data` volume were deleted, and where else in your setup that risk appears.

You are done when the scheduled ping fired at your local time and your paragraph names credentials and execution history, not just workflows.

## Solution

See `solution/SOLUTION.md` in this folder.
