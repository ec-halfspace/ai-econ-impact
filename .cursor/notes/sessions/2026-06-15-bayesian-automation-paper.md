# Parse Bayesian AI-automation paper into research notes

**Date:** 2026-06-15 13:55 (UTC+2)

## What changed
- Ran the papers -> notes workflow end to end on the first PDF (`papers/bayesian-framework-for-forecasting-ai-automation.pdf`, Luo et al. 2026, Faculty AI).
- Created `notes/papers/luo-2026-bayesian-ai-automation.md` (research questions, 3-layer hierarchical Bayesian methodology, data sources, headline results, economic-impact relevance, limitations).
- Created two concept notes: `notes/concepts/automation-forecasting.md` and `notes/concepts/productivity.md`, cross-linked with the paper note.

## Current state / what's working
- First paper note + concept notes exist and are mutually cross-linked per the `papers-research-notes` rule.

## Open issues / blockers
- Concept notes currently synthesize a single paper; will need balancing as more papers land.
- Did not create `jobs.md`/`wages.md`/`by-sector.md` yet — this paper is feasibility-focused (software engineering only), so those felt premature.

## Next steps / TODO
- Add more papers and expand concept notes (esp. jobs, wages, by-sector) once multi-paper evidence exists.
- Consider a simulation/notebook reproducing the METR vs. Bayesian time-horizon trendlines.
