# 0002 - Pin Python to 3.12

**Date:** 2026-06-12
**Status:** accepted

## Context
The system Python is 3.14. PyMC and its backend pytensor do not yet provide reliable support for 3.14, and the project depends on PyMC for Bayesian work.

## Decision
Pin the project to Python `>=3.12,<3.13` via `requires-python` and `.python-version`; uv fetches CPython 3.12.

## Alternatives considered
- Use system Python 3.14 - PyMC/pytensor install and import are not yet dependable on 3.14.
- Python 3.13 - newer, but less battle-tested across the full scientific stack at time of writing.

## Rationale
3.12 is well supported by the entire stack (PyMC, pytensor, numba, scipy) and keeps the environment reproducible via uv.

## Consequences
- Revisit and bump the pin once PyMC officially supports newer Python.
- Also pinned `matplotlib<3.11` to avoid an `arviz-plots` incompatibility (tracked in session notes).
