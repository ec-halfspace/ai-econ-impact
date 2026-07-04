# Beyond AI Exposure: Which Tasks are Cost-Effective to Automate with Computer Vision?

- **Authors / Year**: Maja Svanberg, Wensu Li, Martin Fleming, Brian Goehring, Neil Thompson / 2024
- **Venue / Source**: MIT FutureTech / IDE working paper; SSRN 4700751
- **PDF**: no dedicated local PDF - but note: the embedded **metadata title of `papers/OpenAI_the-ai-jobs-transition-framework_report.pdf` is "Beyond AI Exposure"**, so the local file may actually be this paper (or a mislabel). This note is compiled from the public paper (fetched 2026-07-01); confirm the source file.
- **Themes**: [[task-to-role-aggregation]], [[automation-forecasting]], [[productivity]]

## Research question(s)
- Not "can AI do this task?" but **"is it cost-effective to build and deploy AI to do this task?"** - i.e. the **feasibility != profitability** gate that exposure measures ignore.

## Methodology
- First **end-to-end** AI-automation model: (1) technical performance needed for a task, (2) characteristics/cost of an AI system meeting it, (3) firm's **economic build/deploy decision** (AI cost vs. wage x time). Focus on **computer vision** (best-developed cost modelling).

## Main results
- **36%** of US non-farm jobs have at least one vision task exposed, but only **~23% of the associated worker wages** are **cost-effective to automate at today's prices** - exposure massively overstates near-term automation.
- Roll-out is **gradual, two-phase**: first the already-profitable tasks, then a slow tail gated by cost declines / AI-as-a-service scale. Implied job loss stays below normal job-turnover rates.

## Relevance to AI economic impact
- **The canonical reference for thread D (profitability gate)** and the empirical basis behind Acemoglu (2025)'s "profitable share". For workstream A: supplies the **cost-vs-wage filter** that should sit between task feasibility (Stage 1 `p`) and the structural aggregator, so A forecasts *profitable* automation, not just *feasible* automation.
- Complementary, **not** a competitor: it's a per-task cost model (vision), not an occupation-level structural aggregator; it doesn't model within-job task complementarity/bottlenecks.

## Limitations & open questions
- Computer-vision-specific cost curves; generalising to LLM/agent tasks needs new cost modelling.
- Point-in-time costs; sensitive to the assumed cost-decline trajectory and deployment model.
