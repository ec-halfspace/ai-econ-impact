# O-Ring Automation

- **Authors / Year**: Joshua S. Gans, Avi Goldfarb / 2026 (NBER WP 34639, January 2026)
- **Venue / Source**: NBER Working Paper (not peer-reviewed)
- **PDF**: ../../papers/Gans_Goldfarb_2026.pdf
- **Themes**: [[task-to-role-aggregation]], [[automation-forecasting]], [[productivity]]

## Research question(s)
- How does automation play out when tasks are **quality complements** (O-ring), rather than separable as in the standard task/exposure model?
- What does this imply for the widely-used **linear task-exposure roll-ups**?

## Methodology
- Stylised model: a job/process needs `n` **essential** tasks; **output is the product of task qualities** (Kremer 1993 O-ring): `Y = prod_s q_s`. One worker allocates a fixed time endowment `h` across manual tasks (more time -> higher quality `q_s = a*h_s`); a machine can do a task at fixed quality for rental cost `r`. Firm chooses which tasks to automate; if any task stays manual, wage set by Nash bargaining. When a task is automated, the worker **reallocates freed time to remaining manual tasks** ("focus" mechanism).

## Main results (three messages)
1. **Task-by-task substitution logic is incomplete** - automating one task changes the return to automating the others (via reallocation + multiplicative complementarity).
2. **Automation decisions are discrete / bundle-like, with thresholds** - even when automation quality improves *smoothly*, the optimal number of automated tasks jumps; it can be unprofitable to automate the *first* task at the margin yet optimal to automate *many* together. **Undermines simple marginal adoption rules.**
3. **Labour income can RISE under partial automation** - automation scales the value of the remaining **bottleneck** tasks (opposite of separable-substitution intuition).
- **Headline implication:** "widely-used exposure indices, which aggregate task-level automation risk using **linear formulas, will overstate displacement when tasks are complements**. The relevant object is **not average task exposure but the structure of bottlenecks** and how automation reshapes worker time around them."

## Relevance to AI economic impact
- **This is the theoretical microfoundation for workstream A's gap #2** (the non-marginal / bottleneck-threshold regime). It formally proves the linear roll-up (TBI / Anthropic / AISI) overstates displacement under complementarity, and that adoption is threshold/bundled - exactly A's premise.
- **Positioning:** ASSET + citation cover, and a partial competitor to *claim* on the theory. A must **not** claim the theoretical O-ring/threshold insight as novel - Gans-Goldfarb own it. A's contribution is the **empirical operationalisation at occupation scale**: plug forecast task-success `p` + O*NET into an O-ring/bottleneck aggregator, produce **occupation automation forecasts/timelines**, and show they differ from the linear sum (and from Hampole's smooth statistics). Gans-Goldfarb is theory (single worker, no data, no forecasting, no O*NET calibration).
- Also touches **thread D**: the machine rental cost `r` + discrete adoption is a profitability/feasibility margin.

## Limitations & open questions
- Highly stylised: single worker, all tasks essential, homogeneous labour productivity, Nash bargaining; no empirical calibration, no occupations, no forecasting.
- Assumes strict multiplicative O-ring; real jobs are a **mix** of complementary and separable tasks (A will need a nested structure).
