# Kelp release showcase

A disposable repository for demonstrating Kelp's phone-to-PR flow.

Demo prompt: Change the heading in README.md from "Kelp merge showcase" to
"Kelp release showcase". Leave all other files unchanged.

Expected outcome: Kelp prepares a one-line diff and runs the test suite.
Review and approve the candidate on the phone. Open the resulting PR and
check the diff. Merge it manually on GitHub after reviewing it.

The included repository-dispatch workflow and worker come from Kelp.
Configure them using docs/KELP_DEMO_BACKEND.md in Anshieee/kelp. Point the
demo backend's GITHUB_REPOSITORY and DEMO_ALLOWED_REPOS at this repository,
and scope the dispatch, read and publish credentials to it. Set DEMO_API_BASE
and the worker secrets on this repository's Actions settings. Keep all values
in the relevant secret store. Coordinate the repo switch with other demo users.

Local checks: python -m pip install -e '.[dev]' && python -m pytest -q

## Quick start

To install development dependencies and run the tests, use the following commands:

```bash
python -m pip install -e '.[dev]'
python -m pytest -q
```
