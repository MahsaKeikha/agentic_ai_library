# C06 Checklist driven editor

**Goal:** Run edits against a fixed checklist so quality does not depend on memory of the prompt alone.

**Primary users:** Writers, support leads, anyone reviewing agent drafts.

**Human gate:** Human still signs off before send. The checklist is a helper, not a substitute.

## Run

```bash
cd catalog/core/C06_checklist_editor
python3 run.py --offline
```

## What you should learn

- Checklist as code you can version  
- Report of pending items  

## Limits

Offline mode marks items in a simple way. Live models can fill notes per item, but humans still decide.
