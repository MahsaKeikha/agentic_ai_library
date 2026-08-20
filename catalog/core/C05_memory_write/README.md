# C05 Structured memory write

**Goal:** Persist agent notes as files so the next step does not rely on chat history alone.

**Primary users:** Builders of multi step agents.

**Human gate:** Not required for local note files in this demo. Protect real customer data with access control.

## Run

```bash
cd catalog/core/C05_memory_write
python3 run.py --offline
```

## What you should learn

- Working memory versus files on disk  
- Stable paths for notes and drafts  

## Limits

Local files are not a full vector database. Use this pattern first, then add search when needed.
