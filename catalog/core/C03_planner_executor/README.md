# C03 Planner then executor

**Goal:** Plan steps first, then execute them in order without replanning every time.

**Primary users:** Builders of multi step workflows.

**Human gate:** Approve the plan before execution when steps can change production data.

## Run

```bash
cd catalog/core/C03_planner_executor
python3 run.py --offline
```

## What you should learn

- Plan artifact separate from execution log  
- Easier review and reuse of plans  

## Limits

Planner output here is fixed offline. In live mode, still review plans that call write tools.
