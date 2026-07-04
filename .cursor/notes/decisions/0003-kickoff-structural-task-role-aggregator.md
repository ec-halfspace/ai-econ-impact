# 0003 - Kick off workstream A (structural task->role aggregator) as the flagship

**Date:** 2026-06-26
**Status:** accepted

## Context
- The 2026-06-19 brainstorm mapped Faculty's Economic Impact program (tasks -> jobs/roles -> economy) and identified five research threads (A-E) on the fragile Stage 1->2 seam (task-to-role aggregation). Thread **A** (replace the linear roll-up `occupation_index = sum_k w_k * p_k` with a structural CES/nested + Leontief "bottleneck" job-production technology) was flagged as Esther's flagship, given her profile (applied microeconometrics, organizational + labour economics).
- This session began scoping/drafting a project plan for workstream A. Goals: (1) stress-test whether the aggregator is a strong contribution vs. the current literature, (2) get an initial feasibility read, (3) produce an initial scoping/timeline/approach/deliverables view to refine over coming weeks.
- New evidence this session: parsed Faculty's exported **Fellowship-35** Notion material (`notion/Fellowship-35/`). It is the **Stage-1 capability/eval workstream** (operationalizing GDPval in AISI's Inspect; studying `Agent = Model x Harness`). It does **not** touch task->role aggregation. So the Stage 1->2 seam is unclaimed by the team closest to the task-level data.

## Decision
- Commit to **workstream A — the structural task->role aggregator — as the flagship project**, and scope it this session (stress-test + feasibility + initial plan), refining over the coming weeks.
- Treat the 2026-06-19 "spine" framing (B measure -> A specify -> C validate) as the surrounding program, with **A as the centrepiece** rather than committing to B or C first.

## Alternatives considered
- **Pick thread B (measurement crosswalk) or C (causal calibration) first** - both are strong and feed A, but they are enabling/validation layers; leading with A puts the economic contribution (the mislabelled "established" link) front and centre and best uses the org-econ comparative advantage. B and C remain in scope as support.
- **Contribute to Stage 1 (capability/harness forecasting)** - explicitly rejected: Fellowship-35 already owns this, it is ML/eval-engineering heavy, and it is not Esther's comparative advantage.
- **Defer choosing a flagship** (status quo after 2026-06-19) - rejected; the Notion finding (seam unclaimed) plus session goals make now the right time to lock A.

## Rationale
A over B/C/Stage-1 because: (i) it targets the actual economic gap (jobs are not separable weighted sums of tasks: O-ring/non-separability, endogenous weights, reinstatement, feasibility != profitability); (ii) it is squarely in Esther's wheelhouse (structural micro + org/labour econ); (iii) it is unclaimed by Faculty's Stage-1 team, so it is additive rather than duplicative; (iv) it can bootstrap on Faculty's existing task-level estimates (software from Paper 1; broader via GDPval's 44 occupations / 9 sectors) and feed both the ACN workforce product and the Stage-3 macro model.

## Consequences
- Need to turn A into a concrete research design (question / identification / data / deliverable) and a timeline - this session starts that.
- Data dependency: the most useful Faculty inputs (scored GDPval results, Bayesian-paper forecast trajectories, exact Stage-2 spec, "Blue Rose") are **not** in the current export and need member-level access; planned via the Notion MCP connector once Esther is added as a workspace member (guest access blocks MCP + most exports). Interim: the exported Fellowship-35 task board, error telemetry CSV, and charts are usable, but not the scored results.
- Inherits a measurement-error caveat from Stage 1: task-level `p_k` are noisy (small samples, judge variance) - A must propagate this uncertainty, not assume point estimates.
- Revisit if Faculty's own Stage-2 work turns out to be further along than the map suggests, or if member access reveals an existing aggregation effort.
