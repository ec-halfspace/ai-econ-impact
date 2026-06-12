# 0001 - Tooling and repo structure

**Date:** 2026-06-12
**Status:** accepted

## Context
Bootstrapping a research repo that doubles as a second brain + RA for the economic-impact-of-AI workstream. Python stack with pandas/numpy/PyMC and matplotlib/plotly. Needed an environment manager, linter/formatter, type checker, and a directory layout.

## Decision
- Tooling: `uv` (env/deps) + `Ruff` (lint + format) + `mypy` (type checking).
- Structure: `papers/`, `notes/papers/`, `notes/concepts/`, `data/`, `notebooks/`, `simulations/`, `src/`.

## Alternatives considered
- Poetry + Black + Flake8/isort + mypy - more moving parts; Ruff replaces several tools.
- pip + venv - lighter, but uv is faster and reproducible.
- Pyright instead of mypy - viable; mypy chosen as the more common default for now.
- Flatter or numbered (`01_papers/`) layouts - rejected in favour of separating raw input (`papers/`) from derived notes (`notes/`) and shared code (`src/`).

## Rationale
uv + Ruff minimize tool sprawl and are fast; the nested layout cleanly separates inputs, derived knowledge, analysis, and reusable code, which the per-workstream rules can target with globs.

## Consequences
- `pyproject.toml` / `uv` environment still needs to be initialized.
- If type-checking needs grow (heavy notebook typing), revisit Pyright.
