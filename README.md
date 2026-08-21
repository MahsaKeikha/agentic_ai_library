# Agentic AI Library

A practical engineering library of **170 agentic AI and multi-agent systems** spanning executive operations, AI engineering, software, healthcare, neuroscience, robotics, science, education, legal and compliance, manufacturing, marketing, creative work, public-sector workflows, finance and risk, and personal productivity.

The goal is not to collect prompt demos. The library is organized around reusable engineering principles: specialized roles, explicit state, evidence discipline, orchestration, evaluation, failure handling, and human approval before consequential actions.

## AI Engineering Handbook Series

This repository is a companion engineering library for my **AI Engineering Handbook Series**. The books provide the conceptual and engineering foundation, while this repository provides practical agentic AI and multi-agent system implementations.

- **AI Engineering Handbook Series, Book 1:** https://a.co/d/0cbZnSMi
- **AI Engineering Handbook Series, Book 2:** https://a.co/d/07HnRY7H

## Mission

Build an open engineering reference collection of standalone multi-agent AI systems that is easy to run, easy to inspect, easy to compare, easy to cite, and difficult to misunderstand.

The project is designed around reproducibility, transparent architecture, evidence discipline, evaluation, safety, human authority, and cross-domain comparability. Recognition and adoption are goals, but technical credibility comes first.

Key project standards and strategy:

- [`Canonical Multi-Agent AI Reference Architecture`](docs/GLOBAL_REFERENCE_ARCHITECTURE.md)
- [`World-Class Multi-Agent AI Reference Standard`](docs/WORLD_CLASS_REFERENCE_STANDARD.md)
- [`Standalone Repository Acceptance Checklist`](docs/REPOSITORY_ACCEPTANCE_CHECKLIST.md)
- [`Trust and Adoption Roadmap`](docs/TRUST_AND_ADOPTION_ROADMAP.md)
- [`Reference Library Principles`](docs/REFERENCE_LIBRARY_PRINCIPLES.md)
- [`F30-F170 Standalone Repository Migration`](docs/STANDALONE_REPOSITORY_MIGRATION.md)

## Direct standalone repository links

The entries below link directly to the standalone repositories that currently exist for this migration cohort.

| ID | Multi-agent system | Direct repository |
|---|---|---|
| F30 | Agentic Corporate Governance | [Open F30](https://github.com/MahsaKeikha/agentic_corporate_governance) |
| F31 | Agentic ML Engineer | [Open F31](https://github.com/MahsaKeikha/agentic_ml_engineer) |
| F32 | Agentic MLOps Team | [Open F32](https://github.com/MahsaKeikha/agentic_mlops_team) |
| F33 | Agentic Data Engineering | [Open F33](https://github.com/MahsaKeikha/agentic_data_engineering) |
| F34 | Agentic Prompt Engineering | [Open F34](https://github.com/MahsaKeikha/agentic_prompt_engineering) |
| F35 | Agentic RAG Engineering | [Open F35](https://github.com/MahsaKeikha/agentic_rag_engineering) |
| F36 | Agentic Multi Agent Orchestrator | [Open F36](https://github.com/MahsaKeikha/agentic_multi_agent_orchestrator) |
| F37 | Agentic LLM Evaluator | [Open F37](https://github.com/MahsaKeikha/agentic_llm_evaluator) |
| F39 | Agentic AI Program Manager | [Open F39](https://github.com/MahsaKeikha/agentic_ai_program_manager) |
| F40 | Agentic AI Infrastructure Architect | [Open F40](https://github.com/MahsaKeikha/agentic_ai_infrastructure_architect) |
| F41 | Mobile App Engineering | [Open F41](https://github.com/MahsaKeikha/mobile_app_engineering) |
| F42 | Cloud Architecture | [Open F42](https://github.com/MahsaKeikha/cloud_architecture) |
| F43 | DevOps | [Open F43](https://github.com/MahsaKeikha/devops) |
| F44 | Kubernetes Operations | [Open F44](https://github.com/MahsaKeikha/kubernetes_operations) |
| F45 | Cybersecurity SOC | [Open F45](https://github.com/MahsaKeikha/cybersecurity_soc) |

F38 is intentionally not listed as a standalone repository here until its exact standalone repository is confirmed and validated.

## Standalone F30-F170 migration

The library is being upgraded so every F30-F170 system becomes its **own independently runnable GitHub repository**, not merely a folder or batch entry inside this umbrella repository.

A system is not marked as a verified standalone repository until the repository actually exists, runs offline, passes tests and CI, has genuine specialized-agent separation, documents architecture, evaluation, and safety, and is linked correctly from the canonical catalog.

## Clickable F01-F170 catalog

The full catalog is available at [`docs/AGENT_LINKS.md`](docs/AGENT_LINKS.md). During the F30-F170 migration, catalog entries must reflect the **actual** repository state and must not claim standalone status prematurely.

## Run the library from one place

The repository includes a unified launcher and a local browser dashboard.

List all F01-F170 systems:

```bash
python launcher.py --list
```

Run a unified system directly:

```bash
python launcher.py F35
```

Run with structured evidence/context:

```bash
python launcher.py F35 --json '{"corpus":"internal knowledge base","retrieval":"hybrid search"}'
```

Launch the browser dashboard:

```bash
python dashboard.py
```

Then open `http://127.0.0.1:8765`.

Full instructions: [`docs/LAUNCHER.md`](docs/LAUNCHER.md).

## Engineering philosophy

A useful multi-agent system needs more than several personas talking to one another. Systems are designed around specialized agents, structured inputs and outputs, traceable workflow state, explicit missing evidence, deterministic offline reference paths where practical, domain-specific evaluation, escalation and stop conditions, and human approval before consequential actions.

The shared engineering contract is documented in [`systems/STANDARD.md`](systems/STANDARD.md).

## Current architecture

- F01-F26 are established standalone flagship repositories.
- F27-F29 have individual system packages inside this repository.
- F30-F37 and F39-F45 have standalone repositories linked above.
- F38 remains pending standalone repository confirmation.
- Remaining F-series systems are being migrated to true standalone repositories under the reference standard above.
- C01-C10 provide reusable core patterns.
- Automated tests run through GitHub Actions on pushes and pull requests to `main`.

## Domains

| Range | Domain |
|---|---|
| F01-F30 | Flagship, executive, and leadership systems |
| F31-F40 | AI engineering |
| F41-F50 | Software engineering |
| F51-F60 | Healthcare |
| F61-F70 | Neuroscience |
| F71-F80 | Robotics |
| F81-F90 | Science |
| F91-F100 | Education |
| F101-F110 | Legal and compliance |
| F111-F120 | Manufacturing |
| F121-F130 | Marketing and growth |
| F131-F140 | Creative and media |
| F141-F150 | Government and public sector |
| F151-F160 | Finance and risk |
| F161-F170 | Personal and productivity |

## Testing

Run locally:

```bash
python -m pip install pytest
python -m pytest -q
```

GitHub Actions runs the umbrella test suite against supported Python versions.

## Safety and responsible use

The library separates decision support from consequential execution. Sensitive systems preserve scope limits and qualified review. Reference workflows should not silently invent missing facts or autonomously perform consequential actions such as clinical decisions, legal certification, financial transactions, physical robot control, industrial equipment commands, targeted voter persuasion, binding public decisions, or external submissions without appropriate authorization and safeguards.

## Repository structure

```text
agentic_ai_library/
├── launcher.py
├── dashboard.py
├── scripts/
│   └── create_standalone_repositories.py
├── docs/
│   ├── INDEX.md
│   ├── AGENT_LINKS.md
│   ├── ROADMAP.md
│   ├── LAUNCHER.md
│   ├── GLOBAL_REFERENCE_ARCHITECTURE.md
│   ├── WORLD_CLASS_REFERENCE_STANDARD.md
│   ├── REPOSITORY_ACCEPTANCE_CHECKLIST.md
│   ├── TRUST_AND_ADOPTION_ROADMAP.md
│   ├── REFERENCE_LIBRARY_PRINCIPLES.md
│   └── STANDALONE_REPOSITORY_MIGRATION.md
├── catalog/core/
├── systems/
├── tests/
└── templates/
```

## Author

**Mahsa Keikha**

Companion engineering library for the **AI Engineering Handbook Series** and related educational work.

**Mission:** build a transparent, reproducible, safety-aware reference collection of multi-agent AI systems that can be studied, tested, cited, and extended across domains.
