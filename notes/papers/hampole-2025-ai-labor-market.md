# Artificial Intelligence and the Labor Market

- **Authors / Year**: Menaka Hampole, Dimitris Papanikolaou, Lawrence D.W. Schmidt, Bryan Seegmiller / 2025 (NBER WP 33509; Feb 2025, rev. Sep 2025)
- **Venue / Source**: NBER Working Paper (not peer-reviewed)
- **PDF**: ../../papers/Hampole_al_2025.pdf
- **Themes**: [[task-to-role-aggregation]], [[jobs]], [[productivity]]

## Research question(s)
- Through which channels does AI affect labour demand, and why are aggregate employment effects muted even when task-level substitution is strong?
- How do task-level AI exposures aggregate to occupation-level labour-demand changes once workers can **reallocate effort** across tasks and firms can grow?

## Methodology
- **Design**: structural model + causal IV estimation. The piece directly relevant to workstream A is the **model of task->occupation aggregation**.
- **Job-level CES production technology over tasks** (eqs 6-7): task-specific capital substitutes for labour *within* a task with elasticity `nu`; elasticity across occupations within firm `chi`; across firm output `theta`. Workers choose a job (occupation-firm, Fréchet taste shocks, labour-supply elasticity `zeta`) and **allocate one unit of time across tasks**; effective task labour `l(j) = alpha(j)^beta h(j)^(1-beta)`, where `beta` governs decreasing returns to effort / scope for reallocation (smaller `beta` => more reallocation).
- **Key derivation = a LOCAL (second-order) approximation around a symmetric equilibrium** (eq 13). Employment growth ~ `zeta * eta_m * m(eps)` (first order) + `(zeta/2) * beta * eta_o^2 * C(eps)` (second-order correction) + firm spillovers + aggregate spillovers.
  - **Mean exposure** `m(eps)` (eq 14): O*NET-importance-weighted average task exposure. Depresses labour demand; sign via `eta_m` depends on `nu - chi` (task substitution vs. occupation demand elasticity).
  - **Concentration** `C(eps)` (eq 15): importance-weighted variance of exposure across tasks. **Raises** labour demand (workers reallocate to unaffected tasks; log-wage convexity / Jensen). Importance via `eta_o`, function of `nu`, `psi`, `beta`.
- **Empirical analogues** (eqs 21-24): `AI Exposure Average = mu_{o,f,t} * log(1+N_{f,t})` and `AI Exposure Concentration = c_{o,f,t} * log(1+N_{f,t})`, weights `omega_{o,j}` = **O*NET task importance scores (1-5, rescaled to sum to 1)**.
- **Identification**: shift-share IV for firm AI adoption = (pre-AI 2005-09 university hiring shares) x (2014-18 share of a university's grads entering AI occupations). Exposure = NLP semantic similarity between firm AI applications (extracted from Revelio/LinkedIn resumes via Llama 3.1 70B) and O*NET task statements.

## Data
- Revelio Labs (~58M LinkedIn profiles, ~14M postings linked to Compustat firms), 2014-2023 (postings 2010-23; profiles back to 2005 for the instrument). O*NET tasks/importance; Compustat firm outcomes. US, public firms, white-collar-skewed.

## Main results
- 1-SD higher task-level AI exposure => ~2% lower relative demand for related skills (within firm-occupation-year).
- **Preferred IV**: +1-SD **mean** task exposure => **-14.5%** within-firm occupation employment share over 5 years; +1-SD **concentration** => **+7.5%**. Net occupation effects are **muted** (countervailing reallocation + firm-growth spillovers); ~14% of variation in occupational employment-share growth attributable to AI exposure.
- Exposure peaks ~90th wage percentile (white-collar), but concentrated exposure mitigates displacement; mean-concentration correlation only ~0.67, so they are distinct margins.
- **Appendix A.4**: the *same* mean+concentration estimating equation arises in **Acemoglu-Restrepo (2018)** automation-threshold model; their CES is a reduced form of task reassignment (coefficients reflect endogenous labour/capital division); reassignment behaves like a higher `nu`.

## Relevance to AI economic impact
- **For workstream A this is the closest structural prior — and, under the applied framing, a calibration/benchmark ASSET, not a competitor.** What A can borrow:
  - **Functional form**: job-level CES over tasks + task-specific capital-labour substitution (`nu`) - a ready nested structure to adopt, then push into the non-marginal regime (drive `nu -> 0` for Leontief bottlenecks).
  - **Two sufficient statistics** (mean `mu`, concentration `c`), importance-weighted - tractable, interpretable summaries A can compute from *forecast* `p` (good for adoptability).
  - **Empirical construction** (eqs 21-24) and **O*NET importance weights** `omega_{o,j}` - note this differs from the *time-share* weights TBI/Anthropic use.
  - **Parameter magnitudes** as calibration targets / validation moments: the -14.5% (mean) and +7.5% (concentration) per-1-SD 5-year elasticities; `nu, chi, theta, beta, zeta, s_k`.
  - **A-R (2018) mapping** (App. A.4) - cover to read CES coefficients as endogenous task reassignment, linking to the feasibility/profitability gate.

## Limitations & open questions
- **The headline result is a LOCAL second-order approximation around a symmetric equilibrium** -> valid for *marginal* (1-SD) exposure changes, **not** the non-marginal `p -> 1` regime that matters for AI. **This is why workstream-A gap #2 (bottleneck/threshold timing) is genuinely open**: although CES *can* represent complementarity (Leontief as `nu -> 0`), Hampole's delivered model (i) is a smooth approximation and (ii) describes marginal labour-*demand reallocation*, not the *timing of full automation* (the discontinuous "tip" when the last bottleneck task falls). Those are different objects.
- Backward-looking **measurement** (2010-23, mostly pre-GenAI), semantic-similarity exposure - no **forecasting** of capability trajectories. A replaces `eps` with forward task-success forecasts `p` (Faculty Bayesian; METR/GDPval).
- No **feasibility-vs-profitability** cost filter (semantic exposure only).
- US public firms, white-collar-skewed resume data; "missing intercept" (year FE) => identifies only *relative* cross-job shifts, silent on level effects.

## See also
- [[task-to-role-aggregation]] - the seam this paper informs; Goal-1 stress-test positioning.
- [Luo et al. 2026](luo-2026-bayesian-ai-automation.md) - the Stage-1 forecasts A would aggregate.
- [[productivity]] - Acemoglu (2025) feasibility/profitability + macro stakes.
