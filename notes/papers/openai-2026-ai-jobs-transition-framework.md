# The AI Jobs Transition Framework: Mapping AI's Near-Term Impact on Jobs

- **Authors / Year**: Alex Martin Richmond (foreword: Ronnie Chatterji) / 2026 (OpenAI Economic Research, April 2026; EU extension June 2026)
- **Venue / Source**: OpenAI Economic Research report (`papers/OpenAI_the-ai-jobs-transition-framework_report.pdf`).
  - **File caveat:** the local PDF is **image-based (not text-extractable)** and its embedded metadata title is **"Beyond AI Exposure"** (the Svanberg et al. paper - see [[svanberg-2024-beyond-ai-exposure]]), which does **not** match the filename. This note was written from **OpenAI's published text** (cdn.openai.com/pdf/the-ai-jobs-transition-framework_report.pdf), fetched 2026-07-01. Confirm the local file actually is this report (it may be mislabelled).
- **Themes**: [[task-to-role-aggregation]], [[jobs]], [[automation-forecasting]]

## Research question(s)
- Which jobs will face near-term AI labour-market pressure - and of what kind (automate / reorganize / grow / little change)? Argues **exposure alone is too blunt**.

## Methodology
- **900+ (921) occupations, 99.7% of US employment**. Combines four occupation-level measures:
  1. **Theoretical exposure** - task-level LLM exposure from **Eloundou et al. (2023)**, aggregated to occupation as the **share of task time on exposed tasks** (i.e. the **linear time/importance-weighted roll-up**; see Appendix 2).
  2. **Observed exposure** - anonymized work-related **ChatGPT usage (H2 2025)** mapped to O*NET tasks -> occupations (the "capability overhang" = theoretical minus realized).
  3. **Human necessity** - GPT-5.4 classifies each occupation as regulatory/accountability, relational, or physical necessity.
  4. **Demand elasticity** - GPT-5.4-mini estimates own-price elasticity per occupation (response to a 10% price fall).
- Sorts occupations into **four archetypes**; net employment effect (Fig 6) = direct labour-saving + demand-driven scale effect for a 10% productivity shock. Validated against ChatGPT usage and CPS unemployment (2024Q1->2026Q1).

## Main results
- **18%** higher near-term automation risk; **24%** reorganize (headcount falls, workers still needed); **12%** grow with AI; **46%** less immediate change. "Not forecasts - a map."
- ChatGPT used **~3x** more in high-risk jobs; large **capability overhang** (e.g. high-risk jobs: realized 23.8% vs theoretical 90.0%) => exposure is a weak predictor of realized pressure.

## Relevance to AI economic impact - IS THIS A COMPETITOR TO WORKSTREAM A?
**Adjacent and validating, NOT a direct competitor on A's core.** Detail:
- **It does NOT fix the aggregation.** Within-occupation, OpenAI still uses the **linear time-weighted task-exposure sum** (Appendix 2); it *bolts on* necessity + elasticity as separate occupation-level filters. It does **not** replace the accounting-identity roll-up with a structural (CES / O-ring / bottleneck) job-production function - which is A's core contribution.
- **It explicitly names A's contribution as an unaddressed limitation.** Its Caveats section: *"a critical limitation... it simplifies how tasks are actually organized within occupations. Recent work underscores that the location of **bottlenecks and complementarities**... is critical... this framework may still **overstate substitution risk**... and miss the possibility that adoption unfolds in **threshold-like or bundled ways rather than smoothly**."* => the field leader concedes gap #2 is open.
- **It is descriptive/near-term, not forecasting.** Explicitly "not forecasts"; "our ability to forecast far into the future is limited." A is forward capability-forecast aggregation into timelines - different object.
- **Its economic layers are GPT-generated proxies**, flagged as "not a substitute for causal evidence." A would use structural estimates (Hampole) + real forecasts + a cost/profitability gate (which OpenAI lacks).
- **Overlap to respect:** it shares the "beyond exposure" thesis, the O*NET spine, Eloundou exposure, and a demand-elasticity/scale channel (adjacent to thread D). And it's from the field leader, moving fast (US Apr, EU Jun 2026).

**Implication for A:** OpenAI's framework is a natural **host/benchmark** - A supplies the **structural within-occupation aggregation layer their Q1 ("can AI do a meaningful share of the work?") is missing**, plus forecasting and bottleneck-threshold timing. Differentiate on those; position as complementary; move promptly given field velocity. This is arguably the **most important applied-field reference point** for the project.

## Limitations & open questions
- Linear within-occupation aggregation (the thing A replaces); GPT-proxy necessity/elasticity; no cost/profitability gate; no GE/spillovers; explicitly non-forecasting; self-flagged bottleneck/complementarity gap.
- Local PDF integrity/labelling unverified (see file caveat).

## See also
- [[task-to-role-aggregation]] - A supplies the structural aggregation this framework lacks.
- [[svanberg-2024-beyond-ai-exposure]] - the cost/profitability side (and the PDF's embedded title).
- [Eloundou et al. 2023](eloudou-2023.md) - the exposure measure OpenAI builds on *(note: create if missing)*.
