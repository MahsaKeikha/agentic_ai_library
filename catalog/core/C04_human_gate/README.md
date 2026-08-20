# C04 Human approval gate

**Goal:** Block a side effect until a human sets approve to true.

**Primary users:** Anyone wiring agents to email, deploy, refund, or file changes.

**Human gate:** This example is the gate. Nothing sensitive runs unless you pass `--approve`.

## Run

```bash
cd catalog/core/C04_human_gate
python3 run.py --offline
python3 run.py --offline --approve
```

## What you should learn

- Default deny for side effects  
- Approval as an explicit argument or checklist item  

## Limits

`--approve` in a demo is not a real identity check. In production, bind approval to auth and audit logs.
