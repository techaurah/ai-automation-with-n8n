# Repository tools

- `validate_workflows.py`: checks every workflow JSON in the repo
  (parses, unique node names, every connection target exists, AI
  sub-node connection types consistent). CI runs it on every push.
- `check_links.py`: checks that relative Markdown links resolve to
  files on disk. Run it before a release; external URLs are reviewed
  by humans, not by this script.

Run either from anywhere: `python3 tools/validate_workflows.py`.
