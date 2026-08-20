# C09 Idempotent tool call

**Goal:** Calling the same tool twice with the same key does not double apply a side effect.

**Primary users:** Automation and workflow builders.

**Human gate:** Still approve real refunds or deploys. Idempotency prevents duplicates, not bad decisions.

## Run

```bash
cd catalog/core/C09_idempotent_tool
python3 run.py --offline
```

## What you should learn

- Idempotency keys  
- Safe retries  

## Limits

Demo uses a local ledger file. Real systems need durable stores.
