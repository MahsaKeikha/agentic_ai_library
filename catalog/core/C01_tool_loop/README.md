# C01 Single tool call loop

**Goal:** Show the smallest useful agent step: decide to call a tool, call it, read the result, stop.

**Primary users:** Beginners learning agent structure.

**Human gate:** None required for this demo. It only reads a fixture file. Do not point this pattern at write APIs without a gate.

## Run

```bash
cd catalog/core/C01_tool_loop
python3 run.py --offline
```

## What you should learn

- One tool, one observation, one stop condition  
- Why the model (or stand in) must not invent tool results  

## Limits

Offline mode uses a fixed stand in. It does not call external networks.
