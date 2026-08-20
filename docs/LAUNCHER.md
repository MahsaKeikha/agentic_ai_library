# Unified F01-F170 Launcher

The library includes two ways to explore and execute the catalog from one place.

## 1. Command-line launcher

List the full registry:

```bash
python launcher.py --list
```

Run a unified system:

```bash
python launcher.py F35
```

Run it with evidence/context supplied as JSON:

```bash
python launcher.py F35 --json '{"corpus":"internal knowledge base","retrieval":"hybrid search"}'
```

Or load a JSON file:

```bash
python launcher.py F61 --case examples/my_case.json
```

Record the explicit human approval flag where the target workflow supports it:

```bash
python launcher.py F40 --case examples/my_case.json --approve
```

F01-F26 are standalone repositories. Selecting one of those IDs returns the repository link rather than pretending the flagship is installed inside the umbrella repository.

## 2. Local web dashboard

Start the zero-dependency dashboard:

```bash
python dashboard.py
```

It opens:

```text
http://127.0.0.1:8765
```

From the browser you can:

- select any F01-F170 ID
- see whether it is a standalone flagship or local unified runner
- provide structured JSON context/evidence
- record the human approval flag
- execute F27-F170 and inspect the structured result
- follow the repository location for F01-F26

The dashboard uses only the Python standard library. It is a local demonstration interface, not a production SaaS deployment.

## What counts as runnable

F27-F30 load their dedicated `systems/Fxx_.../run.py` implementations. F31-F170 route to the appropriate domain batch module and call that system's `run_system` workflow. Missing inputs remain explicit rather than being invented.

## Production direction

A hosted commercial version can later place the same registry and launcher behind an authenticated API/UI, add model providers, persistent state, usage metering, organization workspaces, audit logs, and paid plans without changing the stable F01-F170 IDs.
