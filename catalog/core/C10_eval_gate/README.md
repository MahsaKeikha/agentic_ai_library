# C10 Evaluation gate

**Goal:** Block promotion of a prompt or agent change unless a small golden set still passes.

**Primary users:** Teams who fear silent quality regressions.

**Human gate:** Humans choose the golden set and the pass threshold.

## Run

```bash
cd catalog/core/C10_eval_gate
python3 run.py --offline
```

## What you should learn

- Tiny regression set beats vibes  
- Fail closed when score drops  

## Limits

Checks here are string rules. Real systems add model judges and human review samples.
