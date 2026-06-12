"""Canonical paths for the project, so notebooks and scripts avoid brittle relative paths."""

from __future__ import annotations

from pathlib import Path

ROOT: Path = Path(__file__).resolve().parents[1]

PAPERS: Path = ROOT / "papers"
NOTES: Path = ROOT / "notes"
PAPER_NOTES: Path = NOTES / "papers"
CONCEPT_NOTES: Path = NOTES / "concepts"
DATA: Path = ROOT / "data"
NOTEBOOKS: Path = ROOT / "notebooks"
SIMULATIONS: Path = ROOT / "simulations"


def data_file(name: str) -> Path:
    """Return the path to a dataset in ``data/`` (existence is not checked)."""
    return DATA / name
