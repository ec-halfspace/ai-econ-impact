# Goal 3: timeline, deliverables & resourcing (workstream A)

**Date:** 2026-07-01 21:40 (UTC+2)

## What changed
- Filled the TBD sections of the project plan [workstream-a-structural-task-role-aggregator.md](../../../project-management/workstream-a-structural-task-role-aggregator.md):
  - **APPROACH** revised into **8 steps**, adding a **Feasibility-assessment gate (Step 2)** with a seeded issue list (elasticity count, identification, O*NET<->Luo `(l,m)` crosswalk dependency, noisy `p` propagation, scale, calibrate-vs-estimate). Renamed the old "bootstrap data" step to **"Simulations using Luo (2026) estimates on software engineering"**.
  - **MVP** settled: a de-risked single **software occupation** on **Luo (2026) `p`**, structural aggregator (CES + Leontief bottleneck + profitability gate) vs. weighted linear sum, compared on rankings + timing. Robust to the data-access blocker and field-velocity risk.
  - New **Resourcing and allocation** section: gate-tied ramps - stay solo at 1 d/wk through Steps 1-3; **Ramp-1** (Esther 1 -> 2.5 d/wk) at feasibility-gate-passed + spec-locked + first-simulation signal; **Ramp-2** (+ economist/DS @ ~50%) at scale-out (Step 8) / when data access lands.
  - **Timeline**: per-step effort-days (~28.5 d core), swimlanes, and two calendar scenarios - 1 d/wk ~= 29 wk vs. gated ramp ~= 17 wk to paper draft (~3 months saved).
  - Filled **Delivery** (weekly cadence; artifacts in `src/`/`simulations/`/`notes/`; end-of-Step-6 go/no-go checkpoint) and **Stakeholders**.
- Recorded decision [`0004 - gated resourcing model`](../decisions/0004-gated-resourcing-model.md) (ramp on milestones, not dates).

## Current state / what's working
- **Goal 3 done.** The project plan now has a concrete, resource-aware approach/MVP/timeline/delivery/stakeholders, and no remaining TBD sections except downstream contacts (Accenture, co-authors).
- The gated-resourcing logic keeps burn low until the feasibility gate + first positive signal, then ramps to capture the field-velocity upside.

## Open issues / blockers
- **Feasibility assessment (Step 2) not yet done** - it is the gate that fires Ramp-1; Goal 2 detail still to be worked.
- **Faculty member-level data access still pending** (GDPval scores, Bayesian trajectories, Stage-2 spec, "Blue Rose") - gates Ramp-2 / Step 8.
- Accenture (Stage 2-3) contact and academic co-authors still TBD.

## Next steps / TODO
- **Goal 2 (feasibility):** work the seeded Step-2 issue list into a go/no-go + calibrate-vs-estimate scoping note (count the elasticities; decide what is estimated vs. borrowed from Hampole).
- Begin **Step 3 (specification)** of the aggregator once the gate passes.
- Chase member-level Faculty/Notion access to unblock the later steps.
