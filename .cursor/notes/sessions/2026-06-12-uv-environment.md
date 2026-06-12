# Initialize uv environment (pyproject, deps, tooling)

**Date:** 2026-06-12 12:24 (UTC+2)

## What changed
- Added `pyproject.toml`: project metadata, runtime deps (numpy, pandas, pymc, arviz, matplotlib, plotly) and a dev group (ruff, mypy, jupyterlab, ipykernel, pandas-stubs), plus Ruff and mypy config.
- Pinned Python to 3.12 (`.python-version`) and ran `uv sync` (creates `.venv` + `uv.lock`).
- Pinned `matplotlib<3.11` to work around `arviz-plots` 1.1.0 referencing the removed `matplotlib.style.core`.
- Added `src/paths.py` (canonical project paths) as the first shared module and a real mypy target.
- Updated README setup section; added `.mplcache/` to `.gitignore`.
- Recorded decision 0002 (pin Python 3.12).

## Current state / what's working
- `uv sync` succeeds on CPython 3.12.3; PyMC 6.0.1 / pytensor 3.0.5 import cleanly.
- `uv run ruff check .` passes; `uv run mypy` passes (1 file in `src/`).
- All key libs import (numpy 2.4.6, pandas 3.0.3, pymc 6.0.1, arviz 1.1.0, plotly 6.8.0, matplotlib 3.10.9).

## Open issues / blockers
- Matplotlib warns about a non-writable `~/.matplotlib`; set `MPLCONFIGDIR` to a writable dir if it recurs (sandbox-only nuisance).
- Dependency versions are bleeding-edge (PyMC 6, pandas 3, numpy 2); watch for incompatibilities.

## Next steps / TODO
- Add the first paper PDF and run the papers -> notes workflow end to end.
- Add a first EDA notebook once a dataset is available.
