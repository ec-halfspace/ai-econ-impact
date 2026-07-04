# 0004 - Gated resourcing model for workstream A (ramp on milestones, not dates)

**Date:** 2026-07-01
**Status:** accepted

## Context
- Goal 3 needed to turn the project plan's TBD sections (MVP, delivery, stakeholders, timeline) into a concrete, resource-aware plan. See [`workstream-a-structural-task-role-aggregator.md`](../../../project-management/workstream-a-structural-task-role-aggregator.md).
- Current reality: **Esther is the sole contributor at 1 day/week.** The open questions were *if/when* to ramp her allocation (to ~2-2.5 days/week) and *if/when* to add a second person (economist/data scientist @ ~50%).
- Two live risks shape the answer: **field-velocity / being-scooped** (OpenAI shipped US + EU jobs-transition frameworks in 3 months) argues for speed; but **feasibility is not yet established** (elasticity count, identification, the O*NET<->Luo `(l,m)` crosswalk, scale) and **member-level Faculty data access is still pending**, which argue against committing resource early.

## Decision
- **Ramp allocation on project gates, not calendar dates.**
  - **Steps 1-3 (Foundation -> Feasibility gate -> Specification): stay at 1 day/week, solo.**
  - **Ramp-1 (Esther 1 -> 2.5 days/week)** when all hold: (a) feasibility gate passed, (b) specification locked, (c) the first software simulation shows early signal the structure changes the answer vs. the linear sum.
  - **Ramp-2 (add economist/DS @ ~50%)** at the Step 5 -> Step 8 boundary, strongest at Step 8 (occupation scale-out), also gated on Faculty data access landing.
- Also settled the **MVP** as a de-risked single software occupation on Luo (2026) `p` (robust to the data-access blocker), which is what makes the "stay lean until the gate" stance safe.

## Alternatives considered
- **Fixed-date staffing (e.g. commit 2.5 d/wk + a second person from week 1).** Rejected: pours resource into a project whose feasibility gate might shrink or reshape it, before there is any signal the structure changes the answer. High burn, low information.
- **Stay solo at 1 day/week throughout.** Rejected as the *default*: ~29 weeks (~7 months) to a paper draft is too slow given field-velocity risk; keeps the option but the gated ramp saves ~3 months.
- **Ramp on the calendar (e.g. "2.5 d/wk from week 4").** Rejected: dates are arbitrary when work is milestone-shaped and the feasibility gate outcome is unknown; tie the ramp to the gate instead.

## Rationale
- Allocation should step up **only as risk retires and the work shifts from thinking-bound to hands-bound.** Steps 1-3 are conceptual, single-owner, option-value work; Steps 4+ are execution-heavy and parallelizable. Gating the ramp captures the field-velocity upside (move fast once de-risked) without paying the burn of early over-staffing.
- Quantified payoff: gated ramp reaches a paper draft in ~17 weeks vs. ~29 weeks solo (~3 months saved) - and only spends the extra allocation after the feasibility gate + first positive signal.

## Consequences
- The **feasibility assessment (Step 2) becomes a real gate**, not a formality: its go/no-go and calibrate-vs-estimate scoping decides whether/when Ramp-1 fires.
- Need an explicit **early-signal check** in the first software simulation (does the structural aggregator diverge from the linear sum?) to trigger Ramp-1.
- Ramp-2 depends on **unblocking Faculty member-level access**; if it stays blocked, Step 8 (GDPval/EnterpriseVal extension) slips and the second-person hire should wait.
- Revisit if a hard external deadline appears (Faculty/ACN demo, paper submission) - that would convert the milestone-based timeline into a date-anchored one and could justify earlier ramping.
