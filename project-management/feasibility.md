# Feasibility assessment - structural task->role aggregator (Workstream A, Phase 1)

> **Phase 1 deliverable (first deliverable) for workstream A.** This is the go/no-go gate before committing to the production stage. See the project plan [`workstream-a-structural-task-role-aggregator.md`](workstream-a-structural-task-role-aggregator.md) (section "Scope and deliverables").
>
> - **Owner:** Esther Chevrot
> - **Status:** in progress (structure below; verdict TBD)
> - **Purpose:** decide whether the structural aggregator can be specified, calibrated, and validated with the data available - and, if yes, produce a "calibrate-vs-estimate" scoping note for Phase 2.

## The five feasibility dimensions

Each is a distinct way the project could turn out to be infeasible, so each needs its own "can we actually do this?" answer. A "no" at any link is what the go/no-go gate is there to catch.

### 1. Data - do we have the inputs the model needs, at the right granularity?

The aggregator consumes task-level automation forecasts `p` and O*NET task structure; this checks whether those inputs actually exist and are usable.

- Task-level `p` from Luo et al. (2026) - currently software-only, and member-level Faculty access is still pending.
- O*NET task lists + time/importance weights - public, but indexed by O*NET tasks, not by Luo's `(l, m)` coordinates (hence the crosswalk dependency, thread B).
- Calibration / validation data - Hampole et al. (2025) published elasticities (to borrow parameter magnitudes) and AI-rollout shocks (ChatGPT/Copilot timing by occupation) to check predictions.

If the data isn't there or can't be linked, the rest is moot - so this is checked first.

### 2. Modeling formulation - what exactly is the production function, and how many knobs does it have?

This is the mathematical spec of the "job": CES *within* tasks (human and AI substitute), a Leontief *bottleneck* across tasks (the O-ring effect), endogenous time allocation, and the profitability gate. The feasibility concern is the **parameter count**: each substitution elasticity, the bottleneck degree (`nu -> 0`), and each time-allocation term is a free parameter. A rich model with hundreds of free parameters is a red flag because you can't pin them all down - which leads straight to identification.

### 3. Identification - can these parameters actually be pinned down from data, or only assumed?

The econometrician's core question. Even with data and a model, a parameter is only *identified* if the data can distinguish its value from other values. Here: can the human-AI and task-task substitution elasticities be **estimated** from what we have (Luo `p`, rollout shocks), or must they be **calibrated** (borrowed from Hampole's IV estimates and plugged in)? The output of this check is the **calibrate-vs-estimate call** - deciding, parameter by parameter, which ones we estimate and which we import. If nothing is identifiable, the model becomes pure assumption and the contribution weakens.

### 4. Uncertainty - can we carry the noise through, tractably?

The Stage-1 `p` are noisy (small samples, LLM-judge variance), so they are distributions, not point values. The aggregator must **propagate** that uncertainty into the occupation-level output (report a band, not false-precision). Feasibility question: can this be done analytically (cheap, closed-form), or does it need Monte Carlo (feed many sampled `p` vectors through the model)? Monte Carlo is doable but interacts with scale.

### 5. Scale / computation - does it run for one occupation now, and for ~900 later?

The MVP is one software occupation, which is tractable. But the eventual ambition is ~900 occupations x ~20k O*NET tasks. This checks whether the chosen formulation + uncertainty method stays computationally feasible at that size, or whether parameters must be shared/calibrated across occupations and the model simplified. Full per-task estimation at scale is a non-starter, so scale constraints feed back into the modeling and identification choices.

## How the dimensions chain

Data (do inputs exist?) -> Modeling formulation (how many parameters?) -> Identification (can we estimate them, or must we calibrate?) -> Uncertainty (can we propagate the noise?) -> Scale (does any of this survive at ~900 occupations?).

## Output / verdict  [TBD]

- **Go / no-go:** *TBD - to be filled once the five dimensions are assessed.*
- **Calibrate-vs-estimate scoping note:** *TBD - which parameters are estimated vs. imported from Hampole.*
