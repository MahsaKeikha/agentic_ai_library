# Contributing

Thank you for helping this library stay useful.

## What we accept

- Small, runnable examples that teach one idea well  
- Improvements to docs, checklists, and offline reliability  
- Fixes that make human gates clearer  

## What we reject

- Examples that hide side effects or claim full autonomy in production  
- Huge dumps of generated text with no structure  
- Secrets, real customer data, or private keys  
- Wet lab procedures, exploit instructions, or anything unsafe to publish  

## Rules for every example

1. Runs offline without an API key  
2. Names a human gate in the README  
3. Keeps agents narrow  
4. Writes outputs to files under a clear folder  
5. Uses plain language in docs (no en dash or em dash characters in user facing text)  
6. States limits honestly  

## How to add a micro example

1. Copy `templates/micro_example`  
2. Rename agents and the run script  
3. Add fixtures under `fixtures/`  
4. Fill README with goal, users, how to run, and limits  
5. Add a row to `docs/INDEX.md`  
6. Open a pull request with a short note on what learners should take away  

## Voice

Write like a careful colleague. Prefer short sentences. Prefer concrete verbs. Avoid hype words like "revolutionary" or "autonomous everything."
