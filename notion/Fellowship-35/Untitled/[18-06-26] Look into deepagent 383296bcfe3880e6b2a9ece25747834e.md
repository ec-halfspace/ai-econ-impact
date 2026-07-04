# [18-06-26] Look into deepagent

Status: In progress
Assign: Xiaoliang Luo, Anamaria Leonescu

inspect deepagent: [https://inspect.aisi.org.uk/reference/inspect_ai.agent.html#deepagent](https://inspect.aisi.org.uk/reference/inspect_ai.agent.html#deepagent)

Ken: I don’t think generate_loop or react really speak to the question of how harness design lifts model performance across task domains. The more interesting dimensions there are things like: how context is managed on long tasks, what tools the model actually has access to, whether there's any task-aware scaffolding, and how the harness handles context window exhaustion. So I think deepagent provides the right foundation to explore above questions.

One intuition is to start with looking at the failure modes of runs produced via generate or react (including successful runs but scored 0 against human solutions) and have a think about does any of the failure modes can be mitigated by customising any of the knobs provided by the deepagent interface.