# The Simple Macroeconomics of AI

- **Authors / Year**: Daron Acemoglu / 2024-2025
- **Venue / Source**: Economic Policy (published 2025); NBER WP 32487 (May 2024)
- **PDF**: ../../papers/2025_Acemoglu_simple_economics_AI.pdf
- **Status**: **verified against PDF (2026-07-01)** - all headline numbers below confirmed from the source.
- **Themes**: [[productivity]], [[task-to-role-aggregation]], [[jobs]]

## Research question(s)
- What are the likely **aggregate (TFP / GDP) effects** of generative AI over ~10 years, using a task-based, cost-based lens rather than exposure counts? Are the large forecasts (Goldman Sachs, McKinsey) plausible?

## Methodology
- Task-based macro built on Acemoglu-Restrepo (2018, 2019, 2022): a final good needs many tasks allocated to capital or labour; automation expands the capital-performed set. Focuses on two channels - **extensive-margin automation** and **task complementarity** (sets aside deepening + new tasks for the main estimate).
- Central result - a version of **Hulten's theorem**: when AI's micro effects are task-level cost savings, `aggregate TFP gain ~= (fraction of tasks impacted) x (average task-level cost saving)`.
- Key discipline: **feasibility != profitability**. Uses Svanberg et al. (2024) to keep only the *profitable* share of exposed tasks, not all technically exposed ones.

## Main results (verified)
- **The task/cost chain:** ~**20%** of US labour tasks exposed to AI (Eloundou et al. 2023, aggregated to occupation and weighted by wage-bill share) x **23%** of exposed tasks profitably automatable (Svanberg et al. 2024, computer vision) => ~**4.6%** of tasks. Average **labour** cost saving **27%** (Noy-Zhang 2023; Brynjolfsson et al. 2023) -> **14.4%** average **overall** cost saving (via industry labour shares).
- **Headline:** TFP effect **<= 0.66%** over 10 years (~**0.064%/yr**); ~0.9% if bigger Peng et al. gains / GPU cost declines are added.
- **GDP:** **+0.93% to +1.16%** over the decade (capital stock rising proportionally to TFP); up to **+1.4% to +1.56%** under an Acemoglu-Restrepo (2022)-style larger investment response.
- **Refinement (hard-to-learn tasks):** early evidence is from *easy-to-learn* tasks (upper-bounded at ~73% of exposed tasks); assuming hard-task gains are ~1/4 of easy ones lowers the bounds to **TFP < 0.53%** and **GDP < 0.90%**.
- **Contrast with hype:** dwarfed by Goldman Sachs (~7% GDP / +1.5pp annual productivity) and McKinsey (+1.5-3.4pp annual GDP growth).
- **Wages / inequality:** productivity gains unlikely to raise wages much; AI can *increase* inequality even when it helps low-skill workers; unlikely to reduce inequality; **widens the capital-labour gap**; possible negative effect on low-education women's earnings.
- **Bad new tasks:** manipulation/attack tasks can inflate measured output while cutting welfare - illustratively AI could *appear* to add ~+2% GDP while reducing welfare by ~-0.72% (consumption-equivalent).

## Relevance to AI economic impact
- **The macro anchor for thread D (feasibility/profitability gate)** in workstream A: gives the headline that *exposure massively overstates near-term impact once cost is priced in*, and a quantitative template (profitable-share x cost-saving) for A's profitability filter.
- Complements [[task-to-role-aggregation]]: A's structural aggregator supplies the *meso* (occupation) layer between task feasibility (Stage 1) and this *macro* (economy) layer (Stage 3). Note the shared inputs - Eloundou (exposure) and Svanberg (cost) also underpin OpenAI's and A's work.

## Limitations & open questions
- Explicitly back-of-the-envelope and "speculative"; the profitable-share estimate is contested (depends on cost trajectories, AI-as-a-service scale - cf. Svanberg) and the CV-based 23% is extrapolated to all AI.
- Aggregate/macro; silent on the occupation-level aggregation A targets (no within-job bottleneck/complementarity structure).
- Deliberately excludes big **new-task**/reinstatement upside and science-transforming effects from the main number.
