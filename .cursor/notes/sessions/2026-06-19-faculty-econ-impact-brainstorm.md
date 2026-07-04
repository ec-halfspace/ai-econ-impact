# Brainstorm: Faculty Economic Impact Modelling program & where Esther contributes

**Date:** 2026-06-19 14:28 (UTC+2)

> Conversation/brainstorm session (no code; deliberately created **no** paper/concept notes per request). Goal was to (1) understand Faculty's program map, (2) brainstorm business-relevant research, (3) locate Esther's contribution given her profile: PhD + postdoc, applied microeconometrics, organizational economics, labor economics.

## What we did
- Parsed `papers/Faculty Economic Impact Modelling.pdf` — a one-page **program map** (June 2026), not a paper. It lays out a 3-stage pipeline: **tasks -> jobs/roles -> economy**.
- Confirmed abbreviations: **ACN = Accenture**; **Enterprise Val = a Faculty enterprise-task eval benchmark** (parallel to OpenAI GDPVal); **Blue Rose = a task/role data source** (alongside O*NET).
- Did a full pass over the map; went deepest on the **Stage 1->2 seam** (task-to-role mapping).

## The map (as parsed)
- **Stage 1 - "How fast are TASKS being automated?" (Faculty Forecasting Work):**
  - METR Time Horizon: software, unbounded, LLM-only.
  - Paper 1 (Faculty Bayesian Model): software, **bounded** (power/compute constraints), LLM-only. = `notes/papers/luo-2026-bayesian-ai-automation.md`.
  - Paper 2 (Knowledge Work Time Horizon): all knowledge work, bounded, LLM-only; GDPVal & Enterprise Val.
  - Paper 3 (Scaffolded Time Horizon): all knowledge work, bounded, **LLM + agentic harness**; GDPVal & Enterprise Val.
- **Stage 2 - "How fast are JOBS being automated & what does it mean?":**
  - AISI Labour Market Impacts: task efficiencies roll up to jobs; **Task>Role mapping (O*NET & Blue Rose)**; labelled "fairly established".
  - Faculty + ACN Workforce Planning proposals (help businesses plan).
  - "Which statistics to collect" (propose ONS & other indicators).
  - Re-roling / new jobs / jobs forecast.
- **Stage 3 - "What does it mean for the ECONOMY?":** build an economic model; forecast which sectors & countries win/lose.

## Key framing / decisions reached
- Intellectual backbone = **task-based automation framework** (Acemoglu-Autor-Restrepo lineage).
- **Central insight:** the Stage 1->2 seam that Faculty calls "fairly established" is actually the **fragile joint**. The naive roll-up `occupation index = sum_k w_k * p_k` is an accounting identity, not an economic model of a job. It breaks because of: non-separability/O-ring (Kremer 1993), task complementarities (endogenous weights), reinstatement/new tasks (Acemoglu-Restrepo), and feasibility != profitability (Acemoglu 2025; Svanberg/MIT). Paper 1 itself flags this gap (Williamson, Simon, Becker-Murphy, Holmstrom).
- **Esther's comparative advantage is NOT Stage 1 (capability/ML forecasting)** but the seams and Stages 2-3.

## Research threads identified for the seam (A-E)
- **A. Structural task->role aggregator** — replace linear roll-up with a CES/nested + Leontief("bottleneck") production technology for the job; estimable human-AI and task-task substitution elasticities. (Org-econ core; flagged as her **flagship**.)
- **B. Measurement crosswalk** — O*NET tasks are not labelled with Paper 1's coordinates (human length `l`, messiness `m`); build & validate that crosswalk (LLM-assisted coding vs human raters, anchored on ATUS/time-use). Ties to "which statistics to collect".
- **C. Causal calibration** — use AI rollout shocks (ChatGPT/Copilot, occupation exposure) to estimate realized displacement/hours/wages and discipline the roll-up; exposure-as-treatment with shift-share caveats. Critique AIOE/Eloundou as *potential exposure != impact*.
- **D. Profitability filter** — task automates when AI cost < human cost (wage x time) AND feasible; answers "which roles, when, what saving" (ACN-relevant).
- **E. Re-roling dynamics** — re-bundling of non-automatable residual + net-new roles (oversight/verification).

## Proposed "spine" (recommended program)
**B (measure) -> A (specify economically-correct aggregation) -> C (validate causally).** One coherent program that fixes the mislabelled "established" link, uses all three of her hats, and feeds both the ACN product and the Stage-3 macro model. (Stage 2 "which statistics to collect" is also a strong standalone, policy-facing deliverable that is squarely microeconometrics.)

## Open / undecided
- User skipped picking a single thread (A-E) to develop — spine framing proposed but not yet locked.
- Not yet turned any thread into a concrete research design (question / identification / data / deliverable).

## Next steps (for next session)
1. Decide whether the **A->B->C spine** is the right framing, or pick one thread to develop first.
2. Turn the chosen thread into a concrete research design: research question, identification strategy, data sources, deliverable.
3. Optionally stress-test the claim that Stage 1 is not where she should spend time.
4. Once a direction is locked, consider whether to write it up as a concept note (e.g. `notes/concepts/task-to-role-aggregation.md`) — was deliberately deferred this session.
