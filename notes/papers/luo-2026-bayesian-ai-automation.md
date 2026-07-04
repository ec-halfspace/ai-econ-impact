# A Bayesian framework for forecasting and scenario analysis of AI task automation under scaling constraints

- **Authors / Year**: Xiaoliang Luo, Hannan Saddiq, Rachel Asquith, Srish Bhasin, Jamie McGraw, Marc Warner (Faculty AI) / 2026
- **Venue / Source**: Working paper / preprint (Faculty AI). Correspondence: xiaoliang.luo@faculty.ai
- **PDF**: ../../papers/bayesian-framework-for-forecasting-ai-automation.pdf
- **Themes**: [[automation-forecasting]], [[productivity]]

## Research question(s)
- When will AI systems be capable of automating real-world (software engineering) tasks, once forecasts are grounded in *physical and algorithmic* limits rather than naive temporal extrapolation?
- How do competing assumptions about the binding constraints — electrical power supply, the share of power directed to AI training, and the rate/shape of algorithmic-efficiency progress — change projected automation timelines?
- Can previously disconnected datasets (power projections, training-compute histories, algorithmic-efficiency benchmarks, task performance) be unified so that uncertainty propagates across the whole causal chain from infrastructure to task-level outcomes?

## Methodology
- **Design**: Structural / causal forecasting model estimated via **hierarchical Bayesian inference**. Explicitly modular so any component can be swapped for counterfactual scenario analysis.
- **Three causal layers** (Figure 1a / Figure 5):
  1. **Power → compute**: U.S. total power capacity `Ptotal` × allocation share (`f_datacenter · f_AI · f_training / n_hyperscalers`) → power bound; modulated by Power Usage Effectiveness `u(t)` (falling over time) and utilization fraction `ϕ(t)` (rising, sigmoidal) → realized power `P`. Combined with sigmoidal training duration `T` → energy `E = P·T` → training compute `c` via a log-linear energy→compute law.
  2. **Algorithmic efficiency → effective compute**: time-varying efficiency `η(t)` converts raw compute to effective compute `c_eff = c·η`. Three interchangeable parametric forms for `η`: **scaled sigmoid** (saturating), **exponential** (unbounded), **sum of shifted sigmoids** (staircase / episodic breakthroughs). `c_eff` maps to general capability `Q` (Epoch Capabilities Index) via a log-linear scaling law.
  3. **Task automation**: logistic regression for task success probability `p`:
    `logit(p) = β0 + β1·m + β2·log10(l) + β3·log10(c)`, outcome `o ~ Bernoulli(p)`, where `l` = human completion time (task length), `m` = task "messiness" (complexity proxy, 0–16).
- **Identification via data partitioning**: a time-compute / time-capability frontier (top-5 by compute at release, or 2D Pareto on time vs. capability) informs power & compute scaling; a 3D time-capability-compute Pareto frontier (high capability at minimal compute) separately identifies algorithmic efficiency — separating scale from innovation.
- **Inference**: implemented in **NumPyro**, two-stage: (1) SVI to optimize prior hyperparameters by maximizing marginal likelihood; (2) full MCMC with NUTS for posteriors. Domain-knowledge priors (power-allocation fractions, PUE floor) are held fixed during SVI.

## Data
- **METR task benchmark** (Kwa et al. 2025): 170 real-world software-engineering tasks (HCAST 97; RE-Bench 7; SWAA 66 single-step) spanning ~1 min to 30 hours; 13 frontier models GPT-2 (2019) → Claude 3.7 Sonnet (2025); 8 runs/task. Task length = geometric mean of >800 human baselines (~5 yrs experience; 2,529 hours). Mean messiness 3.2/16.
- **Frontier training power / compute histories**: Epoch AI ML Systems Electricity dataset + All AI Models DB (You et al. 2025 / EPRI), calibrated on NVIDIA DGX H100 specs.
- **Algorithmic efficiency / capability**: Epoch Capabilities Index (ECI), a composite benchmark score (EpochAI 2025).
- **U.S. electrical capacity projections**: EIA Annual Energy Outlook 2025 (net summer capacity, reference/high/low growth, 2019–2050).

## Main results
- **Task-automation model fit**: accuracy 0.877 (F1 0.884, precision 0.896, recall 0.871); well-calibrated; posterior-predictive check p-value 0.964.
- **Power becomes binding**: physically-constrained model tracks historical training-power growth but projects a **significant slowdown beginning mid-2030s** as AI training demand hits structural limits of U.S. capacity and realistic efficiency gains — sharply below naive exponential extrapolation.
- **"Rising tide" of automation** (reference scenario): models limited to short, low-messiness tasks (~minutes) in 2022; by 2030, high success rates on **multi-hour tasks even under moderate messiness**; maximum reliably-handled task length (>50% success) moves from minutes toward days.
- **Compute cost of harder tasks**: maintaining a fixed success rate for longer or messier tasks requires an **exponential increase in compute** — a map for estimating resources needed to automate specific work.
- **Scenario analysis** (Figure 4): the three algorithmic-efficiency forms fit history near-identically (RMSE ≈ 5.3–5.4 on ECI) but **diverge sharply in forecasts** — exponential keeps accelerating; sigmoids plateau. Algorithmic-efficiency assumptions dominate timelines.
- **Investment share matters; aggregate power supply largely does not**: raising the datacenter-AI-training share (baseline ~1.74%; estimated power-envelope median share 0.71%) toward 3% or 8% lifts time horizons; switching EIA baseline/high/low *total* power growth has minimal effect — under baseline share, aggregate capacity growth can't keep pace with exponential training-compute demand.
- **vs. METR**: METR fits per-model logistic regressions on task length alone and extrapolates the 50% time-horizon exponentially (doubling ~every 7 months). This framework jointly models all systems with shared, physically-constrained effective compute plus continuous messiness — yielding differentiated, constraint-dependent (and generally more conservative) trajectories.

## Relevance to AI economic impact
- Provides a **transparent, updatable forecasting tool** ("living tool") for *when* categories of cognitive work (currently software engineering) become technically automatable — the upstream input to any jobs/wages/sector analysis.
- Reframes scaling laws in **human-labor units** (task length × messiness), making capability forecasts directly interpretable for workforce and sector planning.
- Section 3.4 explicitly separates **technical feasibility from economic impact**: adoption is still low (~10% of U.S. enterprises, Sept 2025; +4pp YoY); cites macro estimates — Acemoglu (2025) ~0.66% TFP gain → ~0.93–1.16% GDP over 10 yrs (assuming only 4.6% of tasks profitably exposed, 14.4% avg cost saving) vs. Goldman Sachs ~7% GDP. See [[productivity]].
- Flags that benchmarks beyond software engineering (GDPval — 44 occupations; Remote Labor Index — frontier agents <2.5% on end-to-end freelance work) imply automation of real economic work lags simplified benchmarks.

## Limitations & open questions
- **Software-engineering-only** task data; success criteria there are unusually well-defined and may not generalize to open-ended cognitive labor. Automated grading may inflate success (~24% of SWE-bench-passing PRs would be rejected by humans; Whitfill et al. 2026), which would flatten trendlines.
- **Training data omitted** as an explicit constraint (data-exhaustion debate unresolved).
- Models **fully-autonomous** performance only — ignores human-AI collaboration (evidence mixed: Becker et al. 2025 find AI slowed experienced devs; Patwardhan et al. 2025 find gains with expert oversight) and organizational-economics frictions (task bundling, coordination costs, joint-production attribution).
- Cannot anticipate **discontinuities** (test-time scaling, recursive self-improvement) that decouple capability from training-compute constraints.
- Functional form of `η` (number/spacing of breakthroughs `K`, `Δ`) is a **scenario assumption, not data-constrained**; forecasts are explicitly conditional, not predictions.
- Single-country (U.S.) power supply; aggregate capacity treated as roughly fixed envelope.
