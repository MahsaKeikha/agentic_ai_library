# F30-F170 Standalone Repository Migration

## Goal

Convert every F-number from **F30 through F170** into its own real GitHub repository and its own independently runnable multi-agent AI system.

The umbrella `agentic_ai_library` remains the canonical index, but the final catalog will point to a separate repository for each F-number.

This migration is governed by [`WORLD_CLASS_REFERENCE_STANDARD.md`](WORLD_CLASS_REFERENCE_STANDARD.md). Repository count alone is not the success criterion. Every repository must meet the engineering, documentation, evaluation, safety, reproducibility, and open-source hygiene requirements in that standard.

## Required quality bar

A generated F-system is accepted only when all of the following are true:

- the standalone GitHub repository actually exists
- it contains multiple specialized agents with distinct responsibilities
- the agents are coordinated by a real orchestrator with shared traceable state
- it runs offline without importing `agentic_ai_library`
- missing evidence remains explicit rather than being invented
- human approval cannot erase open risks
- domain-specific blocking conditions are tested
- runnable examples are included
- automated tests pass locally
- GitHub Actions passes
- architecture, agent, evaluation, safety, and extension documentation are present
- citation, contribution, security, changelog, version, and license metadata are present
- the umbrella catalog points to the real repository URL

## Target repository structure

Each standalone repository should converge on:

```text
agentic_<system>/
├── README.md
├── LICENSE
├── CITATION.cff
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── pyproject.toml
├── run.py
├── src/agentic_system/
│   ├── agents.py
│   ├── orchestrator.py
│   ├── models.py
│   ├── policies.py
│   └── evaluation.py
├── examples/
├── tests/
├── docs/
└── .github/
```

## Repository naming

Names follow stable descriptive slugs, for example:

- F30 `agentic_corporate_governance`
- F31 `agentic_ml_engineer`
- F35 `agentic_rag_engineering`
- F61 `agentic_parkinson_research`
- F170 `agentic_habit_builder`

The F-number itself remains stable even if implementation details evolve.

## Migration strategy

Do not generate 141 repositories blindly. Use quality-gated waves.

### Wave 1: Reference validation

Create F30-F35 first. Inspect each repository manually and verify cloning, offline execution, tests, CI, links, architecture docs, role separation, and safety gates.

```bash
python scripts/create_standalone_repositories.py --start 30 --end 35 --push
```

No later wave should proceed until the reference batch meets the world-class standard.

### Wave 2: AI and software engineering

Create F36-F50, validate CI and documentation, then update the master catalog.

### Wave 3: Healthcare, neuroscience, and robotics

Create F51-F80 with additional attention to domain safety boundaries and qualified-human review.

### Wave 4: Science, education, legal, manufacturing

Create F81-F120 and validate domain-specific red-team tests.

### Wave 5: Marketing, creative, public sector, finance, personal productivity

Create F121-F170 and complete final catalog validation.

## Preview

From the root of `agentic_ai_library`:

```bash
python scripts/create_standalone_repositories.py --dry-run
```

This prints the planned repositories without changing GitHub.

## GitHub authentication

Repository creation requires the GitHub CLI on an authenticated machine:

```bash
gh auth status
```

If needed:

```bash
gh auth login
```

The migration process must be resumable. Existing repositories should be detected and skipped unless an explicit update workflow is being performed.

## Verification after every wave

For every created repository:

```bash
git clone <repository-url>
cd <repository>
python run.py
python -m pip install pytest
python -m pytest -q
```

Also verify the GitHub Actions result and manually inspect all README/documentation links.

## Parent-catalog updates

Only after repositories actually exist, update:

1. `docs/AGENT_LINKS.md` to point to standalone repository URLs.
2. `launcher.py` to classify the migrated systems as standalone and return their repository URLs.
3. `README.md` to describe the actual final architecture.
4. `docs/INDEX.md` and `docs/ROADMAP.md` to reflect verified repository state.
5. Add maturity/version/status metadata to the catalog.

Never mark a system as standalone merely because a folder exists inside the umbrella repository.

## Final acceptance

The F30-F170 migration is complete only after all 141 repositories exist, their CI passes, their links resolve, their documentation matches their implementations, and the canonical `agentic_ai_library` catalog has been verified against GitHub.
