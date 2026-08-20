# C02 ReAct style thought and act

**Goal:** Separate a short thought from a tool act and an observation.

**Primary users:** Anyone implementing explicit reasoning steps.

**Human gate:** Demo is read only. Add a gate before any tool that changes state.

## Run

```bash
cd catalog/core/C02_react_step
python3 run.py --offline
```

## What you should learn

- Thought, act, observe as three lines you can log  
- Why logging thoughts helps debugging  

## Limits

Thought text is a stand in. Live models may differ. Always log the real tool result, not a guessed one.
