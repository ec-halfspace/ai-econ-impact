# Bootstrap: rules, README, notes system

**Date:** 2026-06-12 12:16 (UTC+2)

## What changed
- Scaffolded the repo: `papers/`, `notes/papers/`, `notes/concepts/`, `data/`, `notebooks/`, `simulations/`, `src/` (with `.gitkeep`).
- Added Cursor rules in `.cursor/rules/`: `project-overview` (always-apply), `papers-research-notes`, `data-eda`, `simulations`, and `session-logging` (always-apply).
- Added `README.md` introducing the project for new cloners.
- Set up the working-notes system: `.cursor/notes/session-log.md` (entry point), `sessions/` + `decisions/` with templates.
- Recorded decision 0001 (tooling and repo structure).

## Current state / what's working
- Rules and notes scaffolding are in place; globs reference real directories.
- No Python environment yet (no `pyproject.toml`).

## Open issues / blockers
- None.

## Next steps / TODO
- Initialize the `uv` environment and `pyproject.toml` with pandas, numpy, PyMC, matplotlib, plotly, plus Ruff and mypy config.
- Add the first paper PDF to validate the papers -> notes workflow end to end.
