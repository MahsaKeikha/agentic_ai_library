# C07 Offline stand in client

**Goal:** Same call shape for live and offline so classrooms and CI never hard depend on a key.

**Primary users:** Teachers, open source maintainers, CI authors.

**Human gate:** Not a side effect demo. Still keep gates on real tools.

## Run

```bash
cd catalog/core/C07_offline_client
python3 run.py --offline
```

## What you should learn

- One interface, two backends  
- Offline path returns structured placeholders  

## Limits

Offline text is not a substitute for evaluation on real models.
