# Task-to-Role Aggregation (the Stage 1 -> Stage 2 seam)

How task-level automation forecasts get turned into statements about *jobs/roles* — and why this "fairly established" step is actually the fragile economic joint, not a solved plumbing problem.

## Summary
- The task-based framework (Acemoglu-Autor-Restrepo) treats a **job as a bundle of tasks**. To go from "how automatable is each task?" (Stage 1, see [[automation-forecasting]]) to "how exposed is each occupation?" (Stage 2), the standard move is a **linear, time-weighted roll-up**:
  `occupation_index = Σ_k w_k · p_k`, where `p_k` is task-k's automation/exposure score and `w_k` is task-k's share of work time.
- In Faculty's program map this seam (labelled "AISI Labour Market Impacts; Task>Role mapping via **O*NET & Blue Rose**") is marked **"fairly established"** — i.e. treated as off-the-shelf. See [[automation-forecasting]] and the 2026-06-19 brainstorm session note.
- **Central argument of this repo's research angle:** the roll-up is an **accounting identity, not an economic model of a job**. "Established" describes the *mechanics* (O*NET gives the tasks, the weights, and the crosswalks); it masks the *economics* (jobs are not separable sums of tasks). This seam — not Stage 1 capability forecasting — is the proposed contribution. See [[productivity]] for the related feasibility-vs-profitability gap.

## What the roll-up actually is (verified)
The Faculty Bayesian paper ([Luo et al. 2026](../papers/luo-2026-bayesian-ai-automation.md)) is **task-level only** (software engineering); it does **not** perform any task->role aggregation. The roll-up lives in the Stage-2 literature the map cites, where the linear time-weighted form is stated verbatim:
- **Tony Blair Institute (2026)**: "we aggregated these task-level results to the occupation level, **using weights that reflect the proportion of total work time spent on each task**." (O*NET, ~20k tasks, ~900 occupations; merged to UK Labour Force Survey.)
- **Anthropic Economic Index (Massenkoff & McCrory 2026)**: "the task-level coverage measures are **averaged to the occupation level weighted by the fraction of time spent on each task**."
- **AISI / IFOW pilot (2026, w/ Faculty)**: frames jobs as "bundles of tasks... formalised in O*NET"; benchmarks at the O*NET **Generalised Work Activity** level (chosen because GWAs generalise across most UK SOC2020 groups).

So the linear weighted-sum is the documented field standard, not a strawman.

### Data backbone
- **O*NET** (US DoL): ~873-900 SOC occupations, ~18-20k task statements, hierarchy Task -> Detailed Work Activity (DWA) -> Generalised Work Activity (GWA), plus importance/frequency ratings that supply the weights `w_k`. US-anchored (needs SOC2020/ONS bridging for the UK).
- **Blue Rose**: listed alongside O*NET as a task/role data source. **Not a recognised public dataset** in the AI-automation literature; most likely a proprietary/commercial source, a UK-specific (ONS/SOC2020) source, or an internal Faculty codename. Unconfirmed — would need Faculty's own Stage-2 spec to pin down.

## Why the linear roll-up is fragile (the economics it omits)
The practitioners themselves flag this. Anthropic (2026) raises and then sets aside the objection "with an eye toward simplicity":
- **Non-separability / O-ring** (Kremer 1993; Gans & Goldfarb 2025): output can require *all* tasks to succeed, so a job is closer to a Leontief bottleneck than a weighted average; partial task automation may yield ~zero impact until the last bottleneck task falls.
- **Task complementarities -> endogenous weights**: automating some tasks changes the value/time-share of the rest, so `w_k` is not fixed (Hampole et al. 2025: concentration of exposure can counteract mean exposure).
- **Reinstatement / new tasks** (Acemoglu-Restrepo): automation creates new tasks and re-bundles residual human work; a static task list misses this.
- **Remaining-task expertise** (Autor & Thompson 2025): what is left after automation may be the high-expertise core, changing wages/skill demand non-linearly.
- **Feasibility != profitability** (Acemoglu 2025; see [[productivity]]): a task automates only when AI cost < human cost *and* it is feasible — a filter the pure exposure roll-up ignores.

## Research threads on the seam (from 2026-06-19 brainstorm)
- **A. Structural task->role aggregator (flagship)** — replace `Σ w_k p_k` with a CES/nested + Leontief ("bottleneck") job production technology; estimate human-AI and task-task substitution elasticities.
- **B. Measurement crosswalk** — O*NET tasks are *not* labelled with the Luo et al. coordinates (human length `l`, messiness `m`); build & validate that crosswalk (LLM-assisted coding vs human raters, anchored on time-use/ATUS). Feeds "which statistics to collect".
- **C. Causal calibration** — use AI rollout shocks (ChatGPT/Copilot, occupation exposure) to estimate realised displacement/hours/wages and discipline the roll-up; critique potential-exposure-as-impact (AIOE/Eloundou) with shift-share caveats.
- **D. Profitability filter** — task automates when AI cost < wage x time AND feasible; answers "which roles, when, what saving" (ACN-relevant).
- **E. Re-roling dynamics** — re-bundling of non-automatable residual + net-new oversight/verification roles.

Proposed spine: **B (measure) -> A (specify economically-correct aggregation) -> C (validate causally).**

### Candidate aggregator specifications (thread A detail)
- **Nested CES + Leontief structure**: CES where human and AI labour substitute *within* tasks, with Leontief "bottleneck" tasks that must be completed for the job to produce - capturing the O-ring effect the linear sum misses.
- **Endogenous task assignment (Acemoglu-Restrepo style)**: tasks are allocated to AI vs. humans by comparative cost, with capital (compute) priced in - which folds the profitability filter in directly.
- **Estimable substitution elasticities** (human-AI and task-task), calibrated against real AI-rollout shocks so the aggregator is disciplined by data rather than assumed.

**Bootstrapping strategy**: start from Faculty's existing **software-engineering** task estimates (Paper 1) to build and test the aggregator on one occupation family, then extend across occupations as the GDPVal / EnterpriseVal results broaden task coverage to all knowledge work.

## Tensions / disagreements
- "Fairly established" (Faculty map) vs. "fragile joint" (this repo): both can be true — the *plumbing* is established, the *economic model of a job* is not.
- Mean exposure vs. O-ring/concentration: linear average vs. bottleneck/complementarity give materially different occupation rankings and displacement timing.
- Static vs. dynamic task sets: exposure roll-ups assume a fixed task bundle; reinstatement implies the bundle itself evolves.

## Open questions
- What is Faculty's *exact* Stage-2 aggregation formula, and does "Blue Rose" change the weighting (vs. plain O*NET time shares)? Not answerable from the repo's current `papers/`.
- Which production technology (CES vs. nested CES vs. Leontief-bottleneck) best fits observed occupation-level displacement?
- Can `w_k` be made endogenous and still kept estimable at scale across ~900 occupations?
- How to build and validate the O*NET <-> (`l`, `m`) crosswalk, and bridge US O*NET to UK SOC2020/ONS?

## Contribution stress-test vs. Hampole et al. (2025) (Goal 1, 2026-06-26)
Hampole et al. (2025, NBER WP 33509, "Artificial Intelligence and the Labor Market") is the closest prior work: a structural model where worker output aggregates tasks with task-specific capital substituting for labour and **endogenous time reallocation**, turning on labour-capital substitution + task complementarity, summarised by two sufficient statistics (**mean exposure** depresses demand; **concentration** offsets it via reallocation; shown to nest in Acemoglu-Restrepo 2018), and **estimated causally** via a university-hiring-network IV at firm x occupation x year granularity.

### What still survives - and where the real, defensible contribution is
Hampole is **backward-looking causal measurement** of realised AI effects 2010-2023 using NLP semantic-similarity exposure, estimating **local (marginal, 1-SD) responses**. That leaves four gaps it does not fill, and A should reposition onto them:

1. **Forecasting, not measurement.** Hampole tells you what AI *did* to labour demand. The Faculty programme needs to turn **forward capability forecasts** (Luo et al.'s compute-constrained task-success `p`; METR/GDPval time horizons) into occupation-level automation **timelines**. Nobody is structurally aggregating *those* forecasts. This is the Stage 1->2 bridge and it is genuinely open.
2. **The non-marginal / full-automation regime.** Hampole estimates responses to *small* exposure changes (1-SD). The AI question is what happens as `p->1` across many tasks. A Leontief/O-ring structure makes a distinct, sign-different prediction from Hampole's reallocation story: complementarity there means **near-zero impact until the last bottleneck task falls, then a discontinuous tip** - a timing/threshold claim, not a demand-cushioning claim. That is not in Hampole.
3. **Feasibility != profitability gating.** Hampole uses semantic exposure, not a cost filter. Integrating Acemoglu (2025) / Svanberg-style **AI-cost vs wage x time** gating into the aggregator (thread D) is distinct and ACN-relevant.
4. **The applied bridge into the pipelines that use the naive sum.** TBI / Anthropic / AISI still use the linear roll-up. Porting the structural insight into Faculty's actual forecasting stack is a real applied contribution (high value to Faculty + ACN), even if it is synthesis rather than new theory.

### Verdict (first pass)
- As written, A is **too close to Hampole et al. (2025) to be a strong *academic* contribution**. The "linear sum is naive, add complementarity + endogenous weights + causal estimation" angle is taken.
- A is **still a strong contribution if repositioned** onto: forecast aggregation (capability trajectories -> occupation timelines) + bottleneck/threshold timing in the non-marginal regime + profitability gating - i.e. a forward-looking, threshold-aware job-production model that *consumes* Stage-1 forecasts, rather than a backward-looking exposure-elasticity estimator.
- **(F) feasibility** is the next constraint: full structural estimation of task-level elasticities at scale is unrealistic; the realistic version is **calibrate the production structure + estimate a few key parameters + validate against rollout shocks** (and against Hampole's own estimates as a benchmark).
- **(I) impact** rests on demonstrating the bottleneck/threshold model gives **materially different occupation rankings and displacement timing** than both the linear sum *and* Hampole's smooth sufficient statistics. That is the empirical crux to design around.

### Hampole model read - gap #2 confirmed OPEN (2026-06-26)
Read Hampole's Section 2 model ([paper note](../papers/hampole-2025-ai-labor-market.md)). Their job is a **CES production function over tasks** with task-specific capital-labour substitution `nu`, workers reallocating one unit of time across tasks (`beta`). The famous **mean + concentration sufficient statistics come from a LOCAL second-order approximation around a symmetric equilibrium** (eq 13).
- **CES *can* represent complementarity** (Leontief bottleneck as `nu -> 0`), so the production form is not the obstacle.
- **But the delivered result does not cover gap #2**, for two reasons: (i) it is a *smooth marginal* approximation valid for ~1-SD exposure changes, not the non-marginal `p -> 1` regime; (ii) it models marginal labour-**demand reallocation** (concentration *cushions* demand), not the **timing of full automation** (the discontinuous "tip" when the last bottleneck task falls). Different objects. **=> the forecast-aggregation + threshold-timing angle is genuinely open.**

### What to borrow from Hampole as calibration (applied framing)
Hampole is an **asset**, not a competitor, here:
- **Functional form** - job-level CES over tasks + task-specific `nu`; adopt, then push `nu -> 0` for bottlenecks.
- **Two sufficient statistics** (importance-weighted **mean** `mu` and **concentration** `c`, eqs 21-24) - tractable, interpretable summaries computable from *forecast* `p` (adoptability).
- **Parameter magnitudes as calibration/validation targets** - the IV elasticities (**-14.5%** per 1-SD mean, **+7.5%** per 1-SD concentration, over 5 yrs) and `nu, chi, theta, beta, zeta, s_k`.
- **Weighting nuance** - Hampole weights by **O*NET task importance** (1-5), not the **time shares** TBI/Anthropic use; worth testing which matters.
- **Acemoglu-Restrepo (2018) mapping** (App. A.4) - read CES coefficients as endogenous task reassignment; links to the profitability gate.

### De-risking reads - DONE (2026-07-01)
All four reads completed; **none pre-empts A's repositioned contribution**, and two strengthen it materially:
- **[Gans-Goldfarb 2026, "O-Ring Automation"](../papers/gans-goldfarb-2026-o-ring-automation.md)** - the **theoretical microfoundation for gap #2**. Formally proves that under task quality-complementarity: (i) task-by-task substitution logic is incomplete, (ii) adoption is **discrete/threshold/bundled even when quality improves smoothly**, (iii) labour income can *rise* under partial automation. States outright that **linear exposure indices overstate displacement** and "the relevant object is not average task exposure but the structure of bottlenecks." => A must **not** claim the theory as novel (they own it); A's novelty is the **empirical, occupation-scale, forecast-driven operationalisation**.
- **[Autor & Thompson 2025, "Expertise"](../papers/autor-thompson-2025-expertise.md)** - a **complement, not a competitor**: a conceptual+retrospective model of how the *expertise of remaining tasks* drives wage/employment direction after automation. A wage/skill layer to add on top of A's timing model; not a forecast-ready aggregator.
- **[Acemoglu 2025, "Simple Macroeconomics of AI"](../papers/acemoglu-2025-simple-macroeconomics-ai.md)** - macro anchor for the **profitability gate (thread D)**: ~0.66% TFP / ~1% GDP over 10 yrs once only the *profitable* share is counted (20% exposed x 23% profitable = ~4.6% of tasks, 14.4% avg cost saving). **Verified against PDF (2026-07-01).** Backed empirically by **[Svanberg et al. 2024, "Beyond AI Exposure"](../papers/svanberg-2024-beyond-ai-exposure.md)** (only ~23% of vision-task wages cost-effective to automate).
- **[Acemoglu-Restrepo 2019](../papers/acemoglu-restrepo-2019-automation-new-tasks.md)** - the task-framework backbone (displacement / productivity / reinstatement); shared root of both Hampole and A.

### Competitor check: OpenAI AI Jobs Transition Framework (2026) - NOT a direct competitor
[OpenAI's framework](../papers/openai-2026-ai-jobs-transition-framework.md) (Richmond, Apr 2026; EU Jun 2026; 921 occupations, 99.7% US employment) is the closest **applied-field** artifact. Verdict: **adjacent + validating, not a competitor on A's core.**
- It still uses the **linear time-weighted task-exposure roll-up** within occupations (Appendix 2); it only *bolts on* human-necessity + demand-elasticity as separate occupation-level filters - it does **not** replace the aggregation with a structural job-production function.
- Its own Caveats section **explicitly names A's contribution as an open limitation**: "the location of **bottlenecks and complementarities**... is critical... may still overstate substitution risk... and miss the possibility that adoption unfolds in **threshold-like or bundled ways rather than smoothly.**"
- It is **descriptive/near-term, not forecasting**; its necessity/elasticity are GPT proxies; it has **no cost/profitability gate**.
- **Implication:** treat it as a **host/benchmark** - A supplies the structural aggregation their Q1 ("can AI do a meaningful share of the work?") is missing, plus forecasting + threshold timing. Field is moving fast (OpenAI shipped US + EU in 3 months) -> move promptly and position as complementary.
- **File caveat:** `papers/OpenAI_the-ai-jobs-transition-framework_report.pdf` is image-based and its embedded title reads "Beyond AI Exposure" (Svanberg) - may be mislabelled; note written from OpenAI's published text.

> **Framing update (2026-06-26, later):** the "too close to Hampole" verdict is judged against an *academic* bar. This workstream is **applied research** benchmarked against the **AI-automation-forecasting field** (TBI, Anthropic Economic Index, AISI/IFOW), which still uses the linear roll-up. Against that bar, Hampole flips from competitor to **asset** (calibration source + validation benchmark), and the contribution is "bring the best current economic structure into a forecasting field that still uses an accounting identity, and show it changes the answers." See `project-management/workstream-a-structural-task-role-aggregator.md`.

## See also
- [[automation-forecasting]] - the upstream Stage-1 task forecasts feeding this seam.
- [[productivity]] - feasibility-vs-profitability and the macro GDP/TFP stakes.
- [Luo et al. 2026](../papers/luo-2026-bayesian-ai-automation.md) - the Stage-1 paper (task-level; no roll-up).
- [Hampole et al. 2025](../papers/hampole-2025-ai-labor-market.md) - closest structural prior; CES-over-tasks aggregator + mean/concentration sufficient statistics; calibration asset for workstream A.
- [Gans-Goldfarb 2026](../papers/gans-goldfarb-2026-o-ring-automation.md) - O-ring/bottleneck theory; microfoundation for gap #2.
- [Autor-Thompson 2025](../papers/autor-thompson-2025-expertise.md) - expertise of remaining tasks; wage/skill layer.
- [Acemoglu-Restrepo 2019](../papers/acemoglu-restrepo-2019-automation-new-tasks.md) - task-framework backbone (displacement/productivity/reinstatement).
- [Acemoglu 2025](../papers/acemoglu-2025-simple-macroeconomics-ai.md) + [Svanberg et al. 2024](../papers/svanberg-2024-beyond-ai-exposure.md) - feasibility != profitability gate (thread D).
- [OpenAI AI Jobs Transition Framework 2026](../papers/openai-2026-ai-jobs-transition-framework.md) - closest applied-field artifact; adjacent/validating, not a competitor.
- `project-management/workstream-a-structural-task-role-aggregator.md` - the workstream-A project plan (applied framing locked).
- `.cursor/notes/sessions/2026-06-19-faculty-econ-impact-brainstorm.md` - origin of the threads A-E and the spine.
