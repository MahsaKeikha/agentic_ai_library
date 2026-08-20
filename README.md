# Agentic AI Library

A practical engineering library of **170 agentic AI and multi-agent systems** spanning executive operations, AI engineering, software, healthcare, neuroscience, robotics, science, education, legal and compliance, manufacturing, marketing, creative work, public-sector workflows, finance and risk, and personal productivity.

The goal is not to collect prompt demos. The library is organized around reusable engineering principles: specialized roles, explicit state, evidence discipline, orchestration, evaluation, failure handling, and human approval before consequential actions.

## AI Engineering Handbook Series

This repository is a companion engineering library for my **AI Engineering Handbook Series**. The books provide the conceptual and engineering foundation, while this repository provides practical agentic AI and multi-agent system implementations.

- **AI Engineering Handbook Series, Book 1:** https://a.co/d/0cbZnSMi
- **AI Engineering Handbook Series, Book 2:** https://a.co/d/07HnRY7H

## Run the library from one place

The repository now includes a unified launcher and a local browser dashboard.

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

Then open `http://127.0.0.1:8765`. The dashboard lets you select an F-number, provide JSON context, record a human-approval flag, and inspect the structured result. F27-F170 execute from this repository. F01-F26 are standalone flagships, so the launcher returns their repository locations rather than pretending they are installed locally.

Full instructions: [`docs/LAUNCHER.md`](docs/LAUNCHER.md).

## Current status

**F01-F170 are represented in the library and integrated into `main`.**

- F01-F26 are standalone flagship repositories.
- F27-F170 use the unified `systems/` architecture.
- C01-C10 provide small reusable core patterns.
- Automated tests run through GitHub Actions on pushes and pull requests to `main`.
- `launcher.py` provides one CLI entry point.
- `dashboard.py` provides a zero-dependency local web interface.

See [`docs/INDEX.md`](docs/INDEX.md) for the full catalog and [`docs/ROADMAP.md`](docs/ROADMAP.md) for domain organization.

## Library at a glance

| Range | Domain | Architecture |
|---|---|---|
| F01-F26 | Standalone flagship systems | Dedicated repositories |
| F27-F30 | Executive and leadership | Unified individual packages |
| F31-F40 | AI engineering | Unified batch |
| F41-F50 | Software engineering | Unified batch |
| F51-F60 | Healthcare | Unified batch |
| F61-F70 | Neuroscience | Unified batch |
| F71-F80 | Robotics | Unified batch |
| F81-F90 | Science | Unified batch |
| F91-F100 | Education | Unified batch |
| F101-F110 | Legal and compliance | Unified batch |
| F111-F120 | Manufacturing | Unified batch |
| F121-F130 | Marketing and growth | Unified batch |
| F131-F140 | Creative and media | Unified batch |
| F141-F150 | Government and public sector | Unified batch |
| F151-F160 | Finance and risk | Unified batch |
| F161-F170 | Personal and productivity | Unified batch |

## Engineering philosophy

A useful multi-agent system needs more than several personas talking to one another. Unified systems are designed around specialized agents, structured inputs and outputs, traceable workflow state, explicit missing evidence, deterministic offline reference paths where practical, domain-specific evaluation, escalation/stop conditions, and human approval before consequential actions.

The shared engineering contract is documented in [`systems/STANDARD.md`](systems/STANDARD.md).

## Standalone flagships F01-F26

| ID | Repository | Focus |
|---|---|---|
| F01 | [agentic_book_writer](https://github.com/MahsaKeikha/agentic_book_writer) | Book chapter pipeline with ship gate |
| F02 | [agentic_research_lab](https://github.com/MahsaKeikha/agentic_research_lab) | Academic research pipeline |
| F03 | [agentic_biotech_rd](https://github.com/MahsaKeikha/agentic_biotech_rd) | Biotech R&D planning |
| F04 | [agentic_tech_support](https://github.com/MahsaKeikha/agentic_tech_support) | Support workflow with send gate |
| F05 | [agentic_online_shop](https://github.com/MahsaKeikha/agentic_online_shop) | Online-shop case handling |
| F06 | [agentic_debug_automation](https://github.com/MahsaKeikha/agentic_debug_automation) | Incident debugging and automation |
| F07 | [agentic_software_design](https://github.com/MahsaKeikha/agentic_software_design) | Senior software design package |
| F08 | [agentic_ceo_assistant](https://github.com/MahsaKeikha/agentic_ceo_assistant) | CEO daily briefing |
| F09 | [agentic_ai_safety](https://github.com/MahsaKeikha/agentic_ai_safety) | AI safety review |
| F10 | [agentic_phd_assistant](https://github.com/MahsaKeikha/agentic_phd_assistant) | PhD research-week assistant |
| F11 | [agentic_account_manager](https://github.com/MahsaKeikha/agentic_account_manager) | B2B account management |
| F12 | [agentic_robotics_governance](https://github.com/MahsaKeikha/agentic_robotics_governance) | Robotics AI safety and governance |
| F13 | [agentic_qa_safety_manager](https://github.com/MahsaKeikha/agentic_qa_safety_manager) | QA and AI safety management |
| F14 | [agentic_client_inquiry_bot](https://github.com/MahsaKeikha/agentic_client_inquiry_bot) | Client inquiry workflow |
| F15 | [agentic_fullstack_web](https://github.com/MahsaKeikha/agentic_fullstack_web) | Full-stack web engineering specs |
| F16 | [agentic_engineering_professor](https://github.com/MahsaKeikha/agentic_engineering_professor) | Engineering course and lecture preparation |
| F17 | [agentic_immigration_assistant](https://github.com/MahsaKeikha/agentic_immigration_assistant) | Immigration workflow support, not legal advice |
| F18 | [agentic_real_estate](https://github.com/MahsaKeikha/agentic_real_estate) | Real-estate workflow support |
| F19 | [agentic_psychologist_assistant](https://github.com/MahsaKeikha/agentic_psychologist_assistant) | Psychology-practice templates, not therapy |
| F20 | [agentic_dating_advisor](https://github.com/MahsaKeikha/agentic_dating_advisor) | Adult dating coaching with safety/send gate |
| F21 | [agentic_coo_assistant](https://github.com/MahsaKeikha/agentic_coo_assistant) | COO operations and KPI workflow |
| F22 | [agentic_cfo_assistant](https://github.com/MahsaKeikha/agentic_cfo_assistant) | CFO forecast, variance, and risk workflow |
| F23 | [agentic_board_advisor](https://github.com/MahsaKeikha/agentic_board_advisor) | Board package and governance workflow |
| F24 | [agentic_chief_of_staff](https://github.com/MahsaKeikha/agentic_chief_of_staff) | Executive priorities and follow-up |
| F25 | [agentic_strategy_consultant](https://github.com/MahsaKeikha/agentic_strategy_consultant) | Competitive strategy workflow |
| F26 | [agentic_venture_capital_analyst](https://github.com/MahsaKeikha/agentic_venture_capital_analyst) | Evidence-aware venture due diligence |

## Unified systems F27-F170

| Range | Domain | Representative systems |
|---|---|---|
| F27-F30 | Executive | M&A Advisor, Startup Accelerator, Innovation Officer, Corporate Governance |
| F31-F40 | AI Engineering | ML Engineer, MLOps, Data Engineering, Prompt Engineering, RAG, Orchestration, LLM Evaluation |
| F41-F50 | Software | Mobile, Cloud, DevOps, Kubernetes, SOC, API, Database, Embedded, IoT |
| F51-F60 | Healthcare | Digital Health, Clinical Trials, Medical Devices, FDA Documentation, Hospital Operations, Caregiver Support |
| F61-F70 | Neuroscience | Parkinson, Dementia, EEG, Sleep, Neurotechnology, BCI, Aging, Biomarkers |
| F71-F80 | Robotics | Industrial, Service, Medical, AV, Drone, Humanoid, Safety, HRI, Swarm, Ethics |
| F81-F90 | Science | Physics, Quantum, Materials, Chemistry, Climate, Space, Astronomy, Energy, Nuclear |
| F91-F100 | Education | Professor, Curriculum, Tutor, Exams, STEM Lab, Grants, Thesis, Accreditation |
| F101-F110 | Legal & Compliance | Contracts, Privacy, IP, Patents, Employment, Trade, Export, Regulatory Affairs |
| F111-F120 | Manufacturing | Manufacturing, Production, Quality, Maintenance, Supply Chain, Digital Twin, Automation, Safety |
| F121-F130 | Marketing & Growth | Brand, Content, SEO, Social, Lifecycle, Acquisition, Product Marketing, PR, Growth |
| F131-F140 | Creative & Media | Publishing, Screenwriting, Music, Graphic Design, UX, Architecture, Games, Animation |
| F141-F150 | Public Sector | Smart City, Emergency, Disaster, Public Health, Transport, Environment, Policy |
| F151-F160 | Finance & Risk | Investment Research, Portfolio, Quant Research, Insurance, Banking, Tax, Risk, Treasury |
| F161-F170 | Personal & Productivity | Life Planning, Knowledge, Career, Resume, Speaking, Interview, Language, Travel, Habits |

## Testing

Run locally:

```bash
python -m pip install pytest
python -m pytest -q
```

GitHub Actions runs the test suite against Python 3.10, 3.11, and 3.12.

## Safety and responsible use

The library separates decision support from consequential execution. Sensitive systems preserve scope limits and qualified review. Reference workflows should not silently invent missing facts or autonomously perform consequential actions such as clinical decisions, legal certification, financial transactions, physical robot control, industrial equipment commands, targeted voter persuasion, binding public decisions, or external submissions without appropriate authorization and safeguards.

## Repository structure

```text
agentic_ai_library/
├── launcher.py
├── dashboard.py
├── .github/workflows/tests.yml
├── README.md
├── catalog/core/
├── docs/
│   ├── INDEX.md
│   ├── ROADMAP.md
│   └── LAUNCHER.md
├── flagships/
├── systems/
│   ├── STANDARD.md
│   ├── F27_agentic_ma_advisor/
│   ├── F28_agentic_startup_accelerator/
│   ├── F29_agentic_innovation_officer/
│   ├── F30_agentic_corporate_governance/
│   ├── domain specifications
│   ├── deterministic reference workflows
│   ├── evaluation frameworks
│   └── tests/
├── tests/
│   └── test_launcher.py
└── templates/
```

## Author

**Mahsa Keikha**

Companion engineering library for the **AI Engineering Handbook Series** and related educational work.

**One line:** 170 agentic AI systems built around tools, state, orchestration, evidence, evaluation, safety boundaries, and human gates.
