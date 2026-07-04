# Automation Forecasting (when will AI automate which tasks?)

How the field predicts *which* tasks AI can do and *when* — the upstream input to jobs, wages, and sector impact. For how these task-level forecasts get rolled up into occupations/jobs, see [[task-to-role-aggregation]].

## Summary
- The dominant empirical anchor is the **METR "time horizon"**: the length of task (in human completion time) a model can finish with 50% success, observed to double roughly every 7 months (Kwa et al. 2025). Naive extrapolation implies continued exponential capability growth.
- Recent work argues raw temporal extrapolation ignores **physical and algorithmic limits** (power, datacenter build-out lead times, algorithmic-efficiency saturation). [Luo et al. 2026](../papers/luo-2026-bayesian-ai-automation.md) builds a hierarchical Bayesian model linking power → compute → effective compute → task success, propagating uncertainty end-to-end and enabling scenario analysis.
- Forecasts are best treated as **conditional scenarios**, not predictions: outcomes depend heavily on assumptions about algorithmic-efficiency trajectory and the share of power directed to AI training.

## Evidence
- 50%-task-completion time horizon doubling ~every 7 months - METR (Kwa et al. 2025), via [Luo et al. 2026](../papers/luo-2026-bayesian-ai-automation.md).
- Physically-constrained model projects a **slowdown in training-power growth from the mid-2030s**, well below naive exponential extrapolation - [Luo et al. 2026](../papers/luo-2026-bayesian-ai-automation.md).
- Under a reference scenario, max reliably-automatable task length (>50% success, moderate messiness) moves from minutes (2022) to multi-hour by 2030, toward days by ~2040 - [Luo et al. 2026](../papers/luo-2026-bayesian-ai-automation.md).
- Maintaining a fixed success rate on longer/messier tasks requires **exponentially more compute** - [Luo et al. 2026](../papers/luo-2026-bayesian-ai-automation.md).
- Task-success model: accuracy 0.877, PPC p-value 0.964 on 170 METR software-engineering tasks - [Luo et al. 2026](../papers/luo-2026-bayesian-ai-automation.md).

## Tensions / disagreements
- **Continued exponential vs. saturation**: METR's exponential extrapolation vs. Luo et al.'s constraint-driven slowdown. The three algorithmic-efficiency forms (sigmoid / sum-of-sigmoids / exponential) fit history near-identically yet diverge sharply in forecasts — the choice is an assumption, not data-determined.
- **Which constraint binds**: Luo et al. find the *share* of power allocated to AI training matters far more than *total* power-supply growth scenarios.
- **Benchmark validity**: software-engineering success criteria are unusually clean; automated grading may overstate success (~24% of SWE-bench-passing PRs would be human-rejected; Whitfill et al. 2026). Broader benchmarks (GDPval, Remote Labor Index <2.5% on end-to-end freelance work) suggest real economic tasks lag.

## Open questions
- Does the framework extend beyond software engineering (finance, healthcare, legal), where messiness distributions and error costs differ?
- How to model **human-AI collaboration** rather than full autonomy (mixed evidence on whether AI speeds or slows experts)?
- Should training-data availability be an explicit constraint?
- How to anticipate discontinuities (test-time scaling, recursive self-improvement) that decouple capability from training-compute limits?
