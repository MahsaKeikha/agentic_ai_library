# C08 Escalation package

**Goal:** Build a fixed handoff package when the agent should stop and a human specialist continues.

**Primary users:** Support, SRE, sales engineering.

**Human gate:** Escalation itself is the handoff to a human.

## Run

```bash
cd catalog/core/C08_escalation_package
python3 run.py --offline
```

## What you should learn

- Required fields for handoff  
- Why free form chat is a bad escalations format  

## Limits

This does not create a ticket in Jira or Zendesk. It writes a local package file.
