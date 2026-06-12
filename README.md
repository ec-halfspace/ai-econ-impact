# AI Economic Impact

A research initiative studying the **economic impact of AI** - on jobs, working hours, sectors, wages, productivity, and more.

This repository is designed to act as a **second brain and research assistant**: it ingests papers, datasets, and theoretical models, and turns them into structured notes, exploratory analyses, and simulations.

## Repository structure

```
papers/            Raw research PDFs (input only)
notes/papers/      One Markdown note per paper (questions, methodology, results)
notes/concepts/    Thematic notes (impact on jobs, hours, sectors, wages, ...)
data/              Datasets
notebooks/         Exploratory data analysis
simulations/       Simulations from data + theoretical models in the papers
src/               Shared, reusable Python code
.cursor/rules/     Agent rules (project conventions and per-workstream guidance)
.cursor/notes/     Session log and decision records (see below)
```

## The three workstreams

1. **Papers -> notes.** Drop a PDF in `papers/`; it is parsed into a structured note in `notes/papers/`, and the findings are folded into a thematic note in `notes/concepts/`.
2. **Data & EDA.** Datasets go in `data/`; exploratory analysis lives in `notebooks/`, with each figure accompanied by a short note on the interesting pattern it reveals.
3. **Simulations.** Theoretical models and empirical estimates from the papers are operationalized in `simulations/` (including Bayesian models with PyMC).

Detailed conventions for each workstream are in `.cursor/rules/`.

## Getting started

This project uses [`uv`](https://docs.astral.sh/uv/) for environment and dependency management.

```bash
git clone <repo-url>
cd ai-econ-impact

uv sync                # creates .venv from pyproject.toml + uv.lock (Python 3.12)
uv run jupyter lab     # or: uv run python ...
```

Core libraries: pandas, numpy, matplotlib/plotly (visualization), PyMC + ArviZ (Bayesian work). The Python version is pinned to 3.12 (see `.python-version`) because PyMC/pytensor do not yet support 3.14.

### Tooling

| Purpose        | Tool   |
| -------------- | ------ |
| Env & deps     | `uv`   |
| Lint + format  | `Ruff` |
| Type checking  | `mypy` |

```bash
uv run ruff check .
uv run ruff format .
uv run mypy
```

Shared, reusable code lives in `src/` (e.g. `src/paths.py` for canonical project paths) and is type-checked by mypy.

## Working notes & decisions

To stay oriented across short, weekly sessions:

- **Session log** - `.cursor/notes/session-log.md` is the entry point. Start each session by reading it, then continue from the latest entry in `.cursor/notes/sessions/`.
- **Decision records** - `.cursor/notes/decisions/` documents choices ("we chose X over Y because Z").

## Maintenance

This README, the rules in `.cursor/rules/`, and the notes are **living documents** - keep them short and update them as the project evolves.
