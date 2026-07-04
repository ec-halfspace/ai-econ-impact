# Harnesses deep dive

<aside>
💡

*We define the harness as the series of actions undertaken by the agent or agentic framework to solve the problem given.*

*In this definition space, a corollary is that **Agent = Model x Harness.***

</aside>

![Screenshot 2026-06-22 at 15.58.01.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_15.58.01.png)

# Background - harnesses in InspectAI

## Solvers - default generate()

A [**solver**](https://inspect.aisi.org.uk/solvers.html) is the **Inspect AI procedure that defines how an eval is executed.** Their purposes range from providing system prompts and prompt engineering (e.g. chain-of-thought), to model generation, self-critique, multi-turn dialog, and running agentic harnesses.

A solver is a Python `async` function that takes the key data structure, called `TaskState` (prompt, messages, tools, sandbox) and a `generate` function, transforms the state, and returns it. Prompt engineering solvers modify `messages`; generation solvers call the model, append its response, and update `output`.

InspectAI provides a range of in-built solvers, such as:

- **`system_message()` / `user_message()`** — insert messages into the conversation
- **`prompt_template()`** — rewrites the user prompt using a template
- **`chain_of_thought()`** — asks the model to reason step-by-step before answering
- **`generate()`** — simply calls the model and captures the output
- **`self_critique()`** — sends the model's answer to another model for critique, then regenerates an improved answer
- **`multiple_choice()`** — formats A/B/C/D style questions and handles answer parsing

When running the GDPval tasks using the current codebase, the default `solver` is InspectAI’s `generate()` - it generates output from the model, and appends it to the task message history. The key parameter is `tool_calls`(here, a Python or bash command), which controls how the model handles tool use:

- **`"loop"`** (default) — resolves tool calls and then re-invokes `generate()`, proceeding in a loop that terminates when there are no more tool calls, or a `message_limit` or `token_limit` is exceeded.
- **`"single"`** — resolves at most a single set of tool calls and then returns.
- **`"none"`** — does not resolve tool calls at all; you'd need to invoke `call_tools()` directly.

Here, `generate()`involves a chain of steps:

`use_tools([bash, python])` →`generate(tool_calls="loop")` → `extract_deliverable_files()` 

On the other hand, `Generate` is a protocol (it’s callable) that takes a `TaskState` as its first argument, calls the model, and returns an updated `TaskState`. `generate()` **the solver** is essentially just a thin wrapper that calls `Generate` **the function:**

```jsx
async def solve(state: TaskState, generate: Generate) -> TaskState:
	return await generate(state)
```

## Agents - ReAct

Apart from standalone solvers, agents (like [ReAct](https://inspect.aisi.org.uk/react-agent.html)) live separately under `inspect_ai/agent/`  (see `_react.py`, `_as_solver.py`), but can get plugged into the solver chain via `as_solver()`. This is also helpful because it means that custom solvers could include multiple agents.

`react()` is a general purpose agent based [on this paper](https://arxiv.org/abs/2210.03629). It is the most common architecture used in agent frameworks and is the baseline against which you should measure more complex agents (according to InspectAI).

In a core ReAct loop, the model reasons, calls tools, sees the results, and repeats — until it explicitly signals it's done via a special `submit()` tool:

![Screenshot 2026-06-22 at 15.58.01.png](Harnesses%20deep%20dive/93f7c0f8-3672-417d-947a-d4b1e5b6aa69.png)

If the model stops calling tools it is encouraged to continue, or to call `submit()` if it believes it has completed the task.

The reason for using an explicit `submit()` tool rather than just stopping when tools aren't called is deliberate: in some cases models will unintentionally stop calling tools (e.g. write a message saying they are going to call a tool and then not do it). The use of an explicit `submit()` tool call works around this problem, as the model can be encouraged to keep calling tools rather than terminating.

- Some key features of `react()` according to the API wrapper in`.venv/lib/python3.12/site-packages/inspect_ai/agent/_react.py.`
    
    ![Screenshot 2026-06-18 at 16.48.08.png](Harnesses%20deep%20dive/Screenshot_2026-06-18_at_16.48.08.png)
    

The default `AgentPrompt()` is later on passed via `agent/_types.py`:

```jsx
PARALLEL_TOOLS_PROMPT = "Prioritize parallel tool calls: when operations 
are independent, run them in one response — e.g. reading several files or 
running several searches at once — rather than one at a time. Only sequence 
calls when one depends on another's result."

DEFAULT_ASSISTANT_PROMPT = f"""You are a helpful assistant attempting to submit 
the best possible answer. You have several tools available to help with finding 
the answer. You will see the result of tool calls right after sending the 
message. {PARALLEL_TOOLS_PROMPT} Do some reasoning before your actions, 
describing what tool calls you are going to use and how they fit into your plan.
"""

DEFAULT_SUBMIT_PROMPT = """When you have completed the task and have an answer, 
call the {submit}() tool to report it.
"""
```

- *Note that there is a `basic_agent()` older solver version which is constructed like ReAct (`.venv/lib/python3.12/site-packages/inspect_ai/solver/_basic_agent.py`).
    
    ![Screenshot 2026-06-18 at 16.41.27.png](Harnesses%20deep%20dive/Screenshot_2026-06-18_at_16.41.27.png)
    

## The difference between *generate()* and *react()*

Because `generate()` is by default a solver, it will **not** call another prompt on top of the GDPval task prompt. The `tool_calls` default is set as ‘`loop’`, i.e. the model will keep calling tools (in ‘loops’) until it will generate text (such as a concluding message) or exceed the message or token limit.

Although `react()` is passed as a solver using the `as_solver()` wrapper, its architecture is that of an agent, i.e. it will include other instructions for tool use, reasoning-before-action, parallel tools, explicit submission etc. Here, it will automatically append the DEFAULT_ASSISTANT_PROMPT and DEFAULT_SUBMIT_PROMPT to the GDPval task prompt. By construction, it will only stop when the model calls `submit()` - even if no tool is called, the model might go back and try to improve the current `TaskState`.

<aside>
💡

TLDR

Given the current defaults, there are **two big differences** between `generate()` and `react()`:

1. Only `react()` uses a default prompt via the InspectAI API. Currently, it’s [this one](Harnesses%20deep%20dive%20380296bcfe3880948622ff84d3e26040.md).
2. When the model thinks it’s done completing the task, `react()` calls `submit()`. Otherwise, it keeps going in `tool_call`loops (in fact it sometimes does that by e.g. checking the location of the current deliverable files). `generate()` doesn’t do this, it only stops when it simply doesn’t call any more tools (in many prompts it will give a concluding message that it has already produced the required deliverables of the task).

But ultimately their core design will be similar - read the task prompt, think about how to solve it via the calling the tools available in loops, at some point finish the loop and output the deliverables. Both have the exact same tools available.

</aside>

## Discussion of tasks ran with generate() and react()

As a starting point of adapting different harnesses to solving tasks in GDPval, ~5 tasks were run for each sector using o3 model with both `generate()` and `react()` → see them [here](../Fellowship-35%20367296bcfe38803e849bdd32bf3d1c37.md). There didn’t seem to be any consistent change in the scores.

![Screenshot 2026-06-22 at 10.37.56.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_10.37.56.png)

Some metrics comparison for the react vs generate tasks one by one (using averaged values for the same task) across different sectors are shown below. 

You can see a plot comparing all metadata per task here (you need to download the file and open in browser): 

[solver-comparison_generate_react_scores.html](Harnesses%20deep%20dive/solver-comparison_generate_react_scores.html)

Some empirical findings:

- The task completion time per task with `react()` is slightly shorter than for `generate()` (doesn’t include the scoring time).
    
    ![Screenshot 2026-06-22 at 16.56.23.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_16.56.23.png)
    
- *Model calls* are the number of LLM calls in the eval log (each assistant generation step, whether or not it invokes a tool):

![Screenshot 2026-06-22 at 16.46.13.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_16.46.13.png)

- There are on average more model calls (and subsequently tool calls) for react() than generate(), but that is to be expected given that in react() the model is explicitly asked to make a plan and to call a submit() function.

![Screenshot 2026-06-22 at 10.33.26.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_10.33.26.png)

- There  doesn’t seem to be any correlation between how many bash and Python tool calls are being made and the average score per task.

![Screenshot 2026-06-22 at 17.13.35.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_17.13.35.png)

## **CoT traces analysis**

For the preliminary data obtained by running ~5 tasks/ sector using o3 with ReAct, some of the CoT traces were qualitatively analysed side-by-side with the corresponding ones for the default runs (o3 with generate).

For the prompt examples, ReAct is shown on the LEFT side, and generate on RIGHT. These are examples of evals; the repeats for the same task might show different tool calls.

#### ReAct ~ generate

1. Task 96 (retail-trade) - same score (1), slightly longer time for completion of generate(), similar model turns (3 with ReAct, 2 with generate)
- ReAct initially, the assistant drafts a more comprehensive plan than generate

![Screenshot 2026-06-22 at 11.16.17.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_11.16.17.png)

- then ReAct takes an extra step to double-check the quality of the output (generate doesn’t do this); as a result, it also does a tool call for submit()

![Screenshot 2026-06-22 at 11.20.17.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_11.20.17.png)

- they both score 1, and it seems like both explanations are fair; the deliverables are quite similar in quality, but react seems to be more comprehensive and clearer (but I am not an expert)

![Screenshot 2026-06-22 at 11.22.59.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_11.22.59.png)

1. Task 111 (manufacturing) → same score for both, react takes less time than generate
- longer initial reasoning for react

![Screenshot 2026-06-18 at 11.20.18.png](Harnesses%20deep%20dive/Screenshot_2026-06-18_at_11.20.18.png)

#### ReAct > generate

1. Task 162 (Real estate) - better score for ReAct, tool calls:1 8 with ReAct, 10 with generate
- both solvers start by trying to find a way to open and parse the pdf provided; reasoning is encrypted by provider for these steps. this seems to take much longer for ReAct (10 calls) wrt generate (5 calls)
- **React overall tries to call more tools that are not available, whilst generate seems to first check what is provided and think about how to use these.**
- the final evaluation for ReAct is again quite comprehensive:
    
    ![Screenshot 2026-06-22 at 11.42.48.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_11.42.48.png)
    

#### Generate > ReAct

1. Task 146 (also retail trade) - generate score ~2x than React (1 vs 0.55); similar completion time
- the react trace shows more planning - initially the model is confused by some of the goals, but then reasons what the required steps actually are; the generate trace indicates a clearer plan
- when looking at the eval with score 0 for ReAct, it seems like that was awarded solely because of naming a file wrongly (the one mentioned in the trace below. All generate evals were scored 1, or 2 runs timed out due to the judge timeout being set as 120s rather than 300s usually used for the other evals

![Screenshot 2026-06-22 at 12.51.50.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_12.51.50.png)

- the generate case shows ‘excitement’ in some evals?! → ‘I feel good about this’, ‘I am excited to try this’, ‘I can’t wait to implement this’

1. Task 117 (healthcare, scoring better for generate in general) - generate score x2 than react (0.625 vs 0.33); similar completion times
- this task required more calculations, and it seems like React tried multiple times but in the end got them wrong - however the plots required were better than in the golden deliverable; Generate included a longer text prompt for calculating the same parameters (this was roughly halfway through the tool calls)
    
    ![Screenshot 2026-06-22 at 13.28.26.png](Harnesses%20deep%20dive/Screenshot_2026-06-22_at_13.28.26.png)
    

#### Other examples

1. Task 52 → same score, slightly more tool calls on average for react; React takes longer than generate
- React shows multiple tool calls for the same action:
    
    ![Screenshot 2026-06-18 at 14.31.47.png](Harnesses%20deep%20dive/Screenshot_2026-06-18_at_14.31.47.png)
    

Qualitatively, it seems like the ReAct tasks do the final internal evaluation (before submit) after similar tool calls as generate().