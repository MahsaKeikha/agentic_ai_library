# F30-F170 Standalone Repository Migration

## Goal

Convert every F-number from **F30 through F170** into its own real GitHub repository and its own independently runnable multi-agent AI system.

The umbrella `agentic_ai_library` remains the master catalog, but the production catalog will point to a separate repository for each F-number.

## What each new repository contains

Every generated repository is self-contained and includes:

- `README.md` with the system identity, domain, multi-agent team, run instructions, book links, and parent catalog link
- `agents.py` defining multiple specialized agents
- `orchestrator.py` coordinating agents through shared traceable state
- `run.py` standalone CLI
- `tests/test_system.py`
- `pyproject.toml`
- `.github/workflows/tests.yml` testing Python 3.10, 3.11, and 3.12
- `.gitignore`

The standalone repositories do not import `agentic_ai_library` at runtime.

## Repository naming

Names follow the existing style, for example:

- F30 `agentic_corporate_governance`
- F31 `agentic_ml_engineer`
- F35 `agentic_rag_engineering`
- F61 `agentic_parkinson_research`
- F170 `agentic_habit_builder`

## Preview first

From the root of `agentic_ai_library`:

```bash
python scripts/create_standalone_repositories.py --dry-run
```

This prints the complete F30-F170 creation plan without changing GitHub.

## Create a small validation batch

```bash
python scripts/create_standalone_repositories.py --start 30 --end 35 --push
```

Review those repositories before creating the remaining set.

## Create the entire F30-F170 catalog

```bash
python scripts/create_standalone_repositories.py --start 30 --end 170 --push
```

The script requires the GitHub CLI and an authenticated account:

```bash
gh auth status
```

If needed:

```bash
gh auth login
```

The migration is resumable. Existing repositories are skipped by default, so the command can safely be run again after an interruption.

## After creation

Once all repositories exist, update:

1. `docs/AGENT_LINKS.md` so F30-F170 point to their standalone repository URLs.
2. `launcher.py` so F30-F170 are classified as standalone systems and return their repository URLs.
3. `README.md` so the architecture accurately states that F01-F170 are standalone repositories.
4. `docs/INDEX.md` and `docs/ROADMAP.md` so the catalog reflects the final repository architecture.

Do not mark these systems as standalone repositories until the GitHub repositories actually exist.
