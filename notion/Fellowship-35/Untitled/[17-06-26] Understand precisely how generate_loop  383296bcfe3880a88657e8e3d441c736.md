# [17-06-26] Understand precisely how generate_loop and react differ

Status: Done
Assign: Anamaria Leonescu

- [ ]  What are the differences between two harnesses?
    - [ ]  Are they using the same system prompt?
        - no, ReAct has a short one appended before the gdpval task prompt
    - [ ]  Are they managing context the same way?
        - currently yes, as the tasks aren’t long enough to lead to any saturation
    - [ ]  Does react (with nudge) tend to produce longer trajectories?
        - not necessarily, it’s not super consistent across different tasks and sectors
    - [ ]  How is reasoning traces handled across iterations?
        - at the moment quite similar as we’ve been using o3 only so far and has in-built CoT

Conclusion: [Harnesses deep dive](../Harnesses%20deep%20dive%20380296bcfe3880948622ff84d3e26040.md)